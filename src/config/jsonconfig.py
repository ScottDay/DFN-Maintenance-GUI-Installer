import os
import sys

from .auto_attr_dict import AutoAttrDict
from .util import load, convert_dict, reset_modified, dump, merge_dict


# for python 2.x and 3.x compatibility
if sys.version_info.major == 3:
	unicode = str


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

	return convert_dict(d)


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
		base = get_config(filename)
		dev = get_config(init)

		return merge_dict(base, dev)

	if os.path.exists(filename):
		return read_config(filename)
	else:
		d = AutoAttrDict()
		write_config(d, filename)

		return d
