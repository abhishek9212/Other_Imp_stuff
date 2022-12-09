# COMMANDS TO ACTIVATE VIRTUAL ENVIRONMENTS
# For MacOS/Linux Users: source myprojectenv/bin/activate
# For Windows powershell(terminal) users: .\myprojectenv\Scripts\activate.ps1
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

import flask # flask - 0.5.2  ---> Let's say we developed in flask version 0.5.2, and now we want to 
# develop in 1.1.x or some other latest version using flask.
# Then what we can do is either we can uninstall this flask and install latest, but if we do that then 
# the apps we made using this version of flask will not work properly. And also we don't want to convert that
# app that was made using old flask to new flask. Then the solution for this can be something like, if we could 
# somehow save a copy of the python enviroment that is installed in our system somewhere else also(it is 
# currently installed in C:\Program Files\Python310). Then, we can install flask 0.5.2 in one of them and
# 1.1.x in the other and we can then work in both of them parallely. Now, this can be either achieved using
# two different systems altogether OR we can use the concept of virtual environment here. We can create an 
# independent python environment which is also called virtual environment. 
# To use virtual environment we have to install a package firstly which is virtualenv.
import pandas as pd
import pygame # Since this module is not installed it's giving error (ModuleNotFoundError: No module named 'pygame')

