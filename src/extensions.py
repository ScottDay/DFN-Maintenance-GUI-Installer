from logging import basicConfig, StreamHandler

from src.config import get_config, write_config


def init():
	conf = config()
	logger(conf)


def config():
	"""
	Setup either the base configuration file.
	"""
	conf = get_config('config/base.json')
	write_config(conf)

	return conf


def logger(conf):
	"""
	Sets up the applications root logger.

	Logging Levels:
		- CRITICAL: 50
		- ERROR: 40
		- WARNING: 30
		- INFO: 20
		- DEBUG: 10
		- NOTSET: 0
	"""
	def color_logs(function):
		# Add methods we need to the class.
		def new(*args):
			levelno = args[1].levelno

			if(levelno >= 40):
				color = '\x1b[31m' # Red.
			elif(levelno >= 30):
				color = '\x1b[33m' # Yellow.
			elif(levelno == 10):
				color = '\x1b[35m' # Pink.
			else:
				color = '\x1b[0m' # Normal.

			args[1].msg = color + args[1].msg +  '\x1b[0m' # Normal.

			return function(*args)

		return new

	basicConfig(
		level = conf.logger.level,
		format = conf.logger.format,
		datefmt = conf.logger.datefmt)

	if conf.logger.color:
		StreamHandler.emit = color_logs(StreamHandler.emit)



