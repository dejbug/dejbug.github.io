import os, logging

from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET


FORMAT = '%(asctime)s [%(levelname)s] (%(relmod)s:%(lineno)s:%(funcName)s) : %(message)s'


class Logger:
	def __init__(self, debug = False, opath = None, __file__ = ""):
		logging.basicConfig(format = FORMAT, filename = opath)

		setRoot(__file__)

		self.logger = logging.getLogger()
		self.logger.setLevel(logging.NOTSET if debug else logging.WARNING)

		self.setLevel = self.logger.setLevel

		self.debug = self.logger.debug
		self.info = self.logger.info
		self.warning = self.logger.warning
		self.error = self.logger.error
		self.critical = self.logger.critical
		self.exception = self.logger.exception


def setRoot(__file__ = ""):
	old_factory = logging.getLogRecordFactory()

	def record_factory(*args, **kwargs):
	    record = old_factory(*args, **kwargs)
	    root = os.path.dirname(__file__)
	    relpath = os.path.relpath(record.pathname, root)
	    record.relmod = os.path.splitext(relpath)[0]
	    return record

	logging.setLogRecordFactory(record_factory)


setRoot()
