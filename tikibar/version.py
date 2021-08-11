from six.moves import map
__version_info__ = (0, 3, 0)
__version__ = '-'.join([_f for _f in ['.'.join(map(str, __version_info__[:3])), (__version_info__[3:] or [None])[0]] if _f])
