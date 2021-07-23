from typing import Any
from PySide2.QtCore import Slot
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


class XlsIO:
    """A class for handling file IO and parsing and handling xls files"""

    def __init__(self) -> None:
        self.__file_path = ""
        self.__worksheet = None
        self.__parser = Xlparser()

    @property
    def filepath(self) -> Any:
        return self.__file_path

    @filepath.setter
    def filepath(self, path: str) -> None:
        self.__file_path = path

    @property
    def xl_worksheet(self) -> Worksheet:
        return self.__worksheet

    @xl_worksheet.setter
    def xl_worksheet(self, sheet: Worksheet) -> None:
        self.__worksheet = sheet

    def xlsheet_from_path(self, path: str) -> Worksheet:
        self.xl_worksheet = openpyxl.load_workbook(path).active

    @Slot(str)
    def import_excel(self, import_path: str) -> None:
        self.filepath = import_path
        self.xlsheet_from_path(self.filepath)
        self.__parser.parse_xl(self.xl_worksheet)


class Xlparser:
    def __init__(self) -> None:
        self.__header_row: int
        self.__merged_cells: list

    @property
    def header_row(self) -> int:
        return self.__header_row

    @header_row.setter
    def header_row(self, row_number: int) -> None:
        self.__header_row = row_number

    @property
    def merged_cells(self) -> list:
        return self.__merged_cells

    @merged_cells.setter
    def merged_cells(self, cell_ranges: list) -> None:
        self.__merged_cells = cell_ranges

    def find_merged_cells(self, xldata) -> list:
        self.merged_cells = xldata.merged_cells

    def get_header_row(self, xldata: Worksheet) -> None:
        for row in xldata.rows:
            for cell in row:
                if cell.value == "Class":
                    self.header_row = cell.row
                    print(self.header_row)
                    break

    def parse_xl(self, xldata: Worksheet) -> None:
        self.get_header_row(xldata)
        self.find_merged_cells(xldata)
