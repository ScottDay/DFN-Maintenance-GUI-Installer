from src import log
from src.commands import common


@common
def restart(args):
	"""
	Restart the GUI.
	"""
	log.debug('restart')
