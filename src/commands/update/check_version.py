import re

from src.util.logger import logger, section, debug
from src.util.json import load_json


@section('Checking version tags')
def check_version(conf):
	local_version = load_json(conf.installerPath, conf.envFile, keys = 'version.release')
	remote_version = load_json(conf.releaseUrl, keys = 'tag_name')

	return parse_tags(local_version, remote_version)


@debug('Parsing version tags')
def parse_tags(local, remote):
	result = False

	local = re.sub('[^0-9]', '', local)
	remote = re.sub('[^0-9]', '', remote)

	logger.info('local:  v{0}'.format(local))
	logger.info('remote: v{0}'.format(remote))

	if remote > local:
		result = True

	return result
