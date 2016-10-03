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
    def __init__(self, realm, verbose=False, sort_collections=False):
        """Instance constructor.

        """
        self.realm = realm
        self.sort_collections = sort_collections
        self.verbose = verbose


    def run(self):
        """Runs the parser raising events as it does so.

        """
        if self.verbose:
            log("parsing: {}".format(self.realm.id))

        # Apply sorting priot to parsing.
        if self.sort_collections:
            self._sort()

        # Raise realm parse event.
        self.on_realm_parse(self.realm)

        # Parse grid.
        if self.realm.grid:
            self._parse_grid(self.realm, self.realm.grid)

        # Parse grid.
        if self.realm.key_properties:
            self._parse_key_properties(self.realm, self.realm.key_properties)

        # Parse processes.
        for process in self.realm.processes:
            self._parse_process(self.realm, process)

        # Raise realm parsed event.
        self.on_realm_parsed(self.realm)


    def _sort(self):
        """Sort collections priot to parsing.

        """
        self.realm.processes = sorted(self.realm.processes, key=lambda p: p.name)
        for process in self.realm.processes:
            process.sub_processes = sorted(process.sub_processes, key=lambda sp: sp.name)


    def on_realm_parse(self, realm):
        """On realm parse event handler.

        """
        pass


    def on_realm_parsed(self, realm):
        """On realm parsed event handler.

        """
        pass


    def on_grid_parse(self, realm, grid):
        """On grid parse event handler.

        """
        pass


    def on_grid_discretisation_parse(self, realm, grid, discretisation):
        """On grid discretisation parse event handler.

        """
        pass


    def on_grid_parsed(self, realm, grid):
        """On grid parsed event handler.

        """
        pass


    def on_key_properties_parse(self, realm, key_properties):
        """On key_properties parse event handler.

        """
        pass


    def on_key_properties_conservation_parse(self, realm, grid, conservation):
        """On key-properties conservation parse event handler.

        """
        pass


    def on_key_properties_extent_parse(self, realm, grid, extent):
        """On key-properties extent parse event handler.

        """
        pass


    def on_key_properties_resolution_parse(self, realm, grid, resolution):
        """On key-properties resolution parse event handler.

        """
        pass


    def on_key_properties_tuning_parse(self, realm, grid, tuning):
        """On key-properties tuning parse event handler.

        """
        pass


    def on_key_properties_parsed(self, realm, key_properties):
        """On key_properties parsed event handler.

        """
        pass


    def on_process_parse(self, realm, process):
        """On process parse event handler.

        """
        pass


    def on_process_parsed(self, realm, process):
        """On process parsed event handler.

        """
        pass


    def on_subprocess_parse(self, process, subprocess):
        """On sub-process parse event handler.

        """
        pass


    def on_subprocess_parsed(self, process, subprocess):
        """On sub-process parsed event handler.

        """
        pass


    def on_detail_parse(self, owner, detail):
        """On detail parse event handler.

        """
        pass


    def on_detail_property_parse(self, detail, prop):
        """On process detail parse event handler.

        """
        pass


    def on_detail_property_choice_parse(self, detail, prop, choice):
        """On process detail property choice parse event handler.

        """
        pass


    def _parse_grid(self, realm, grid):
        """Parses a grid.

        """
        if self.verbose:
            log("parsing: {}".format(grid.id))

        self.on_grid_parse(realm, grid)
        self._parse_details(grid)
        if grid.discretisation:
            self.on_grid_discretisation_parse(realm, grid, grid.discretisation)
            self._parse_details(grid.discretisation)
        self.on_grid_parsed(realm, grid)


    def _parse_key_properties(self, realm, key_properties):
        """Parses key properties.

        """
        if self.verbose:
            log("parsing: {}".format(key_properties.id))

        self.on_key_properties_parse(realm, key_properties)
        self._parse_details(key_properties)
        if key_properties.conservation:
            self.on_key_properties_conservation_parse(realm, key_properties, key_properties.conservation)
            self._parse_details(key_properties.conservation)
        if key_properties.extent:
            self.on_key_properties_extent_parse(realm, key_properties, key_properties.extent)
            self._parse_details(key_properties.extent)
        if key_properties.resolution:
            self.on_key_properties_resolution_parse(realm, key_properties, key_properties.resolution)
            self._parse_details(key_properties.resolution)
        if key_properties.tuning:
            self.on_key_properties_tuning_parse(realm, key_properties, key_properties.tuning)
            self._parse_details(key_properties.tuning)
        self.on_key_properties_parsed(realm, key_properties)


    def _parse_process(self, realm, process):
        """Parses a realm process.

        """
        # Raise process parse event.
        if self.verbose:
            log("parsing: {}".format(process.id))
        self.on_process_parse(realm, process)

        # Parse details.
        self._parse_details(process)

        # Parse child sub-processes.
        for sub_process in process.sub_processes:
            self._parse_subprocess(realm, process, sub_process)

        # Raise process parsed event.
        self.on_process_parsed(realm, process)


    def _parse_subprocess(self, realm, process, sub_process):
        """Parses a realm sub process.

        """
        # Raise sub-process parse event.
        if self.verbose:
            log("parsing: {}".format(sub_process.id))
        self.on_subprocess_parse(process, sub_process)

        # Iterate set of sub-process details.
        self._parse_details(sub_process)

        # Raise sub-process parsed event.
        self.on_subprocess_parsed(process, sub_process)


    def _parse_details(self, owner):
        """Parses a collection of details.

        """
        # Iterate set of details.
        for detail in owner.details:
            # Raise detail parse event.
            if self.verbose:
                log("parsing: {}".format(detail.id))
            self.on_detail_parse(owner, detail)

            # Iterate set of detail properties.
            for prop in detail.properties:
                # Raise detail-property parse event.
                if self.verbose:
                    log("parsing: {}".format(prop.id))
                self.on_detail_property_parse(detail, prop)

                # Iterate set of detail property choices.
                if prop.enum:
                    for choice in prop.enum.choices:
                        self.on_detail_property_choice_parse(detail, prop, choice)


def log(msg):
    """Outputs a message to log.

    :param str msg: Logging message.

    """
    if msg.startswith('-'):
        print(msg)
    else:
        print("ES-DOC :: {}".format(msg))
