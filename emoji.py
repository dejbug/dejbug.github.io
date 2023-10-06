import re

PATH = 'emoji.lut'

UNKNOWN_EMOJI = None # '[emoji]'

# REGEX = re.compile(r'\[:(.+?)([!]*):(?:(.*?):)?]', re.S) # shouldn't this work too?
REGEX = re.compile(r'\[:([^!:\]]+)(!*):(?:([^:\]]*):)?]', re.S)
LUT = None

def load(path = PATH):
	global LUT
	LUT = {}
	with open(path) as file:
		mm = re.finditer(r'^(\S+)\s+(\S+)', file.read(), re.M)
		LUT = {m.group(1): m.group(2) for m in mm}

def translate(text):
	# Must be called AFTER html.escape().
	return REGEX.sub(replace, text)

def translateShortcuts(text):
	# Must be called BEFORE html.escape().
	text = re.sub(r'<3', '[:heart!!:]', text)
	# ...
	return text

def replace(m):
	if LUT is None:
		raise Exception("Call emoji.load() first.")
	key, flags, cc = m.groups()
	u = LUT.get(key)
	if u:
		cc = makeClassString(flags, cc)
		return makeSpan('&#x' + u, cc)
	return UNKNOWN_EMOJI if UNKNOWN_EMOJI else key.upper()

def makeClassString(flags, cc):
	'''
	>>> makeClassString('', None)
	>>> makeClassString('', '')
	[]
	>>> makeClassString('!', None)
	['emoji']
	>>> makeClassString('!!', None)
	['red', 'emoji']
	>>> makeClassString('!!', '')
	['red', 'emoji']
	>>> makeClassString('!!', 'strong xyz')
	['red', 'emoji', 'strong', 'xyz']
	'''
	if cc is not None:
		cc = cc.split() if cc else []
	if flags:
		if not cc: cc = []
		if '!!' in flags:
			cc.insert(0, 'emoji')
			cc.insert(0, 'red')
		elif '!' in flags:
			cc.insert(0, 'emoji')
	return cc

def makeSpan(u, cc = None):
	'''
	>>> makeSpan('&#x2764')
	'&#x2764'
	>>> makeSpan('&#x2764', '')
	'<span>&#x2764</span>'
	>>> makeSpan('&#x2764', 'emoji')
	'<span class="emoji">&#x2764</span>'
	'''
	if cc is None: return u
	if not isinstance(cc, str): cc = ' '.join(cc)
	if cc: return f'<span class="{cc}">{u}</span>'
	return f'<span>{u}</span>'
