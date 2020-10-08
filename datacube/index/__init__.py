#
# Copyright (c) 2015-2020 ODC Contributors
#
# This file is part of the Open Data Cube
# See https://opendatacube.org for more information
#
# SPDX-License-Identifier: Apache-2.0
#
"""
Modules for interfacing with the index/database.
"""

from ._api import index_connect
from .fields import UnknownFieldError
from .exceptions import DuplicateRecordError, MissingRecordError, IndexSetupError
from .index import Index

__all__ = [
    'index_connect',
    'Index',

    'DuplicateRecordError',
    'IndexSetupError',
    'MissingRecordError',
    'UnknownFieldError',
]
