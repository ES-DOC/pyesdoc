"""
.. module:: software_classes.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 software package class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""


def component_language():
    """Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('name', 'str', '1.1'),
            ('properties', 'software.component_language_property', '0.N'),
        ],
        'doc_strings': {
            'name': 'The name of the language.'
        },
        'decodings' : [
            ('name', 'child::cim:name'),
        ]
    }


def component_language_property():
    """This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).

    """
    return {
        'type' : 'class',
        'base' : 'shared.property',
        'is_abstract' : False
    }


def component_property():
    """ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.

    """
    return {
        'type' : 'class',
        'base' : 'shared.data_source',
        'is_abstract' : False,
        'properties' : [
            ('sub_properties', 'software.component_property', '0.N'),
            ('citations', 'shared.citation', '0.N'),
            ('description', 'str', '0.1'),
            ('grid', 'str', '0.1'),
            ('intent', 'software.component_property_intent_type', '0.1'),
            ('is_represented', 'bool', '1.1'),
            ('long_name', 'str', '0.1'),
            ('short_name', 'str', '1.1'),
            ('standard_names', 'str', '0.N'),
            ('units', 'shared.unit_type', '0.1'),
            ('values', 'str', '0.N'),
        ],
        'doc_strings': {
            'grid': 'A reference to the grid that is used by this component.',
            'intent': 'The direction that this property is intended to be coupled: in, out, or inout.',
            'is_represented': 'When set to false, means that this property is not used by the component. Covers the case when, for instance, a modeler chooses not to represent some property in their model. (But still allows meaningful comparisons between components which _do_ model this property.)',
            'units': 'The standard name that this property is known as (for example, its CF name).',
            'values': 'The value of the property (not applicable to fields).',
        },
        'decodings' : [
            ('sub_properties', 'child::cim:componentProperty'),
            ('citations', 'child::cim:citation'),
            ('description', 'child::cim:description'),
            ('grid'),
            ('intent', 'self::cim:componentProperty/@intent'),
            ('is_represented', 'self::cim:componentProperty/@represented'),
            ('long_name', 'child::cim:longName'),
            ('short_name', 'child::cim:shortName'),
            ('standard_names', 'child::cim:standardName/@value'),
            ('units', 'child::cim:units/@value'),
            ('values', 'child::cim:value'),
        ]
    }


def composition():
    """The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('couplings', 'str', '0.N'),
            ('description', 'str', '0.1'),
        ]
    }


def connection():
    """A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('properties', 'software.connection_property', '0.N'),
            ('sources', 'software.connection_endpoint', '0.N'),
            ('target', 'software.connection_endpoint', '0.1'),
            ('description', 'str', '0.1'),
            ('priming', 'shared.data_source', '0.1'),
            ('spatial_regridding', 'software.spatial_regridding', '0.N'),
            ('time_lag', 'str', '0.1'),
            ('time_profile', 'software.timing', '0.1'),
            ('time_transformation', 'software.time_transformation', '0.1'),
            ('transformers', 'software.processor_component', '0.N'),
            ('type', 'software.connection_type', '0.1'),
        ],
        'doc_strings': {
            'sources': 'The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource.',
            'target': 'The target property being connected.  This is optional to support the way that input is handled in the CMIP5 questionnaire.',
            'priming': 'A priming source is one that is active on the first available timestep only (before "proper" coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.',
            'spatial_regridding': 'Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)',
            'time_lag': 'The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.',
            'time_profile': 'All information having to do with the rate of this connection; the times that it is active.  This overrides any rate of a Coupling.',
            'time_transformation': 'Temporal transformation performed on the coupling field before or after regridding onto the target grid.',
            'transformers': 'An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.',
            'type': 'The type of Connection'
        },
        'decodings' : [
            ('properties', 'child::cim:connectionProperty'),
            ('sources', 'child::cim:connectionSource'),
            ('target', 'child::cim:connectionTarget'),
            ('description', 'child::cim:description'),
            ('priming', 'child::cim:priming/cim:priming/cim:dataObject', 'data.data_object'),
            ('priming', 'child::cim:priming/cim:priming/cim:dataContent', 'data.data_content'),
            ('priming', 'child::cim:priming/cim:priming/cim:componentProperty', 'software.component_property'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.model_component'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.processor_component'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.statistical_model_component'),
            ('priming', 'child::cim:priming/cim:reference', 'shared.doc_reference'),
            ('spatial_regridding', 'child::cim:spatialRegridding'),
            ('time_lag', 'child::cim:timeLag'),
            ('time_profile', 'child::cim:timeProfile'),
            ('time_transformation', 'child::cim:timeTransformation'),
            ('transformers', 'child::cim:transformer/cim:processorComponent'),
            ('transformers', 'child::cim:transformer/cim:reference', 'shared.doc_reference'),
            ('type', 'child::cim:type/@value'),
        ]
    }


