"""Common CLI arguments across the src module."""
import logging

from argh import arg, expects_obj
from functools import wraps


log = logging.getLogger()


def common(function):
	@arg('-s', '--silent', default = False, help = 'Suppress all output.')
	@arg('-d', '--debug', default = False, help = 'Log all debug output.')
	@expects_obj
	@wraps(function)
	def wrapper(*args, **kwds):
		if args[0].silent:
			logging.disabled = True

		if args[0].debug:
			log.setLevel(logging.DEBUG)

		return function(*args, **kwds)

	return wrapper
