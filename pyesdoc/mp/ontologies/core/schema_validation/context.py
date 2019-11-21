"""
.. module:: pyesdoc.mp.ontologies.core.schema_validation.context
   :platform: Unix, Windows
   :synopsis: Contextual information passed to a validator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect



class ValidationContext(object):
    """Encapsulates schema validation processing information.

    """
    def __init__(self, schema):
        """Instance constructor.

        """
        self.schema = schema
        self.report = list()


    def set_error(self, err):
        """Adds an error to the manged collection.

        """
        self.report.append(err)


    @property
    def schema_name(self):
        """Gets schema name.

        """
        return self.schema.NAME


    @property
    def schema_version(self):
        """Gets schema version.

        """
        return "v{}".format(self.schema.VERSION)


    @property
    def package_factories(self):
        """Gets package factories.

        """
        return self.get_functions(self.schema)


    @property
    def packages(self):
        """Gets package definitions.

        """
        result = list()
        for factory in self.package_factories:
            try:
                result.append((factory, factory()))
            except Exception as err:
                pass

        return sorted([p for p in result if isinstance(p[1], set) and len(p[1])])


    @property
    def type_modules(self):
        """Gets type modules.

        """
        result = list()
        for factory, modules in self.packages:
            result += [(factory, m) for m in modules
                       if inspect.ismodule(m) and self.get_functions(m)]

        return sorted(result)


    @property
    def type_factories(self):
        """Gets type factories.

        """
        result = list()
        for factory, module in self.type_modules:
            result += [(module, f) for f in self.get_functions(module)]

        return sorted(result)


    @property
    def types(self):
        """Gets type definitions.

        """
        result = list()
        for module, factory in self.type_factories:
            try:
                type_ = factory()
            except Exception as err:
                pass
            else:
                if isinstance(type_, dict):
                    result.append((module, factory, type_))

        return sorted(result)


    @property
    def classes(self):
        """Get class definitions.

        """
        return [(t[0], t[1], t[2]) for t in self.types
                if 'type' in t[2] and t[2]['type'] == 'class']


    @property
    def enums(self):
        """Get enum definitions.

        """
        return [(t[0], t[1], t[2]) for t in self.types
                if 'type' in t[2] and t[2]['type'] == 'enum']


    def get_name(self, factory, module=None):
        """Gets a name used when displaying an error message.

        """
        if module is None or module == self.schema:
            return "{0}.v{1}.{2}".format(
                self.schema.NAME,
                self.schema.VERSION,
                factory.__name__)
        else:
            return "{0}.v{1}.{2}.{3}".format(
                self.schema.NAME,
                self.schema.VERSION,
                self.get_package_name(module),
                factory.__name__)


    def get_package_name(self, module):
        """Returns name of a package from a module.

        """
        return module.__name__.split('.')[-1].split('_')[0]


    def get_class_property_types(self, cls):
        """Returns class property type definitions.

        """
        return [(p[0], p[1]) for p in cls.get('properties', [])
                if len(p[1].split(".")) > 1]


    def get_type_name(self, factory, module):
        """Gets a type name.

        """
        return "{0}.{1}".format(
            self.get_package_name(module),
            factory.__name__)


    def get_functions(self, module):
        """Returns a collection of function pointers declared within a module.

        """
        return sorted({ m[1] for m in inspect.getmembers(module) if inspect.isfunction(m[1]) })


    def get_valid_types(self):
        """Return set of valid types.

        """
        return [self.get_type_name(defn[1], defn[0]) for defn in self.types]
