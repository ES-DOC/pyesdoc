# -*- coding: utf-8 -*-

"""
.. module:: constants.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Notebook constants.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# QC status: draft.
QC_STATE_DRAFT = 0

# QC status: in-review.
QC_STATE_IN_REVIEW = 1

# QC status: review.ed
QC_STATE_REVIEWED = 2

# Set of valid QC states.
QC_STATES = {
	QC_STATE_DRAFT,
	QC_STATE_IN_REVIEW,
	QC_STATE_REVIEWED
	}

# Publication state: not ready.
PUBLICATION_STATE_NOT_READY = 0

# Publication state: ready.
PUBLICATION_STATE_READY = 1

# Set of valid publication states.
PUBLICATION_STATES = {
	PUBLICATION_STATE_NOT_READY,
	PUBLICATION_STATE_READY
	}
