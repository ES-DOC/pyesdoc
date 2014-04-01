"""
.. module:: activity_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.activity.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
def parse(doc):
	# Set document type display name.
	doc._type_display_name = doc.doc_info.type_display_name = "Experiment"
