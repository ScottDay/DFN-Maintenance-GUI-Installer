from argh import arg, expects_obj

from src import log, common


# TODO: Default to online, optionally pass a tar file or directory to check.
# TODO: Shutdown the project if an update is available.
# TODO: Option to just check for a new version. Don't download.
@common
def update(args):
	"""
	Update the project to the latest version.
	"""
	log.debug('update')
