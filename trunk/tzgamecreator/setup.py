from distutils.core import setup
import py2exe

setup(
		windows = [{
			"script": "tz.py",
			"icon_resources": [(1, "tz.ico")]
			}],
		data_files = [
			("dic", ["dic\\main.dic"]),
			("save", ["save\\1.xml"])
			]
		)

