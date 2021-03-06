#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013-2014 Tribus Developers
#
# This file is part of Tribus.
#
# Tribus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tribus is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import urllib
from django.core.management.base import BaseCommand
from tribus.common.repository import download_sample_packages
from tribus.config.pkgrecorder import CANAIMA_ROOT, LOCAL_ROOT, SAMPLES_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):
        download_sample_packages(CANAIMA_ROOT, SAMPLES_DIR)
        urllib.urlretrieve(os.path.join(CANAIMA_ROOT, "distributions"),
                           os.path.join(LOCAL_ROOT, "distributions"))
