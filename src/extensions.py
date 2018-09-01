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

	logging.basicConfig(
		level = 20,
		format = "[%(asctime)s] [%(levelname)s] %(message)s",
		datefmt = '%Y-%m-%d %H:%M:%S')
