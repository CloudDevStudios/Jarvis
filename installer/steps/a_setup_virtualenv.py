import os
import shutil
import re

from helper import *
import unix_windows


section("Preparing virtualenv")

# Make sure that not running in virtualenv
if hasattr(sys, 'real_prefix'):
    fail("""Please exit virtualenv!""")

# check that virtualenv on python3 installed
py3_installed = shell(f"{unix_windows.PY3} --version")
if not py3_installed.success() or not py3_installed.cli_output.startswith('Python 3'):
    fail("Please install Python3!\n")

py3venv_installed = shell(f"{unix_windows.VIRTUALENV_CMD} --version")
if not py3venv_installed.success():
    venv_installed = shell("virtualenv --version")

    if not venv_installed.success():
        printlog("Please install virtualenv!")
        printlog("https://github.com/pypa/virtualenv")
        printlog(unix_windows.VIRTUALENV_INSTALL_MSG)
        printlog("")

    fail(
        f">>> Apparently virtualenv on Python3 ({unix_windows.VIRTUALENV_CMD}) does not work. Exiting!"
    )

# Check if 'virtualenv' exists
virtualenv_exists = os.path.isdir("env")

# Check that virtualenv works + is Python 3
if virtualenv_exists:
    venv_version = shell(f"{unix_windows.VIRTUALENV_PYTHON} --version")
    if not venv_version.cli_output.startswith('Python 3'):
        log(f"WARNING: python --version returns {venv_version.cli_output}")

        printlog("Recreating virtualenv...")
        shutil.rmtree("env")
        virtualenv_exists = False

# Create virtualenv if necessary
if not virtualenv_exists:
    shell(f"{unix_windows.VIRTUALENV_CMD} env").should_not_fail()
