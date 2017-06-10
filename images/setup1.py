# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

application_title = "Floyd Warshall Algorithm" #what you want to application to be called
main_python_file = "Final.py" #the name of the python file you use to run the program

import sys

from distutils.core import setup
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re"]

setup(
        name = application_title,
        version = "0.1",
        description = "Floyd Warshall Algorithm",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable(main_python_file, base = base)]
        )

