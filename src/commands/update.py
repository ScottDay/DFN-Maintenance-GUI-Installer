import re

from src.util.logger import logger, section, debug
from src.util.wrappers import wrapper
from src.util.json import load_json


__all__ = ['update']


# TODO: Default to online, optionally pass a tar file or directory to check.
# TODO: Shutdown the project if an update is available.
@wrapper
def update(args):
	"""
	Update the project to the latest version.
	"""
	update = check_version(args.conf)

	if not args.dry:
		download_update(args.conf)


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


@section('Downloading update')
def download_update(conf):
	logger.debug('test...')
