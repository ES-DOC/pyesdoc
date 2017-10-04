# -*- coding: utf-8 -*-

"""
.. module:: model_topic.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Model topic notebook data wrapper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections
import json
import os

from pyesdoc.ipython import constants
from pyesdoc.mp.specializations import get_model_specialization
from pyesdoc.mp.specializations import get_property_specialization



class NotebookOutput(object):
    """Model topic ipython data wrapper.

    """
    def __init__(self, mip_era, institute, source_id, topic):
        """Instance initialiser.

        """
        self.authors = []
        self.contributors = []
        self.content = dict()
        self.institute = unicode(institute).strip().lower()
        self.mip_era = unicode(mip_era).strip().lower()
        self.publication_status = 0
        self.seeding_source = None
        self.source_id = unicode(source_id).strip().lower()
        self.specialization = get_model_specialization(mip_era, topic)
        self.topic = unicode(topic).strip().lower()
        self._prop = None
        self._prop_specialization = None

        # Initialise output directory.
        if os.getenv('ESDOC_CMIP6_NOTEBOOK_HOME') is not None:
            output_dir = os.getenv('ESDOC_CMIP6_NOTEBOOK_HOME')
            output_dir = os.path.join(output_dir, self.institute)
        else:
            output_dir = os.path.expanduser('~')
            output_dir = os.path.join(output_dir, 'notebooks')
        output_dir = os.path.join(output_dir, self.mip_era)
        output_dir = os.path.join(output_dir, 'models')
        output_dir = os.path.join(output_dir, self.source_id)
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        # Initialise state from previously saved output file.
        self.fpath = os.path.join(output_dir, '.{}.json'.format(self.topic))
        if os.path.exists(self.fpath):
            with open(self.fpath, 'r') as fstream:
                self._from_dict(json.loads(fstream.read()))


    def save(self):
        """Persists state to file system.

        """
        obj = self._to_dict()
        with open(self.fpath, 'w') as fstream:
            fstream.write(json.dumps(obj, indent=4))


    def _from_dict(self, obj):
        """Initialises internal state from a dictionary.

        """
        self.publication_status = obj.get('publicationState', 0)
        self.mip_era = obj['mipEra']
        self.institute = obj['institute']
        self.seeding_source = obj.get('seedingSource')
        self.source_id = obj['sourceID']
        self.topic = obj['topic']
        self.authors = [(i['name'], i['email']) for i in obj['authors']]
        self.contributors = [(i['name'], i['email']) for i in obj['contributors']]
        self.content = obj['content']


    def _to_dict(self):
        """Returns a dictionary representation of internal state.

        """
        obj = collections.OrderedDict()
        obj['publicationState'] = self.publication_status
        obj['mipEra'] = self.mip_era
        obj['institute'] = self.institute
        obj['seedingSource'] = self.seeding_source
        obj['sourceID'] = self.source_id
        obj['topic'] = self.topic
        obj['authors'] = [{'name': i[0], 'email': i[1]} for i in self.authors]
        obj['contributors'] = [{'name': i[0], 'email': i[1]} for i in self.contributors]
        obj['content'] = collections.OrderedDict()
        for specialization_id in sorted(self.content.keys()):
            specialization_obj = self.content[specialization_id]
            if specialization_obj['qcStatus'] or specialization_obj['values']:
                obj['content'][specialization_id] = self.content[specialization_id]

        return obj


    def set_author(self, name, email):
        """Adds an author to managed collection.

        """
        # Format inputs.
        if name is not None:
            name = unicode(name).strip()
        if email is not None:
            email = unicode(email).strip()

        # Validate inputs.
        if name is None or len(name) == 0:
            raise ValueError('Invalid contributor name')
        if email is None or len(email) == 0:
            raise ValueError('Invalid contributor email')
        # TODO: validate with reg-ex.

        # Reject duplicates.
        for i, j in self.authors:
            if name.lower() == i.lower() and email.lower() == j.lower():
                return

        # Update state.
        self.authors.append((name, email))
        self.save()


    def set_contributor(self, name, email):
        """Adds a contributor to managed collection.

        """
        # Format inputs.
        if name is not None:
            name = unicode(name).strip()
        if email is not None:
            email = unicode(email).strip()

        # Validate inputs.
        if name is None or len(name) == 0:
            raise ValueError('Invalid contributor name')
        if email is None or len(email) == 0:
            raise ValueError('Invalid contributor email')
        # TODO: validate with reg-ex.

        # Reject duplicates.
        for i, j in self.contributors:
            if name.lower() == i.lower() and email.lower() == j.lower():
                return

        # Update state.
        self.contributors.append((name, email))
        self.save()


    def set_id(self, prop_id):
        """Sets id of specialized property being edited.

        """
        self.content[prop_id] = {
            'values': [],
            'qcStatus': 0
        }
        self._prop = self.content[prop_id]
        self._prop_specialization = get_property_specialization(prop_id)


    def set_qc_status(self, qc_status):
        """Sets qc-status of specialized property being edited.

        """
        # Validate input.
        if qc_status not in constants.QC_STATES:
            raise ValueError('Invalid QC status')

        # Update state.
        self._prop['qcStatus'] = qc_status
        self.save()


    def set_publication_status(self, publication_status):
        """Sets publication status of document being edited.

        """
        # Validate input.
        if publication_status not in constants.PUBLICATION_STATES:
            raise ValueError('Invalid publication status')

        # Update state.
        self.publication_status = publication_status
        self.save()


    def set_value(self, val):
        """Sets a scalar value.

        """
        # Validate input:
        # ... error if trying to add > 1 value to a property with singular cardinality.
        if not self._prop_specialization.is_collection and \
           len(self._prop['values']) >= 1:
            raise ValueError('Invalid property: only one value can be added')

        # ... error if adding a duplicate value.
        if val in self._prop['values']:
            raise ValueError('Invalid property: cannot add duplicate values')

        # ... error if specialization complains.
        self._prop_specialization.validate_value(val)

        # Update state.
        self._prop['values'].append(val)
        self.save()


    def get_values(self, specialization_id):
        """Returns a set of values.

        """
        return self.content.get(specialization_id, dict()).get('values', [])


    def get_qc_status(self, specialization_id):
        """Returns a property qc status.

        """
        return self.content.get(specialization_id, dict()).get('qcStatus', 0)

