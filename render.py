import sys, re, io, os
import traceback, pprint

import tools
import logger

class Error(Exception): pass
class ProcessError(Exception): pass

log = None


def main(argv=sys.argv):
	p = tools.ArgParser()
	p.add("ipath", "PATH", help="input file")
	p.add("args", "KEY=VAL", nargs="*", help="globals")
	p.add("-o", "--opath", "PATH", default=None, help="output file")
	p.add("-e", "--epath", "PATH", default=None, help="log file")
	p.add("-d", "--debug", action="store_true")
	aa = p.parse(argv)

	if aa.epath is None:
		aa.epath = aa.ipath + ".log" # tools.noext(aa.ipath) + ".log"

	global log
	log = logger.Logger(debug = True, opath = aa.epath, __file__ = __file__)

	aa.args = {k : v for k, v in (s.split("=") for s in aa.args if "=" in s)}

	generate(p, aa)

def trace(p, aa, e):
	if not aa.debug: return

	sio = io.StringIO()
	sio.write("\n" + "-" * 79 + "\n")
	pprint.pprint(aa.__dict__, stream = sio, sort_dicts = False)
	sio.write("\n")
	traceback.print_exception(e, file = sio)

	if log: log.error(sio.getvalue())
	else: sys.stderr.write(sio.getvalue())

def generate(p, aa):
	# splitter = re.compile(r'\{\{\s*(.+?)\s*\}\}')
	# splitter = re.compile(r'(?P<pre>[ \t]*)(?:\{\{\s*(?P<cmd>.+?)\s*\}\})(?P<post>\r\n|\r|\n)')
	splitter = re.compile(r'((?:^[ \t]+)?)((?:[#][ \t]*)?)\{\{\s*(.+?)\s*\}\}', re.MULTILINE)
	text = open(aa.ipath, encoding="utf-8").read()
	with tools.oopen(aa.opath, force=True) as ofile:
		for key, chunk in tools.rsplit(text, splitter):
			ofile.write(process(p, aa, chunk) if key else chunk)

def process(p, aa, groups):
	prefix, cmt, cmd = groups
	if cmt: return ""
	# print("|%s| |%s| (%d)" % (cmd, prefix, len(prefix)))
	# TODO: Improve this simple hack to be more useful.
	#	Either by making it more intelligent, or by
	#	extending our handlbar syntax. Should call it shellbars.
	#	bashtashes? bournetashes? moustbashe? handlebash?
	try: cmd = cmd.format(p=p, aa=aa, prefix=prefix, **aa.args)
	except KeyError as e:
		trace(p, aa, e)
	except Exception:
		trace(p, aa, e)
		return ""
	out, err = tools.shell(cmd, "utf-8")
	if err: raise ProcessError(err)
	return out

if __name__ == "__main__":
	main()
