# NOTE: Regexes for diff taken from:
# 	/usr/share/grc/conf.diff
#	See: <https://github.com/garabik/grc>

import sys, os, re, argparse, difflib, shutil

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

	@property
	def path(self):
		return f'{ARCHIVE_ROOT}/{self.year}-{self.month:02d}-{self.day:02d}.md'

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
		return sorted(seq, key = key, reverse = reverse)

	@classmethod
	def iter(cls):
		regex = re.compile('(\d{4})-(\d\d)-(\d\d)\.md')
		nn = os.listdir(ARCHIVE_ROOT)
		nn = (regex.match(n) for n in nn)
		nn = (ArchiveItem(*n.groups()) for n in nn if n)
		for n in nn: yield n

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

def getLatestArchiveItemByName():
	aa = ArchiveItem.sorted(ArchiveItem.iter(), reverse = True)
	return aa[0] if aa else None


def file_mtime(path):
	t = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
	return t.astimezone().isoformat()

def get_diff(fromfile, tofile):
	fromdate = file_mtime(fromfile)
	todate = file_mtime(tofile)

	with open(fromfile) as ff:
		fromlines = ff.readlines()
	with open(tofile) as tf:
		tolines = tf.readlines()

	# return difflib.ndiff(fromlines, tolines)
	return difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=3)
	# return difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=3)
	# return difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile, context=True, numlines=5)

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


def print_diff(args, file = sys.stdout):
	# grc -c conf.diff python archive.py -a index.md
	# python archive.py -a index.md | grcat conf.diff

	cur = make_current_archive_item(args)
	top = getLatestArchiveItemByName()
	# print(cur - top)
	diff = get_diff(args.ipath, top.path)
	lines = list(diff)
	if lines:
		if not args.plain:
			lines = colorize_lines(lines)
		file.writelines(lines)

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

def get_quickdiff(apath, bpath, strip = '', colorize = False):
	same = same_first_line(apath, bpath, strip)
	same_str = 'the same'
	diff_str = 'different'
	if colorize:
		same_str = '\033[32;1m' + same_str + '\033[0m'
		same_str = '\033[31m' + same_str + '\033[0m'
	return f'(different versions of) {same_str}' if same else diff_str

def parse_args(args = sys.argv[1:]):
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', '--archive', action='store_true', help='archive current blog file')
	parser.add_argument('-d', '--diff', action='store_true', help='show diff of current blog and top archive file')
	parser.add_argument('-f', '--force', action='store_true', help='overwrite existing archive files')
	parser.add_argument('-m', '--mtime', action='store_true', help='use last modified time to generate paths')
	parser.add_argument('-p', '--plain', action='store_true', help='no rainbows')
	parser.add_argument('--colors' , action='store_true', help='unicorns')
	parser.add_argument('ipath', nargs='?', default=DEFAULT_IPATH, help='blog file to archive')
	return parser, parser.parse_args(args)

if __name__ == '__main__':
	parser, args = parse_args()
	# print(args)

	if args.diff:
		print_diff(args)
		exit()

	elif args.colors:
		for fg in range(8):
			for bg in range(8):
				print(f'\033[{30+fg};{40+bg};1m{30+fg};{40+bg}\033[0m', end=' ')
			print()

	elif args.archive:
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
			print(f'Writing "{cur.path}" with contents of "{args.ipath}"')
			shutil.copy(args.ipath, cur.path)
			exit()

	else:
		cur = make_current_archive_item(args)
		qdiff = get_quickdiff(args.ipath, cur.path, colorize = not args.plain)

		if cur.exists:
			print(f'''Attempting to archive without the --force flag would fail because the
default target path "{cur.path}" for the current blog page
is occupied already.

The two files are probably {qdiff}.

Try `python archive.py -d | less -R` to see the the diff.''')
			exit(1)

		else:
			print(f'Archiving will succeeed because the current blog page\'s archive slot is free.')
			exit(0)
