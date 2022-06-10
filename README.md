# SAT

This repo contains source files of a program that can import, edit and show time information about Sea Acceptance Trial schedules for new built sea vessels.

## Library Info / Installation

This script utilizes PySide6 and openpyxl and environment is contained with poetry.

### Notice

This application still under active development. Repository only opened to access for review purposes.

## Features

- Reads strictly formatted excel files (*.xlsx extention) prepared for sea acceptance trial schedules
- Manipulates necessary data to create a custom TestItem type
- Displays information on both QML and QWidget type views
- Test Items can be edited from QWidget side
- Keeps track of test start time according to the system clock and/or test item status
- QML View aimed to be used as a dahsboard to be shown on external monitor(s)
