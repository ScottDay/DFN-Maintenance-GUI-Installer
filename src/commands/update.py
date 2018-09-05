from src.util.logger import logger
from src.util.wrappers import wrapper
from src.util.json import load_json
from src.config import get_config


# TODO: Default to online, optionally pass a tar file or directory to check.
# TODO: Shutdown the project if an update is available.
# TODO: Option to just check for a new version. Don't download.
@wrapper
def update(args):
	"""
	Update the project to the latest version.
	"""
	conf = get_config()

	# Download and check version information.
	check_version(conf)


def check_version(conf):
	logger.debug('Checking versions')

	remote_version = load_json(conf.releaseUrl, keys = 'tag_name')
	local_version = load_json(conf.installerPath, conf.envFile, keys = 'version.release')

	return parse_tags(remote_version, local_version)


def parse_tags(remote, local):
	import re

	result = False

	logger.debug('Parsing version tags.')

	remote = re.sub('[^0-9]', '', remote)
	local = re.sub('[^0-9]', '', local)

	logger.debug('Remote / local versions v{0}:v{1}'.format(remote, local))

	if remote > local:
		result = True

	return result
