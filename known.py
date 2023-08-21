import sys, re, pickle

KNOWN_SUBS = {
	'org': {
		'wikipedia': {
			'en': '',
		},
	},
}

# FIXME: Move to python-dejlib.
def setdict(d, *aa):
	'''
	>>> setdict({}, 'a', 'b', 'c')
	{'a': {'b': 'c'}}
	>>> setdict({'a': 'x'}, 'a', 'b', 'c')
	{'a': {'b': 'c'}}
	>>> setdict({'a': {'y': 'z'}}, 'a', 'b', 'c')
	{'a': {'y': 'z', 'b': 'c'}}
	'''
	assert len(aa) >= 2
	out = d
	for i, a in enumerate(aa):
		if a not in d or not isinstance(d[a], dict):
			d[a] = {}
		if i >= len(aa) - 2:
			break
		d = d[a]
	d[aa[-2]] = aa[-1]
	return out


def compile(ipath):
	import os

	assert ipath
	assert os.path.isfile(ipath)

	# regex = re.compile(r'^\s*([^#].*?)\.(.+?)(?:[ \t]*:[ \t]*(.+)?[ \t]*)?$', re.M)
	regex = re.compile(r'^\s*([^#].*?)\.(.+?)[ \t]*([:\\].*)?$', re.M)

	aka = { 'domains': {}, 'subdomains': {} }
	with open(ipath) as file:
		for m in re.finditer(regex, file.read()):
			name, top, alias = m.groups()
			rest = []

			if alias:
				if alias.startswith(':'):
					x = alias[1:].split('\\')
					alias = x[0]
					rest = x[1:]
				elif alias.startswith('\\'):
					alias, rest = name, alias[1:].split('\\')

			if not alias:
				alias = name

			# print(name, '.', top, ':', alias, '/', rest)

			setdict(aka, 'domains', top, name, alias)

			for pair in rest:
				pair = pair.strip()
				if not pair: continue
				x = pair.split(':')
				key, val = x if len(x) == 2 else (x[0], '')
				setdict(aka, 'subdomains', top, name, key, val)

	return aka


def load(ipath = "known.aka.pickle"):
	with open(ipath, 'rb') as file:
		return pickle.load(file)


def translate(text):
	text = text.lower()
	x = text.split('.')
	assert len(x) >= 2, "invalid netloc?"

	a = ".".join(x[:-2]) if len(x) >= 3 else ""
	b = x[-2]
	c = x[-1]

	a = re.sub(r'www\.?', '', a)

	aka = load()
	DOMAINS = aka['domains']
	SUBDOMAINS = aka['subdomains']

	isknown = False
	if c in DOMAINS:
		if b in DOMAINS[c]:
			isknown = True
			if c in SUBDOMAINS:
				if b in SUBDOMAINS[c]:
					if a in SUBDOMAINS[c][b]:
						a = SUBDOMAINS[c][b][a]
			b = DOMAINS[c][b]

	if a: b = f'{a}:{b}'
	return b, isknown


def parseArgs(args = sys.argv[1:]):
	import os, argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--opath')
	parser.add_argument('ipath')
	args = parser.parse_args(args)
	if not os.path.isfile(args.ipath):
		parser.error(f'input file not found: "{args.ipath}"')
	return parser, args


def main(args = sys.argv[1:]):
	parser, aa = parseArgs()
	aka = compile(aa.ipath)
	if aa.opath:
		with open(aa.opath, 'wb') as file:
			pickle.dump(aka, file)
	else:
		import pprint
		pprint.pprint(aka)


if __name__ == '__main__':
	sys.exit(main())
