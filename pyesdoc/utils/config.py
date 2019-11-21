"""
.. module:: utils.config.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Configuration utility functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
import os

from pyesdoc.utils.convert import json_file_to_namedtuple
from pyesdoc.utils.logger import log



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


def init():
    """Initializes configuration.

    """
    global data

    # Escape if config data already initialized.
    if data is not None:
        return

    # Attempt to load config.
    config_path = _init_from_local_config() or \
                  _init_from_user_home() or \
                  _init_from_shell_config()

    if not config_path:
        raise RuntimeError("""
            WARNING :: pyesdoc configuration file not found.
            If running pyesdoc within ES-DOC shell the config file location should be:
                SHELL-HOME/ops/config/pyesdoc.conf.
            If running pyesdoc in standalone mode the config file location should be:
                $HOME/.pyesdoc
            Otherwise:
                1.  Download the following default configuration file:
                    http://bit.ly/2g3NUmQ
                2.  Copy downloaded file to $HOME/.pyesdoc
            If this problem persists them contact es-doc-support@list.woc.noaa.gov
        """)

    log("Loading pyesdoc config from: {}".format(config_path))
    data = json_file_to_namedtuple(config_path)
