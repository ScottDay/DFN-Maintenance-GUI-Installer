from argh import arg, expects_obj

from src import log, common


@common
def restart(args):
	"""
	Restart the GUI.
	"""
	log.debug('restart')
