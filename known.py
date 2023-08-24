import sys, re, pickle, urllib.parse

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

def parseLine(line) -> list[tuple[str | None, ...]]:
# def parseLine(line) -> list[tuple]:
	'''
	>>> parseLine('')
	[]
	>>> parseLine('wikipedia.org')
	[(None, 'wikipedia.org', None)]
	>>> parseLine('wikipedia.org:')
	[(None, 'wikipedia.org', '')]
	>>> parseLine('wikipedia.org:wiki')
	[(None, 'wikipedia.org', 'wiki')]
	>>> parseLine('wikipedia.org:wiki/')
	[(None, 'wikipedia.org', 'wiki')]
	>>> parseLine(r'wikipedia.org:wiki/en')
	[(None, 'wikipedia.org', 'wiki'), ('/', 'en', None)]
	>>> parseLine(r'wikipedia.org:wiki/en:')
	[(None, 'wikipedia.org', 'wiki'), ('/', 'en', '')]
	>>> parseLine(r'wikipedia.org:wiki/en:e')
	[(None, 'wikipedia.org', 'wiki'), ('/', 'en', 'e')]
	>>> parseLine(r'wikipedia.org:wiki/en:e/de:d')
	[(None, 'wikipedia.org', 'wiki'), ('/', 'en', 'e'), ('/', 'de', 'd')]
	>>> parseLine('wikipedia.org:wiki/en:e/de:d//fr.wikipedia.org:friki')
	[(None, 'wikipedia.org', 'wiki'), ('/', 'en', 'e'), ('/', 'de', 'd'), ('//', 'fr.wikipedia.org', 'friki')]
	>>> parseLine('wikipedia.org:wiki/en:e//fr.wikipedia.org:friki/de:d')
	[(None, 'wikipedia.org', 'wiki'), ('/', 'en', 'e'), ('//', 'fr.wikipedia.org', 'friki'), ('/', 'de', 'd')]
	'''
	mm = re.finditer(r'(:|/+)?(?:([^:/]+)(?:[:]([^:/]*))?)', line.strip())
	return [m.groups() for m in mm]

class Substitution:
	src : str
	dst : str | None

	def __init__(self, src : str, dst : str | None):
		self.src = src
		self.dst = dst

	def apply(self, text):
		return self.dst if text.lower() == self.src else text

	def __str__(self):
		return f'{self.src} -> {self.dst}'

	__repr__ = __str__

def makeSubstitutions(parsedLine : list[tuple[str | None, str, str | None]]):
	'''
	>>> list(makeSubstitutions(parseLine('')))
	[]
	>>> list(makeSubstitutions(parseLine('wikipedia.org')))
	[('org', 'wikipedia', wikipedia.org -> wikipedia)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:')))
	[('org', 'wikipedia', wikipedia.org -> wikipedia)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki')))
	[('org', 'wikipedia', wikipedia.org -> wiki)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki/')))
	[('org', 'wikipedia', wikipedia.org -> wiki)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki/en')))
	[('org', 'wikipedia', wikipedia.org -> wiki), ('org', 'wikipedia', en.wikipedia.org -> wiki)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki/en:')))
	[('org', 'wikipedia', wikipedia.org -> wiki), ('org', 'wikipedia', en.wikipedia.org -> wiki)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki/en:e')))
	[('org', 'wikipedia', wikipedia.org -> wiki), ('org', 'wikipedia', en.wikipedia.org -> e:wiki)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki/en:e/de:d')))
	[('org', 'wikipedia', wikipedia.org -> wiki), ('org', 'wikipedia', en.wikipedia.org -> e:wiki), ('org', 'wikipedia', de.wikipedia.org -> d:wiki)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki/en:e/de:d/fr:friki')))
	[('org', 'wikipedia', wikipedia.org -> wiki), ('org', 'wikipedia', en.wikipedia.org -> e:wiki), ('org', 'wikipedia', de.wikipedia.org -> d:wiki), ('org', 'wikipedia', fr.wikipedia.org -> friki:wiki)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki/en:e/de:d//fr:friki')))
	[('org', 'wikipedia', wikipedia.org -> wiki), ('org', 'wikipedia', en.wikipedia.org -> e:wiki), ('org', 'wikipedia', de.wikipedia.org -> d:wiki), ('org', 'wikipedia', fr.wikipedia.org -> friki)]
	>>> list(makeSubstitutions(parseLine('wikipedia.org:wiki/en:e//fr:friki/de:d')))
	[('org', 'wikipedia', wikipedia.org -> wiki), ('org', 'wikipedia', en.wikipedia.org -> e:wiki), ('org', 'wikipedia', fr.wikipedia.org -> friki), ('org', 'wikipedia', de.wikipedia.org -> d:wiki)]
	'''
	for x, key, val in parsedLine:
		# NOTE: Assumes that the 'not x' case will always happen first,
		#	so 'host' and `short` will be set before the other cases occur.
		if not x:
			host, top = key.split('.')
			short = val if val else host
			src = f'{host}.{top}'
			dst = short
		elif x == '/':
			src = f'{key}.{host}.{top}'
			dst = f'{val + ":" if val else ""}{short}'
		elif x == '//':
			src = f'{key}.{host}.{top}'
			dst = val or ''

		yield top, host, Substitution(src, dst)

