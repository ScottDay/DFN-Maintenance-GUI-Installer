from .logger import logging, logger


def wrapper(function):
	from argh import arg, expects_obj
	from functools import wraps

	@arg('-s', '--silent', default = False, help = 'Suppress all output.')
	@arg('-d', '--debug', default = False, help = 'Log all debug output.')
	@arg('--dev', default = False, help = 'Use the development config "config/dev.json"')
	@expects_obj
	@wraps(function)
	def wrapper(*args, **kwds):
		try:
			if args[0].silent:
				logging.disabled = True

			if args[0].debug:
				logger.debug('Debug logging enabled...')
				logger.setLevel(logging.DEBUG)

			if args[0].dev:
				logger.debug('Using development config...')
				from src.config import get_config, write_config

				conf = get_config('config/config.json', 'config/dev.json')
				write_config(conf)

			return function(*args, **kwds)
		except Exception as error:
			import sys, os

			exc_type, exc_obj, exc_tb = sys.exc_info()
			filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			line_number = exc_tb.tb_lineno

			logger.critical("{0} [{1}:{2}]: {3}".format(type(error).__name__, filename, line_number, str(error)))

			if args[0].dev:
				raise error

	return wrapper
