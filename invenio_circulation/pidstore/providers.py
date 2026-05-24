# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Circulation PID providers."""

from invenio_pidstore.models import PIDStatus
from invenio_pidstore.providers.recordid import RecordIdProvider

from .pids import CIRCULATION_LOAN_PID_TYPE


class CirculationLoanIdProvider(RecordIdProvider):
    """Record identifier provider."""

    pid_type = CIRCULATION_LOAN_PID_TYPE
    """Type of persistent identifier."""

    pid_provider = None
    """Provider name.

    The provider name is not recorded in the PID since the provider does not
    provide any additional features besides creation of record ids.
    """

    default_status = PIDStatus.REGISTERED
    """Record IDs are by default registered immediately."""
