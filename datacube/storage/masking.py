#
# Copyright (c) 2015-2020 ODC Contributors
#
# This file is part of the Open Data Cube
# See https://opendatacube.org for more information
#
# SPDX-License-Identifier: Apache-2.0
#
import warnings

warnings.warn("datacube.storage.masking has moved to datacube.utils.masking",
              category=DeprecationWarning)

from datacube.utils.masking import *
