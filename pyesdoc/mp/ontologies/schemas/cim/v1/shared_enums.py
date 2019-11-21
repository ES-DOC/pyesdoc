"""
.. module:: shared_enums.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 shared package enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def change_property_type():
    """Creates and returns instance of change_property_type enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('InputMod', None),
            ('ModelMod', None),
            ('Decrement', None),
            ('Increment', None),
            ('Redistribution', None),
            ('Replacement', None),
            ('ParameterChange', 'A specific type of ModelMod'),
            ('CodeChange', 'A specific type of ModelMod'),
            ('AncillaryFile', 'A specific type of ModelMod'),
            ('BoundaryCondition', 'A specific type of ModelMod'),
            ('InitialCondition', 'A specific type of ModelMod'),
            ('Unused', None),
        ],
    }


def compiler_type():
    """Creates and returns instance of compiler_type enum.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def data_purpose():
    """Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('ancillaryFile', None),
            ('boundaryCondition', None),
            ('initialCondition', None),
        ],
    }


def interconnect_type():
    """A list of connectors between machines.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def machine_type():
    """A list of known machines.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('Parallel', None),
            ('Vector', None),
            ('Beowulf', None),
        ],
    }


def machine_vendor_type():
    """A list of organisations that create machines.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def operating_system_type():
    """A list of common operating systems.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def processor_type():
    """A list of known cpu's.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


def unit_type():
    """A list of scientific units.

    """
    return {
        'type' : 'enum',
        'is_open' : True
    }


