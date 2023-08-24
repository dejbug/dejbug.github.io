# Optimal IO

I had to check two files for equality in Python and was about to use `mmap` but started wondering what size its preferred input buffer was.

Someone https://stackoverflow.com/questions/15979793/is-there-any-way-to-find-the-buffer-size-of-a-file-object pointed out that it used to be hard-coded to 8192 http://hg.python.org/cpython/file/84cd07899baf/Objects/fileobject.c#l2313 . Well, even in 3.11 it still does **look** like it https://github.com/python/cpython/blob/154477be722ae5c4e18d22d0860e284006b09c4f/Modules/_io/fileio.c#L694 Well, kinda.

#tldr; Everything is explained in `_pyio.py` https://github.com/python/cpython/blob/93714b7db795b14b26adffde30753cfda0ca4867/Lib/_pyio.py#L123 .

	""" Binary files are buffered in fixed-size chunks; the size of the buffer is chosen using a heuristic trying to determine the underlying device's "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`. https://github.com/python/cpython/blob/93714b7db795b14b26adffde30753cfda0ca4867/Lib/_pyio.py#L129 """

Alas! I've read these lines too late. And because I knew the block size was available with `stat` I had with that a ____pretty little trap____ laid out for me already.

```
$ stat /tmp/tags/GTAGS
  File: /tmp/tags/GTAGS
  Size: 52051968        Blocks: 101664     IO Block: 4096   regular file
Device: #,##    Inode: ###         Links: #
Access: (0644/-rw-r--r--)  Uid: (#####/xxxxxxxx)   Gid: (#####/xxxxxxxx)
Access: 2023-08-23 16:30:49.290685452 +0200
Modify: 2023-08-23 15:51:15.817349681 +0200
Change: 2023-08-23 15:51:15.820683015 +0200
 Birth: 2023-08-23 15:51:11.780683011 +0200
$ stat -c'The "optimal I/O transfer size hint" for %n is %o.' /tmp/tags/GTAGS
The "optimal I/O transfer size hint" for /tmp/tags/GTAGS is 4096.
```

Even here I could have saved myself by simply calling into the shell with `os.system` or `subprocess.run` but `os.stat` was just perplexing me!

```
$ python -c 'import os; print(os.stat("/tmp/tags/GTAGS"))'
os.stat_result(st_mode=33188, st_ino=###, st_dev=##, st_nlink=#, st_uid=#####,
	st_gid=#####, st_size=52051968, st_atime=1692801049, st_mtime=1692798675,
	st_ctime=1692798675)
```

See what's missing?

```
$ sed -n '61p' /usr/include/bits/struct_stat.h
    __blksize_t st_blksize;     /* Optimal block size for I/O.  */
```

So I spent an hour oscillating between `sys/stat.h`, `bits/types.h`, `bits/typesizes.h`, `bits/struct_stat.h` trying to recreate `struct stat` in ctypes. Here it is.

```
class stat(ctypes.Structure):
	_fields_ = [
		('st_dev', ctypes.c_ulonglong),
		('st_ino', ctypes.c_ulonglong),
		('st_nlink', ctypes.c_ulonglong),
		('st_mode', ctypes.c_uint),
		('st_uid', ctypes.c_uint),
		('st_gid', ctypes.c_uint),
		('__pad0', ctypes.c_uint),
		('st_rdev', ctypes.c_ulonglong),
		('st_size', ctypes.c_longlong),
		('st_blksize', ctypes.c_longlong),
		('st_blocks', ctypes.c_longlong),
		('st_atim', ctypes.c_longlong),
		('st_atimensec', ctypes.c_ulong),
		('st_mtim', ctypes.c_longlong),
		('st_mtimensec', ctypes.c_ulong),
		('st_ctim', ctypes.c_longlong),
		('st_ctimensec', ctypes.c_ulong),
		('__glibc_reserved', ctypes.c_long * 3)
	]
```
https://www.youtube.com/watch?v=q0Se2f0Rq88

