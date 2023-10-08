#!/bin/env python

import sys, os, re, io, random
import argparse, urllib.parse, html, subprocess, datetime

import known, emoji

DEFAULT_INPUT_FILEPATH = "index.md"
DEFAULT_OUTPUT_FILEPATH = None

LINKCC = r"[-A-Za-z0-9._~:/?#[\]@!$&()+*,;=%']"


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
	# return f' <strong title-level="{level}">{text}</strong> '
	return f' <h3>{text}</h3> '


def transquote(m):
	text = m.group(1)
	ref = m.group(2)
	if ref:
		text += fr'<cite> &mdash; {ref} </cite>'
	return fr'<blockquote>{text}</blockquote>'


def ruby(m):
	text = m.group(1)
	note = m.group(2)
	return f'''<ruby><rb>{text}</rb><rt>{note}</rt></ruby>'''


def runGnuHighlighter(lang, text):
	stdout, stderr, throw = '', '', ''
	try:
		p = subprocess.run(
			[	'source-highlight',
				'-t 4',
				'--style-file=conf/default.style',
				'--outlang-def=conf/html_common.outlang',
				'--src-lang=%s' % lang,
				'--no-doc'
			], input = bytes(text, 'utf8'), capture_output = True)
		if p.stdout: stdout = p.stdout.decode('utf8')
		if p.stderr: stderr = p.stderr.decode('utf8')
	except Exception as e:
		throw = str(e)
	return stdout, stderr, throw


def highlight(m):
	def pre(text, error = None, source = False):
		error = f'<pre class="error">{error}</pre>' if error else ''
		return error + f'<pre>{text}</pre>'
	def source(text):
		return f'<pre class="source">{text}</pre>'
	def scrollable(pre):
		return f'<div class="source-wrapper">{pre}</div>'
	lang = m.group(1)
	text = m.group(2)
	text = html.unescape(text)
	if not lang:
		return scrollable(pre(text))
	stdout, stderr, throw = runGnuHighlighter(lang, text)
	err = stderr or throw
	if err:
		return scrollable(pre(text, err))
	return scrollable(source(stdout))


def iterBlocks(pattern, text, flags = 0):
	# yields: (blockBegin, blockEnd, matchObject?)
	offset = 0
	for m in re.finditer(pattern, text, flags):
		yield offset, m.start(0), None
		yield m.start(0), m.end(0), m
		offset = m.end(0)
	yield offset, len(text), None

def translate(text):
	text = re.sub(r'^!.*$', '', text, flags = re.S|re.M)

	text = emoji.translateShortcuts(text)
	text = html.escape(text, quote = False)
	text = emoji.translate(text)

	text = re.sub(r'(\s+)(#[A-Za-z][-_.0-9A-Za-z]*[0-9A-Za-z]+)', r'\1<i>\2</i>', text, re.S)
	text = re.sub(r'(?<=\W)([*]{2})(.+?)\1', r'<b>\2</b>', text, flags = re.S)
	text = re.sub(r'\\\\(.+?)\\\\(.+?)\\\\', ruby, text, flags = re.S)
	text = re.sub(r'____(.+?)____', r'<u>\1</u>', text, flags = re.S)
	text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text, flags = re.S)
	text = re.sub(r'\${3}(.+?)\${3}', r'<div class="columns">\1</div>', text, flags = re.S)
	text = re.sub(r'\^{3}(.+?)\^{3}', r'<div class="upright">\1</div>', text, flags = re.S)
	text = re.sub(r'`([^`\r\n]+)`', r'<code>\1</code>', text, flags = re.S)
	text = re.sub(r'"""(.+?)(?:\s*---\s*(.+?)\s*)?"""', transquote, text, flags = re.S)
	text = re.sub(r'""(.+?)""', r'<q>\1</q>', text, flags = re.S)
	text = re.sub(r'^((#+)[ \t]+([^\r\n]+))\s*', transtit, text, flags = re.S|re.M)
	text = re.sub(r'(?<=\s)<?(https?://' + LINKCC + '+)>?(?=\s)', transuri, text, flags = re.S|re.M)
	text = re.sub(r'/a>\s+([.:,;!?])', r'/a>\1', text, flags = re.S)
	text = re.sub(r'///', '<br>', text, flags = re.S)
	text = re.sub(r'\s+---\s+', ' &mdash; ', text, flags = re.S)
	text = re.sub(r'"([^"\r\n]+)"="([^"\r\n]+?)"', r'<abbr title="\2">\1</abbr>', text, flags = re.S)
	text = re.sub(r'"([^"\r\n]+)"\(\(([^)\r\n]+?)\)\)', r'<details open><summary>\1</summary>\2</details>', text, flags = re.S)
	text = re.sub(r'"([^"\r\n]+)"\(([^)\r\n]+?)\)', r'<details><summary>\1</summary>\2</details>', text, flags = re.S)
	return text


