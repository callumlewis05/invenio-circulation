# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-FileCopyrightText: 2018 RERO.
# SPDX-License-Identifier: MIT

"""Signals for Invenio-Circulation."""

from blinker import Namespace

_signals = Namespace()

loan_state_changed = _signals.signal("loan-state-changed")
"""Loan state changed signal.

Broadcasted when a loan action is triggered, sending the old and the updated
loan object.
"""

loan_replace_item = _signals.signal("loan-replace-item")
"""Loan item changed signal.

Broadcasted when the item in a Loan is replaced, sending the old and the new
item_pid.
"""
