import os
from dash_window import DashWindow
from delegate import TestItemDelegate
from model import ScheduleModel
from PySide2.QtCore import QUrl, Signal
from xlsIO import XlsIO
from PySide2.QtWidgets import QApplication, QFileDialog
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
            parent=self.main_window,
            caption="Import SAT Excel",
            filter="Excel file (*.xlsx)"
        )

        self.my_model = ScheduleModel()
        self.main_window.schedule_view.setModel(self.my_model)
        self.my_delegate = TestItemDelegate(
            parent=self.main_window.schedule_view
            )
        self.main_window.schedule_view.setItemDelegate(self.my_delegate)

        self.dash_window = DashWindow(None)
        self.dash_window.hide()
        self.dash_window.model = self.main_window.schedule_view.model()
        self.dash_window.rootContext().setContextProperty(
            "ScheduleModel",
            self.my_model)
        self.dash_window.setSource(QUrl.fromLocalFile(
            os.path.join(os.path.dirname(__file__), 'qml/Dash.qml')
            ))

        # Connections.
        self.main_window.import_button.clicked.connect(self.filename)
        self.import_path.connect(self.file_handler.import_excel)

        self.file_handler.schedule_to_update.connect(
            self.my_model.updateSchedule)
        self.main_window.dash_button.clicked.connect(self.show_model)

        self.main_window.window_closed.connect(self.dash_window.close)

        # Compulsory show method for main window
        self.main_window.show()

    def filename(self):
        path, _ = app.import_diag.getOpenFileName()
        self.import_path.emit(path)

    def show_model(self):
        self.dash_window.show()


if __name__ == "__main__":
    app = App()

    app.exec_()
