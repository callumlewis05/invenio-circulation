# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Circulation Item JSON Resolver module."""

import jsonresolver
from werkzeug.routing import Rule


@jsonresolver.hookimpl
def jsonresolver_loader(url_map):
    """Resolve the item reference."""
    from flask import current_app

    resolving_path = current_app.config.get("CIRCULATION_ITEM_RESOLVING_PATH") or "/"
    url_map.add(
        Rule(
            resolving_path,
            endpoint=current_app.config.get("CIRCULATION_ITEM_RESOLVER_ENDPOINT"),
            host=current_app.config.get("JSONSCHEMAS_HOST"),
        )
    )
