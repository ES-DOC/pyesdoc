"""
.. module:: software_model_component_2.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.software.modelcomponent document.


"""
from pyesdoc.ontologies.cim.v1 import ComponentProperty



def _create_property(p_tree, values, name, description):
    """Sets & returns a component standard property.

    """
    def append_value(p, v):
        if v is not None:
            p.values.append(v)

    # Instantiate.
    p = ComponentProperty()
    p.short_name = p.long_name = name
    p.description = description

    # Append each value.
    if values:
        try:
            iter(values)
        except ValueError:
            for v in values:
                append_value(p, v)
        else:
            append_value(p, values)

    # Append to tree.
    p_tree.append(p)

    return p


def _set_standard_properties_descriptive(c, p_tree):
    """Sets descriptive standard properties.

    """
    _create_property(p_tree,
                     c.description,
                     'Description',
                     'High-level component description')
    _create_property(p_tree,
                     c.short_name,
                     'Short Name',
                     'Abbreviated component name')
    _create_property(p_tree,
                     c.long_name,
                     'Long Name',
                     'Full component name')


def _set_standard_properties_pi(c, p_tree):
    """Sets principal investigator standard properties.

    """
    # Set PI.
    pi = None
    for rp in c.responsible_parties:
        if rp.role and rp.role.upper() == "PI":
            pi = rp
            break

    # Set PI properties.
    if pi:
        _create_property(p_tree,
                         pi.individual_name,
                         'PI Name',
                         'PI Name')
        _create_property(p_tree,
                         pi.email,
                         'PI Email Address',
                         'PI Email Address')


def _set_standard_properties_citations(c, p_tree):
    """Sets citation standard properties.

    """
    def get_citation_title(citation):
        return citation.title.strip()

    def get_citation_url(citation):
        if citation.location is None or citation.location.strip() == "":
            return "N/A"
        else:
            return citation.location.strip()

    # Set container property.
    p = _create_property(p_tree,
                         None,
                         'Citations',
                         'Set of component citations')

    # Set citation title.
    _create_property(p.sub_properties,
                     [get_citation_title(i) for i in c.citations if i.title is not None],
                     'Title',
                     'Title')

    # Set citation location.
    _create_property(p.sub_properties,
                     [get_citation_url(i) for i in c.citations if i.title is not None],
                     'Location',
                     'Location')


def set_standard_properties(c):
    """Sets standard scientific properties.

    :param c: A model component.
    :type c: pyesdoc.ontologies.cim.v1.software.ModelComponent

    """
    # Create property group.
    p = _create_property(c.ext.standard_properties,
                         None,
                         'Standard Properties',
                         'Set of component standard properties')
    # Create sub-groups.
    for setter in [
        _set_standard_properties_descriptive,
        _set_standard_properties_pi,
        _set_standard_properties_citations
    ]:
        setter(c, p.sub_properties)


def set_scientific_properties(c):
    """Sets component scientific properties.

    :param c: A model component.
    :type c: pyesdoc.ontologies.cim.v1.software.ModelComponent

    """
    # Create property group.
    group = _create_property(c.ext.scientific_properties,
                             None,
                             'Scientific Properties',
                             'Set of component scientific properties')

    # Key properties == scientific properties.
    for cp in c.properties:
        if "Key Properties" in cp.short_name or \
           "KeyProperties" in cp.short_name:
            for cpp in cp.sub_properties:
                if cpp.short_name.lower().find("qc properties") == -1:
                    group.sub_properties.append(cpp)
            return

    # Filter out QC properties.
    for cp in c.properties:
        if cp.short_name.lower().find("qc properties") == -1:
            group.sub_properties.append(cp)


def set_qc_properties(c):
    """Sets component qc properties.

    :param c: A model component.
    :type c: pyesdoc.ontologies.cim.v1.software.ModelComponent

    """
    # Create property group.
    group = _create_property(c.ext.qc_properties,
                             None,
                             'QC Properties',
                             'Set of component quality control properties')

    # Append qc properties.
    for cp in c.properties:
        if cp.short_name.lower().find("qc properties") != -1:
            group.sub_properties = cp.sub_properties
            break
