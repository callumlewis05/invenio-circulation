# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Helper proxy to the state object."""

from flask import current_app
from werkzeug.local import LocalProxy

current_circulation = LocalProxy(lambda: current_app.extensions["invenio-circulation"])
"""Helper proxy to circulation state object."""
