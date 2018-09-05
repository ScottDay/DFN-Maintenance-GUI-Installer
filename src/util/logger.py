import logging


logger = logging.getLogger()


def section(message):
	def decorator_log(function):
		from functools import wraps

		@wraps(function)
		def decorator(*args, **kwds):
			logger.debug("===== SECTION: {0} =====".format(message))

			return function(*args, **kwds)

		return decorator

	return decorator_log


def debug(message):
	def decorator_log(function):
		from functools import wraps

		@wraps(function)
		def decorator(*args, **kwds):
			logger.debug(message)

			return function(*args, **kwds)

		return decorator

	return decorator_log
