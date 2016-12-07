# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq.content.initializer.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates content initialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
from pyesdoc.drq.content.section import Section
from pyesdoc.drq.content.section_item import SectionItem
from pyesdoc.drq.content.wrapper import Wrapper
from pyesdoc.drq.content.xml_parser import XMLParser



class Initializer(XMLParser):
    """Initialises library with parsed content.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Initializer, self).__init__()
        self.sections = {}
        self.execute()


    def on_parse_section(self, cfg, elem):
        """On table element parse event handler.

        """
        self.sections[elem] = Section(cfg, elem)


    def on_parse_section_item(self, section_elem, elem):
        """On table section item element parse event handler.

        """
        section = self.sections[section_elem]
        section.items.append(SectionItem(section, elem))


    def on_parse_complete(self):
        """On parse complete event handler.

        """
        wrapper = Wrapper(self.sections.values())

        # Set relation: mip --> objective
        for mip in wrapper['mip']:
            mip.objectives = [o for o in wrapper['objective'] if o.mip == mip.label]

        # TODO set links
        # requestVarGroup --> mip
        # requestItem --> mip
        # requestItem --> expt
        # requestItem --> timeslice

        setattr(pyesdoc.drq, "content", wrapper)
