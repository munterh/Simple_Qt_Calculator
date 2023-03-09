# A Simple Qt Calculator: Overview

The project aims to provide clean, well-structured code for a calculator with a graphical user interface, employing PyQt6.

The calculator is based on a self-contained calculator class found in models/calculator.py. The file redering.py links the calculator class with the Qt GUI. It is organized in a way that avoids repetition of code. For this purpose, it uses partial functions from the functools standard library.

The program uses parameters stored in config.py which are intended to be changed as needed.

Please note that Python 3.10 or later is required due to match-statements in models/calculator.py.
