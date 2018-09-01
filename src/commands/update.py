import re

from src.util import load_json_file
from .shared import wrapper, log


# TODO: Default to online, optionally pass a tar file or directory to check.
# TODO: Shutdown the project if an update is available.
# TODO: Option to just check for a new version. Don't download.
@wrapper
def update(args):
	"""
	Update the project to the latest version.
	"""
	# Download and check version information.
	check_version()


def check_version():
	log.debug('Checking versions')

	result = False

	downloaded_json = download_json('https://api.github.com/repos/ScottDay/DFN-Maintenance-GUI/releases/latest')
	# TODO: Give path to project install dir, load env.json.
	package_json = load_json_file('')

	log.debug('Parsing local and remote version tags.')
	remote_version = downloaded_json['tag_name']
	remote_version = re.sub('[^0-9]', '', remote_version)

	local_version = package_json['version']
	local_version = re.sub('[^0-9]', '', local_version)

	log.debug('Remote version: v{}'.format(remote_version))
	log.debug('Local version: v{}'.format(local_version))

	if remote_version > local_version:
		result = True

	return result


def download_json(url):
	# https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3#answer-7244263
	from urllib import request
	import json

	# Download from url.
	response = request.urlopen(url)
	data = response.read()
	text = data.decode('utf-8')

	# Load json.
	return json.loads(text)
