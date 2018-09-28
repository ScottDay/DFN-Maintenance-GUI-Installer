#!/bin/sh
''''which python3.8 >/dev/null 2>&1 && exec python3.8 "$0" "$@" # '''
''''which python3.7 >/dev/null 2>&1 && exec python3.7 "$0" "$@" # '''
''''which python3.6 >/dev/null 2>&1 && exec python3.6 "$0" "$@" # '''
''''exec echo "Error: I can't find python3.[6|7|8] anywhere."   # '''

from argh import ArghParser

from src.extensions import init
from src.util.json import load_json
from src.util.logger import logging
from src.commands import update, start, stop, restart


def package_info():
	description = 'Could not load description...'
	epilog = 'Could not load epilog...'
	version = 'Could not load version...'

	package_json = load_json('package.json')

	if package_json is not None:
		description = package_json['description']
		version = 'v' + package_json['version']
		epilog = '''
author:  {0}
version: {1}
license: {2}
url:     {3}
		'''.format(package_json['author'],
					version,
					package_json['license'],
					package_json['repository']['url'])

	return description, epilog, version


# TODO: Command to check if it can be installed (correct python version, distribution, packages, maybe node / npm, etc.)
# TODO: Check out nvm (node version manager) for its commands and how it works.
# TODO: Rename project to maybe dfnvm, or dfn-gui-vm.
if __name__ == '__main__':
	"""
	Entry-point function.
	"""
	init()
	description, epilog, version = package_info()

	parent_parser = ArghParser(description = description, epilog = epilog)
	parent_parser.add_commands([update, start, stop, restart])
	parent_parser.add_argument('-v', '--version', action = 'version', version = version)

	parent_parser.dispatch()
	logging.shutdown()
