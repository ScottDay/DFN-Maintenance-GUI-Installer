from src.util.wrappers import logger, injector


@logger('Downloading update')
@injector
def download_update(conf, log):
	log.debug('test...')
