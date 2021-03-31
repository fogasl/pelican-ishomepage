"""Add Jinja global function `ishomepage(url, output_file)`.

Invoking this function in a template can tell whether the currently
generated page is front page or not. This dirty little hack is required
to correctly add e.g. `active` class to the home page menu element.
"""

import logging

from pelican import signals

logger = logging.getLogger(__name__)


def add_ishomepage_fn(pelican):
    def ishomepage(url, output_file):
        res = url == pelican.settings["SITEURL"] + "/" and \
            output_file == pelican.settings["INDEX_SAVE_AS"]

        logger.debug("Is home page: url: %s, output_file: %s -> %s" % \
            (url, output_file, res))

        return res

    pelican.settings["JINJA_GLOBALS"]["ishomepage"] = ishomepage


def register():
    signals.initialized.connect(add_ishomepage_fn)
