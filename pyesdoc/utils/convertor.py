import collections
import csv
import datetime as dt
import pathlib
import re
import types
import typing
import uuid

import arrow

from pyesdoc.utils.serialisation import JSONDecoder
from pyesdoc.utils.serialisation import JSONEncoder


# Values considered to be abbreviations.
_ABBREVIATIONS = ("id", "uid", "uuid")


def capitalize(target: str) -> str:
    """Capitalizes passed string.

    :param target: A string to be converted.
    :returns: The target string capitalized.

    """
    if len(target) == 0:
        return target
    elif len(target) == 1:
        return target[0].upper()
    else:
        return target[0].upper() + target[1:]


def str_to_pascal_case(target: str, separator: str = "_") -> str:
    """Converts passed name to pascal case.

    :param target: A string to be converted.
    :param separator: A separator used to split target string into constituent parts.
    :returns: The target string converted to pascal case.

    """
    r = ""
    if target is not None and len(target):
        if target[0:len(separator)] == separator:
            # ... preserve initial separator
            r = separator

        # Iterate string parts.
        s = target.split(separator)
        for s in s:
            if s.lower() in _ABBREVIATIONS:
                r += s.upper()
            elif (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]

    return r


def str_to_camel_case(target: str, separator = "_") -> str:
    """Converts passed name to camel case.

    :param target: A string to be converted.
    :param separator: A separator used to split target string into constituent parts.
    :returns: The target string converted to camel case.

    """
    r = ""
    if target is not None and len(target):
        s = str_to_pascal_case(target, separator)
        if s[0:len(separator)] == separator:
            # ... preserve initial separator
            r += separator
            s = s[len(separator):]

        if s.lower() in _ABBREVIATIONS:
            # ... lower case abbreviations
            r += s.lower()

        elif len(s):
            # ... lower case initial character
            r += s[0].lower()
            r += s[1:]

    return r


def str_to_spaced_case(target: str, separator="_") -> str:
    """Helper function to convert a string value from camel case to spaced case.

    :param target: A string for conversion.
    :returns: A string converted to spaced case.

    """
    if target is None:
        return ""
    elif separator is not None and len(target.split(separator)) > 1:
        return " ".join(target.split(separator))
    elif target.find(" ") == -1:
        return re.sub("([A-Z])", ' \g<0>', target).strip()
    else:
        return target


def str_to_underscore_case(target: str) -> str:
    """Helper function to convert a from camel case string to an underscore case string.

    :param target: A string for conversion.
    :returns: A string converted to underscore case, e.g. account_number.

    """
    if target is None or not len(target):
        return ""

    r = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", target)
    r = re.sub("([a-z0-9])([A-Z])", r"\1_\2", r)
    r = r.lower()

    return r


def json_to_dict(repr: str, key_formatter: typing.Callable = None) -> dict:
    """Converts a json encoded string to a dictionary.

    :param repr: A json encoded string.
    :param key_formatter: Dictionary key formatter.
    :returns: A dictionary.

    """
    return JSONDecoder(key_formatter).decode(repr)


def json_to_namedtuple(
    repr: str,
    key_formatter: typing.Callable = None
) -> collections.namedtuple:
    """Converts a json encoded string to a namedtuple.

    :param repr: A json encoded string.
    :param key_formatter: Dictionary key formatter.
    :returns: A namedtuple.

    """
    return JSONDecoder(key_formatter, to_namedtuple=True).decode(repr)


def json_file_to_dict(
    fp: pathlib.Path,
    key_formatter: typing.Callable = None
) -> dict:
    """Converts a json file to a dictionary.

    :param fp: A json file path.
    :param key_formatter: Dictionary key formatter.
    :returns: A dictionary.

    """
    return _convert_file(fp, json_to_dict, key_formatter)


def json_file_to_namedtuple(
    fp: pathlib.Path,
    key_formatter: typing.Callable = None
) -> collections.namedtuple:
    """Converts a json file to a namedtuple.

    :param fp: A json file path.
    :param key_formatter: Dictionary key formatter.
    :returns: A namedtuple.

    """
    return _convert_file(fp, json_to_namedtuple, key_formatter)


def dict_to_json(obj: dict, key_formatter: typing.Callable =None) -> str:
    """Converts a dictionary to a JSON string.

    :param obj: A dictionary.
    :param key_formatter: Dictionary key formatter.
    :returns: A JSON encoded string.

    """
    if key_formatter is not None:
        obj = dict_keys(obj, key_formatter)

    return JSONEncoder().encode(obj)


def dict_to_namedtuple(obj: dict, key_formatter: typing.Callable =None) -> collections.namedtuple:
    """Converts a dictionary to a named tuple.

    :param obj: Dictionary being converted.
    :param key_formatter: Dictionary key formatter.
    :returns: A named tuple.

    """
    if key_formatter is not None:
        obj = key_formatter(obj)

    return collections.namedtuple("_Class", obj.keys())(**obj)


