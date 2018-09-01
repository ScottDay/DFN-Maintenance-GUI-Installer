import json
import logging


log = logging.getLogger()


def load_json_file(url):
	log.debug('Parsing json file: "{}"'.format(url))

	json_data = open(url)
	package_json = json.load(json_data)
	json_data.close()

	return package_json
