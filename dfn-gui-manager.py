#!/usr/bin/python3.6

from argh import arg, aliases, ArghParser, expects_obj


def update():
	"""Update command."""


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
	description, epilog, version = package_info()

	parser = ArghParser(description = description, epilog = epilog)
	parser.add_commands([update])
	parser.add_argument('--version', action = 'version', version = version)
	parser.dispatch()


if __name__ == '__main__':
	main()
