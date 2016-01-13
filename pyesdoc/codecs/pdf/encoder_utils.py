# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.pdf.encoder_utils.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: PDF encoding utility functions.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import datetime
import os
import tempfile

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import PageBreak
from reportlab.platypus import Table
from reportlab.rl_config import defaultPageSize

import pyesdoc



# Default set of stylesheets.
STYLES = getSampleStyleSheet()

# Default font.
PAGE_FONT = 'Helvetica'

# Default height.
PAGE_HEIGHT = defaultPageSize[1]

# Default width.
PAGE_WIDTH = defaultPageSize[0]

# Default seperation between headers.
HEADER_SEPARATION = 0.3

# Default paragraph style.
PARAGRAPH_STYLE = STYLES['BodyText']

# The PDF 'story' being written.
story = []


def format_date(date):
    """Returns a date formatted for output.

    """
    return unicode(date)[0:10]


def linebreak(sep=HEADER_SEPARATION):
    """Adds a line break to active story.

    """
    story.append(Spacer(0.2 * inch, sep * inch))


def header(txt, level=1, sep=HEADER_SEPARATION):
    """Adds a header to active story.

    """
    linebreak(sep=sep)
    paragraph(txt, STYLES["Heading{}".format(level)])


def h1(txt, sep=0.3):
    """Adds a header (level 1) to active story.

    """
    header(txt, level=1, sep=sep)


def h2(txt, sep=HEADER_SEPARATION):
    """Adds a header (level 2) to active story.

    """
    header(txt, level=2, sep=sep)


def h3(txt, sep=HEADER_SEPARATION):
    """Adds a header (level 3) to active story.

    """
    header(txt, level=3, sep=sep)


def h4(txt, sep=HEADER_SEPARATION):
    """Adds a header (level 4) to active story.

    """
    header(txt, level=4, sep=sep)


def h5(txt, sep=HEADER_SEPARATION):
    """Adds a header (level 5) to active story.

    """
    header(txt, level=5, sep=sep)


def h6(txt, sep=HEADER_SEPARATION):
    """Adds a header (level 6) to active story.

    """
    header(txt, level=6, sep=sep)


def pagebreak():
    """Adds a page break to active story.

    """
    story.append(PageBreak())


def paragraph(txt, style=PARAGRAPH_STYLE):
    """Adds a text paragraph to active story.

    """
    story.append(Paragraph(txt, style))


def section_header(txt, level=1):
    header(txt, level=level)


def table(data):
    for row in data:
        h4(row[0], sep=0)
        paragraph(unicode(row[1]))
    # story.append(Table(data, colWidths=[0, 2.0]))


def set_frontis(doc):
    """Sets a PDF document's front page.

    """
    h1("Earth System Documentation")

    h1("Project: {}".format(doc.meta.project))
    h1("{}: {}".format(doc.meta.type_display_name, doc.ext.display_name), sep=0)

    h4("Document Version: {}".format(doc.meta.version))
    h4("Document Create Date: {}".format(format_date(doc.meta.create_date)), sep=0)
    h4("Document Update Date: {}".format(format_date(doc.meta.update_date)), sep=0)
    h4("PDF Generation Date: {}".format(format_date(datetime.datetime.now())), sep=0)
    pagebreak()


def get_content():
    global story

    fpath = tempfile.mkstemp()[1]
    try:
        template = SimpleDocTemplate(fpath)
        template.build(story)
        with open(fpath, 'r') as f:
            return f.read()
    finally:
        story = []
        if os.path.exists(fpath):
            os.remove(fpath)
