import re


_var_re = re.compile(r'\$([a-zA-Z0-9_\?]+|\{[^}]*\})')


class AutoAttrDict(dict):
	"""
	A dictionary with attribute-style access and automatic container node creation.
	"""
	def __init__(self, *args, **kwargs):
		dict.__init__(self, *args, **kwargs)
		self.__dict__["_dirty"] = False

	def __getstate__(self):
		return self.__dict__.items()

	def __setstate__(self, items):
		for key, val in items:
			self.__dict__[key] = val

	def __repr__(self):
		return "%s(%s)" % (self.__class__.__name__, dict.__repr__(self))

	def __str__(self):
		s = []

		if self:
			for key in self:
				val = self[key]

				if isinstance(val, AutoAttrDict):
					s.append("{:>22s}=[AutoAttrDict()]".format(key))
				else:
					s.append("{:>22s}={!r}".format(key, val))
		else:
			s.append("{[empty]}")

		if self.__dict__["_dirty"]:
			s.append("  (modified)")

		return "\n".join(s)

	def __setitem__(self, key, value):
		self.__dict__["_dirty"] = True
		return super(AutoAttrDict, self).__setitem__(key, value)

	def __getitem__(self, name):
		try:
			return super(AutoAttrDict, self).__getitem__(name)
		except KeyError:
			d = AutoAttrDict()
			super(AutoAttrDict, self).__setitem__(name, d)

			return d

	def __delitem__(self, name):
		self.__dict__["_dirty"] = True
		return super(AutoAttrDict, self).__delitem__(name)

	__getattr__ = __getitem__
	__setattr__ = __setitem__
	__delattr__ = __delitem__

	def copy(self):
		return AutoAttrDict(self)

	# Perform shell-like variable expansion.
	def expand(self, value):
		if not isinstance(value, (str, unicode)):
			return value

		if '$' not in value:
			return value

		ii = 0

		while 1:
			mo = _var_re.search(value, ii)

			if not mo:
				return value

			ii, jj = mo.span(0)
			oname = vname = mo.group(1)

			if vname.startswith('{') and vname.endswith('}'):
				vname = vname[1:-1]

			tail = value[jj:]
			value = value[:ii] + str(self.get(vname, "$" + oname))
			ii = len(value)
			value += tail

	def add_container(self, name):
		d = AutoAttrDict()
		super(AutoAttrDict, self).__setitem__(name, d)
		self.__dict__["_dirty"] = True

		return d
