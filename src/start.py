from argh import arg

from src import log, silent, debug, common_handler


@silent
@debug
@expects_obj
@common_handler
def start(args):
	"""
	Start the GUI.
	"""
	print('start')
