"""
.. module:: pyesdoc.mp.ontologies.core.schema_validation.package_validator
   :platform: Unix, Windows
   :synopsis: Validates ontology package definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect
import re



# Regular expressions.
_RE_PACKAGE_NAME = '^[a-z]+$'


def _validate_factory(ctx, module, factory, expected_type, type_description):
    """Validates a factory function.

    """
    try:
        instance = factory()
    except Exception as error:
        err = 'Invalid {0}: {1} --> type creation error occurred (type must be declared as a no-arg callable): {2}'
        err = err.format(type_description, ctx.get_name(factory, module), error)
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


def _validate(ctx, factory, modules):
    """Validates a package.

    """
    if not re.match(_RE_PACKAGE_NAME, factory.__name__):
        err = 'Invalid package: {} --> must be a single word in lower case'
        err = err.format(ctx.get_name(factory))
        ctx.set_error(err)

    if not factory.__doc__ or not factory.__doc__.strip():
        err = 'Invalid package: {} --> must have a doc string'
        err = err.format(ctx.get_name(factory))
        ctx.set_error(err)
        return

    if not len(modules):
        err = 'Invalid package: {} --> must have at least one package type module'
        err = err.format(ctx.get_name(factory))
        ctx.set_error(err)
        return

    for module in modules:
        if not inspect.ismodule(module):
            err = 'Invalid package: {} --> all package type modules must be defined as python modules'
            err = err.format(ctx.get_name(factory))
            ctx.set_error(err)
            continue

        if not ctx.get_functions(module):
            err = 'Invalid package: {} --> all package type modules must contain at least one type factory'
            err = err.format(ctx.get_name(factory))
            ctx.set_error(err)
            continue

        for type_factory in  ctx.get_functions(module):
            _validate_factory(ctx, module, type_factory, dict, 'type')


def validate(ctx):
    """Validates package level attributes.

    """
    for factory, modules in ctx.packages:
        _validate(ctx, factory, modules)