def dict_keys(obj: dict, key_formatter: typing.Callable = str_to_pascal_case) -> dict:
    """Converts keys of a dictionary using the passed key formatter.

    :param obj: A dictionary.
    :param key_formatter: A dictionary key formatter function pointer.
    :returns: A dictionary with it"s keys formatted accordingly.

    """
    if not isinstance(obj, dict):
        return obj
    
    def _get_value(val: object) -> object:
        if isinstance(val, dict):
            return dict_keys(val, key_formatter)
        elif isinstance(val, types.ListType):
            return map(lambda i: dict_keys(i, key_formatter), val)
        else:
            return val

    return {key_formatter(k): _get_value(v) for k, v in obj.items()}


def dict_keys_to_lower_case(obj: dict) -> dict:
    """Converts keys of a dictionary to lower case.

    :param obj: A dictionary.
    :returns: A dictionary with it"s keys formatted accordingly.

    """
    return dict_keys(obj, lambda k: k.lower())


def dict_keys_to_upper_case(obj: dict) -> dict:
    """Converts keys of a dictionary to upper case.

    :param d: A dictionary.
    :returns: A dictionary with it"s keys formatted accordingly.

    """
    return dict_keys(obj, lambda k: k.upper())


def dict_keys_to_camel_case(obj: dict) -> dict:
    """Converts keys of a dictionary to camel case.

    :param obj: A dictionary.
    :returns: A dictionary with it"s keys formatted accordingly.

    """
    return dict_keys(obj, str_to_camel_case)


def dict_keys_to_pascal_case(obj: dict) -> dict:
    """Converts keys of a dictionary to pascal case.

    :param obj: A dictionary.
    :returns: A dictionary with it"s keys formatted accordingly.

    """
    return dict_keys(obj, str_to_pascal_case)


def dict_keys_to_underscore_case(obj: dict) -> dict:
    """Converts keys of a dictionary to underscore case.

    :param obj: A dictionary.
    :returns: A dictionary with it"s keys formatted accordingly.

    """
    return dict_keys(obj, str_to_underscore_case)


def now_to_timestamp(offset: int = 0) -> float:
    """Returns an timestamp (optionally) offseted from utcnow.

    :param offset: Number of ticks to offset now by.
    :returns: A POSIX timestamp.

    """
    dt.datetime.utcnow().timestamp + offset


def csv_file_to_dict(fp) -> typing.List[dict]:
    """Converts a csv file -> list of dictionaries.

    :param fp: Path to a csv file.
    :returns: A list of dictionaries.

    """
    with open(fp, "r") as fstream:
        return map(lambda r: r, csv.DictReader(fstream))


def csv_file_to_namedtuple(fp: pathlib.Path) -> typing.List[collections.namedtuple]:
    """Converts a csv file -> list of named tuples.

    :param fp: Path to a csv file.
    :returns: A list of named tuples.

    """
    with open(fp, "r") as fstream:
        return map(dict_to_namedtuple, csv.DictReader(fstream))


def csv_file_to_json(fp: pathlib.Path) -> str:
    """Converts a csv file -> json text blob.

    :param fp: Path to a csv file.
    :returns: A json text blob.

    """
    return dict_to_json(csv_file_to_dict(fp))


def csv_file_to_json_file(fp: pathlib.Path, dest: pathlib.Path=None) -> pathlib.Path:
    """Converts a csv file -> json file.

    :param fp: Path to a csv file.
    :param dest: Path to output file.
    :returns: Path to output file.

    """
    if dest is None:
        dest = fp.split(".")[0] + ".json"
    with open(dest, "w") as f:
        f.write(dict_to_json(csv_file_to_dict(fp)))
    
    return dest


def text_to_typed_value(
    text: str,
    kls: type
) -> typing.Union[bool, int, float, str, dt.datetime, uuid.uuid4, object]:
    """Converts text to a typed value.

    :param text: Text to be converted to a typed value.
    :param kls: Target type.
    :returns: A typed value.

    """
    if len(text) == 0:
        return None
    elif kls is str:
        return text
    elif kls in {dt.datetime, dt.date, dt.time}:
        return arrow.get(text).datetime
    elif kls is uuid.UUID:
        return uuid.UUID(text)
    elif kls is bool:
        return text.lower() in {"yes", "true", "t", "1", "y"}
    else:
        try:
            return kls(text)
        except Exception:
            print(f"SCALAR TYPE DECODING ERROR: {text} :: {kls}")


def _convert_file(
    fp: pathlib.Path,
    convertor: typing.Callable,
    key_formatter: typing.Callable =None
) -> object:
    """Converts a file.
    
    """
    with open(fp, "r") as fstream:
        return convertor(fstream.read(), key_formatter)
