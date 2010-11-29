from distutils.core import setup
import py2exe

includes = ["encodings", "encodings.*"]

options = {"py2exe":
			{
				"compressed": 1,
#				"optimize": 2,
#				"includes": includes,
#				"bundle_files": 1,
			}
		  }

setup(
	version = "0.1.0",
	description = "Tree Maker",
	name = "Tree",
	options = options,
	zipfile = None,
#	console = [{"script": "tree.py", "icon_resources": [(1, "tree.ico")]}],
	windows = [{"script": "tree.py", "icon_resources": [(1, "tree.ico")]}],
	)
