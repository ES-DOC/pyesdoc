# -*- coding: utf-8 -*-

"""
.. module:: parser.py
   :platform: Unix, Windows
   :synopsis: An event style specializations parser.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class RealmSpecializationParser(object):
    """An event driven CMIP6 realm specializations parser.

    """
    def __init__(self, realm):
        """Instance constructor.

        """
        self.realm = realm


    def run(self):
        """Runs the parser raising events as it does so.

        """
        self.on_realm_parse(self.realm)
        self._parse_topic(self.realm, False)
        if self.realm.grid:
            self.on_grid_parse(self.realm.grid)
            self._parse_topic(self.realm.grid)
            self.on_grid_parsed(self.realm.grid)
        if self.realm.key_properties:
            self.on_keyproperties_parse(self.realm.key_properties)
            self._parse_topic(self.realm.key_properties)
            self.on_keyproperties_parsed(self.realm.key_properties)
        for p in self.realm.processes:
            self.on_process_parse(p)
            self._parse_topic(p)
            self.on_process_parsed(p)
        self.on_realm_parsed(self.realm)


    def _parse_topic(self, topic, parse_sub_topics=True):
        """Parses a topic.

        """
        self._parse_topic_properties(topic.properties)
        for ps in topic.property_sets:
            self.on_topic_property_set_parse(ps)
            self._parse_topic_properties(ps.properties)
            self.on_topic_property_set_parsed(ps)
        if parse_sub_topics:
            for st in topic.sub_topics:
                self.on_subprocess_parse(st)
                self._parse_topic(st)
                self.on_subprocess_parsed(st)


    def _parse_topic_properties(self, properties):
        """Parses a collection of properties associated with either a topic or a property-set.

        """
        for p in properties:
            self.on_topic_property_parse(p)
            if p.enum:
                self.on_enum_parse(p.enum)
                for ec in p.enum.choices:
                    self.on_enumchoice_parse(ec)
                    self.on_enumchoice_parsed(ec)
                self.on_enum_parsed(p.enum)
            self.on_topic_property_parsed(p)


    def on_realm_parse(self, realm):
        """On realm parse event handler.

        """
        pass


    def on_realm_parsed(self, realm):
        """On realm parsed event handler.

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


    def on_keyproperties_parse(self, key_properties):
        """On key-properties parse event handler.

        """
        pass


    def on_keyproperties_parsed(self, key_properties):
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


    def on_topic_property_set_parse(self, prop_set):
        """On topic property set parse event handler.

        """
        pass


    def on_topic_property_set_parsed(self, prop_set):
        """On topic property set parsed event handler.

        """
        pass


    def on_topic_property_parse(self, prop):
        """On topic property parse event handler.

        """
        pass


    def on_topic_property_parsed(self, prop):
        """On topic property parsed event handler.

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


    def on_enumchoice_parse(self, choice):
        """On enum choice parse event handler.

        """
        pass


    def on_enumchoice_parsed(self, choice):
        """On enum choice parsed event handler.

        """
        pass
