import enum
import inspect

import pyesdoc


def _has_class(mod, cls):
    """Asserts that a container exposes a class.

    """
    _has_member(mod, cls)
    assert inspect.isclass(getattr(mod, cls)), "{} is not a class".format(cls)


def _has_constant(mod, constant):
    """Asserts that a container exposes a constant.

    """
    _has_member(mod, constant)


def _has_enum(mod, enm):
    """Asserts that a container exposes an enumeration.

    """
    _has_member(mod, enm)
    assert issubclass(getattr(mod, enm), enum.Enum), "{} is not an enum".format(enm)


def _has_exception(mod, err):
    """Asserts that a container exposes an exception.

    """
    _has_class(mod, err)
    assert issubclass(getattr(mod, err), Exception), \
           "Exception type does not inherit from builtin Exception class."


def _has_function(mod, func):
    """Asserts that a container exposes a function.

    """
    _has_member(mod, func)
    assert inspect.isfunction(getattr(mod, func)), "{} is not a function".format(func)


def _has_member(mod, member):
    """Asserts that a module exposes a member.

    """
    assert inspect.ismodule(mod)
    assert hasattr(mod, member), "Missing member: {}".format(member)


# Expected interface.
_INTERFACE_OF_LIBRARY = {
    _has_class: set(),
    _has_enum: set(),
    _has_constant: set(),
    _has_exception: set(),
    _has_function: set(),
    _has_member: set()
}


def test_version_of_library():
    assert pyesdoc.__version__ == "1.0.0.0"


def test_exports_of_library():
    for assertor, members in _INTERFACE_OF_LIBRARY.items():
        for member in members:
            assertor(pyesdoc, member)


def _test_exports(module, interface):
    for assertor, members in interface.items():
        for member in members:
            assertor(module, member)
