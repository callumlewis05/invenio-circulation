# SPDX-FileCopyrightText: 2019 CERN.
# SPDX-FileCopyrightText: 2019 RERO.
# SPDX-License-Identifier: MIT

"""Circulation Patron JSON Resolver module."""

import jsonresolver
from werkzeug.routing import Rule


@jsonresolver.hookimpl
def jsonresolver_loader(url_map):
    """Resolve the patron reference."""
    from flask import current_app as app

    resolving_path = app.config.get("CIRCULATION_DOCUMENT_RESOLVING_PATH") or "/"
    url_map.add(
        Rule(
            resolving_path,
            endpoint=app.config.get("CIRCULATION_DOCUMENT_RESOLVER_ENDPOINT"),
            host=app.config.get("JSONSCHEMAS_HOST"),
        )
    )
