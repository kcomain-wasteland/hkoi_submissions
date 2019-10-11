import os
import sys
import re

def restart():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def space(reg,b):
    print(re.sub(reg,' ',b))