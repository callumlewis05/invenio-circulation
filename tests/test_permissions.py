# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Test circulation permissions on transitions."""

import pytest
from invenio_records_rest.utils import allow_all, deny_all

from invenio_circulation.errors import InvalidPermissionError
from invenio_circulation.transitions.transitions import CreatedToPending


def test_valid_permission(loan_created, params):
    """Test transition with valid permission."""
    transition = CreatedToPending(
        "CREATED", "PENDING", trigger="next", permission_factory=allow_all
    )
    transition.execute(loan_created, **params)
    assert loan_created["state"] == "PENDING"


def test_invalid_permission(loan_created, params):
    """Test transition without permission."""
    transition = CreatedToPending(
        "CREATED", "PENDING", trigger="next", permission_factory=deny_all
    )
    with pytest.raises(InvalidPermissionError):
        transition.execute(loan_created, **params)
    assert loan_created["state"] == "CREATED"
