"""Common CLI arguments across the src module."""
from .update import update
from .start import start
from .stop import stop
from .restart import restart


__all__ = ['update', 'start', 'stop', 'restart']
