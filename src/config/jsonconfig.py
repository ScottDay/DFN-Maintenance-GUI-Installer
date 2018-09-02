# https://github.com/kdart/pycopia/blob/master/core/pycopia/basicconfig.py
# https://github.com/kdart/pycopia/blob/master/core/etc/logging.conf.dist

"""
Config object backed by a JSON encoded file.
"""

import sys
import os

from json.encoder import JSONEncoder
from json.decoder import JSONDecoder

from src.config.auto_attr_dict import AutoAttrDict


# for python 2.x and 3.x compatibility
if sys.version_info.major == 3:
	unicode = str


def get_encoder():
	return JSONEncoder(skipkeys = False,
						ensure_ascii = False,
						check_circular = True,
						allow_nan = True,
						indent = 2,
						separators = (',', ': '))

def dump(conf, fo):
	encoder = get_encoder()

	for chunk in encoder.iterencode(conf):
		fo.write(chunk)


def dumps(conf):
	encoder = get_encoder()
	return encoder.encode(conf)


def load(fo):
	s = fo.read()
	return loads(s)


def loads(s):
	decoder = JSONDecoder(object_hook = _object_hook,
							parse_float = None,
							parse_int = None,
							parse_constant = None,
							object_pairs_hook = None)

	return decoder.decode(s)


# Json gives us unicode strings. This hook makes them strings.
def _object_hook(d):
	result = {}

	for key, value in d.items():
		result[key] = value

	return result


def _convert_dict(d):
	for key, value in d.items():
		if isinstance(value, dict):
			d[str(key)] = _convert_dict(value)

	return AutoAttrDict(d)


def reset_modified(conf):
	conf.__dict__["_dirty"] = False

	for value in conf.values():
		if isinstance(value, AutoAttrDict):
			reset_modified(value)


def is_modified(conf):
	result = False

	if conf.__dict__["_dirty"]:
		result = True

	for value in conf.values():
		if isinstance(value, AutoAttrDict):
			if is_modified(value):
				result = True

	return result


def read_config(path_or_file):
	"""
	Read a JSON config file.
	"""
	if isinstance(path_or_file, (str, unicode)):
		fp = open(path_or_file, "r")
		doclose = True
	else:
		fp = path_or_file
		doclose = False

	d = load(fp)

	if doclose:
		fp.close()

	return _convert_dict(d)


def write_config(conf, path_or_file = 'config/config.json'):
	"""
	Write a JSON config file.
	"""
	if isinstance(path_or_file, (str, unicode)):
		fp = open(path_or_file, "w+")
		doclose = True
	else:
		fp = path_or_file
		doclose = False

	reset_modified(conf)
	dump(conf, fp)

	if doclose:
		fp.close()


def get_config(filename = 'config/config.json', init = None):
	"""
	Get an existing or new json config object.

	Optionally initialize from another dictionary.
	"""
	if init is not None:
		return _convert_dict(init)

	if os.path.exists(filename):
		return read_config(filename)
	else:
		d = AutoAttrDict()
		write_config(d, filename)

		return d
