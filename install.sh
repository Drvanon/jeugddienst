# First create the folder where you wish to install the software
# with mkdir command. Then go to this folder with cd command.

# Windows users: Please manually download virtualenv.py
# to the target folder  ith your web browser. UNIX users
# can use curl command line downloader as below.

# Note: Don't rely on operating system virtualenv command.
# It might be hassle to instruct virtualenv package installation
# due to distribution flavours.
# Old Ubuntus ship really old virtualenv.py and it has not worked
# on all cases.
# Github virtualenv.py is the msot reliable method.
curl -L -o virtualenv.py https://raw.github.com/pypa/virtualenv/master/virtualenv.py

# Create a virtualenv environment
# where the software and its dependencies
# will be pulled from PyPi. In our case
# we call the created virtualenv folder "venv"
python virtualenv.py venv

# Activate the virtualenv environment.
# This will set your PATH environment
# variable so that following "python"
# command executes from under the virtualenv,
# not from your global system setup.
#

# Windows equivalent: .\venv\Scripts\activate
. venv/bin/activate

# Now when virtualenv is activated,
# pip and easy_install will install any software
# under this virtualenv environment, not on your operating system files
 pip install -r requirements.txt

# Usually, if you install Python command line software,
# new launcher scripts get created in venv/bin
# folder. When venv environment is active,
# this folder takes precedence in PATH environment
# variable. Meaning, when you have virtualenv activated
# you can simply type in the installed command name
# without full path to execute it.