def connection_endpoint():
    """The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('properties', 'software.connection_property', '0.N'),
            ('data_source', 'shared.data_source', '0.1'),
            ('instance_id', 'str', '0.1'),
        ],
        'doc_strings': {
            'properties': 'The place to describe features specific to the source/target of a connection.',
            'instance_id': 'If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).',
        },
        'decodings' : [
            ('properties', 'child::cim:connectionProperty'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:dataObject', 'data.data_object'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:dataContent', 'data.data_content'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:componentProperty', 'software.component_property'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.model_component'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.processor_component'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.statistical_model_component'),
            ('data_source', 'child::cim:dataSource/cim:reference', 'shared.doc_reference'),
            ('instance_id', 'child::cim:instanceID'),
        ]
    }


def connection_property():
    """A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.

    """
    return {
        'type' : 'class',
        'base' : 'shared.property',
        'is_abstract' : False
    }


def coupling():
    """A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('connections', 'software.connection', '0.N'),
            ('properties', 'software.coupling_property', '0.N'),
            ('sources', 'software.coupling_endpoint', '1.N'),
            ('target', 'software.coupling_endpoint', '1.1'),
            ('description', 'str', '0.1'),
            ('is_fully_specified', 'bool', '1.1'),
            ('purpose', 'shared.data_purpose', '1.1'),
            ('priming', 'shared.data_source', '0.1'),
            ('spatial_regriddings', 'software.spatial_regridding', '0.N'),
            ('time_profile', 'software.timing', '0.1'),
            ('time_lag', 'software.time_lag', '0.1'),
            ('time_transformation', 'software.time_transformation', '0.1'),
            ('transformers', 'software.processor_component', '0.N'),
            ('type', 'software.connection_type', '0.1')
        ],
        'doc_strings': {
            'sources': 'The source component of the coupling. (note that there can be multiple sources).',
            'target': 'The target component of the coupling.',
            'description': 'A free-text description of the coupling.',
            'is_fully_specified': 'If true then the coupling is fully-specified.  If false then not every Connection has been described within the coupling.',
            'priming': 'A priming source is one that is active on the first available timestep only (before "proper" coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created.',
            'spatial_regriddings': 'Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).',
            'time_profile': 'Describes how often the coupling takes place.',
            'time_lag': 'The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time.',
            'time_transformation': 'Temporal transformation performed on the coupling field before or after regridding onto the target grid.',
            'transformers': 'An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here.',
            'type': 'Describes the method of coupling.'
        },
        'decodings' : [
            ('connections', 'child::cim:connection'),
            ('properties', 'child::cim:couplingProperty'),
            ('sources', 'child::cim:couplingSource'),
            ('target', 'child::cim:couplingTarget'),
            ('description', 'child::cim:description'),
            ('is_fully_specified', '@fullySpecified'),
            ('priming', 'child::cim:priming/cim:priming/cim:dataObject', 'data.data_object'),
            ('priming', 'child::cim:priming/cim:priming/cim:dataContent', 'data.data_content'),
            ('priming', 'child::cim:priming/cim:priming/cim:componentProperty', 'software.component_property'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.model_component'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.processor_component'),
            ('priming', 'child::cim:priming/cim:priming/cim:softwareComponent', 'software.statistical_model_component'),
            ('priming', 'child::cim:priming/cim:reference', 'shared.doc_reference'),
            ('purpose', '@purpose'),
            ('spatial_regriddings', 'child::cim:spatialRegridding'),
            ('time_lag', 'child::cim:timeLag'),
            ('time_profile', 'child::cim:timeProfile'),
            ('time_transformation', 'child::cim:timeTransformation'),
            ('transformers', 'child::cim:transformer/cim:processorComponent'),
            ('transformers', 'child::cim:transformer/cim:reference', 'shared.doc_reference'),
            ('type', 'child::cim:type/@value')
        ]
    }


