import sys, re, io, urllib.parse

KNOWN = {
	'com': {
		'github': 'gh',
		'google': 'G',
		'stackexchange': 'Sx',
		'stackoverflow': 'So',
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
	return f'\n\n<strong title-level="{level}">{text}</strong>\n\n'


def parse(text, file = sys.stdout):
	text = re.sub(r'^\s*((#+)[ \t]*([^\r\n]+))\s*', transtit, text, flags = re.S|re.M)
	text = re.sub(r'\s*(https?://\S+)\s*', transuri, text, flags = re.S)
	file.write(text)


def bluegender(text, fin, fout = sys.stdout):
	for line in fin:
		if line == '# HERE\n':
			fout.write(text)
		else:
			fout.write(line)


def main(args = sys.argv[1:]):
	s = io.StringIO()
	if len(args) > 0:
		with open(args[0]) as file:
			parse(file.read(), s)

		if len(args) > 1:
			text = s.getvalue()
			s = io.StringIO()
			with open(args[1]) as file:
				bluegender(text, file, s)

			if len(args) > 2:
				with open(args[2], 'w') as file:
					file.write(s.getvalue())
			else:
				print(s.getvalue())


if __name__ == '__main__':
	sys.exit(main())