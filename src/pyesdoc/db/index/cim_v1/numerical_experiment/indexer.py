"""
.. module:: indexer.py
   :platform: Unix, Windows
   :synopsis: Indexes a cim.v1.activity.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from .... import (
    dao,
    models,
    utils
    )



def index(project_id, e):
    """Indexes a cim v1 numerical experiment document.

    :param int project_id: ID of associated project.
    :param e: A numerical experiment document.
    :type e: ontologies.cim.v1.activity.NumericalExperiment

    """
    utils.create_node(models.NODE_TYPE_EXPERIMENT,
                      e.short_name,
                      project_id)