def coupling_endpoint():
    """The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('properties', 'software.coupling_property', '0.N'),
            ('data_source', 'shared.data_source', '0.1'),
            ('instance_id', 'str', '0.1')
        ],
        'doc_strings': {
            'properties': 'A place to describe features specific to the source/target of a coupling',
            'instance_id': 'If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG).'
        },
        'decodings' : [
            ('properties', 'child::cim:couplingProperty'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:dataObject', 'data.data_object'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:dataContent', 'data.data_content'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:componentProperty', 'software.component_property'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.model_component'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.processor_component'),
            ('data_source', 'child::cim:dataSource/cim:dataSource/cim:softwareComponent', 'software.statistical_model_component'),
            ('data_source', 'child::cim:dataSource/cim:reference', 'shared.doc_reference'),
            ('instance_id', 'child::cim:instanceID')
        ]
    }


def coupling_property():
    """A CouplingProperty is a name/value pair used to specify OASIS-specific properties.

    """
    return {
        'type' : 'class',
        'base' : 'shared.property',
        'is_abstract' : False
    }


def deployment():
    """Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('deployment_date', 'datetime', '0.1'),
            ('description', 'str', '0.1'),
            ('parallelisation', 'software.parallelisation', '0.1'),
            ('platform', 'shared.platform', '0.1'),
            ('executable_name', 'str', '0.1'),
            ('executable_arguments', 'str', '0.N'),
        ],
        'doc_strings': {
            'platform': 'The platform that this deployment has been run on. It is optional to allow for "unconfigured" models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS).'
        },
        'decodings' : [
            ('deployment_date', 'child::cim:deploymentDate'),
            ('description', 'child::cim:description'),
            ('parallelisation', 'child::cim:parallelisation'),
            ('platform', 'child::cim:platform/cim:platform'),
            ('platform', 'child::cim:platform/cim:reference', 'shared.doc_reference'),
            ('executable_name', 'child::cim:executableName'),
            ('executable_arguments', 'child::cim:executableArgument'),
        ]
    }


def entry_point():
    """Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the "proceeds" and "follows" attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('name', 'str', '0.1'),
        ]
    }


def model_component():
    """A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """
    return {
        'type' : 'class',
        'base' : 'software.component',
        'is_abstract' : False,
        'is_document': True,
        'properties' : [
            ('type', 'software.model_component_type', '0.1'),
            ('types', 'software.model_component_type', '1.N'),
            ('timing', 'software.timing', '0.1'),
            ('activity', 'activity.activity', '0.1'),
        ],
        'doc_strings': {
            'type': 'Describes the type of component. There can be multiple types.',
            'types': 'Describes the type of component. There can be multiple types.',
            'timing': 'Describes information about how this component simulates time.',
        },
        'decodings' : [
            ('meta', 'self::cim:modelComponent'),
            ('timing', 'child::cim:timing'),
            ('type', 'child::cim:type[1]/@value'),
            ('types', 'child::cim:type/@value'),
        ]
    }


def parallelisation():
    """Describes how a deployment has been parallelised across a computing platform.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('processes', 'int', '1.1'),
            ('ranks', 'software.rank', '0.N'),
        ],
        'decodings' : [
            ('processes', 'child::cim:processes'),
            ('ranks', 'child::cim:rank'),
        ]
    }


