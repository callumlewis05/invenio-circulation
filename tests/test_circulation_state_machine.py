# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Tests for circulation state machine logic."""

import pytest

from invenio_circulation.errors import NoValidTransitionAvailableError
from invenio_circulation.proxies import current_circulation


def test_invalid_transitions(loan_created, app, params):
    """Test that there are no conditional transitions at this state."""
    with pytest.raises(NoValidTransitionAvailableError):
        current_circulation.circulation.trigger(loan_created, **params)
