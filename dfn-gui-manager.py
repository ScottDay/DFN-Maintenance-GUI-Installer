#!/usr/bin/python3.6

import logging

from argh import ArghParser

from src import log
from src.util import load_package_json
from src.commands.update import update
from src.commands.start import start
from src.commands.stop import stop
from src.commands.restart import restart


def init_logger():
	logging.basicConfig(
		level = logging.INFO,
		format = "[%(asctime)s] [%(levelname)s] %(message)s",
		datefmt = '%Y-%m-%d %H:%M:%S')


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


def main():
	"""Entry-point function."""

	init_logger()

	try:
		description, epilog, version = package_info()

		parent_parser = ArghParser(description = description, epilog = epilog)
		parent_parser.add_commands([update, start, stop, restart])
		parent_parser.add_argument('-v', '--version', action = 'version', version = version)
		parent_parser.dispatch()
	except Exception as error:
		log.critical(error)
		log.critical('Error! Exiting...')
	else:
		log.debug('Success! Exiting...')

	logging.shutdown()


if __name__ == '__main__':
	main()
