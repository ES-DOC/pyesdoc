"""
.. module:: cim_1.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v1 HTML field sets.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc._codecs.html.fieldsets.field import Field



def _get_grids_grid_tile_resolution(resolution):
    """Returns a dynamically constructed fieldset.

    """
    props = sorted(resolution.properties, key=lambda p: p.name)
    result = [Field(p.name, value=p.value) for p in props]
    result.insert(0, Field('Description', path='description'))

    return result


def _get_activity_ensemble_member(member):
    """Returns a dynamically constructed fieldset.

    """
    result = []

    for change in member.simulation.changes:
        result.append(Field('Change type', value=change.type))
        result.append(Field('Change name', value=change.name))
        result.append(Field('Change date', value=change.date))
        result.append(Field('Change description', value=change.details[0].description))

    return result


def _get_activity_simulation_run_model_mods(mods):
    """Returns a dynamically constructed fieldset.

    """
    result = []

    for mod in mods:
        result.append(Field(mod.name, value=mod.details[0].description))

    return result


def _get_software_modelcomponent_properties(properties):
    """Returns a dynamically constructed fieldset.

    """
    result = []

    for prop in properties:
        display_name = prop.ext.display_name.replace("Scientific Properties > ", "")
        for value in sorted(prop.values):
            result.append(Field(display_name, value=value))

    return result


# Document field sets.
FIELDSETS = {
    'cim.1.activity.ensemble-member': \
        _get_activity_ensemble_member,

    'cim.1.activity.ensemble-overview': [
        Field('Project', path='meta.project'),
        Field('Institute', path='meta.institute'),
        Field('Name', path='short_name'),
        Field('Long Name', path='long_name'),
        Field('Type', path='types'),
        Field('Description', path='description'),
        Field('Rationale', path='rationales'),
        Field('Simulation', path='members.0.simulation.name'),
        Field('Experiment', path='supports.0.name')
    ],

    'cim.1.activity.numericalexperiment-overview': [
        Field('Project', path='meta.project'),
        Field('Institute', path='meta.institute'),
        Field('Name', path='short_name'),
        Field('Long Name', path='long_name'),
        Field('ID', path='ext.full_experiment_name'),
        Field('Description', path='description'),
        Field('Rationale', path='rationales'),
    ],

    'cim.1.activity.simulationrun-overview': [
        Field('Project', path='meta.project'),
        Field('Institute', path='meta.institute'),
        Field('Name', path='short_name'),
        Field('Long Name', path='long_name'),
        Field('ID', path='simulation_id'),
        Field('Experiment', path='supports[0].name'),
        Field('Experiment conformances', path='ext.conformances'),
        Field('Authors', path='authors'),
        Field('Funder',
            path='responsible_parties.role=funder.organisation_name',
            link_path='responsible_parties.role=funder.url'
            ),
        Field('RIP Value', path='simulation_id'),
        Field('Spinup start', path='spinup_date_range.start'),
        Field('Spinup duration', path='spinup_date_range.duration')
    ],

    'cim.1.activity.simulationrun-model-mods': \
        _get_activity_simulation_run_model_mods,

    'cim.1.data.dataobject-overview': [
        Field('Project', path='meta.project'),
        Field('Institute', path='meta.institute'),
        Field('Acronym', path='acronym'),
        Field('Format', path='distribution.format'),
        Field('State', path='data_status', output_formatter=unicode.upper),
        Field('Description', path='description')
    ],

    'cim.1.grids.grid-mosaic': [
        Field('Name', path='short_name'),
        Field('Long Name', path='long_name'),
        Field('Type', path='type'),
        Field('Tiles', path='tile_count'),
        Field('Mosaics', path='mosaic_count'),
        Field('Is Leaf ?', path='is_leaf'),
        Field('Has Congruent Tiles', path='has_congruent_tiles'),
        Field('Description', path='description')
    ],

    'cim.1.grids.grid-tile-overview': [
        Field('Area', path='area'),
        Field('Cell Array', path='cell_array'),
        Field('Coord File', path='coord_file'),
        Field('Coordinate Pole', path='coordinate_pole'),
        Field('Description', path='description'),
        Field('Discretization Type', path='discretization_type'),
        Field('Geometry Type', path='geometry_type'),
        Field('Grid North Pole', path='grid_north_pole'),
        Field('Horizontal CRS', path='horizontal_crs'),
        Field('id', path='id'),
        Field('Is Conformal ?', path='is_conformal'),
        Field('Is Regular ?', path='is_regular'),
        Field('Is Terrain Following ?', path='is_terrain_following'),
        Field('Is Uniform ?', path='is_uniform'),
        Field('Long Name', path='long_name'),
        Field('Mnemonic', path='mnemonic'),
        Field('NX', path='nx'),
        Field('NY', path='ny'),
        Field('NZ', path='nz'),
        Field('Refinement Scheme', path='refinement_scheme'),
        Field('Short Name', path='short_name'),
        Field('Simple Grid Geom', path='simple_grid_geom'),
        Field('Vertical CRS', path='vertical_crs'),
        Field('Z-Coords', path='zcoords')
    ],

    'cim.1.grids.grid-tile-extent': [
        Field('maximum_latitude', path='maximum_latitude'),
        Field('minimum_latitude', path='minimum_latitude'),
        Field('maximum_longitude', path='maximum_longitude'),
        Field('minimum_longitude', path='minimum_longitude'),
        Field('units', path='units')
    ],

    'cim.1.grids.grid-tile-resolution': \
        _get_grids_grid_tile_resolution,

    'cim.1.quality.cimquality': [
        Field('Measure', path='measure.name',
            link_path='evaluation.type_hyperlink'),
        Field('Outcome', path='evaluation.specification',
            link_path='evaluation.specification_hyperlink'),
        Field('Evaluator', path='evaluator.individual_name',
            email_path='evaluator.individual_name'),
        Field('Evaluation Date', path='evaluation.date'),
        Field('Details', path='evaluation.explanation')
    ],

    'cim.1.shared.citation' : [
        # Field('Title', path='title'),
        Field('Long Title', path='collective_title'),
        Field('Location', path='location', link_path='location')
    ],

    'cim.1.shared.license': [
        Field('Contact', path='contact'),
        Field('Description', path='description'),
        Field('Is Unrestricted ?', path='is_unrestricted'),
        Field('Name', path='name'),
    ],

    'cim.1.shared.platform': [
        Field('Project', path='meta.project'),
        Field('Institute', path='meta.institute'),
        Field('Name', path='short_name'),
        Field('Long Name', path='long_name'),
        Field('Description', path='description')
    ],

    'cim.1.shared.platform.unit.machine': [
        Field('Name', path='name'),
        Field('Vendor', path='vendor'),
        Field('Operating System', path='operating_system'),
        Field('Processor Type', path='processor_type'),
        Field('Max. Processors', path='maximum_processors'),
        Field('Cores / Processor', path='cores_per_processor'),
        Field('System', path='system'),
        Field('Interconnect', path='interconnect')
    ],

    'cim.1.shared.platform.unit.compiler': [
        Field('Name', path='name'),
        Field('Type', path='type'),
        Field('Version', path='version'),
        Field('Language', path='language'),
        Field('Options', path='options'),
        Field('Env. Variables', path='environment_variables')
    ],

    'cim.1.shared.responsibleparty': [
        # Field('Role', path='role', output_formatter=unicode.upper),
        Field('Name', path='individual_name'),
        Field('Organisation', path='organisation_name'),
        Field('Address', path='address'),
        Field('Email', path='email', email_path='email'),
        Field('URL', path='url', link_path='url')
    ],

    'cim.1.software.modelcomponent-details': [
        Field('Project', path='meta.project'),
        Field('Institute', path='meta.institute'),
        Field('Name', path='short_name'),
        Field('Long Name', path='long_name'),
        Field('Home Page', path='online_resource', link_path='online_resource'),
        Field('Type', path='ext.type_display_name'),
        Field('Funder',
            path='responsible_parties.role=funder.organisation_name',
            link_path='responsible_parties.role=funder.url'
            ),
        Field('Principal Investigator',
            path='responsible_parties.role=pi.individual_name',
            email_path='responsible_parties.role=pi.email'
            ),
        Field('Release Date', path='release_date'),
        Field('Version', path='version'),
        Field('Previous Version', path='previous_version'),
        Field('Language', path='language.name'),
        Field('Code Access', path='code_access'),
        Field('Funding Source(s)', path='funding_sources'),
        Field('Coupling Framework', path='coupling_framework'),
        Field('Description', path='description'),
        Field('Document author', path='meta.author.individual_name'),
        Field('Document created', path='meta.create_date')
    ],

    'cim.1.software.modelcomponent-properties': \
        _get_software_modelcomponent_properties,

    'cim.1.software.timing': [
        Field('Rate', path='rate'),
        Field('Units', path='units'),
        Field('Is Rate Variable ?', path='is_variable_rate'),
        Field('Start', path='start'),
        Field('End', path='start')
    ]
}
