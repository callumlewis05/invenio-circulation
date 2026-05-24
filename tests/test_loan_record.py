# SPDX-FileCopyrightText: 2018-2019 CERN.
# SPDX-FileCopyrightText: 2018-2019 RERO.
# SPDX-License-Identifier: MIT

"""Tests for loan JSON schema."""

from copy import deepcopy

from invenio_circulation.proxies import current_circulation


def test_state_checkout_with_loan_pid(
    loan_created, db, params, mock_is_item_available_for_checkout
):
    """Test that created Loan validates after a checkout action."""
    new_params = deepcopy(params)
    new_params["trigger"] = "checkout"
    loan = current_circulation.circulation.trigger(loan_created, **new_params)
    loan.validate()


def test_indexed_loans(indexed_loans):
    """Test mappings, index creation and loans indexing."""
    assert indexed_loans
