import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
DOC_TYPE = cim.v1.GridSpec

# Test representation file.
DOC_FILE = 'cim/v1_5_0/grids.grid_spec.xml'

# Test document uid.
DOC_UID = '9cef52e4-e2af-11df-bf17-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = '2012-03-01 13:08:34.746335'


def assert_doc(doc):
    assert len(doc.esm_model_grids) == 1
    assert len(doc.esm_exchange_grids) == 0

    assert doc.esm_model_grids[0].description.startswith('Specification of the ocean grid configuration')
    assert doc.esm_model_grids[0].long_name == 'Met Office Unified Model 360-column 40-level Ocean Grid System'
    assert doc.esm_model_grids[0].short_name == 'UM N180L40 OCN Grid System'

    assert len(doc.esm_model_grids[0].citations) == 2
    assert doc.esm_model_grids[0].citations[0].title == 'Johns_2005'
    assert doc.esm_model_grids[0].citations[0].collective_title.startswith('Johns T.C., et al. (2005).')

    assert doc.esm_model_grids[0].extent is None
    assert doc.esm_model_grids[0].has_congruent_tiles == False
    assert doc.esm_model_grids[0].id == ''
    assert doc.esm_model_grids[0].is_leaf == True
    assert doc.esm_model_grids[0].mosaic_count == 0
    assert doc.esm_model_grids[0].tile_count == 1
    assert doc.esm_model_grids[0].type == 'regular_lat_lon'

    assert len(doc.esm_model_grids[0].tiles) == 1
    assert doc.esm_model_grids[0].tiles[0].description.startswith('Horizontal properties: Between the poles')
    assert doc.esm_model_grids[0].tiles[0].extent is not None
    assert doc.esm_model_grids[0].tiles[0].extent.minimum_latitude == '-90'
    assert doc.esm_model_grids[0].tiles[0].extent.maximum_latitude == '90'
    assert doc.esm_model_grids[0].tiles[0].extent.minimum_longitude == '0'
    assert doc.esm_model_grids[0].tiles[0].extent.maximum_longitude == '360'
    assert doc.esm_model_grids[0].tiles[0].extent.units is None
    assert doc.esm_model_grids[0].tiles[0].mnemonic == 'N180'
    assert doc.esm_model_grids[0].tiles[0].horizontal_resolution is not None
    assert doc.esm_model_grids[0].tiles[0].horizontal_resolution.description.startswith('1 deg by 1 deg')
    assert len(doc.esm_model_grids[0].tiles[0].horizontal_resolution.properties) == 2
    assert doc.esm_model_grids[0].tiles[0].horizontal_resolution.properties[0].name == 'NumberOfLatitudinalGridCells'
    assert doc.esm_model_grids[0].tiles[0].horizontal_resolution.properties[0].value == '216'
    assert doc.esm_model_grids[0].tiles[0].vertical_resolution is not None
    assert len(doc.esm_model_grids[0].tiles[0].vertical_resolution.properties) == 4
    assert doc.esm_model_grids[0].tiles[0].vertical_resolution.properties[0].name == 'NumberOfLevelsInUpper100m'
    assert doc.esm_model_grids[0].tiles[0].vertical_resolution.properties[0].value == '10'

    assert doc.esm_model_grids[0].tiles[0].zcoords is not None
    assert doc.esm_model_grids[0].tiles[0].zcoords.type == 'space-based'
    assert doc.esm_model_grids[0].tiles[0].zcoords.form == 'depth'


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass