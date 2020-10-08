#!/usr/bin/env python

#
# Copyright (c) 2015-2020 ODC Contributors
#
# This file is part of the Open Data Cube
# See https://opendatacube.org for more information
#
# SPDX-License-Identifier: Apache-2.0
#
"""
Datacube command-line interface
"""


from datacube.ui.click import cli
import datacube.scripts.dataset
import datacube.scripts.ingest
import datacube.scripts.product
import datacube.scripts.metadata
import datacube.scripts.system
import datacube.scripts.user


if __name__ == '__main__':
    cli()
