# -*- coding: utf-8 -*-

"""
.. module:: test_archive.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc document archive tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import pyesdoc
import test_utils as tu


def _test_archive_config():
    """Test archive configuration."""
    import pyesdoc.archive.config as cfg

    tu.assert_path(cfg.get_directory())
    tu.assert_int(cfg.get_projects(), 6)
    tu.assert_int(cfg.get_sources(), 4)
    tu.assert_int(cfg.get_projects()[0].feeds, 2)
    tu.assert_int(cfg.get_projects()[1].feeds, 1)
    tu.assert_int(cfg.get_projects()[2].feeds, 1)
    tu.assert_int(cfg.get_projects()[3].feeds, 1)
    tu.assert_int(cfg.get_projects()[4].feeds, 1)
    tu.assert_int(cfg.get_project_sources(), 7)


def _test_archive_doc_dirs():
    """Test archive document directories."""
    folders = list(pyesdoc.archive.yield_folders())
    for folder in folders:
        assert folder.exists, True


def _test_archive_get_counts():
    """Test archive document counts."""
    tu.assert_int(pyesdoc.archive.get_count(), 37019, assert_type=tu.COMPARE_LTE)


def test():
    """Runs set of archive unit tests."""
    for func in (
        _test_archive_config,
        _test_archive_doc_dirs,
        _test_archive_get_counts
        ):
        tu.init(func, func.__doc__[5:])
        yield func