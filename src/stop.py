from argh import arg, expects_obj

from src import log, common


@common
def stop(args):
	"""
	Stop the GUI.
	"""
	log.debug('stop')
