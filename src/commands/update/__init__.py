from src.util.wrappers import wrapper, logger, injector
from .check_version import check_version
from .download_update import download_update

__all__ = ['update']


# TODO: Default to online, optionally pass a tar file or directory to check.
# TODO: Shutdown the project if an update is available.
# TODO: Compare requirements.txt files and see if dependencies need to be installed (any there are any differences).
# TODO: Self update command (seperate to gui update)
# TODO: Use this update command to update everything, specific commands for each project (update-installer, update-gui, etc.)
# TODO: Command to update to the dev version. Tie in with the specified projects dev version (installer dev version update, or gui dev version update).
# TODO: Command to use docker version.
# TODO: Place a installer config file in each project, use it to specify how to install and what commands to run.
@wrapper
@logger('Update')
@injector
def update(args):
	"""Update the project to the latest version."""

	update = check_version(args.conf)

	if not args.dry:
		download_update(args.conf)
