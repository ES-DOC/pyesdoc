import os

from pyesdoc.cv.model import Authority
from pyesdoc.cv.model import Term
from pyesdoc.cv.io_mgr.read import read_authority
from pyesdoc.cv.io_mgr.write import write_authority



def delete_authority(authority):
    """Deletes authority CV data from file system.

    """
    if not isinstance(authority, Authority):
        raise ValueError("Invalid authority: unknown type")

    if authority.io_path:
        os.remove(authority.io_path)


def delete_term(term):
    """Deletes term CV data from file system.

    """
    if not isinstance(term, Term):
        raise ValueError("Invalid term: unknown type")

    if term.io_path:
        os.remove(term.io_path)