def parse(text, file = sys.stdout):
	emoji.load()

	pattern = r'^```(?:([^\r\n]+?)[\r\n]+)?(.+?)^```'
	for b, e, m in iterBlocks(pattern, text, re.S | re.M):
		if m:
			file.write(highlight(m))
		else:
			file.write(translate(text[b:e]))
		file.write('\n')


def getDateStringFromPath(path):
	m = re.match(r'archive/(\d{4})-(\d{2})-(\d{2})\.md', path)
	if m: return '%d-%02d-%02d' % tuple(int(x) for x in m.groups())


def getCurrentDateString():
	d = datetime.datetime.now()
	return d.strftime('%Y-%m-%d')


def parseArgs(args = sys.argv[1:]):
	parser = argparse.ArgumentParser()
	parser.add_argument('-P', '--purple-haze', action='store_true')
	parser.add_argument('-R', '--root-style', action='store_true')
	parser.add_argument('-d','--date', action='store_true')
	parser.add_argument('-t', '--title', action='store_true')
	parser.add_argument('-b', '--backref', action='store_true')
	parser.add_argument('-v', '--variable')
	parser.add_argument('--default')
	parser.add_argument('--shake')
	parser.add_argument('-o', '--opath', default = DEFAULT_OUTPUT_FILEPATH)
	parser.add_argument('ipath', nargs='?', default = DEFAULT_INPUT_FILEPATH)
	args = parser.parse_args(args)
	if not os.path.isfile(args.ipath):
		parser.error(f'input file not found: "{args.ipath}"')
	return parser, args


def extractVariables(text):
	ss = {}
	vv = {}
	for m in re.finditer(r'^![ \t]*(--.+?)[ \t]*=[ \t]*(.+?)[ \t]*$', text, re.S|re.M):
		k, v = m.groups()
		if k.endswith('-shake'):
			ss[k] = v
		else:
			vv[k] = v
	for k, v in ss.items():
		k = k.rstrip('-shake')
		if k in vv:
			try:
				v = int(v)
				vv[k] = int(vv[k]) + random.randint(-v, v)
			except:
				continue
	return vv


def doRootStyle(args):
	with open(args.ipath) as ifile:
		for k,v in extractVariables(ifile.read()).items():
			print(f'{k}: {v};')


def extractVariable(text, key):
	m = re.search(
		r'^![ \t]*' + key + r'[ \t]*=[ \t]*(.+?)[ \t]*$',
		text, re.S|re.M)
	if m: return m.group(1)


def doVariable(args):
	with open(args.ipath) as ifile:
		text = ifile.read()

	v = extractVariable(text, args.variable)
	if v is None:
		v = args.default

	if args.shake:
		d = extractVariable(text, args.shake)
		try:
			d = int(d)
			v = 0 if v is None else int(v)
			return v + random.randint(-d, d)
		except: pass

	return v


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
					rendered = f'/{backref}.html'
					print(f'<strong><a href="{rendered}">[back]</a></strong>')

	elif args.date:
		d = getDateStringFromPath(args.ipath)
		if not d: d = getCurrentDateString()
		print(d)

	elif args.variable:
		v = doVariable(args)
		if v is not None: print(v)

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

	elif args.root_style:
		doRootStyle(args)

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
