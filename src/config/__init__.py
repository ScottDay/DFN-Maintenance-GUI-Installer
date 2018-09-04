from .jsonconfig import get_config, read_config, write_config, is_modified

__all__ = ['get_config', 'read_config', 'write_config', 'is_modified']


# Usage.
# cf = get_config()
# cf.parts.program.flags.flagname = 2
# write_config(cf, "/tmp/testjson.json")
# cf = read_config("/tmp/testjson.json")
