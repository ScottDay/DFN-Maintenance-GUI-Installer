import json

from src import log


def load_json_file(url):
	try:
		log.debug('Parsing json file: {}'.format(url))

		json_data = open(url)
		package_json = json.load(json_data)
		json_data.close()

		return package_json
	except FileNotFoundError as error:
		log.error(error)

		raise ValueError('Error while parsing json file: {}'.format(url))
