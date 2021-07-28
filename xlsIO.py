from typing import Any
from PySide2.QtCore import Slot
import openpyxl
from dataclasses import Schedule, TestItem
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
        self.__indexes: dict
        self.__schedule = Schedule()

    @property
    def schedule(self):
        return self.__schedule

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

    @property
    def indexes(self) -> dict:
        return self.__indexes

    @indexes.setter
    def indexes(self, index_dict: dict) -> None:
        self.__indexes = index_dict

    def find_merged_cells(self, xldata: Worksheet) -> None:
        self.merged_cells = xldata.merged_cells

    def get_header_info(self, xldata: Worksheet) -> None:
        for row in xldata.rows:
            for cell in row:
                if cell.value == "Class":
                    self.header_row = cell.row
                    class_column = cell.column
                    indexes = {
                        "sfi": class_column-2,
                        "item_name": class_column-1,
                        "class": class_column,
                        "flag": class_column+1,
                        "owner": class_column+2,
                        "record_stat": class_column+3,
                        "responsible": class_column+4,
                        "date": class_column+5,
                        "start_time": class_column+6,
                        "est": class_column+7,
                    }
                    self.indexes = indexes
                    break

    def get_cell_range(self, cell):
        for r in self.merged_cells:
            if cell.coordinate in r:
                return r

    def add_rows2schedule(self, row: tuple, xldata) -> None:
        item = TestItem()

        for cell in row:
            if cell.coordinate in self.merged_cells:
                r = self.get_cell_range(cell)
                i_row, i_col = r.top[0]
                cell = xldata.cell(i_row, i_col)

            if cell.column == self.indexes['sfi']:
                item.sfi =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['item_name']:
                item.item_name =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['class']:
                item.class_attendance =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['flag']:
                item.flag_attendance =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['owner']:
                item.owner_attendance =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['record_stat']:
                item.record_status =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['responsible']:
                item.ressponsible_dept =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['date']:
                item.date =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['start_time']:
                item.start_hour =\
                    cell.value if cell.value is not None else ''

            elif cell.column == self.indexes['est']:
                item.est =\
                    cell.value if cell.value is not None else ''

        if item.date == '' or\
                item.start_hour == '':
            print('dot')
            return
        else:
            self.schedule.add_item(item)

    def get_item_rows(self, xldata: Worksheet) -> None:
        min_row = self.header_row+1
        for row in xldata.iter_rows(min_row):
            self.add_rows2schedule(row, xldata)
        print(len(self.schedule.agenda_items))
        for i in self.schedule.agenda_items:
            print(i.item_name)

    def parse_xl(self, xldata: Worksheet) -> None:
        self.get_header_info(xldata)
        self.find_merged_cells(xldata)
        self.get_item_rows(xldata)
