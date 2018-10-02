import re

from src.util.wrappers import logger, injector
from src.util.json import load_json


@logger('Checking version tags')
def check_version(conf):
	local_version = load_json(conf.installerPath, conf.envFile, keys = 'version.release')
	remote_version = load_json(conf.releaseUrl, keys = 'tag_name')

	return parse_tags(local_version, remote_version)


@logger('Parsing version tags')
@injector
def parse_tags(local, remote, log):
	result = False

	local = re.sub('[^0-9]', '', local)
	remote = re.sub('[^0-9]', '', remote)

	log.info('local:  v{0}'.format(local))
	log.info('remote: v{0}'.format(remote))

	if remote > local:
		result = True

	return result
