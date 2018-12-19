from src.util.wrappers import wrapper, logger, injector


@wrapper
@logger('Stop')
@injector
def stop(args, log):
	"""Stop the GUI."""
	log.debug('TODO: Implement stop...')

