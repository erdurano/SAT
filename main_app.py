import os

from PySide2.QtCore import QTimer, QUrl, Signal
from PySide2.QtWidgets import QApplication, QFileDialog

from dash_window import DashWindow
from delegate import TestItemDelegate
from main_win import MainWindow
from model import ScheduleModel
from xlsIO import XlsIO


class App(QApplication):
    """A class to organize main functions of the application and create
    a bridge between qml and qt components"""

    # Signals
    import_path = Signal(str)

    def __init__(self):
        super().__init__()

        self.schedule_model = ScheduleModel()
        self.create_main_window()
        self.create_dash_window()

        # Creating timer for the auto status update function
        # of ScheduleModel class
        self.updateTimer = QTimer(self)

        self.make_connections()
        # Compulsory show method for main window
        self.main_window.show()

    def create_main_window(self):
        # widgets and types that's gonna be used in application
        self.main_window = MainWindow()
        self.file_handler = XlsIO()
        self.import_diag = QFileDialog(
            parent=self.main_window,
            caption="Import SAT Excel",
            filter="Excel file (*.xlsx)",
        )
        self.main_window.schedule_view.setModel(self.schedule_model)
        self.main_window.schedule_view.setItemDelegate(self.get_delegate())

    def create_dash_window(self):
        self.dash_window = DashWindow(None)
        self.dash_window.hide()
        self.dash_window.model = self.main_window.schedule_view.model()
        self.dash_window.rootContext().setContextProperty(
            "ScheduleModel", self.schedule_model
        )
        self.dash_window.setSource(
            QUrl.fromLocalFile(
                os.path.join(os.path.dirname(__file__), "qml/Dash.qml")
            )
        )

    def get_delegate(self):
        return TestItemDelegate(
            parent=self.main_window.schedule_view
        )

    def filename(self):
        path, _ = app.import_diag.getOpenFileName()
        if path.endswith(('.xlsx', '.xls')):
            self.import_path.emit(path)

    def make_connections(self):
        # Connections.
        self.main_window.import_button.clicked.connect(self.filename)
        self.import_path.connect(self.file_handler.import_excel)

        self.file_handler.schedule_to_update.connect(
            self.schedule_model.updateSchedule
        )
        self.main_window.dash_button.clicked.connect(self.dash_window.show)

        self.main_window.window_closed.connect(self.dash_window.close)

        self.updateTimer.timeout.connect(self.schedule_model.check_activated)
        self.updateTimer.start(10000)

        self.main_window.new_item_button.clicked.connect(
            self.main_window.schedule_view.itemDelegate().newItem
        )



if __name__ == "__main__":
    app = App()

    app.exec_()
