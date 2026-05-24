# SPDX-FileCopyrightText: 2019-2020 CERN.
# SPDX-FileCopyrightText: 2019-2020 RERO.
# SPDX-License-Identifier: MIT

"""Circulation record loaders module."""

from invenio_records_rest.loaders import marshmallow_loader

from .schemas.json import LoanReplaceItemSchemaV1, LoanSchemaV1

loan_loader = marshmallow_loader(LoanSchemaV1)
loan_replace_item_loader = marshmallow_loader(LoanReplaceItemSchemaV1)
