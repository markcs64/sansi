# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

includes = ["encodings", "encodings.*"]
options = {"py2exe": {
        "compressed": 1,
        "optimize": 2,
        "includes": includes,
        "bundle_files": 2
        }
    }

setup(
        version = "0.1.0",
        description = "TSP",
        name = "TSP",
        options = options,
        zipfile = None,
        windows=[{"script": "TSP.py", "icon_resources": [(1, "doraemon.ico")] }],
    )