def processor_component():
    """A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

    """
    return {
        'type' : 'class',
        'base' : 'software.component',
        'is_abstract' : False,
        'is_document': True,
        'properties' : [

        ],
        'decodings' : [
            ('meta', 'self::cim:modelComponent'),
        ]
    }


def rank():
    """Creates and returns instance of rank class.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('value', 'int', '0.1'),
            ('min', 'int', '0.1'),
            ('max', 'int', '0.1'),
            ('increment', 'int', '0.1'),
        ],
        'decodings' : [
            ('value', 'child::cim:rankValue'),
            ('min', 'child::cim:rankMin'),
            ('max', 'child::cim:rankMax'),
            ('increment', 'child::cim:rankIncrement'),
        ]
    }


def component():
    """A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested "child" components. Every component can have "componentProperties" which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component\'s composition must be owned by that component or a child of that component; child components cannot couple together their parents\' properties.

    """
    return {
        'type' : 'class',
        'base' : 'shared.data_source',
        'is_abstract' : False,
        'properties' : [
            ('sub_components', 'software.component', '0.N'),
            ('citations', 'shared.citation', '0.N'),
            ('code_access', 'str', '0.1'),
            ('composition', 'software.composition', '0.1'),
            ('coupling_framework', 'software.coupling_framework_type', '0.1'),
            ('dependencies', 'software.entry_point', '0.N'),
            ('deployments', 'software.deployment', '0.N'),
            ('description', 'str', '0.1'),
            ('funding_sources', 'str', '0.N'),
            ('grid', 'grids.grid_spec', '0.1'),
            ('is_embedded', 'bool', '0.1'),
            ('language', 'software.component_language', '0.1'),
            ('license', 'shared.license', '0.1'),
            ('long_name', 'str', '0.1'),
            ('online_resource', 'uri', '0.1'),
            ('parent', 'software.component', '0.1'),
            ('previous_version', 'str', '0.1'),
            ('properties', 'software.component_property', '0.N'),
            ('release_date', 'datetime', '0.1'),
            ('responsible_parties', 'shared.responsible_party', '0.N'),
            ('short_name', 'str', '1.1'),
            ('version', 'str', '0.1'),
        ],
        'doc_strings': {
            'code_access': 'Instructions on how to access the source code for this component.',
            'coupling_framework': 'The coupling framework that this entire component conforms to.',
            'description': 'A free-text description of the component.',
            'funding_sources': 'The entities that funded this software component.',
            'grid': 'A reference to the grid that is used by this component.',
            'is_embedded': 'An embedded component cannot exist on its own as an atomic piece of software; instead it is embedded within another (parent) component. When embedded equals "true", the SoftwareComponent has a corresponding piece of software (otherwise it is acting as a "virtual" component which may be inexorably nested within a piece of software along with several other virtual components).',
            'license': 'The license held by this piece of software.',
            'long_name': 'The name of the model (that is recognized externally).',
            'online_resource': 'Provides a URL location for this model.',
            'properties': 'The properties that this model simulates and/or couples.',
            'release_date': 'The date of publication of the software component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)',
            'short_name': 'The name of the model (that is used internally).',
            'version': 'A free text description of the component version #.'
        },
        'decodings' : [
            ('sub_components', 'child::cim:childComponent/cim:modelComponent', 'software.model_component'),
            ('sub_components', 'child::cim:childComponent/cim:processorComponent', 'software.processor_component'),
            ('citations', 'child::cim:citation'),
            ('description', 'child::cim:description'),
            ('language', 'child::cim:componentLanguage'),
            ('long_name', 'child::cim:longName'),
            ('properties', 'child::cim:componentProperties/cim:componentProperty'),
            ('properties', 'child::cim:scientificProperties/cim:componentProperty'),
            ('properties', 'child::cim:numericalProperties/cim:componentProperty'),
            ('release_date', 'child::cim:releaseDate'),
            ('responsible_parties', 'child::cim:responsibleParty'),
            ('short_name', 'child::cim:shortName'),
        ]
    }


def spatial_regridding():
    """Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('dimension', 'software.spatial_regridding_dimension_type', '0.1'),
            ('properties', 'software.spatial_regridding_property', '0.N'),
            ('standard_method', 'software.spatial_regridding_standard_method_type', '0.1'),
            ('user_method', 'software.spatial_regridding_user_method', '0.1'),
        ],
        'decodings' : [
            ('dimension', 'child::cim:spatialRegriddingDimension'),
            ('properties', 'child::cim:spatialRegriddingProperty'),
            ('standard_method', 'child::cim:spatialRegriddingStandardMethod'),
            ('user_method', 'child::cim:spatialRegriddingUserMethod'),
        ]
    }


