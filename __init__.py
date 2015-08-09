__author__ = 'James Veitch'

import sys

import os

this_file = os.path.abspath(__file__)
this_dir = os.path.dirname(this_file)

# Add the current project root to the system path
sys.path.append(this_dir)

# Load settings
try:
    import config
except Exception as e:
    print(e)
    sys.exit(1)


def update_settings(**kwargs):
    """ Override the default / local settings in a constructor.

        Allows a post-initialisation update of the main settings using keyword args **kwargs
    """
    for key in kwargs:
        config.SETTINGS.__dict__[key] = kwargs[key]


if __name__ == '__main__':
    if not config.SETTINGS.DEBUG:
        config.print_settings()