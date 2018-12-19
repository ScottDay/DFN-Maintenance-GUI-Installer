from src.util.wrappers import wrapper, logger, injector


@wrapper
@logger('Start')
@injector
def start(args, log):
	"""Start the GUI."""
	log.debug('TODO: Implement start...')

