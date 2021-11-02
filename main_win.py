from typing import Optional
from PySide2.QtCore import QTimer, Signal
from PySide2.QtGui import QCloseEvent, QIcon, QPixmap
from PySide2.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
from dash_window import DashWindow
from delegate import TestItemDelegate
from model import ScheduleModel
from view import ScheduleView
from xlsIO import XlsIO


class MainWindow(QMainWindow):
    """MainWindow class to import, see and adjust test items"""

    # Signals
    window_closed = Signal()
    import_path = Signal(str)

    def __init__(self):
        super().__init__()

        # Visual of main window

        self.setWindowTitle('SAT Scheduler')
        self.setWindowIcon(QIcon(QPixmap('./imgsrc/cemre_logo.ico')))

        self.dash_button = QPushButton("Show Dash")
        self.import_button = QPushButton("Import .xls")
        self.new_item_button = QPushButton('New Item')
        self.delete_button = QPushButton("Delete Selected")

        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        self.schedule_view = ScheduleView(main_widget)
        main_layout.addWidget(self.schedule_view)

        add_remove_layout = QHBoxLayout()
        add_remove_layout.addItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )
        add_remove_layout.addWidget(self.new_item_button)
        add_remove_layout.addWidget(self.delete_button)

        main_layout.addLayout(add_remove_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.dash_button)
        button_layout.addItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )
        button_layout.addWidget(self.import_button)

        main_layout.addLayout(button_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.setFixedSize(600, 480)

        # Initialization of data structures and other functions
        self.updateTimer = QTimer(self)

        self.file_handler = XlsIO()
        self.schedule_model = ScheduleModel()
        self.schedule_view.setModel(self.schedule_model)
        self.schedule_view.setItemDelegate(
            TestItemDelegate(self.schedule_view)
        )
        self.filename = ''

        self.dash_window = self.createDashWindow()

        self.make_connections()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.window_closed.emit()
        return super().closeEvent(event)

    def delete_handler(self) -> None:
        del_list = 'Are you sure about deletion of below items?\n'
        rows_to_del = self.schedule_view.getSelected()
        for index in rows_to_del:
            item_name = index.data(ScheduleModel.NameRole)
            if item_name is None or item_name == '':
                item_name = "(Empty Item)"

            del_list += '-' + item_name + "\n"

        if rows_to_del != [] and self.schedule_view.model().rowCount() != 0:
            delete_answer = QMessageBox().question(
                self,
                self.tr('Delete'),
                self.tr(del_list),
                QMessageBox.Yes | QMessageBox.No
            )

            if delete_answer == delete_answer.Yes:
                while rows_to_del:
                    self.schedule_view.model().removeRow(rows_to_del[0].row())
                    if not rows_to_del:
                        break
                    rows_to_del = self.schedule_view.getSelected()

    def make_connections(self):
        # Connections.
        self.import_button.clicked.connect(self.get_filename)
        self.import_path.connect(self.file_handler.import_excel)

        self.file_handler.schedule_to_update.connect(
            self.schedule_model.updateSchedule
        )
        self.dash_button.clicked.connect(self.dash_window.show)
        self.window_closed.connect(self.dash_window.close)
        self.updateTimer.timeout.connect(self.schedule_model.check_activated)
        self.updateTimer.start(10000)
        self.new_item_button.clicked.connect(
            self.schedule_view.newItem
        )
        self.delete_button.clicked.connect(self.delete_handler)

    def createDashWindow(self):
        dash_window = DashWindow()
        dash_window.rootContext().setContextProperty(
            "ScheduleModel", self.schedule_model
        )
        dash_window.setDashRoot()
        return dash_window

    def get_filename(self) -> Optional[str]:
        diag = QFileDialog(
            parent=self,
            caption="Import SAT Excel",
            filter="Excel file (*.xlsx)",
        )
        path, _ = diag.getOpenFileName()
        if path.endswith(('.xlsx', '.xls')):
            self.import_path.emit(path)
            return path
        else:
            return None
