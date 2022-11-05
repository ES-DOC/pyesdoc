import datetime as dt
import json
import uuid

from pyesdoc.utils import convert as convertor


# Default character set.
_JSON_CHARSET = "ISO-8859-1"

# ISO date formats.
_ISO_DATE_FORMATS = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"]


class JSONEncoder(json.JSONEncoder):
    """Extends json encoder so as to handle extended types.

    """
    def default(self, obj):
        if isinstance(obj, dt.datetime):
            return obj.isoformat().replace('T', ' ')
        elif isinstance(obj, dt.date):
            return obj.isoformat()
        elif isinstance(obj, dt.time):
            return obj.isoformat()
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        else:
            raise TypeError(f"{repr(obj)} is not JSON serializable")


class JSONDecoder(json.JSONDecoder):
    """A JSON decoder that handles extended types.

    """
    def __init__(self, key_formatter, to_namedtuple=False):
        json.JSONDecoder.__init__(self, encoding=_JSON_CHARSET, object_hook=self._to_object)
        self.key_formatter = key_formatter
        self.to_namedtuple = to_namedtuple
        self.value_parsers = [
            self._to_datetime,
            self._to_uuid
            ]

    def _to_object(self, obj: dict) -> object:
        """Maps a dictionary to an object.

        """
        # Parse values.
        for k, v in obj.items():
            for parser in self.value_parsers:
                if parser(obj, k, v):
                    break

        # Format keys.
        if self.key_formatter is not None:
            obj = convertor.dict_keys(obj, self.key_formatter)

        # Return dictionary | named tuple.
        return obj if not self.to_namedtuple else convertor.dict_to_namedtuple(obj)

    def _to_datetime(self, obj: dict, key: str, val: object) -> bool:
        """Maps a string to a datetime.

        """
        if isinstance(val, str) and len(val):
            try:
                float(val)
            except ValueError:
                for format in _ISO_DATE_FORMATS:
                    try:
                        val = dt.dt.strptime(val, format)
                    except (ValueError, TypeError):
                        pass
                    else:
                        obj[key] = val
                        return True

        return False

    def _to_uuid(self, obj: dict, key: str, val: object) -> bool:
        """Maps a dictionary value to a UUID instance.

        """
        if isinstance(val, str) and len(val):
            try:
                val = uuid.UUID(val)
            except ValueError:
                pass
            else:
                obj[key] = val
                return True

        return False
