
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

def translate(text):
	text = text.lower()
	x = text.split('.')
	assert len(x) >= 2, "invalid netloc?"

	a = ".".join(x[:-2]) if len(x) >= 3 else ""
	b = x[-2]
	c = x[-1]

	if a and a == 'www': a = ""

	isknown = False
	if c in KNOWN:
		if b in KNOWN[c]:
			isknown = True
			if c in KNOWN_SUBS:
				if b in KNOWN_SUBS[c]:
					if a in KNOWN_SUBS[c][b]:
						a = KNOWN_SUBS[c][b][a]
			b = KNOWN[c][b]

	if a: b = f'{a}:{b}'
	return b, isknown
