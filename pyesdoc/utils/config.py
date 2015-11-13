# -*- coding: utf-8 -*-

"""
.. module:: utils.config.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Configuration utility functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
import os

from pyesdoc.utils.convert import json_file_to_namedtuple
from pyesdoc.utils. runtime import log



# Users home directory.
_HOME = os.path.expanduser("~")

# Default configuration file path.
_CONFIG_FPATH = "pyesdoc.conf"

# Configuration data.
data = None


def _init_from_shell_config():
    """Attempts to initialize configuration from the shell.

    """
    # Find.
    dir_path = os.path.dirname(os.path.abspath(__file__))
    while dir_path != '/':
        config_path = os.path.join(dir_path, "ops/config/pyesdoc.conf")
        if os.path.exists(config_path):
            return config_path
        dir_path = os.path.dirname(dir_path)


def _init_from_local_config():
    """Attempts to initialize configuration from local file system.

    """
    # Find.
    dir_path = os.path.dirname(os.path.abspath(__file__))
    while dir_path != '/':
        config_path = os.path.join(dir_path, "pyesdoc.conf")
        if os.path.exists(config_path):
            return config_path
        dir_path = os.path.dirname(dir_path)


def _init_from_user_home():
    """Attempts to initialize configuration from a file foud on user's home directory.

    """
    config_path = os.path.join(_HOME, ".pyesdoc")
    if os.path.exists(config_path):
        return config_path


def _init():
    """Initializes configuration.

    """
    global data

    # Attempt to load config from file system.
    for func in (
        _init_from_local_config,
        _init_from_user_home,
        _init_from_shell_config,
        ):
        config_path = func()
        if config_path:
            log("Loading pyesdoc config from: {}".format(config_path))
            break

    # Decode.
    if config_path:
        data = json_file_to_namedtuple(config_path)

    # Warn
    else:
        msg = """
            WARNING :: pyesdoc configuration file not found.
            If you are running pyesdoc as part of the ES-DOC shell then the config file location should be:
                SHELL-HOME/ops/config/pyesdoc.conf.
            If you are running pyesdoc as part of the ES-DOC notebook-shell then the config file location should be:
                SHELL-HOME/pyesdoc.conf.
            If you are running pyesdoc in standalone mode then the config file location should be:
                $HOME/.pyesdoc
            If neither of these files exist then:
                1.  Download the following default configuration file:
                    https://raw.githubusercontent.com/ES-DOC/esdoc-shell/master/resources/user/template-pyesdoc.conf
                2.  Copy downloaded file to $HOME/.pyesdoc
            If this problem persists them contact es-doc-support@list.woc.noaa.gov
        """
        raise RuntimeError(msg)


# Auto-initialize.
# _init()
