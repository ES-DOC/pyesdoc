# -*- coding: utf-8 -*-

"""
.. module:: model.py
   :platform: Unix, Windows
   :synopsis: A repesentation of CMIP6 specializations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class Specialization(object):
    """Wraps a specialization.

    """
    def __init__(self, mod):
        """Instance constructor.

        """
        self.mod = mod


    @property
    def doc_name(self):
        """A simplified name useful in documentation scenrios.

        """
        name = self.name

        return " ".join(["{}{}".format(i[0].upper(), i[1:]) for i in name.split("_")])


class SpecializationModule(Specialization):
    """Wraps a standard specialization module.

    """
    def __init__(self, owner, mod, cfg_section):
        """Instance constructor.

        """
        super(SpecializationModule, self).__init__(mod)

        self.authors = mod.AUTHORS
        self.cfg_section = cfg_section
        self.contact = mod.CONTACT
        try:
            self.contributors = mod.CONTRIBUTORS
        except AttributeError:
            self.contributors = ""
        self.description = mod.DESCRIPTION
        self.full_name = mod.__name__.split(".")[-1]
        self.mod = mod
        self.qc_status = mod.QC_STATUS

        if owner:
            self.name = "_".join(mod.__name__.split(".")[-1].split("_")[1:])
            self.id = "{}.{}".format(owner.id, self.name)
        else:
            self.name = mod.REALM
            self.id = "cmip6.{}".format(self.name)
        self.name_camel_case = to_camel_case(self.name)
        self.name_camel_case_spaced = to_camel_case_spaced(self.name)

        try:
            self.mod.DETAILS
        except AttributeError:
            self.details = []
        else:
            self.details = [Detail(self.mod, self, i, j)
                            for i, j in self.mod.DETAILS.items()
                            if isinstance(j, dict)]

    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id),
            ("QC status", self.qc_status),
            ("Contact", self.contact),
            ("Authors", self.authors),
            ("Contributors", self.contributors)
        ]


class SpecializationDetailCollection(Specialization):
    """Wraps a detail collection, e.g. TUNNING_APPLIED.

    """
    def __init__(self, mod, owner, name, collection):
        """Instance constructor.

        """
        super(SpecializationDetailCollection, self).__init__(mod)

        details = getattr(mod, "{}_DETAILS".format(collection))
        obj = getattr(mod, collection)[name]

        self.id = "{}.{}".format(owner.id, name)
        self.description = obj['description']
        self.detail_keys = obj['details']
        self.details = [Detail(mod, self, i, j)
                        for i, j in details.items()
                        if isinstance(j, dict)]
        self.name = name
        self.owner = owner


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id),
        ]


class Realm(SpecializationModule):
    """Wraps a realm specialization.

    """
    def __init__(self, specializations, sort_collections=False):
        """Instance constructor.

        :param tuple specializations: Set of realm related specialization.

        """
        # Unpack specializations.
        mod, grid, key_properties, processes = specializations

        super(Realm, self).__init__(None, mod, "realm")

        self.grid = Grid(self, grid) if grid else None
        self.key_properties = KeyProperties(self, key_properties) if key_properties else None
        self.processes = [Process(self, i, sort_collections) for i in processes]


class Process(SpecializationModule):
    """Wraps a process specialization.

    """
    def __init__(self, realm, mod, sort_collections):
        """Instance constructor.

        """
        super(Process, self).__init__(realm, mod, "process")

        try:
            self.sub_processes = [SubProcess(self, i, j, sort_collections) for i, j in mod.SUB_PROCESSES.items()]
        except AttributeError:
            self.sub_processes = []


class Grid(SpecializationModule):
    """Wraps a grid specialization.

    """
    def __init__(self, realm, mod):
        """Instance constructor.

        """
        super(Grid, self).__init__(realm, mod, "grid")

        self.discretisation = GridDiscretisation(mod, self)


class GridDiscretisation(SpecializationDetailCollection):
    """Wraps a grid discretization specialization.

    """
    def __init__(self, mod, owner):
        """Instance constructor.

        """
        super(GridDiscretisation, self).__init__(
            mod, owner, "discretisation", "DISCRETISATION")


class KeyProperties(SpecializationModule):
    """Wraps a key properties specialization.

    """
    def __init__(self, owner, mod):
        """Instance constructor.

        """
        super(KeyProperties, self).__init__(owner, mod, "key-properties")

        try:
            self.conservation = KeyPropertiesConservation(mod, self)
        except KeyError:
            self.conservation = None
        try:
            self.extent = KeyPropertiesExtent(mod, self)
        except KeyError:
            self.extent = None
        try:
            self.resolution = KeyPropertiesResolution(mod, self)
        except KeyError:
            self.resolution = None
        try:
            self.tuning = KeyPropertiesTuning(mod, self)
        except KeyError:
            self.tuning = None


class KeyPropertiesConservation(SpecializationDetailCollection):
    """Wraps a key properties conservation specialization.

    """
    def __init__(self, mod, kp):
        """Instance constructor.

        """
        super(KeyPropertiesConservation, self).__init__(
            mod, kp, "conservation", "EXTRA_CONSERVATION_PROPERTIES")


class KeyPropertiesExtent(SpecializationDetailCollection):
    """Wraps a key properties extent specialization.

    """
    def __init__(self, mod, kp):
        """Instance constructor.

        """
        super(KeyPropertiesExtent, self).__init__(
            mod, kp, "extent", "EXTENT")


class KeyPropertiesResolution(SpecializationDetailCollection):
    """Wraps a key properties resolution specialization.

    """
    def __init__(self, mod, kp):
        """Instance constructor.

        """
        super(KeyPropertiesResolution, self).__init__(
            mod, kp, "resolution", "RESOLUTION")


class KeyPropertiesTuning(SpecializationDetailCollection):
    """Wraps a key properties tuning specialization.

    """
    def __init__(self, mod, kp):
        """Instance constructor.

        """
        super(KeyPropertiesTuning, self).__init__(
            mod, kp, "tuning", "TUNING_APPLIED")


class SubProcess(Specialization):
    """Wraps a sub-process specialization.

    """
    def __init__(self, process, name, obj, sort_collections):
        """Instance constructor.

        """
        super(SubProcess, self).__init__(process.mod)

        # Expand full sub-process detail keys.
        obj['details'] = ["{}:{}".format(name, i) for i in obj['details']]

        self.obj = obj
        self.name = name
        self.description = obj.get('description', name)
        self.id = "{}.{}".format(process.id, name)
        self.process = process
        self.cfg_section = "sub-process"
        self.details = [Detail(process.mod, self, i, process.mod.SUB_PROCESS_DETAILS[i])
                        for i in obj['details']]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id)
        ]


class Detail(Specialization):
    """Wraps a detail specialization.

    """
    def __init__(self, mod, container, name, obj):
        """Instance constructor.

        """
        super(Detail, self).__init__(mod)

        # Contract name where container is referenced as part of the name.
        name = name.split(":")[-1]
        try:
            self.id = "{}.{}".format(container.id, name)
        except AttributeError:
            self.id = None
        self.name = name
        self.obj = obj
        self.cfg_section = "detail"
        self.description = self.obj['description']
        self.properties = [DetailProperty(mod, self, i) for i in self.obj['properties']]


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id)
        ]


class DetailProperty(Specialization):
    """Wraps a detail-property specialization.

    """
    def __init__(self, mod, container, obj):
        """Instance constructor.

        """
        super(DetailProperty, self).__init__(mod)

        self.name, self.typeof, self.cardinality, self.description = obj
        self.container = container
        self.cfg_section = "detail-property"
        if self.typeof.startswith("ENUM"):
            self.enum = Enum(mod, self.typeof.split(":")[-1])
            self.typeof = "enum"
        else:
            self.enum = None


    @property
    def id(self):
        """Gets id associated with detail-property.

        """
        return "{}.{}".format(self.container.id, self.name)


    def short_id(self, idx):
        return ".".join(self.id.split(".")[idx:])


    @property
    def is_mandatory(self):
        """Gets flag indicating whether cardinality is mandatory or not.

        """
        return self.cardinality.split(".")[0] == "0"


    @property
    def is_collection(self):
        """Gets flag indicating whether property is a collection or not.

        """
        try:
            int(self.cardinality.split(".")[1])
        except ValueError:
            return True
        else:
            return False

    @property
    def typeof_label(self):
        """Gets label for the property type.

        """
        if self.typeof == 'str':
            return "STRING"
        elif self.typeof == 'bool':
            return "BOOLEAN"
        elif self.typeof == 'int':
            return "INTEGER"
        elif self.typeof == 'float':
            return "FLOAT"

        return self.typeof.upper()


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description),
            ("ID", self.id),
            ("Type", self.typeof),
            ("Cardinality", self.cardinality)
        ]


class Enum(Specialization):
    """Wraps the definitions of a CMIP6 enumeration definition.

    """
    def __init__(self, mod, name):
        """Instance constructor.

        """
        super(Enum, self).__init__(mod)

        self.id = name
        self.cfg_section = "enum"
        self.description = mod.ENUMERATIONS[name]['description']
        self.is_open = mod.ENUMERATIONS[name]['is_open']
        self.label = name
        self.name = name
        self.choices = [EnumChoice(self, i[0], i[1]) for i in
                        sorted(mod.ENUMERATIONS[name]['members'])]
        if self.is_open:
            self.choices.append(EnumChoice(self, "Other", None))


    @property
    def notes(self):
        """Returns notes.

        """
        return []


class EnumChoice(Specialization):
    """Wraps the definitions of a CMIP6 enumeration choice definition.

    """
    def __init__(self, owner, value, description):
        """Instance constructor.

        """
        super(EnumChoice, self).__init__(owner.mod)

        self.description = description
        self.id = "{}.{}".format(owner.id, value)
        self.value = value
        self.cfg_section = "enum-choice"
        self.is_other = value == 'Other'


    @property
    def notes(self):
        """Returns notes.

        """
        return [
            ("Description", self.description.replace("&", "and")),
            ("ID", self.id.lower().replace(" ", "-").replace("_", "-"))
        ]


def to_camel_case_spaced(name, separator='_'):
    """Converts passed name to camel case with space.

    :param str name: A name as specified in ontology specification.
    :param str separator: Separator to use in order to split name into constituent parts.

    """
    s = to_camel_case(name, separator)
    r = s[0]
    for s in s[1:]:
        if s.upper() == s:
            r += " "
        r += s

    return r


def to_camel_case(name, separator='_'):
    """Converts passed name to camel case.

    :param str name: A name as specified in ontology specification.
    :param str separator: Separator to use in order to split name into constituent parts.

    """
    r = ''
    if name is not None:
        s = name.split(separator)
        for s in s:
            if (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]
    return r