import logging


log = logging.getLogger()


def wrapper(function):
	from argh import arg, expects_obj, wrap_errors
	from functools import wraps

	@arg('-s', '--silent', default = False, help = 'Suppress all output.')
	@arg('-d', '--debug', default = False, help = 'Log all debug output.')
	@wrap_errors([Exception])
	@expects_obj
	@wraps(function)
	def wrapper(*args, **kwds):
		import logging

		log = logging.getLogger()

		if args[0].silent:
			logging.disabled = True

		if args[0].debug:
			log.setLevel(logging.DEBUG)

		return function(*args, **kwds)

	return wrapper
