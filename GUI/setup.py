

# ======================================================== #
# File automagically generated by GUI2Exe version 0.5.3
# Copyright: (c) 2007-2012 Andrea Gavana
# ======================================================== #

# Let's start with some default (for me) imports...

from cx_Freeze import setup, Executable
import sys, os

if len(sys.argv)==1:
    sys.argv+=['build','--build-exe=PDSimGUI']


# Process the includes, excludes and packages first

include_files = []
includes = ['numpy',]
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'PyQt4',
            'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs',
            'tcl', 'Tkconstants', 'Tkinter']
packages = ['h5py']
path = []

# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.

import glob,os

for plugins in glob.glob(os.path.join('plugins','*.py')):
	include_files.append(plugins)
for ico in glob.glob(os.path.join('ico','*.png')):
	include_files.append(ico)
for img in glob.glob(os.path.join('imgs','*.png')):
	include_files.append(img)
for cfg in glob.glob(os.path.join('configs','*.cfg')):
	include_files.append(cfg)

packages += ['quantities']

# The setup for cx_Freeze is different from py2exe. Here I am going to
# use the Python class Executable from cx_Freeze

base = None
if sys.platform == "win32":
    base = "Win32GUI"

GUI2Exe_Target_1 = Executable(
    # what to build
    script = "PDSimGUI.py",
    initScript = None,
    base = base,
    targetDir = r"PDSimGUI",
    targetName = "PDSimGUI.exe",
    compress = True,
    copyDependentFiles = False,
    appendScriptToExe = False,
    appendScriptToLibrary = False,
    icon = None
    )


# That's serious now: we have all (or almost all) the options cx_Freeze
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.

setup(
    
    version = "1.0",
    description = "No Description",
    author = "No Author",
    name = "cx_Freeze Sample File",
    
    options = {"build_exe": {"include_files": include_files,
                             "includes": includes,
                             "excludes": excludes,
                             "packages": packages,
                             "path": path
                             }
               },
                           
    executables = [GUI2Exe_Target_1]
    )

# This is a place where any post-compile code may go.
# You can add as much code as you want, which can be used, for example,
# to clean up your folders or to do some particular post-compilation
# actions.

if sys.platform.startswith('win'):
    #Further windows packaging things
    import subprocess
    #Compress the files if UPX is found on the system path
    subprocess.call(['upx','PDSimGUI/*.*'])
    #Make an installer using InnoSetup
    subprocess.call(['C:\Program Files (x86)\Inno Setup 5\Compil32.exe','/cc','package_gui.iss'])
    #Rename the installer to include the PDSim version
    old_name = os.path.join('Output','SetupPDSimGUI.exe')
    import PDSim
    new_name = os.path.join('Output','SetupPDSimGUI_version-'+PDSim.__version__+'.exe')
    if os.path.exists(new_name):
        os.remove(new_name)
    os.rename(old_name, new_name)
# And we are done. That's a setup script :-D

