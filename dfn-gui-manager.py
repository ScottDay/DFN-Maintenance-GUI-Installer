#!/usr/bin/python3.6

import logging

from argh import ArghParser

from src.extensions import init
from src.util import load_json_file
from src.commands import update, start, stop, restart


def package_info():
	description = 'Could not load description...'
	epilog = 'Could not load epilog...'
	version = 'Could not load version...'

	package_json = load_json_file('package.json')

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


if __name__ == '__main__':
	"""Entry-point function."""
	init()
	description, epilog, version = package_info()

	parent_parser = ArghParser(description = description, epilog = epilog)
	parent_parser.add_commands([update, start, stop, restart])
	parent_parser.add_argument('-v', '--version', action = 'version', version = version)

	parent_parser.dispatch()
	logging.shutdown()
