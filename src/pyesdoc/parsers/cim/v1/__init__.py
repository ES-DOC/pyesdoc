# Module imports.
from . import software_model_component



# Module exports.
__all__ = ['parsers']



# Supported parsers keyed by document type.
supported = {
	"cim.1.software.modelcomponent": software_model_component.parse
}
