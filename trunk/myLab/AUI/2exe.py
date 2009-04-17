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
        description = "AUI",
        name = "AUI",
        options = options,
        zipfile = None,
        windows=[{"script": "AUI.py", "icon_resources": [(1, "doraemon.ico")] }],
    )
