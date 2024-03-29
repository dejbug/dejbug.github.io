#!/bin/env python

# NOTE: Regexes for diff taken from:
# 	/usr/share/grc/conf.diff
#	See: <https://github.com/garabik/grc>

import sys, os, re, argparse, difflib, shutil, hashlib

from datetime import datetime, timezone
from functools import cmp_to_key

ARCHIVE_ROOT = 'archive'
DEFAULT_IPATH = 'index.md'

COLORS = {
	'diff-added': '32;1',
	'diff-removed': '31',
	'diff-affected': '95;1',
}

class ArchiveItem:
	year : int
	month : int
	day : int

	def __init__(self, year = None, month = None, day = None):
		self.year = int(year or 0)
		self.month = int(month or 0)
		self.day = int(day or 0)

	def __eq__(self, other):
		if self.year != other.year: return False
		if self.month != other.month: return False
		if self.day != other.day: return False
		return True

	@property
	def name(self):
		return f'{self.year}-{self.month:02d}-{self.day:02d}'

	@property
	def path(self):
		return f'{ARCHIVE_ROOT}/{self.name}.md'

	@property
	def exists(self):
		return os.path.isfile(self.path)

	@property
	def time(self):
		return self.year * 100000 + self.month * 100 + self.day

	def __sub__(self, other):
		return self.time - other.time

	@classmethod
	def sorted(cls, seq , reverse : bool = False):
		key = cmp_to_key(lambda a, b: a.time - b.time)
		# reveal_type(lambda a, b: a.time - b.time)
		# reveal_type(cmp_to_key)
		# reveal_type(key)
		return sorted(seq, key = key, reverse = reverse)

	@classmethod
	def parse(cls, text):
		name = filename(text)
		m =  re.search(r'(\d{4})-(\d\d)-(\d\d)', name)
		if m: return cls(*m.groups())

	@classmethod
	def iter(cls):
		# regex = re.compile(r'(\d{4})-(\d\d)-(\d\d)\.md')
		nn = os.listdir(ARCHIVE_ROOT)
		nn = (cls.parse(n) for n in nn)
		nn = (n for n in nn if n)
		return nn

	@classmethod
	def current(cls, path = None):
		if path:
			t = os.path.getmtime(path)
			dt = datetime.fromtimestamp(t)
		else:
			dt = datetime.now()
		# print(dt.strftime('%Y-%m-%d.md'))
		return cls(dt.year, dt.month, dt.day)

	def __str__(self):
		return type(self).__name__ + str(self.__dict__)

def filename(text):
	_, name = os.path.split(text)
	name, _ = os.path.splitext(name)
	return name

def get_latest_archive_item_by_name():
	aa = ArchiveItem.sorted(ArchiveItem.iter(), reverse = True)
	return aa[0] if aa else None

def file_mtime(path):
	t = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
	return t.astimezone().isoformat()

def get_diff(fromfile, tofile, verbose = False):
	fromdate = file_mtime(fromfile)
	todate = file_mtime(tofile)

	with open(fromfile) as ff:
		fromlines = ff.readlines()
	with open(tofile) as tf:
		tolines = tf.readlines()

	# return difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=3)
	# return difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile, context=True, numlines=5)

	if verbose:
		return difflib.ndiff(fromlines, tolines)
	else:
		return difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=3)

def colorize_lines(lines):
	assert lines and len(lines)
	lf = lines[0][-1]
	assert lf in '\r\n'
	for line in lines:
		line = line.rstrip('\r\n')
		# if line.startswith('-'):
		if re.match(r'^\+(.*$)', line):
			yield f'\033[{COLORS["diff-added"]}m{line}\033[0m' + lf
		elif re.match(r'^\>([^\>].*|$)', line):
			yield f'\033[{COLORS["diff-added"]}m{line}\033[0m' + lf
		elif re.match(r'^\-(--.+$|[^\-].*$|$)', line):
			yield f'\033[{COLORS["diff-removed"]}m{line}\033[0m' + lf
		elif re.match(r'^\<([^\<].*|$)', line):
			yield f'\033[{COLORS["diff-removed"]}m{line}\033[0m' + lf
		elif re.match(r'^@@ .* @@$', line):
			yield f'\033[{COLORS["diff-affected"]}m{line}\033[0m' + lf
		else:
			yield line + lf

def make_current_archive_item(args):
	# return ArchiveItem.current(args.ipath if args.mtime else None)

	if args.mtime:
		# Return last-modified-time-based target path.
		return ArchiveItem.current(args.ipath)
	else:
		# Return now-time-based target path.
		return ArchiveItem.current(None)

def print_diff_last_archived(args):
	# grc -c conf.diff python archive.py -a index.md
	# python archive.py -a index.md | grcat conf.diff

	cur = make_current_archive_item(args)
	top = get_latest_archive_item_by_name()
	# print(cur - top)
	diff = get_diff(args.ipath, top.path, verbose = args.verbose)
	lines = list(diff)
	if lines:
		if not args.plain:
			lines = colorize_lines(lines)
		sys.stdout.writelines(lines)
		if args.verbose:
			print()
	if args.verbose:
		print_hashes(args.ipath, top.path)

