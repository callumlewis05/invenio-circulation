# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Circulation fetchers."""

from invenio_pidstore.fetchers import FetchedPID

from ..api import Loan
from .pids import CIRCULATION_LOAN_PID_TYPE


def loan_pid_fetcher(record_uuid, data):
    """Fetch PID from loan record."""
    return FetchedPID(
        provider=None, pid_type=CIRCULATION_LOAN_PID_TYPE, pid_value=str(data["pid"])
    )
