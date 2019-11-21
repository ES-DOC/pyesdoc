"""
.. module:: pyesdoc.mp.ontologies.core.schema_validation.enum_validator
   :platform: Unix, Windows
   :synopsis: Validates ontology enum definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import re



# Regular expressions.
_RE_ENUM_NAME = '^[a-z_]+$'
_RE_ENUM_MEMBER_NAME = '^[a-zA-Z0-9-_ \.\:+]+$'


def _validate_enum_member(ctx, module, factory, enum, name, doc_string):
    """Validates an enumeration member.

    """
    if not re.match(_RE_ENUM_MEMBER_NAME, name):
        err = 'Invalid enum member: {0}.{1} --> name contain invalid characters'
        err = err.format(ctx.get_name(factory, module), name)
        ctx.set_error(err)

    if doc_string is not None and not len(doc_string.strip()):
        err = 'Invalid enum member: {0}.{1} --> doc string must be either None or a string'
        err = err.format(ctx.get_name(factory, module), name)
        ctx.set_error(err)


def validate(ctx, module, factory, enum):
    """Validates an enumeration.

    """
    if not re.match(_RE_ENUM_NAME, factory.__name__):
        err = 'Invalid enum: {} --> name format must be lower_case_underscore'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if 'is_open' not in enum:
        err = 'Invalid enum: {} --> required attribute "is_open" is missing'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if not isinstance(enum['is_open'], bool):
        err = 'Invalid enum: {} --> "is_open" attribute must be a boolean'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)

    if 'members' in enum and not isinstance(enum['members'], list):
        err = 'Invalid enum: {} --> "members" attribute must be a list'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if [m for m in enum.get('members', []) if not isinstance(m, tuple) or not len(m) == 2]:
        err = 'Invalid enum: {} --> all members must be 2 item tuples (name, doc_string)'
        err = err.format(ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    for m in enum.get('members', []):
        _validate_enum_member(ctx, module, factory, enum, m[0], m[1])
