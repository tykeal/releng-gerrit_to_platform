# SPDX-License-Identifier: Apache-2.0
##############################################################################
# Copyright (c) 2023 The Linux Foundation and others.
#
# All rights reserved. This program and the accompanying materials are made
# available under the terms of the Apache-2.0 license which accompanies this
# distribution, and is available at
# https://opensource.org/licenses/Apache-2.0
##############################################################################
"""Unit tests for config."""

import os

import gerrit_to_platform.config  # type: ignore
from gerrit_to_platform.config import get_config  # type: ignore

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "fixtures",
)


def test_get_config(mocker):
    """Test getting config data."""
    mocker.patch.object(
        gerrit_to_platform.config,
        "G2P_CONFIG_FILE",
        os.path.join(FIXTURE_DIR, "testconfig.ini"),
    )
    assert get_config()