def same_first_line(apath, bpath, strip = ''):
	if not os.path.isfile(apath) or not os.path.isfile(bpath):
		return False
	with open(apath) as f:
		aline = f.readline()
	with open(bpath) as f:
		bline = f.readline()
	if strip:
		aline = aline.strip(strip)
		bline = bline.strip(strip)
	return aline == bline

def green(text):
	return '\033[32;1m' + text + '\033[0m'

def red(text):
	return '\033[31m' + text + '\033[0m'

def get_quickdiff(apath, bpath, strip = '', colorize = False):
	same = same_first_line(apath, bpath, strip)
	same_str = 'the same'
	diff_str = 'different'
	if colorize:
		same_str = green(same_str)
		diff_str = red(diff_str)
	return f'(different versions of) {same_str}' if same else diff_str

def compare_files(apath, bpath, block_size = 8192):
	if not os.path.isfile(apath): return False
	if not os.path.isfile(bpath): return False
	if os.path.getsize(apath) != os.path.getsize(bpath): return False
	# TODO: Use mmaps?
	# TODO: Use ctypes.fopen/close, ctypes.fileno, ctypes.fstat
	#	with the "optimal block size for I/O" ?
	with open(apath, 'rb') as afile:
		with open(bpath, 'rb') as bfile:
			achunk = afile.read(block_size)
			bchunk = bfile.read(block_size)
			if achunk != bchunk:
				return False
	return True

def get_archived_version(ipath = DEFAULT_IPATH):
	for archived in ArchiveItem.sorted(ArchiveItem.iter(), reverse = True):
		if compare_files(ipath, archived.path):
			return archived

def find_backref_for(ipath):
	archived = ArchiveItem.parse(ipath)
	if not archived:
		top = get_latest_archive_item_by_name()
		if top: return top.name
	else:
		aa = ArchiveItem.sorted(ArchiveItem.iter(), reverse = True)
		found = False
		for a in aa:
			if found:
				return a.name
			elif a == archived:
				found = True

def print_colors():
	for fg in range(8):
		for bg in range(8):
			print(f'\033[{30+fg};{40+bg};1m{30+fg};{40+bg}\033[0m', end=' ')
		print()

def print_backref(args):
	backref = find_backref_for(args.ipath)
	if backref: print(backref)

def getFileHash(path):
	md5 = hashlib.md5()
	with open(path, 'rb') as file:
		md5.update(file.read())
	return md5.hexdigest()

def print_hashes(ipath, apath):
	ihash = getFileHash(ipath)
	ahash = getFileHash(apath)
	same = ihash == ahash
	colorize = green if same else red
	print(colorize(ihash), ipath)
	print(colorize(ahash), apath)
	return same

def print_hashes_if_archived(args):
	archived = get_archived_version(args.ipath)
	if archived:
		if args.verbose:
			print(f'"{green(args.ipath)}" is already archived as "{green(archived.path)}".\n')
		print_hashes(args.ipath, archived.path)

def archive_current(args):
	if print_hashes_if_archived(args):
		return

	cur = make_current_archive_item(args)
	if cur.exists:
		if args.force:
			print(f'Overwriting "{cur.path}" with contents of "{args.ipath}"')
			shutil.copy(args.ipath, cur.path)
		else:
			print(f'Target at "{cur.path}" exists. Use --force to overwrite.')
			qdiff = get_quickdiff(args.ipath, cur.path, colorize = not args.plain)
			print(f'The two files are probably {qdiff}.')
	else:
		print(f'Writing to "{cur.path}" with contents of "{args.ipath}"')
		shutil.copy(args.ipath, cur.path)

def make_brand_new(args):
	if not args.force:
		archived = get_archived_version(args.ipath)
		if not archived:
			print(f'Index was {red("not")} archived yet. Watch out!')
			return False
	os.remove(args.ipath)
	with open(args.ipath, 'wb') as file:
		pass
	return os.path.isfile(args.ipath)

def parse_simple_date(text):
	now = datetime.now()
	d = { 'y': now.year, 'm': now.month, 'd': now.day }
	def match(pattern, d = d):
		m = re.match(pattern, text)
		if m: d.update(dict((k, int(v)) for k, v in m.groupdict().items() if v))
		return m
	if '/' in text and match(r'(?P<m>\d+)/(?P<d>\d+)(?:/(?P<y>\d+))?'): return d # print(3, d)
	elif '.' in text and match(r'(?P<d>\d+)(?:\.(?P<m>\d+)(?:\.(?P<y>\d+))?)?'): return d # print(2, d)
	elif match(r'(?:(?:(?P<y>\d+)-)?(?P<m>\d+)-)?(?P<d>\d+)'): return d # print(1, d)

