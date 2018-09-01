from src import log
from src.commands import common


@common
def stop(args):
	"""
	Stop the GUI.
	"""
	log.debug('stop')
