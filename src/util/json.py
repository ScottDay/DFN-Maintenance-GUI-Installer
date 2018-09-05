import json

from urllib.request import urlopen
from os.path import abspath

from .misc import log


__all__ = ['load_json']


def load_json(*url, keys = None):
	url = ''.join(url)

	log.debug('Loading json file: "{0}"'.format(url))

	if not any(value in url for value in ('http://', 'https://', 'file://')):
		url = 'file://' + abspath(url)

	with urlopen(url) as json_data:
		if url in ('http://', 'https://'):
			data = json.loads(json_data.read().decode('utf-8'))
		else:
			data = json.load(json_data)

	return _load_json(data, keys)


def _load_json(data, keys):
	if keys is not None:
		keys = keys.split('.')

		for key in keys:
			data = data[key]

	return data
