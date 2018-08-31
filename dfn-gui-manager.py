#!/usr/bin/python3.6

import logging

from argh import ArghParser

from src import log
from src.update import update
from src.start import start
from src.stop import stop
from src.restart import restart


def init_logger():
	logging.basicConfig(
		level = logging.INFO,
		format = "[%(asctime)s] [%(levelname)s] %(message)s",
		datefmt = '%Y-%m-%d %H:%M:%S')


def package_info():
	try:
		import json

		json_data = open('package.json')
		package_file = json.load(json_data)
		json_data.close()

		description = package_file['description']
		version = 'v' + package_file['version']
		epilog = '''
author:  {0}
version: {1}
license: {2}
url:     {3}
		'''.format(package_file['author'], version, package_file['license'], package_file['repository']['url'])
	except FileNotFoundError as error:
		description = 'Could not load description...'
		epilog = 'Could not load epilog...'
		version = 'Could not load version...'

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
		log.critical('Error! Exiting...')
	else:
		log.info('Success! Exiting...')

	logging.shutdown()


if __name__ == '__main__':
	main()
