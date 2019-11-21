"""
.. module:: pyesdoc.mp.ontologies.core.schema_validation.type_validator
   :platform: Unix, Windows
   :synopsis: Validates ontology type definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from . import class_validator
from . import enum_validator
from pyesdoc.mp.ontologies.schemas import utils



# Whitelist of valid types.
_TYPE_WHITELIST = {'class', 'enum'}

# Whitelist of injected types.
_INJECTED_TYPES_WHITELIST = {'shared.doc_reference',}


def _validate_base_class_references(ctx):
    """Validates base class references.

    """
    valid_classes = [ctx.get_type_name(factory, module)
                     for module, factory, cls in ctx.classes]

    for module, factory, cls in ctx.classes:
        if 'base' in cls and cls['base'] is not None and cls['base'] not in valid_classes:
            err = 'Invalid class: {0} --> base class "{1}" is unrecognized'
            err = err.format(ctx.get_name(factory, module), cls['base'])
            ctx.set_error(err)


def _validate_class_property_type_references(ctx):
    """Validates base class references.

    """
    valid_types = ctx.get_valid_types()
    for module, factory, cls in ctx.classes:
        for name, typeof in ctx.get_class_property_types(cls):
            typeof, qualifier = utils.parse_type(typeof)
            if typeof in _INJECTED_TYPES_WHITELIST:
                continue
            if typeof not in valid_types:
                err = 'Invalid class property: {0}.[{1}] --> '
                err += 'type reference "{2}" is unrecognized'
                err = err.format(ctx.get_name(factory, module), name, typeof)
                ctx.set_error(err)
            if qualifier and qualifier not in valid_types:
                print name, typeof, qualifier
                # for t in valid_types:
                #     print t
                err = 'Invalid linked_to qualifier: {0}.[{1}] --> '
                err += 'type reference "{2}" is unrecognized'
                err = err.format(ctx.get_name(factory, module), name, qualifier)
                ctx.set_error(err)


def _validate_type(ctx, module, factory, type_):
    """Asserts package types.

    """
    if not factory.__doc__ or not factory.__doc__.strip():
        err = 'Invalid type: {} --> must specify a doc string'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if 'type' not in type_:
        err = 'Invalid type: {} --> must specify a type attribute'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if type_['type'] not in _TYPE_WHITELIST:
        err = 'Invalid type: {0} --> type attribute must be in {1}'
        err = err.format(ctx.get_name(factory, module), _TYPE_WHITELIST)
        ctx.set_error(err)
        return

    if type_['type'] == 'class':
        class_validator.validate(ctx, module, factory, type_)

    if type_['type'] == 'enum':
        enum_validator.validate(ctx, module, factory, type_)


def validate(ctx):
    """Asserts package types.

    """
    for module, factory, type_ in ctx.types:
        _validate_type(ctx, module, factory, type_)
    _validate_base_class_references(ctx)
    _validate_class_property_type_references(ctx)
