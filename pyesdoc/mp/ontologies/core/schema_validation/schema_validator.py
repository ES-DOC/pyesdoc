"""
.. module:: pyesdoc.mp.ontologies.core.schema_validation.schema_validator
   :platform: Unix, Windows
   :synopsis: Validates ontology schema definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect
import re



# Regular expressions.
_RE_SCHEMA_NAME = '^[a-z_]+$'
_RE_SCHEMA_VERSION = '^[0-9\.]+$'


def _validate_package_factory(ctx, module, factory, expected_type, type_description):
    """Validates a package factory function.

    """
    try:
        instance = factory()
    except:
        err = 'Invalid {0}: {1} --> must be a no-arg callable'
        err = err.format(type_description, ctx.get_name(factory, module))
        ctx.set_error(err)
        return

    if not isinstance(instance, expected_type):
        err = 'Invalid {0}: {1} --> unexpected return type (was expecting {2})'
        err = err.format(type_description, ctx.get_name(factory, module), expected_type.__name__)
        ctx.set_error(err)
        return

    if not len(instance):
        err = 'Invalid {0}: {1} --> must not return an empty collection'
        err = err.format(type_description, ctx.get_name(factory, module))
        ctx.set_error(err)


def validate(ctx):
    """Validates schema level attributes.

    :param pyesdoc.mp.ontologies.core.schema_validation.ValidationContext: Contextutal information passed between validators.

    """
    if not inspect.ismodule(ctx.schema):
        ctx.set_error('Invalid schema --> must be python modules.')
        return

    if not hasattr(ctx.schema, 'NAME'):
        ctx.set_error('Invalid schema --> required attribute NAME is missing')

    if not hasattr(ctx.schema, 'VERSION'):
        ctx.set_error('Invalid schema --> required attribute VERSION is missing')

    if not hasattr(ctx.schema, 'DOC'):
        ctx.set_error('Invalid schema --> required attribute DOC is missing')

    if not ctx.package_factories:
        ctx.set_error('Invalid schema --> must declare at least one package')

    if ctx.report:
        return

    if ctx.schema.DOC is None or not ctx.schema.DOC.strip():
        ctx.set_error('Invalid schema --> required attribute DOC is missing')

    if not re.match(_RE_SCHEMA_NAME, ctx.schema.NAME):
        ctx.set_error('Invalid schema --> NAME must be a single word in lower case')

    if not re.match(_RE_SCHEMA_VERSION, ctx.schema.VERSION):
        ctx.set_error('Invalid schema --> VERSION must be a postive integer')

    for factory in ctx.package_factories:
        _validate_package_factory(ctx, ctx.schema, factory, set, 'package')
