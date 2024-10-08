# Objectives

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# Use the python os function to print the following commands below.  These are bash commands and we are going to run them through a python script.
# Add description printed to the terminal of what is about to run



# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.



# This will not run on windows needs to be mac or linux due to os being bash

import subprocess
import os

print("running whoami")
whoami_command = "whoami"

os.system(whoami_command)

print("running ip a")
ipa_command = "ip a"

os.system(ipa_command)

print("running lshw -short")
ishwshort_command = "lshw -short"

os.system(ishwshort_command)


