# SPDX-FileCopyrightText: 2018-2019 CERN.
# SPDX-FileCopyrightText: 2018-2019 RERO.
# SPDX-License-Identifier: MIT

"""Module tests."""


def test_version():
    """Test version import."""
    from invenio_circulation import __version__

    assert __version__
