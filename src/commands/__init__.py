"""Common CLI arguments across the src module."""
import logging

from argh import arg, expects_obj, wrap_errors
from functools import wraps

from src import log


def common(function):
	@arg('-s', '--silent', default = False, help = 'Suppress all output.')
	@arg('-d', '--debug', default = False, help = 'Log all debug output.')
	@wrap_errors([ValueError])
	@expects_obj
	@wraps(function)
	def wrapper(*args, **kwds):
		if args[0].silent:
			logging.disabled = True

		if args[0].debug:
			log.setLevel(logging.DEBUG)

		return function(*args, **kwds)

	return wrapper