def spatial_regridding_property():
    """Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)

    """
    return {
        'type' : 'class',
        'base' : 'shared.property',
        'is_abstract' : False
    }


def spatial_regridding_user_method():
    """Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('file', 'data.data_object', '0.1'),
            ('name', 'str', '1.1')
        ],
        'decodings' : [
            ('file', 'child::cim:file/cim:dataObject'),
            ('file', 'child::cim:file/cim:reference', 'shared.doc_reference'),
            ('name', 'child::cim:name')
        ]
    }


def statistical_model_component():
    """Creates and returns instance of statistical_model_component class.

    """
    return {
        'type' : 'class',
        'base' : 'software.component',
        'is_abstract' : False,
        'is_document': True,
        'properties' : [
            ('type', 'software.statistical_model_component_type', '0.1'),
            ('types', 'software.statistical_model_component_type', '1.N'),
            ('timing', 'software.timing', '0.1'),
        ],
        'doc_strings': {
            'type': 'Describes the type of component. There can be multiple types.',
            'types': 'Describes the type of component. There can be multiple types.',
            'timing': 'Describes information about how this component simulates time.',
        },
        'decodings' : [
            ('meta', 'self::cim:statisticalModelComponent'),
            ('timing', 'child::cim:timing'),
            ('type', 'child::cim:type[1]/@value'),
            ('types', 'child::cim:type/@value'),
        ]
    }


def time_lag():
    """The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('value', 'int', '0.1'),
            ('units', 'software.timing_units', '0.1'),
        ],
        'decodings' : [
            ('value', 'child::cim:value'),
            ('units', '@units'),
        ]
    }


def timing():
    """Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('end', 'datetime', '0.1'),
            ('is_variable_rate', 'bool', '0.1'),
            ('rate', 'int', '0.1'),
            ('start', 'datetime', '0.1'),
            ('units', 'software.timing_units', '0.1'),
        ],
        'doc_strings': {
            'is_variable_rate': 'Describes whether or not the model supports a variable timestep. If set to true, then rate should not be specified.'
        },
        'decodings' : [
            ('end', 'child::cim:end'),
            ('is_variable_rate', '@variableRate'),
            ('rate', 'child::cim:rate'),
            ('start', 'child::cim:start'),
            ('units', '@units'),
        ]
    }


def time_transformation():
    """The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

    """
    return {
        'type' : 'class',
        'base' : None,
        'is_abstract' : False,
        'properties' : [
            ('description', 'str', '0.1'),
            ('mapping_type', 'software.time_mapping_type', '1.1'),
        ],
        'decodings' : [
            ('description', 'child::cim:description'),
            ('mapping_type', 'child::cim:mappingType/@value'),
        ]
    }
