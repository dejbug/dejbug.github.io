import os, ctypes

os.system('stat index.md')
print('-' * 79)

with open('index.md') as file:
	fd = file.fileno()
	print(os.fstat(fd))

print('-' * 79)

# __SYSCALL_SLONG_TYPE	__SQUAD_TYPE	__uint64_t		c_longlong
# __SYSCALL_ULONG_TYPE	__UQUAD_TYPE	__uint64_t		c_ulonglong
# 						__U32_TYPE		unsigned int	c_uint

# __ino_t		__SYSCALL_ULONG_TYPE	__UQUAD_TYPE __uint64_t
# __mode_t	__U32_TYPE	unsigned int
# __nlink_t	__SYSCALL_ULONG_TYPE
# __dev_t		__UQUAD_TYPE
# __off_t		__SYSCALL_SLONG_TYPE	__SQUAD_TYPE	__int64_t
# __blkcnt_t	__SYSCALL_SLONG_TYPE
# __time_t	__SYSCALL_SLONG_TYPE
# __syscall_slong_t	__SYSCALL_SLONG_TYPE
# __uid_t	__gid_t	__U32_TYPE

# __OFF_T_TYPE
# __OFF64_T_TYPE	__SQUAD_TYPE

# __dev_t		st_dev	st_rdev
# __ino_t		st_ino
# __mode_t	st_mode
# __uid_t		st_uid
# __gid_t		st_gid
# __off_t		st_size

class stat(ctypes.Structure):
	_fields_ = [
		('st_dev', ctypes.c_ulonglong),
		# ('__pad1', ctypes.c_ushort),
		('st_ino', ctypes.c_ulonglong),
		('st_nlink', ctypes.c_ulonglong),
		('st_mode', ctypes.c_uint),
		('st_uid', ctypes.c_uint),
		('st_gid', ctypes.c_uint),
		('__pad0', ctypes.c_uint),
		('st_rdev', ctypes.c_ulonglong),
		# ('__pad2', ctypes.c_ushort),
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

print('sizeof struct stat:', ctypes.sizeof(stat))

libc = ctypes.cdll.LoadLibrary("libc.so.6")
libc.printf(b'sizeof struct stat: %d\n', ctypes.sizeof(stat))

libc.fopen.restype = ctypes.c_voidp
libc.fclose.argtypes = [ctypes.c_voidp]
libc.fileno.argtypes = [ctypes.c_voidp]
libc.fstat.argtypes = [ctypes.c_int, ctypes.c_char_p]

buf = ctypes.create_string_buffer(ctypes.sizeof(stat))

f = libc.fopen(b'/home/dej/work/github/dejbug.github.io/index.md', b'rb')
print('fileno:', libc.fileno(f))
r = libc.fstat(libc.fileno(f), buf)
print('fstat result:', r)
print('-' * 79)
print(repr(buf.raw))
print()
x = ctypes.cast(buf, ctypes.POINTER(stat))
print('  dev', x.contents.st_dev)
print('  ino', x.contents.st_ino)
print(' mode', x.contents.st_mode)
print('nlink', x.contents.st_nlink)
print('  uid', x.contents.st_uid)
print('  gid', x.contents.st_gid)
print(' rdev', x.contents.st_rdev)
print(' size', x.contents.st_size)
print('bsize', x.contents.st_blksize)
print('block', x.contents.st_blocks)
print(' atim', x.contents.st_atim)
print(' mtim', x.contents.st_mtim)
print(' ctim', x.contents.st_ctim)

libc.fclose(f)
