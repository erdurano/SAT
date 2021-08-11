from model import ScheduleModel
from PySide2.QtCore import Signal
from xlsIO import XlsIO
from PySide2.QtWidgets import QApplication, QFileDialog, QStyledItemDelegate
from main_win import MainWindow


class App(QApplication):
    """A class to organize main functions of the application and create
    a bridge between qml and qt components"""

    # Signals
    import_path = Signal(str)

    def __init__(self):
        super().__init__()

        # widgets and types that's gonna be used in application
        self.main_window = MainWindow()
        self.file_handler = XlsIO()
        self.import_diag = QFileDialog(
            parent=None,
            caption="Import SAT Excel",
            filter="Excel file (*.xlsx)"
        )

        self.my_model = ScheduleModel()
        self.main_window.schedule_view.setModel(self.my_model)
        self.my_delegate = QStyledItemDelegate()
        self.main_window.schedule_view.setItemDelegate(self.my_delegate)

        # Connections.
        self.main_window.import_button.clicked.connect(self.filename)
        self.import_path.connect(self.file_handler.import_excel)
        self.main_window.dash_button.clicked.connect(self.show_model)
        self.file_handler.schedule_to_update.connect(
            self.my_model.updateSchedule)

        # Compulsory show method for main window
        self.main_window.show()

    def filename(self):
        path, _ = app.import_diag.getOpenFileName()
        self.import_path.emit(path)

    def show_model(self):
        row_count = self.my_model.rowCount()
        for i in range(row_count):
            print(i)
            ind = self.my_model.hasIndex(i)
            print(ind)


if __name__ == "__main__":
    app = App()

    app.exec_()
