#!/bin/env python

import sys, os, re, io, random
import argparse, urllib.parse, html, subprocess, datetime

import known

DEFAULT_INPUT_FILEPATH = "index.md"
DEFAULT_OUTPUT_FILEPATH = None


def transuri(m):
	name = uri = m.group(1)
	# x = urllib.parse.urlparse(uri)
	# name, isknown = known.translate(x.netloc)
	name, isknown = known.translate(uri)
	return f' <a href="{uri}"' + (
		f' class="known-uri"' if isknown else ''
		) + f'>{name}</a> '


def transtit(m):
	text = m.group(3).strip()
	level = len(m.group(2))
	return f' <strong title-level="{level}">{text}</strong> '

def ruby(m):
	text = m.group(1)
	note = m.group(2)
	return f'''<ruby><rb>{text}</rb><rt>{note}</rt></ruby>'''


def runGnuHighlighter(lang, text):
	try:
		assert os.path.isfile('syntax.style')
		p = subprocess.run(['source-highlight', '-t 4', '--style-file=./syntax.style', '--src-lang=%s' % lang, '--no-doc'], input = bytes(text, 'utf8'), capture_output = True)
		return p.stdout.decode('utf8')
	except Exception as e:
		# text = str(e)
		pass
	return f'<pre>{text}</pre>'


def highlight(m):
	lang = m.group(1)
	text = m.group(2)
	text = html.unescape(text)
	if not lang:
		return f'<pre>{text}</pre>'
	text = runGnuHighlighter(lang, text)
	return f'{text}'


def parse(text, file = sys.stdout):
	LINKCC = r"[-A-Za-z0-9._~:/?#[\]@!$&()+*,;=%']"
	text = re.sub(r'^!.*$', '', text, flags = re.S|re.M)
	text = re.sub(r'<3', '[:heart:]', text, flags = re.S)
	text = html.escape(text, quote = False)
	text = re.sub(r'\[:copyleft:]', '&#x1F12F', text, flags = re.S)
	text = re.sub(r'\[:heart:]', '<span class="red emoji">&#x2764</span>', text, flags = re.S)
	text = re.sub(r'\[:butterfly:]', '<span class="emoji">&#x1F98B</span>', text, flags = re.S)
	text = re.sub(r'\[:rocket:]', '<span class="emoji">&#x1F680</span>', text, flags = re.S)
	text = re.sub(r'(\s+)(#[A-Za-z][-_.0-9A-Za-z]*[0-9A-Za-z]+)', r'\1<i>\2</i>', text, re.S)
	text = re.sub(r'(\s+)[*]{2}(.+?)[*]{2}', r'\1<b>\2</b>', text, flags = re.S)
	text = re.sub(r'\\\\(.+?)\\\\(.+?)\\\\', ruby, text, flags = re.S)
	text = re.sub(r'____(.+?)____', r'<u>\1</u>', text, flags = re.S)
	text = re.sub(r'\${3}(.+?)\${3}', r'<div class="columns">\1</div>', text, flags = re.S)
	text = re.sub(r'\^{3}(.+?)\^{3}', r'<div class="upright">\1</div>', text, flags = re.S)
	text = re.sub(r'```(?:([^\r\n]+?)[\r\n]+)?(.+?)```', highlight, text, flags = re.S)
	text = re.sub(r'`([^`\r\n]+)`', r'<code>\1</code>', text, flags = re.S)
	text = re.sub(r'"""(.+?)"""', r'<blockquote>\1</blockquote>', text, flags = re.S)
	text = re.sub(r'""(.+?)""', r'<q>\1</q>', text, flags = re.S)
	text = re.sub(r'^((#+)[ \t]+([^\r\n]+))\s*', transtit, text, flags = re.S|re.M)
	text = re.sub(r'\s*<?(https?://' + LINKCC + '+)>?\\s*', transuri, text, flags = re.S)
	text = re.sub(r'/a>\s+([.:,;!?])', r'/a>\1', text, flags = re.S)
	text = re.sub(r'///', '<br>', text, flags = re.S)
	text = re.sub(r'\s+---\s+', ' &mdash; ', text, flags = re.S)
	file.write(text)


def getDateStringFromPath(path):
	m = re.match(r'archive/(\d{4})-(\d{2})-(\d{2})\.md', path)
	if m: return '%d-%02d-%02d' % tuple(int(x) for x in m.groups())


def getCurrentDateString():
	d = datetime.datetime.now()
	return d.strftime('%Y-%m-%d')


def parseArgs(args = sys.argv[1:]):
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--purple-haze', action='store_true')
	parser.add_argument('-d','--date', action='store_true')
	parser.add_argument('-t', '--title', action='store_true')
	parser.add_argument('-b', '--backref', action='store_true')
	parser.add_argument('-v', '--variable')
	parser.add_argument('-o', '--opath', default = DEFAULT_OUTPUT_FILEPATH)
	parser.add_argument('ipath', nargs='?', default = DEFAULT_INPUT_FILEPATH)
	args = parser.parse_args(args)
	if not os.path.isfile(args.ipath):
		parser.error(f'input file not found: "{args.ipath}"')
	return parser, args


def main(args = sys.argv[1:]):
	parser, args = parseArgs(args)
	mfile = io.StringIO()

	if args.backref:
		with open(args.ipath) as ifile:
			m = re.search(r'^!\s*back(?:ref)?=(.+?)\s*$', ifile.read(), re.S|re.M)
			if m:
				backref = m.group(1)
			else:
				import archive
				backref = archive.find_backref_for(args.ipath)

			if backref:
				source = f'archive/{backref}.md'
				if os.path.isfile(source):
					rendered = f'/archive/{backref}.html'
					print(f'<strong><a href="{rendered}">[back]</a></strong>')

	elif args.date:
		d = getDateStringFromPath(args.ipath)
		if not d: d = getCurrentDateString()
		print(d)

	elif args.variable:
		with open(args.ipath) as ifile:
			m = re.search(r'^![ \t]*' + args.variable + r'[ \t]*=[ \t]*(.+?)[ \t]*$', ifile.read(), re.S|re.M)
			if m: print(m.group(1))

	elif args.title:
		with open(args.ipath) as ifile:
			m = re.search(r'^#+\s*(.+?)\s*$', ifile.read(), re.S|re.M)
			print(m.group(1) if m else '')

	elif args.purple_haze:
		haze = ''
		cc = ['--color-purple-haze-1', '--color-purple-haze-2']
		for i in range(2):
			x = random.choice((-7, -5, -2, 3, 6, 8))
			y = random.choice((-7, -5, -2, 3, 6, 8))
			r = random.randint(3, 7)
			if i > 0: haze += ', '
			haze += f'{x}px {y}px {r}px var({cc[i]})'
		print(f'text-shadow: {haze};')

	elif args.ipath:
		with open(args.ipath) as ifile:
			parse(ifile.read(), mfile)

		if args.opath:
			with open(args.opath, 'w') as ofile:
				ofile.write(mfile.getvalue())
		else:
			print(mfile.getvalue())


if __name__ == '__main__':
	sys.exit(main())
