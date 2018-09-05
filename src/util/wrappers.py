from src.config import get_config, write_config
from argh import arg, expects_obj
from functools import wraps
from .logger import logging, logger


__all__ = ['wrapper']


def wrapper(function):
	@arg('-s', '--silent', default = False, help = 'Suppress all output.')
	@arg('-d', '--debug', default = False, help = 'Log all debug output.')
	@arg('--dev', default = False, help = 'Use the development config "config/dev.json"')
	@arg('--dry', default = False, help = 'Dry run, runs the command without committing any changes.')
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

				conf = get_config('config/config.json', 'config/dev.json')
				write_config(conf)

			args[0].conf = get_config()

			return function(*args, **kwds)
		except Exception as error:
			logger.critical("{0}: {1}".format(type(error).__name__, str(error)))

			if args[0].dev:
				raise error

	return wrapper
