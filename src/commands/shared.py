import logging


log = logging.getLogger()


def wrapper(function):
	from argh import arg, expects_obj, wrap_errors
	from functools import wraps

	@arg('-s', '--silent', default = False, help = 'Suppress all output.')
	@arg('-d', '--debug', default = False, help = 'Log all debug output.')
	@arg('--dev', default = False, help = 'Use the development config "config/dev.json".')
	@wrap_errors([Exception])
	@expects_obj
	@wraps(function)
	def wrapper(*args, **kwds):
		import logging

		log = logging.getLogger()

		if args[0].silent:
			logging.disabled = True

		if args[0].debug:
			log.debug('Debug logging enabled...')
			log.setLevel(logging.DEBUG)

		if args[0].dev:
			log.debug('Using development config...')
			from src.config import get_config, write_config

			conf = get_config('config/config.json', 'config/dev.json')
			write_config(conf)

		return function(*args, **kwds)

	return wrapper
