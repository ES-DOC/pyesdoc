"""
.. module:: archive_organize.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Organizes document archive.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import sys

import pyesdoc



def _main():
    """Main entry point."""
    # Unpack throttle param.
    try:
        throttle = int(sys.argv[1])
    except IndexError:
        throttle = 0
    except ValueError:
        msg = "Archive organization throttle must be a positive integer value"
        raise ValueError(msg)

    # Organize.
    pyesdoc.archive.organize(throttle)


# Entry point.
if __name__ == '__main__':
    _main()
