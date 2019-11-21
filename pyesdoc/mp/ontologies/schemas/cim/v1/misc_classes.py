"""
.. module:: misc_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 miscellaneous package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def document_set():
    """Represents a bundled set of documents.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'is_document': True,
        'properties' : [
            ('data', 'data.data_object', '0.N'),
            ('ensembles', 'activity.ensemble', '0.N'),
            ('experiment', 'activity.numerical_experiment', '0.1'),
            ('grids', 'grids.grid_spec', '0.N'),
            ('model', 'software.model_component', '0.1'),
            ('platform', 'shared.platform', '0.1'),
            ('simulation', 'activity.simulation_run', '0.1')
        ],
        'doc_strings': {
            'data': 'Associated input/output data.',
            'ensembles': 'Associated ensemble runs.',
            'experiment': 'Associated numerical experiment.',
            'grids': 'Associated grid-spec.',
            'model': 'Associated model component.',
            'platform': 'Associated simulation execution platform.',
            'simulation': 'Associated simulation run.'
        },
        'decodings' : [
            ('data', 'child::cim:dataObject'),
            ('ensembles', 'child::cim:ensemble'),
            ('experiment', 'child::cim:numericalExperiment'),
            ('model', 'child::cim:modelComponent'),
            ('grids', 'child::cim:gridSpec'),
            ('platform', 'child::cim:platform'),
            ('simulation', 'child::cim:simulationRun'),
        ]
    }
