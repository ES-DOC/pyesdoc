# -*- coding: utf-8 -*-

"""
.. module:: cim_1.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: CIM v1 HTML field sets.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.codecs.html.fieldsets.field_info import FieldInfo



def _get_grids_grid_tile_resolution(resolution):
    """Fieldset factory.

    """
    props = sorted(resolution.properties, key=lambda p: p.name)
    result = [FieldInfo(p.name, value=p.value) for p in props]
    result.insert(0, FieldInfo('Description', path='description'))

    return result


def _get_activity_ensemble_member(member):
    """Fieldset factory.

    """
    result = []

    if member.link_to_simulation:
        for change in member.link_to_simulation.changes:
            result.append(FieldInfo('Change type', value=change.type))
            result.append(FieldInfo('Change name', value=change.name))
            result.append(FieldInfo('Change date', value=change.date))
            result.append(FieldInfo('Change description', value=change.details[0].description))

    return result


def _get_activity_simulation_run_model_mods(mods):
    """Fieldset factory.

    """
    result = []

    for mod in mods:
        result.append(FieldInfo(mod.name, value=mod.details[0].description))

    return result


def _get_software_modelcomponent_properties(properties):
    """Fieldset factory.

    """
    result = []

    for prop in properties:
        display_name = prop.ext.display_name.replace("Scientific Properties > ", "")
        for value in sorted(prop.values):
            result.append(FieldInfo(display_name, value=value))

    return result


# Document field sets.
FIELDSETS = {
    'cim.1.activity.ensemble-member': \
        _get_activity_ensemble_member,

    'cim.1.activity.ensemble-overview': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Name', path='short_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Type', path='types'),
        FieldInfo('Description', path='description'),
        FieldInfo('Rationale', path='rationales'),
        FieldInfo('Simulation', path='members.0.link_to_simulation.name'),
        FieldInfo('Experiment', path='link_to_supports.0.name')
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
        FieldInfo('Experiment', path='link_to_supports[0].name'),
        FieldInfo('Experiment conformances', path='ext.conformances'),
        FieldInfo('Authors', path='authors'),
        FieldInfo('Funder', path='responsible_parties.role=funder.organisation_name',
                            link_path='responsible_parties.role=funder.url'),
        FieldInfo('RIP Value', path='simulation_id'),
        FieldInfo('Spinup start', path='spinup_date_range.start'),
        FieldInfo('Spinup duration', path='spinup_date_range.duration')
    ],

    'cim.1.activity.simulationrun-model-mods': \
        _get_activity_simulation_run_model_mods,

    'cim.1.data.dataobject-overview': [
        FieldInfo('Project', path='meta.project'),
        FieldInfo('Institute', path='meta.institute'),
        FieldInfo('Acronym', path='acronym'),
        FieldInfo('Format', path='distribution.format'),
        FieldInfo('State', path='data_status', output_formatter=unicode.upper),
        FieldInfo('Description', path='description')
    ],

    'cim.1.grids.grid-mosaic': [
        FieldInfo('Name', path='short_name'),
        FieldInfo('Long Name', path='long_name'),
        FieldInfo('Type', path='type'),
        FieldInfo('Tiles', path='tile_count'),
        FieldInfo('Mosaics', path='mosaic_count'),
        FieldInfo('Is Leaf ?', path='is_leaf'),
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
        _get_grids_grid_tile_resolution,

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

    'cim.1.shared.license': [
        FieldInfo('Contact', path='contact'),
        FieldInfo('Description', path='description'),
        FieldInfo('Is Unrestricted ?', path='is_unrestricted'),
        FieldInfo('Name', path='name'),
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
        # FieldInfo('Role', path='role', output_formatter=unicode.upper),
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
        FieldInfo('Home Page', path='online_resource', link_path='online_resource'),
        FieldInfo('Type', path='ext.type_display_name'),
        FieldInfo('Funder', path='responsible_parties.role=funder.organisation_name', link_path='responsible_parties.role=funder.url'),
        FieldInfo('Principal Investigator', path='responsible_parties.role=pi.individual_name', email_path='responsible_parties.role=pi.email'),
        FieldInfo('Release Date', path='release_date'),
        FieldInfo('Version', path='version'),
        FieldInfo('Previous Version', path='previous_version'),
        FieldInfo('Language', path='language.name'),
        FieldInfo('Code Access', path='code_access'),
        FieldInfo('Funding Source(s)', path='funding_sources'),
        FieldInfo('Coupling Framework', path='coupling_framework'),
        FieldInfo('Description', path='description'),
        FieldInfo('Document author', path='meta.author.individual_name'),
        FieldInfo('Document created', path='meta.create_date')
    ],

    'cim.1.software.modelcomponent-properties': \
        _get_software_modelcomponent_properties,


    'cim.1.software.timing': [
        FieldInfo('Rate', path='rate'),
        FieldInfo('Units', path='units'),
        FieldInfo('Is Rate Variable ?', path='is_variable_rate'),
        FieldInfo('Start', path='start'),
        FieldInfo('End', path='start')
    ]
}
