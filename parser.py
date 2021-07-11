import openpyxl

class XlsIO():
    """ A class for handling file IO and parsing and handling xls files"""

    def __init__(self) -> None:
        pass

    def get_file_contents(self, filepath) -> None:
        worksheet = openpyxl.load_workbook(filepath).active
        print(worksheet)
