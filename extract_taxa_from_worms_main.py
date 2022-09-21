#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# Copyright (c) 2021-present SMHI, Swedish Meteorological and Hydrological Institute
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import wormsextractor

if __name__ == "__main__":
    """ """
    taxa_mgr = wormsextractor.TaxaListGenerator(
        data_in_dir="data_in",
        data_out_dir="data_out",
    )
    taxa_mgr.run_all()
