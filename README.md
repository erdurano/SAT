# SAT
This repo contains source files of a program that can import, edit and show time information about Sea Acceptance Trial schedules for new built sea vessels.

## Library Info / Installation

This script utilizes PySide6 and openpyxl and environment is contained with Pipenv.

If you have Pipenv installed you can run 
```
pipenv synch
```
from project root directory.

Due to a lack of feature from Pipenv's part this command alone does not install PySide6 automatically. But creates the environment that program could run in and installs openpyxl.

You should also run 
```
pipenv install PySide6
```
After that program can be started with
```
pipenv run python main.py
```
or 
```
pipenv shell
python main.py
```

### Notice
This application still under active developement. Repository only opened to access for review purposes.

## Features
- Reads strictly formatted excel files (*.xlsx extention) prepared for sea acceptance trial schedules
- Manipulates neccessary data to create a custom TestItem type
- Displays information on both QML and QWidget type views
- Test Items can be edited from QWidget side
- Keeps track of test start time according to the system clock and/or test item status
- QML View aimed to be used as a dahsboard to be shown on external monitor(s)
