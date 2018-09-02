import logging

from src.config import get_config


def init():
	# TODO: CLI argument for dev mode, load dev config.
	conf = get_config()

	logger(conf)


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

	logging.basicConfig(
		level = conf.logger.level,
		format = conf.logger.format,
		datefmt = conf.logger.datefmt)

	if conf.logger.color:
		logging.StreamHandler.emit = color_logs(logging.StreamHandler.emit)



