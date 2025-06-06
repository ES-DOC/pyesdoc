"""
.. module:: pyessv._utils.compay.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: python 2 to 3 compatibilty extensions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

import sys

# Syntax sugar.
_ver = sys.version_info

# Is Python 2.x?
is_py2 = (_ver[0] == 2)

# Is Python 3.x?
is_py3 = (_ver[0] == 3)

# JSON.
try:
    import simplejson as json
except (ImportError, SyntaxError):
    # simplejson does not support Python 3.2, it throws a SyntaxError
    # because of u'...' Unicode literals.
    import json


# ---------
# Python 2
# ---------
if is_py2:
    from urllib.parse import quote, unquote, quote_plus, unquote_plus, urlencode
    from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urldefrag
    from urllib2 import parse_http_list
    import http.cookiejar
    from http.cookies import Morsel
    from io import StringIO

    builtin_str = str
    bytes = str
    str = str
    str = str
    numeric_types = (int, int, float)
    integer_types = (int, int)

# ---------
# Python 3
# ---------
elif is_py3:
    from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urlencode, quote, unquote, quote_plus, unquote_plus, urldefrag
    from urllib.request import parse_http_list, getproxies, proxy_bypass
    from http import cookiejar as cookielib
    from http.cookies import Morsel
    from io import StringIO

    builtin_str = str
    str = str
    bytes = bytes
    str = (str, bytes)
    numeric_types = (int, float)
    integer_types = (int,)
