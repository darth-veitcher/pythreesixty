__author__ = 'James Veitch'

from pprint import pprint
import argparse as ap

import yaml
import os



# Global variable
SETTINGS = None

# Load settings
this_file = os.path.abspath(__file__)
this_dir = os.path.dirname(this_file)


def print_settings():
    """ Dumps the current settings to stdout
    """
    pprint(SETTINGS.__dict__)


def reload_settings():
    """ Reloads settings from YAML config file
    """
    global SETTINGS
    try:
        # Load standard settings
        settings_dict = yaml.load(file(os.path.join(this_dir, 'settings.yml')))

        # Overwrite the standard settings and stores local / secret settings
        # Check if exists in users $HOME
        user_settings = os.path.join(os.path.expanduser('~'), '.{name}'.format(name=settings_dict['PACKAGE_NAME']),
                                     '{name}.yml'.format(name=settings_dict['PACKAGE_NAME']))
        if os.path.isfile(user_settings):
            settings_local = yaml.load(file(os.path.join(this_dir, 'settings.local.yml')))
        # Else see if there's one in the package config folder
        elif os.path.isfile(os.path.join(this_dir, 'settings.local.yml')):
            settings_local = yaml.load(file(os.path.join(this_dir, 'settings.local.yml')))
        if settings_local:
            for k in settings_local:
                settings_dict[k] = settings_local[k]  # overwrite key,value

        # Use a namespace from argparse so we can use dot notation for sanity's sake ...
        SETTINGS = ap.Namespace(**settings_dict)

    except Exception as e:
        print(e)

if not SETTINGS:
    # Called on first run (blank settings)
    reload_settings()

if SETTINGS.DEBUG:
    print_settings()