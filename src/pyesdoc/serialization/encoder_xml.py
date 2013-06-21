"""CIM xml encoding functions.

"""


def encode(ctx):
    """Encodes an xml representation of passed pyesdoc document instance.

    :param ctx: Serialization context info.
    :type ctx: namedtuple

    """
    ctx.representation = None

