from json.encoder import JSONEncoder
from json.decoder import JSONDecoder

from .auto_attr_dict import AutoAttrDict


def get_encoder():
	return JSONEncoder(skipkeys = False,
						ensure_ascii = False,
						check_circular = True,
						allow_nan = True,
						indent = 4,
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
	decoder = JSONDecoder(object_hook = object_hook,
							parse_float = None,
							parse_int = None,
							parse_constant = None,
							object_pairs_hook = None)

	return decoder.decode(s)


# Json gives us unicode strings. This hook makes them strings.
def object_hook(d):
	result = {}

	for key, value in d.items():
		result[key] = value

	return result


def convert_dict(d):
	for key, value in d.items():
		if isinstance(value, dict):
			d[str(key)] = convert_dict(value)

	return AutoAttrDict(d)


def reset_modified(conf):
	conf.__dict__["_dirty"] = False

	for value in conf.values():
		if isinstance(value, AutoAttrDict):
			reset_modified(value)


def merge_dict(base, dev):
	result = {}

	for key, value in base.items():
		if dev[key]:
			result[str(key)] = dev[key]
		else:
			result[str(key)] = value

	for key, value in dev.items():
		if not base[key]:
			result[str(key)] = dev[key]

	return AutoAttrDict(result)
