import sys, os, re, io, urllib.parse, html, subprocess

DEFAULT_INPUT_FILEPATH = "blog.md"
DEFAULT_OUTPUT_FILEPATH = None

KNOWN = {
	'com': {
		'github': 'gh',
		'google': 'G',
		'stackexchange': 'Sx',
		'stackoverflow': 'So',
		'sublimetext': 'st',
	},
	'dev': {
		'wasmtime': 'wt',
	},
	'org': {
		'archive': 'ia',
		'wikipedia': 'wiki',
		'mozilla': 'moz',
		'archlinux': 'arch',
		'kernel': 'kern',
		'opengroup': 'og',
		'rust-lang': 'rs',
	},
	'io': {
		'github': 'gh',
		'sublimetext': 'st',
	}
}

KNOWN_SUBS = {
	'org': {
		'wikipedia': {
			'en': '',
		},
	},
}

def transloc(text):
	text = text.lower()
	x = text.split('.')
	assert len(x) >= 2, "invalid netloc?"

	a = ".".join(x[:-2]) if len(x) >= 3 else ""
	b = x[-2]
	c = x[-1]

	if a and a == 'www': a = ""

	known = False
	if c in KNOWN:
		if b in KNOWN[c]:
			known = True
			if c in KNOWN_SUBS:
				if b in KNOWN_SUBS[c]:
					if a in KNOWN_SUBS[c][b]:
						a = KNOWN_SUBS[c][b][a]
			b = KNOWN[c][b]

	if a: b = f'{a}:{b}'
	return b, known


def transuri(m):
	name = uri = m.group(1)
	x = urllib.parse.urlparse(uri)
	name, known = transloc(x.netloc)
	return f' <a href="{uri}"' + (
		f' class="known-uri"' if known else ''
		) + f'>{name}</a> '


def transtit(m):
	text = m.group(3).strip()
	level = len(m.group(2))
	return f' <strong title-level="{level}">{text}</strong> '


def parse(text, file = sys.stdout):
	LINKCC = r"[-A-Za-z0-9._~:/?#[\]@!$&()+*,;=%']"
	text = re.sub('^!.*$', '', text, re.S|re.M)
	text = html.escape(text, quote = False)
	text = re.sub(r'^\s*((#+)[ \t]*([^\r\n]+))\s*', transtit, text, flags = re.S|re.M)
	# text = re.sub(r'\s*<?(https?://' + LINKCC + r'+)>?\s*', transuri, text, flags = re.S)
	# NOTE: Sublime highlights the string after LINKCC weird. Send them a note.
	text = re.sub(r'\s*<?(https?://' + LINKCC + '+)>?\\s*', transuri, text, flags = re.S)
	text = re.sub(r'/a>\s+([.:,;!?])', r'/a>\1', text, flags = re.S)
	file.write(text)


def main(args = sys.argv[1:]):
	ipath = args[0] if len(args) >= 1 else DEFAULT_INPUT_FILEPATH
	opath = args[1] if len(args) >= 2 else DEFAULT_OUTPUT_FILEPATH
	mfile = io.StringIO()

	# FIXME: This is just a HACK. We should automate this based
	#	on the input file path. The '^!' mechanism is good for
	#	other settings though.
	if ipath == '-b':
		# p = subprocess.run('ls', capture_output = True)
		# print(p.stdout.decode('utf-8'))
		with open(DEFAULT_INPUT_FILEPATH) as ifile:
			m = re.search(r'^!\s*back=(.+?)\s*$', ifile.read(), re.S|re.M)
			if m:
				source = f'archive/{m.group(1)}.md'
				if os.path.isfile(source):
					rendered = f'archive/{m.group(1)}.html'
					print(f'<strong><a href="{rendered}">[back]</a></strong>')
		return

	if ipath:
		with open(ipath) as ifile:
			parse(ifile.read(), mfile)

		if opath:
			with open(opath, 'w') as ofile:
				ofile.write(mfile.getvalue())
		else:
			print(mfile.getvalue())


if __name__ == '__main__':
	sys.exit(main())
