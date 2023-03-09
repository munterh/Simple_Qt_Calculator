# A Simple Qt Calculator

## Overview

The project aims to provide clean, well-structured code for a calculator with a graphical user interface, employing PyQt6.  

## Resources

**Python Version**: 3.10  
**Packages**: PyQt6, functools
**Markdown Guide**: [https://www.markdownguide.org/basic-syntax](https://www.markdownguide.org/basic-syntax)

## Structure of the Code

* The calculator is based on a self-contained calculator class found in models/calculator.py.  
* The file redering.py links the calculator class with the Qt GUI. It is organized in a way that avoids repetition of code. For this purpose, it uses partial functions from the functools standard library.
* The program uses the parameters stored in config.py which are intended to be changed as needed.
