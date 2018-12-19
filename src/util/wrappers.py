import logging

from src.config import get_config, write_config
from argh import arg, expects_obj
from functools import wraps
from inspect import getargspec, getmodule


__all__ = ['wrapper', 'injector']


def wrapper(function):
	@arg('-s', '--silent', default = False, help = 'Suppress all output.')
	@arg('-d', '--debug', default = False, help = 'Log all debug output.')
	@arg('--dev', default = False, help = 'Use the development config "config/dev.json"')
	@arg('--dry', default = False, help = 'Dry run, runs the command without committing any changes.')
	@expects_obj
	@wraps(function)
	def wrapper(*args, **kwargs):
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

			return function(*args, **kwargs)
		except Exception as error:
			logger.critical("{0}: {1}".format(type(error).__name__, str(error)))

			if args[0].dev:
				raise error

	return wrapper


def injector(function):
	@wraps(function)
	def decorator(*_args, **_kwargs):
		argsspec = getargspec(function)

		if 'log' in argsspec.args:
			prefix = '{}.{}'.format(getmodule(function).__name__, function.__name__)

			_kwargs['log'] = logging.getLogger(prefix)

		return function(*_args, **_kwargs)
	return decorator


def logger(*args, **kwargs):
	'''
	@log_doc('Gathering debug output...', level = 'DEBUG')
	or
	@log_doc('Gathering debug output...')
	or
	@log_doc()

	If using @log_doc(), in the method doc string, write (remove the -):

	"""
	- :log message: Gathering debug output...
	- :log level: DEBUG
	"""

	Must be placed above the @current_app_injector decorator.
	'''
	def log_doc_decorator(function):
		@wraps(function)
		def decorator(*_args, **_kwargs):
			message_prefix = '\t:log message: '
			level_prefix = '\t:log level: '

			level = kwargs.pop('level', 'INFO')

			if args:
				message = args[0]
			else:
				message = ''

				for line in function.__doc__.splitlines():
					if message_prefix in line:
						message = line.replace(message_prefix, '')

					if level_prefix in line:
						level = line.replace(level_prefix, '')
						level = level.replace(' ', '')

			level = getattr(logging, level)

			prefix = '{}.{}'.format(getmodule(function).__name__, function.__name__)
			log = logging.getLogger(prefix)

			log.log(level, message)

			return function(*_args, **_kwargs)
		return decorator

	if callable(args):
		return log_doc_decorator(args)
	else:
		return log_doc_decorator