The thing is perfectly non-portable and ugly but at least I had a way to get the unabridged fstat. Again, I really should have called into the shell and moved on but ____I tend to get obsessive____ in that way.

It took so long to find the bloody types. What I should have done is `printf("%d\n", sizeof(stat::st_ino));` (g++) etc. and  experimentally determine signedness. But I guess I just wanted to do it the hard way. One of those days.

So one file would point me to another and the other back. Like nobody wanted anything to do with me. For example. #struct_stat.h will tell you that `stat::st_ino` is of `__ino_t` type. E.g. `find /usr/include/ -iname '*.h' | xargs grep __ino_t` will tell you that if you looked in #types.h you would see that `__ino_t` is of type `__INO_T_TYPE`. E.g. `gtags -C /usr/include/ /tmp/tags/ && global -C /tmp/tags/ __INO_T_TYPE` https://www.gnu.org/software/global/globaldoc_toc.html#Basic-usage https://github.com/oracle/opengrok/wiki/Comparison-with-Similar-Tools would refer you kindly to #typesizes.h. There you'll see that `__INO_T_TYPE` is a `__SYSCALL_ULONG_TYPE` which is either `__UQUAD_TYPE` or `__ULONGWORD_TYPE` depending on compile-time flags https://www.ibm.com/docs/en/zos/2.3.0?topic=environments-ilp32-lp64-data-models-data-type-sizes . This would send you back to #types.h to tell you that `__UQUAD_TYPE` is an `__uint64_t` and so on.

It was only later that I stumbled over `_pyio.open` and saw that `st_blksize` was indeed a thing in Python's stat https://github.com/python/cpython/blob/93714b7db795b14b26adffde30753cfda0ca4867/Lib/_pyio.py#L250 .

Compare and contrast:

```
$ python -c 'import os; print(os.stat("/tmp/tags/GTAGS"))'
os.stat_result(st_mode=33188, st_ino=###, st_dev=##, st_nlink=#, st_uid=#####,
	st_gid=#####, st_size=52051968, st_atime=1692801049, st_mtime=1692798675,
	st_ctime=1692798675)
```

But:

```
$ python -c 'import os; print(os.stat("/tmp/tags/GTAGS").st_blksize)'
4096
```

This is where I should be crying but hey ho. You win some you lose some. It's all up there in the Great Material Continuum https://memory-alpha.fandom.com/wiki/Great_Material_Continuum .

# Intermezzo

My good friend P. from my local chess club had me rewrite my tournament announcement and so we spent two happy hours obsessing over things together. We have different communication styles so I had a chance to recall some wisdom which I myself had had forgotten and to pass it on to a slightly younger generation.

# Interference

I had tried to explain a Swiss-style https://spp.fide.com/c-04-3-fide-dutch-system/ tournament with the sentence, "it's like round-robin but with fewer rounds." https://en.wikipedia.org/wiki/Genus%E2%80%93differentia_definition My friend was stuck on the first part, how can it be round-robin when it's not. He was making fun of me. The fact that I had likened it to a round-robin when that was precisely what it wasn't. https://en.wikipedia.org/wiki/Principle_of_charity

# Interpolation

My meaning was more accurate than my words of course. The point of a tournament is to determine the best player. A round-robin is the ideal. In practice there might be too many players to have everyone play everybody, so the next best thing is to reduce the rounds somehow. The Swiss system, though imperfect, is exploiting statistical knowledge about the players to **simulate** https://mitpress.mit.edu/9780936756028/simulations/ the unattainable ideal of perfect information.

All of that reminded me that I had to continue working on my swiss tournament pairer. Our website needs more work as well. It's just a mockup really.

# Suboptimal IQ

I feel like I didn't do a lot today. I went to bed too late today and got up in a haze. I didn't get to eat a lot. Didn't drink a lot. I can plainly see my ego work against me. I was not exaggerating with my getting obsessive over little things like this. Comparing tiny text files but with "optimal I/O" for heaven's sake!

I'm afraid this is a question of intelligence. I'm just not clever enough to also be smart.


! header=block

! blurb=Two steps forward / One step back / Runs the heap / Into the stack
