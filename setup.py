import sys, os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "console"


setup(name = "steetz",
      version = "1.0",
      description = "My application!",
      options = {"build_exe": {"packages":["requests", "urllib", "queue", "idna", "lxml", "bs4", "requests", 'httplib2', 'apiclient', 'oauth2client']}},
      executables = [Executable("steetz.py", base = base, shortcutName="sender")])