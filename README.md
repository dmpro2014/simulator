Ghetto-Cuda Simulator
=====================

# Simulator
run simulator.py with a kernel on stdin

# Assembler
run assembler.py with a kernel on stdin

## Setup

Required for both assembler and simulator.
Use a virtualenv if you don't want to install dependencies globally.

run `pip install -r requirements.txt`

In addition, tkinter is required.
It is part of core python, but sometimes the module is not included in the python installation.
If you get an error importing `_tkinter`, simply run `apt-get install python-tk` or something similar.
