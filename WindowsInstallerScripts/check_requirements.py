"""This module is use to check wether required programs are installed or not.

For example: 
    `$./check_requirements python` 
    will return 0 if python 3.8 or above are installed, and return 1 otherwise

Available options:
    `$./check_requirements python` 
    `$./check_requirements pip`
    `$./check_requirements ffmpeg`  
"""

import re
import sys
import subprocess


def is_python_exist():
    """Check whether python installed is python 3.8 or above, return 1 if not"""

    try:
        call_result = subprocess.run (["python", "--version"], capture_output=True)
        re_results = re.match (r"^python 3\.([0-9]*)\.", call_result.stdout.decode("UTF-8").lower())

        python_subversion = int (re_results.group(1))
        if (python_subversion >= 8):
            return 0
    except:
        pass

    return 1


def is_pip_exist():
    """Check whether pip is installed or not, return 1 if not"""

    try:
        call_result = subprocess.check_output ("pip --version", shell=True, stderr=subprocess.STDOUT)
    except:
        return 1

    return 0


def is_ffmpeg_exist():
    """Check whether ffmpeg is installed or not, return 1 if not"""

    try:
        call_result = subprocess.check_output ("ffmpeg -version", shell=True)
    except:
        return 1

    return 0



def main():
    if len (sys.argv) <= 1:
        return 1

    if   sys.argv[1] == "python":
        return is_python_exist()
    elif sys.argv[1] == "pip":
        return is_pip_exist()
    elif sys.argv[1] == "ffmpeg":
        return is_ffmpeg_exist()

    return 1
    

if  __name__ == "__main__":
    sys.exit (main ())