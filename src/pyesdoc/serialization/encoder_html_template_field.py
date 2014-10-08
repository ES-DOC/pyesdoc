"""
.. module:: encoder_html_template_field.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: HTML encoding template field information.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import datetime

from .. utils import convert, functional



class FieldInfo():
    """Document field processing information."""
    def __init__(self,
                 name,
                 email=None,
                 email_path=None,
                 formatter=None,
                 link=None,
                 link_path=None,
                 path=None,
                 tag_id=None,
                 value=None):
        self.name = name
        self.email = email
        self.email_path = email_path
        self.formatter = formatter
        self.link = link
        self.link_path = link_path
        self.path = path
        self.tag_id = tag_id
        self.value = value


    def get_name(self):
        """Returns formatted field name for html output."""
        return _get_name(self.name)


    def get_value(self, data=None):
        """Returns value of field for html output.

        :param object data: An object from which the field value is derived.

        :returns: The derived field value.
        :rtype str:

        """
        v = _get_value(data, self.path) if self.path else self.value
        v = _format_value(v, self.formatter)

        return v


    def get_link(self, data):
        """Returns value of associated hyperlink.

        :param object data: An object from which the hyperlink value is derived.

        :returns: The derived field hyperlink.
        :rtype str:

        """
        v = _get_value(data, self.link_path)
        v = _format_value(v)

        return v


    def get_email(self, data):
        """Returns value of associated email link.

        :param object data: An object from which the email link value is derived.

        :returns: The derived field email link.
        :rtype str:

        """
        v = _get_value(data, self.email_path)
        v = _format_value(v)

        return v


def _format_value(v, formatter=None):
    """Formats values for document output."""
    def _format(s):
        if s is None:
            s = None
        # TODO add support for time formatting.
        elif isinstance(v, datetime.datetime):
            s = str(s)[:10]
        else:
            s = str(s)

        if s and len(s):
            s = unicode(s.decode('utf8').strip())
            if formatter:
                s = formatter(s)

        return s

    return "  ".join(map(_format, v)).strip() if isinstance(v, list) else _format(v)


def _get_value(data, path):
    """Returns formatted value for document output."""
    if data is None:
        return None

    def is_collection_reference(attr):
        try:
            int(attr)
        except ValueError:
            return False
        else:
            return True

    # Initialise return value.
    value = data

    # Walk attribute path.
    for attr in path.split("."):
        # ... collection filter by index
        if is_collection_reference(attr):
            value = value[int(attr)]
        # ... collection filter by attribute
        elif "=" in attr:
            left, right = attr.split("=")
            value = functional.first(value, left, right.lower(), lambda v: str(v).lower())
        # ... item attribute filter
        elif hasattr(value, attr):
            value = getattr(value, attr)
        # Otherwise escape.
        else:
            break

        # Escape at dead-end.
        if value is None:
            break

    return None if value == data else value


def _get_name(name):
    """Returns formatted name for document output."""
    # Initialise.
    name = "" if name is None else name.strip()

    # Convert to spaced case.
    if len(name) > 4:
        name = convert.str_to_spaced_case(name).strip()

    # Prefixes.
    n = name.lower()
    prefixes = { "number of ": "" }
    for prefix in prefixes.keys():
        if n.startswith(prefix):
            name = prefixes[prefix] + name[len(prefix):]

    # Substrings.
    replacements = {
        "_": " ",
        "Second": "2nd",
        "First": "1st"
    }
    for replacement in replacements.keys():
        name = name.replace(replacement, replacements[replacement])

    # Substitutions.
    swaps = {
        "id": "ID",
    }
    for swap in swaps.keys():
        if name == swap:
            name = swaps[swap]

    return name


def _get_cim_1_grids_grid_tile_resolution(resolution):
    """Returns a fieldset.

    """
    props = sorted(resolution.properties, key=lambda p: p.name)
    result = map(lambda p: FieldInfo(p.name, value=p.value), props)
    result.insert(0, FieldInfo('Description', path='description'))

    return result


# Pre-compiled document field sets.
_FIELDSETS = {
    'cim.1.activity.ensemble-member': [
    ],
    'cim.1.activity.ensemble-overview': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Name', path='short_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Type', path='types'),
        FieldInfo('Description', path='description'),
        FieldInfo('Rationale', path='rationales'),
        FieldInfo('Simulation', path='members.0.simulation_reference.name'),
        FieldInfo('Experiment', path='supports_references.0.name')
    ],
    'cim.1.activity.numericalexperiment-overview': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Name', path='short_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('ID', path='ext.full_experiment_name'),
        FieldInfo('Description', path='description'),
        FieldInfo('Rationale', path='rationales'),
    ],
    'cim.1.activity.simulationrun-overview': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Name', path='short_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('ID', path='simulation_id'),
        FieldInfo('Experiment', path='supports_references[0].name'),
        FieldInfo('Experiment conformances', path='ext.conformances'),
        FieldInfo('Authors', path='authors'),
        FieldInfo('Funder', path='responsible_parties.role=funder.organisation_name', link_path='responsible_parties.role=funder.url'),
        FieldInfo('RIP Value', path='simulation_id'),
        FieldInfo('Spinup start', path='spinup_date_range.start'),
        FieldInfo('Spinup duration', path='spinup_date_range.duration')
    ],
    'cim.1.grids.grid-mosaic': [
        FieldInfo('Name', path='short_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Type', path='type'),
        FieldInfo('Tiles', path='tile_count'),
        FieldInfo('Mosaics', path='mosaic_count'),
        FieldInfo('Is Leaf', path='is_leaf'),
        FieldInfo('Has Congruent Tiles', path='has_congruent_tiles'),
        FieldInfo('Description', path='description')
    ],
    'cim.1.grids.grid-tile-overview': [
        FieldInfo('Area', path='area'),
        FieldInfo('Cell Array', path='cell_array'),
        FieldInfo('Coord File', path='coord_file'),
        FieldInfo('Coordinate Pole', path='coordinate_pole'),
        FieldInfo('Description', path='description'),
        FieldInfo('Discretization Type', path='discretization_type'),
        FieldInfo('Geometry Type', path='geometry_type'),
        FieldInfo('Grid North Pole', path='grid_north_pole'),
        FieldInfo('Horizontal CRS', path='horizontal_crs'),
        FieldInfo('id', path='id'),
        FieldInfo('Is Conformal ?', path='is_conformal'),
        FieldInfo('Is Regular ?', path='is_regular'),
        FieldInfo('Is Terrain Following ?', path='is_terrain_following'),
        FieldInfo('Is Uniform ?', path='is_uniform'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Mnemonic', path='mnemonic'),
        FieldInfo('NX', path='nx'),
        FieldInfo('NY', path='ny'),
        FieldInfo('NZ', path='nz'),
        FieldInfo('Refinement Scheme', path='refinement_scheme'),
        FieldInfo('Short Name', path='short_name'),
        FieldInfo('Simple Grid Geom', path='simple_grid_geom'),
        FieldInfo('Vertical CRS', path='vertical_crs'),
        FieldInfo('Z-Coords', path='zcoords')
    ],
    'cim.1.grids.grid-tile-extent': [
        FieldInfo('maximum_latitude', path='maximum_latitude'),
        FieldInfo('minimum_latitude', path='minimum_latitude'),
        FieldInfo('maximum_longitude', path='maximum_longitude'),
        FieldInfo('minimum_longitude', path='minimum_longitude'),
        FieldInfo('units', path='units')
    ],
    'cim.1.grids.grid-tile-resolution': \
        _get_cim_1_grids_grid_tile_resolution,
    'cim.1.quality.cimquality': [
        FieldInfo('Measure', path='measure.name', link_path='evaluation.type_hyperlink'),
        FieldInfo('Outcome', path='evaluation.specification', link_path='evaluation.specification_hyperlink'),
        FieldInfo('Evaluator', path='evaluator.individual_name', email_path='evaluator.individual_name'),
        FieldInfo('Evaluation Date', path='evaluation.date'),
        FieldInfo('Details', path='evaluation.explanation')
    ],
    'cim.1.shared.citation' : [
        # FieldInfo('Title', path='title'),
        FieldInfo('Long Title', path='collective_title'),
        FieldInfo('Location', path='location', link_path='location')
    ],
    'cim.1.shared.platform': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Name', path='short_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Description', path='description')
    ],
    'cim.1.shared.platform.unit.machine': [
        FieldInfo('Name', path='name'),
        FieldInfo('Vendor', path='vendor'),
        FieldInfo('Operating System', path='operating_system'),
        FieldInfo('Processor Type', path='processor_type'),
        FieldInfo('Max. Processors', path='maximum_processors'),
        FieldInfo('Cores / Processor', path='cores_per_processor'),
        FieldInfo('System', path='system'),
        FieldInfo('Interconnect', path='interconnect')
    ],
    'cim.1.shared.platform.unit.compiler': [
        FieldInfo('Name', path='name'),
        FieldInfo('Type', path='type'),
        FieldInfo('Version', path='version'),
        FieldInfo('Language', path='language'),
        FieldInfo('Options', path='options'),
        FieldInfo('Env. Variables', path='environment_variables')
    ],
    'cim.1.shared.responsibleparty': [
        # FieldInfo('Role', path='role', formatter=unicode.upper),
        FieldInfo('Name', path='individual_name'),
        FieldInfo('Organisation', path='organisation_name'),
        FieldInfo('Address', path='address'),
        FieldInfo('Email', path='email', email_path='email'),
        FieldInfo('URL', path='url', link_path='url')
    ],
    'cim.1.software.modelcomponent-details': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Name', path='short_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Funder', path='responsible_parties.role=funder.organisation_name', link_path='responsible_parties.role=funder.url'),
        FieldInfo('Principal Investigator', path='responsible_parties.role=pi.individual_name', email_path='responsible_parties.role=pi.email'),
        FieldInfo('Release Date', path='release_date'),
        FieldInfo('Description', path='description')
    ]
}


def load(fieldset):
    """Loads a templating fieldset.

    :param fieldset: Fieldset identifier.
    :ptype fieldset: tuple | str

    :returns: A templating fieldset.
    :rtype: list

    """
    if isinstance(fieldset, tuple):
        key, obj = fieldset
        return _FIELDSETS[key](obj)
    elif isinstance(fieldset, str):
        return _FIELDSETS[fieldset]
    else:
        return fieldset or []