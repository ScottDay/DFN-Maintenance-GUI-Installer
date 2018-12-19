from src.util.wrappers import wrapper, logger, injector


@wrapper
@logger('Restart')
@injector
def restart(args, log):
	"""Restart the GUI."""
	log.debug('TODO: Implement restart...')
