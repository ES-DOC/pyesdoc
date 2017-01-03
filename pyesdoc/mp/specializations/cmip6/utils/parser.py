# -*- coding: utf-8 -*-

"""
.. module:: parser.py
   :platform: Unix, Windows
   :synopsis: An event style specializations parser.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class Parser(object):
    """An event driven CMIP6 realm specializations parser.

    """
    def __init__(self, realm):
        """Instance constructor.

        """
        self.realm = realm


    def run(self):
        """Runs the parser raising events as it does so.

        """
        self._parse_realm(self.realm)


    def _parse_realm(self, r):
        """Parses a realm.

        """
        self.on_realm_parse(r)
        self._parse_property_container(r)

        if r.grid:
            self.on_grid_parse(r.grid)
            self._parse_property_container(r.grid)
            self.on_grid_parsed(r.grid)

        if r.key_properties:
            self.on_keyproperties_parse(r.key_properties)
            self._parse_property_container(r.key_properties)
            self.on_keyproperties_parsed(r.key_properties)

        for p in r.processes:
            self._parse_process(p)

        self.on_realm_parsed(r)


    def _parse_process(self, p):
        """Parses a realm process.

        """
        self.on_process_parse(p)
        self._parse_property_container(p)
        for sp in p.sub_processes:
            self.on_subprocess_parse(sp)
            self._parse_property_container(sp)
            self.on_subprocess_parsed(sp)
        self.on_process_parsed(p)


    def _parse_property_container(self, container):
        """Parses a property container.

        """
        for p in container.properties:
            self.on_topic_property_parse(p)
            if p.enum:
                self.on_enum_parse(p.enum)
                for ec in p.enum.choices:
                    self.on_enumchoice_parse(ec)
                    self.on_enumchoice_parsed(ec)
                self.on_enum_parsed(p.enum)
            self.on_topic_property_parsed(p)

        for ps in container.property_sets:
            self.on_topic_property_set_parse(ps)
            self._parse_property_container(ps)
            self.on_topic_property_set_parsed(ps)


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
