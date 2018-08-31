"""Common CLI arguments across the src module."""
import logging

from argh import arg
from functools import wraps


log = logging.getLogger()

silent = arg('-s', '--silent', default = False, help = 'Suppress all output.')
debug = arg('-d', '--debug', default = False, help = 'Log all debug output.')


def common_handler(function):
	@wraps(function)
	def wrapper(*args, **kwds):
		if args[0].silent:
			logging.disabled = True

		if args[0].debug:
			log.setLevel(logging.DEBUG)

		return function(*args, **kwds)

	return wrapper
