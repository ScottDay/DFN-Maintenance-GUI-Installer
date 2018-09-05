from src.util.logger import logger, section
from src.util.wrappers import wrapper

from .check_version import check_version
from .download_update import download_update


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
