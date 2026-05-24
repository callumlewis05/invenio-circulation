# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Circulation PIDs."""

CIRCULATION_LOAN_PID_TYPE = "loanid"
"""Persistent Identifier for Loans."""

CIRCULATION_LOAN_MINTER = "loanid"
"""Minter PID for Loans."""

CIRCULATION_LOAN_FETCHER = "loanid"
"""Fetcher PID for Loans."""

_LOANID_CONVERTER = 'pid(loanid,record_class="invenio_circulation.api:Loan")'
"""Loan PID url converter."""
