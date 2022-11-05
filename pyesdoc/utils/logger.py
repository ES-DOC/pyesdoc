import datetime as dt
import typing


# Set of logging levels.
LOG_LEVEL_DEBUG = "DEBUG"
LOG_LEVEL_INFO = "INFO"
LOG_LEVEL_WARNING = "WARNING"
LOG_LEVEL_ERROR = "ERROR"
LOG_LEVEL_CRITICAL = "CRITICAL"
LOG_LEVEL_FATAL = "FATAL"

# Text to display when passed a null message.
_NULL_MSG = "-------------------------------------------------------------------------------"


def log(msg: object=None, level: str=LOG_LEVEL_INFO):
    """Outputs a message to log.

    :param msg: Message to be written to log.
    :param level: Message level (e.g. INFO).

    """
    # TODO use structlog/logstash.
    print(_get_formatted_message(msg, level))


def log_error(err: typing.Union[BaseException, str]):
    """Logs a runtime error.

    :param err: Error to be written to log.

    """
    msg = "!! RUNTIME ERROR !! :: "
    if issubclass(BaseException, err.__class__):
        msg += "{} :: {}".format(err.__class__, err)
    else:
        msg += "{}".format(err)
    log(msg, LOG_LEVEL_ERROR)


def log_warning(err: typing.Union[BaseException, str]):
    """Logs a runtime warning.

    :param err: Error to be written to log.

    """
    if issubclass(BaseException, err.__class__):
        msg = "{} :: {}".format(err.__class__, err)
    else:
        msg = "{}".format(err)
    log(msg, LOG_LEVEL_WARNING)


def _get_formatted_message(msg: object, level: str) -> str:
    """Returns a message formatted for logging.

    """
    if msg is None:
        return _NULL_MSG
    else:
        return f"{dt.datetime.utcnow()} [{level}] :: PYESDOC :: {str(msg).strip()}"
