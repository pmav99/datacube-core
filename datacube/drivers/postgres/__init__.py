#
# Copyright (c) 2015-2020 ODC Contributors
#
# This file is part of the Open Data Cube
# See https://opendatacube.org for more information
#
# SPDX-License-Identifier: Apache-2.0
#
"""
Lower-level database access.

This package tries to contain any SQLAlchemy and database-specific code.
"""

from ._connections import PostgresDb

__all__ = ['PostgresDb']
