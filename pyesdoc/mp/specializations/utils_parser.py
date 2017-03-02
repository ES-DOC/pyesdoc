# -*- coding: utf-8 -*-

"""
.. module:: utils_parser.py
   :platform: Unix, Windows
   :synopsis: An event style specializations parser.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from constants import *



class SpecializationParser(object):
    """An event driven CMIP6 specializations parser.

    """
    def __init__(self, root):
        """Instance constructor.

        """
        self.root = root


    def run(self):
        """Runs the parser raising events as it does so.

        """
        self.on_root_parse(self.root)
        self._parse_topic(self.root)
        for st in self.root.sub_topics:
            getattr(self, "on_{}_parse".format(st.type_key))(st)
            self._parse_topic(st)
            getattr(self, "on_{}_parsed".format(st.type_key))(st)
        self.on_root_parsed(self.root)


    def _parse_topic(self, topic):
        """Parses a topic.

        """
        self._parse_topic_properties(topic.properties)

        for ps in topic.property_sets:
            self.on_property_set_parse(ps)
            self._parse_topic_properties(ps.properties)
            self.on_property_set_parsed(ps)

        for sp in topic[TYPE_KEY_SUBPROCESS]:
            self.on_subprocess_parse(sp)
            self._parse_topic(sp)
            self.on_subprocess_parsed(sp)


    def _parse_topic_properties(self, properties):
        """Parses a collection of properties associated with either a topic or a property-set.

        """
        for p in properties:
            self.on_property_parse(p)
            if p.enum:
                self.on_enum_parse(p.enum)
                for ec in p.enum.choices:
                    self.on_enum_choice_parse(ec)
                    self.on_enum_choice_parsed(ec)
                self.on_enum_parsed(p.enum)
            self.on_property_parsed(p)


    def on_root_parse(self, root):
        """On root parse event handler.

        """
        pass


    def on_root_parsed(self, root):
        """On root parsed event handler.

        """
        pass


    def on_grid_parse(self, grid):
        """On grid parse event handler.

        """
        pass


    def on_grid_parsed(self, grid):
        """On grid parsed event handler.

        """
        pass


    def on_keyprops_parse(self, key_props):
        """On key-properties parse event handler.

        """
        pass


    def on_keyprops_parsed(self, key_props):
        """On key-properties parsed event handler.

        """
        pass


    def on_process_parse(self, process):
        """On process parse event handler.

        """
        pass


    def on_process_parsed(self, process):
        """On process parsed event handler.

        """
        pass


    def on_subprocess_parse(self, subprocess):
        """On sub-process parse event handler.

        """
        pass


    def on_subprocess_parsed(self, subprocess):
        """On sub-process parsed event handler.

        """
        pass


    def on_property_set_parse(self, prop_set):
        """On property set parse event handler.

        """
        pass


    def on_property_set_parsed(self, prop_set):
        """On property set parsed event handler.

        """
        pass


    def on_property_parse(self, prop):
        """On property parse event handler.

        """
        pass


    def on_property_parsed(self, prop):
        """On property parsed event handler.

        """
        pass


    def on_enum_parse(self, enum):
        """On enum parse event handler.

        """
        pass


    def on_enum_parsed(self, enum):
        """On enum parsed event handler.

        """
        pass


    def on_enum_choice_parse(self, choice):
        """On enum choice parse event handler.

        """
        pass


    def on_enum_choice_parsed(self, choice):
        """On enum choice parsed event handler.

        """
        pass
