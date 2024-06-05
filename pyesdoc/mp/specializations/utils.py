"""
.. module:: utils.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: CMIP6 specialization validation utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
def log(msg):
    """Outputs a message to log.

    :param str msg: Logging message.

    """
    if msg.startswith('-'):
        print(msg)
    else:
        print("ES-DOC :: {}".format(msg))


def get_label(name):
    """Returns a name formatted as a label for UI purposes.

    """
    name = name.replace("_", " ")

    return " ".join("{}{}".format(n[0].upper(), n[1:]) for n in name.split(" "))

