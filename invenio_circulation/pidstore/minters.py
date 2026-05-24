# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Circulation minters."""

from ..api import Loan
from .providers import CirculationLoanIdProvider


def loan_pid_minter(record_uuid, data):
    """Mint loan identifiers."""
    assert "pid" not in data
    provider = CirculationLoanIdProvider.create(
        object_type="rec",
        object_uuid=record_uuid,
    )
    data["pid"] = provider.pid.pid_value
    return provider.pid
