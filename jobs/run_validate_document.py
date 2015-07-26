# -*- coding: utf-8 -*-

"""
.. module:: validate_document.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Validates a document held upon local file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime

from tornado.options import define, options

import pyesdoc



# Define command line options.
define("file", help="Path to file to be validated.")
define("outfile", help="Path to validation report output file.", default=None)


# Report banner.
_BANNER = "--------------------------------------\n"


def _emit(stream, report):
    """Emits report to an I/O stream.

    """
    def _write_header():
        """Writes report header.

        """
        stream(_BANNER)
        stream("ES-DOC Documentation Validation Report\n")
        stream(_BANNER)
        stream("Generated @ {0}\n".format(datetime.datetime.now()))
        stream("Target = {0}\n".format(options.file))
        stream(_BANNER)


    def _write_body():
        """Writes report body.

        """
        stream("------ VALIDATION REPORT BEGINS ------\n")
        stream("\n")
        for err in report:
            stream(str(err) + "\n")
        stream("\n")
        stream("\n------ VALIDATION REPORT ENDS --------")


    _write_header()
    _write_body()


def _emit_to_stdout(report):
    """Emits report to stdout.

    """
    _emit(pyesdoc.rt.log_warning, report)


def _emit_to_file_system(report):
    """Emits report to file system.

    """
    with open(options.outfile, 'w') as ofile:
        _emit(ofile.write, report)
    pyesdoc.rt.log("Validation report written to ---> {0}.".format(options.outfile))


def _main():
    """Main entry point.

    """
    # Open document & validate.
    doc = pyesdoc.read(options.file)
    report = pyesdoc.validate(doc)

    # Inform user of validation result.
    if report:
        if options.outfile:
            _emit_to_file_system(report)
        else:
            _emit_to_stdout(report)
    else:
        pyesdoc.rt.log("Documemt is valid.")



# Entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()