def explain(args):
	text = (args.explain or args.extant).strip()
	if text == '#':
		aa = ArchiveItem.sorted(ArchiveItem.iter())
		print(len(aa))
		return
	try:
		i = int(text)
		aa = ArchiveItem.sorted(ArchiveItem.iter())
		path = aa[i].path
	except:
		text = text.lower()
		d = parse_simple_date(text)
		if not d:
			return
		path = f'archive/{d["y"]:04}-{d["m"]:02}-{d["d"]:02}.md'
	if not args.extant or os.path.isfile(path):
		print(path)

def iter_archived_days():
	def is_leap_year(y):
		return y % 100 == 0 and y % 400 == 0 or y % 4 == 0
	def get_days_in_month(y, m):
		if m == 2:
			return 29 if is_leap_year(y) else 28
		return [0,31,0,31,30,31,30,31,31,30,31,30,31][m]
	aa = ArchiveItem.sorted(ArchiveItem.iter())
	y = 0
	m = 0
	d = 0
	for a in aa:
		if a.year != y:
			y = a.year
			if d == 0:
				first = False
				yield 'F', y
			else:
				yield 'Y', y
			m = a.month
			yield 'M', m
			for i in range(1, a.day):
				yield 'd', i
			d = a.day
			yield 'D', d
		elif a.month != m:
			if m > 0:
				for i in range(d + 1, get_days_in_month(y, m) + 1):
					yield 'd', i
			yield 'Y', y
			m = a.month
			yield 'M', m
			for i in range(1, a.day):
				yield 'd', i
			d = a.day
			yield 'D', d
		else:
			for i in range(d + 1, a.day):
				yield 'd', i
			d = a.day
			yield 'D', d
	if m > 0:
		for i in range(d + 1, get_days_in_month(y, m) + 1):
			yield 'd', i

def list_archive(args):
	# TODO: Make this look like `cal -y`.
	for t, x in iter_archived_days():
		if t in 'FY':
			if t == 'Y':
				print()
			print(x, end=' ')
		elif t == 'M':
			print('%2d' % x, end=' ')
		elif t == 'd':
			if args.plain:
				p = '.' * len(str(x))
				print(p, end=' ')
			else:
				print(red(str(x)), end=' ')
		elif t == 'D':
			if args.plain:
				print(x, end=' ')
			else:
				print(green(str(x)), end=' ')
	print()

def print_dry_run_info(args):
	cur = make_current_archive_item(args)
	qdiff = get_quickdiff(args.ipath, cur.path, colorize = not args.plain)

	if cur.exists:
		print(f'''Attempting to archive without the --force flag would fail because the
default target path "{cur.path}" for the current blog page
is occupied already.

The two files are probably {qdiff}.

Try `python archive.py -d | less -R` to see the the diff.''')

		if args.verbose:
			print()
			print_hashes_if_archived(args)

	else:
		print(f'Archiving will succeeed because the current blog page\'s archive slot is {green("free")}.')

def parse_args(args = sys.argv[1:]):
	notes = '''QUERY is either of the form [[Y-]M-]D or D[.M[.Y]] or M/D[/Y],
		or it is a negative integer, -1 being the most recently archived page, etc.
		The special value -0 (or just 0) will print the oldest archived page.
		The special value # will print the number of archived pages. Note that #
		must be escaped: -x '#'. But -x=# and -x# will also work.'''
	parser = argparse.ArgumentParser(epilog = notes)
	parser.add_argument('-a', '--archive', action='store_true', help='archive current blog file')
	parser.add_argument('-b', '--backref', action='store_true', help='find backref for ipath')
	parser.add_argument('-d', '--diff', action='store_true', help='show diff of current blog and top archive file')
	parser.add_argument('-f', '--force', action='store_true', help='force irreversible operations (with -a and -n)')
	parser.add_argument('-m', '--mtime', action='store_true', help='use modified time to generate archive path (else current time)')
	parser.add_argument('-n', '--new', action='store_true', help='make a brand new index.md')
	parser.add_argument('-x', '--explain', metavar='QUERY', help='print archive path for date')
	parser.add_argument('-X', '--extant', metavar='QUERY', help='print archive path for date (if it exists)')
	parser.add_argument('-l', '--list', action='store_true', help='list archive paths')
	parser.add_argument('-v', '--verbose', action='store_true', help='don\'t be shy')
	parser.add_argument('-p', '--plain', action='store_true', help='no rainbows')
	parser.add_argument('--colors' , action='store_true', help='just rainbows')
	parser.add_argument('ipath', nargs='?', default=DEFAULT_IPATH, help='blog file to archive')
	return parser, parser.parse_args(args)

def main(args = sys.argv[1:]):
	parser, args = parse_args(args)

	if args.colors: print_colors()

	elif args.backref: print_backref(args)

	elif args.diff: print_diff_last_archived(args)

	elif args.archive: archive_current(args)

	elif args.new: make_brand_new(args)

	elif args.explain or args.extant: explain(args)

	elif args.list: list_archive(args)

	else: print_dry_run_info(args)

if __name__ == '__main__':
	sys.exit(main())
