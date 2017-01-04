# -*- coding: utf-8 -*-

"""
.. module:: model_realm_notebook.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Model realm notebook helper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.mp.specializations import get_model_realm_specialization
from pyesdoc.mp.specializations import get_property_specialization



class NotebookData(object):
    """Encpasulates model realm data being edited in an IPython notebook.

    """
    def __init__(self, mip_era, institute, source_id, realm):
        """Instance initialiser.

        """
        self.authors = list()
        self.contributors = list()
        self.content = dict()
        self.institute = institute
        self.mip_era = mip_era
        self.prop = None
        self.prop_specialization = None
        self.realm = realm
        self.source_id = source_id
        self.specialization = get_model_realm_specialization(mip_era, realm)


    def set_author(self, name, email):
        """Adds an author to managed collection.

        """
        # TODO: validate with reg-ex.
        self.authors.append((name, email))


    def set_contributor(self, name, email):
        """Adds a contributor to managed collection.

        """
        # TODO: validate contributor with reg-ex.
        self.contributors.append((name, email))


    def set_id(self, prop_id):
        """Sets id of specialized property being edited.

        """
        self.content[prop_id] = {
            'values': [],
            'qc_status': 0
        }
        self.prop = self.content[prop_id]
        self.prop_specialization = get_property_specialization(prop_id)


    def set_qc_status(self, qc_status):
        """Sets qc-status of specialized property being edited.

        """
        if qc_status not in {0, 1, 2}:
            raise ValueError("Invalid QC status")
        self.prop['qc_status'] = qc_status


    def set_value(self, val):
        """Sets a scalar value.

        """
        # Error if trying to add > 1 value to a property with singular cardinality.
        if not self.prop_specialization.is_collection and \
           len(self.prop['values']) >= 1:
            raise ValueError("Invalid property: only one value can be added")

        # Delegate to specialization.
        self.prop_specialization.validate_value(val)

        # TODO: validate value
        self.prop['values'].append(val)


    def get_values(self, specialization_id):
        """Returns a set of values.

        """
        return []


    def get_qc_status(self, specialization_id):
        """Returns a property qc status.

        """
        return 0


    def list_errors(self):
        """Lists outstanding validation errors.

        """
        raise NotImplementedError()


    def persist(self):
        """Persists to file system.

        """
        raise NotImplementedError()


    def from_dict(self, obj):
        pass


    def to_dict(self):
        pass

