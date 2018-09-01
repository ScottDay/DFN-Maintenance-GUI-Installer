import logging


def init():
	logger()


def logger():
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
		level = 20,
		format = "[%(asctime)s] [%(levelname)8s] %(message)s",
		datefmt = '%Y-%m-%d %H:%M:%S')

	logging.StreamHandler.emit = color_logs(logging.StreamHandler.emit)



