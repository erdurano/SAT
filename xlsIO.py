from PySide2.QtCore import Slot
import openpyxl


class XlsIO():
    """ A class for handling file IO and parsing and handling xls files"""

    def __init__(self) -> None:
        self._worksheet = None

    @Slot(str)
    def get_file_contents(self, filepath: str) -> None:
        self._worksheet = openpyxl.load_workbook(filepath).active
        for row, column in self._worksheet._cells:
            print(self._worksheet.cell(row, column).value)