def aka_get_translator(aka, top, host):
	translator = aka.get(top)
	if translator:
		translator = translator.get(host)
		return translator

def aka_translate(aka, text):
	if not text.strip(): return text

	aka = load()
	domain = urllib.parse.urlparse(text).netloc
	if domain.lower().startswith('www.'): domain = domain[4:]
	x = domain.split('.')

	assert len(x) >= 2, f'unsupported uri |{text}|'

	top = x[-1] if len(x) >= 1 else None
	host = x[-2] if len(x) >= 2 else None
	rest = x[:-2] if len(x) >= 3 else None

	if rest: rest = '.'.join(rest)

	# print()
	# print(f'|{text}|')
	# print(f'|{top}|', f'|{host}|', f'|{rest}|')

	translator = aka_get_translator(aka, top, host)

	if translator:

		alias = translator.get(domain)
		if alias: return alias, True

		halfdomain = host + '.' + top

		alias = translator.get(halfdomain)
		if alias: return rest + ':' + alias if rest else alias, True

	return domain, False

def compile(ipath):
	import os

	assert ipath
	assert os.path.isfile(ipath)

	aka = {}

	with open(ipath) as file:
		lines = (line.strip() for line in file)
		lines = (line for line in lines if not line.startswith('#'))

		for line in lines:
			parsed = parseLine(line)
			for top, host, s in makeSubstitutions(parsed):
				setdict(aka, top, host, s.src, s.dst)

	# import pprint
	# pprint.pprint(aka)

	# print(aka_translate(aka, ''))
	# print(aka_translate(aka, 'https://www.wired.com/blubb'))
	# print(aka_translate(aka, 'https://www.wikipedia.org/blubb'))
	# print(aka_translate(aka, 'https://en.wikipedia.org/blubb'))
	# print(aka_translate(aka, 'https://plato.stanford.edu/Hegel'))
	# print(aka_translate(aka, 'https://firefox.source.docs.mozilla.org/ff-src'))

	return aka

def load(ipath = "known.aka.pickle"):
	with open(ipath, 'rb') as file:
		return pickle.load(file)

def translate(text):
	aka = load()
	return aka_translate(aka, text)

def parse_args(args = sys.argv[1:]):
	import os, argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--opath')
	parser.add_argument('ipath')
	args = parser.parse_args(args)
	if not os.path.isfile(args.ipath):
		parser.error(f'input file not found: "{args.ipath}"')
	return parser, args

def main(args = sys.argv[1:]):
	parser, aa = parse_args()
	aka = compile(aa.ipath)
	if aa.opath:
		with open(aa.opath, 'wb') as file:
			pickle.dump(aka, file)
	else:
		import pprint
		pprint.pprint(aka)


if __name__ == '__main__':
	sys.exit(main())
