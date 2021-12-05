from typing import List, Optional
from PySide6.QtCore import QTimer, Signal
from PySide6.QtGui import QCloseEvent, QIcon, QPixmap
from PySide6.QtWidgets import (
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
from model import ProxyModel, ScheduleModel
from view import ScheduleView
from xlsIO import XlsIO


class MainWindow(QMainWindow):
    """MainWindow class to import, see and adjust test items"""

    # Signals
    window_closed = Signal()
    import_path = Signal(str)
    delete_selected = Signal()

    def __init__(self):
        super().__init__()

        # Visual of main window

        self.setWindowTitle('SAT Scheduler')
        self.setWindowIcon(QIcon(QPixmap('./rsrc/img/cemre_logo.ico')))

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
        self.proxyModel = ProxyModel()
        self.proxyModel.setSourceModel(self.schedule_model)
        self.schedule_view.setModel(self.proxyModel)
        self.proxyModel.setDynamicSortFilter(True)

        self.schedule_view.setItemDelegate(
            TestItemDelegate(self.schedule_view)
        )
        self.filename = ''

        self.dash_window = self.createDashWindow()

        self.makeConnections()
        self.proxyModel.sort(0)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.window_closed.emit()
        return super().closeEvent(event)

    def delete_handler(self) -> None:
        delete_answer = DeletionBox(self).ask()

        if delete_answer is not None and\
                delete_answer == delete_answer.Yes:
            self.delete_selected.emit()

    def makeConnections(self):
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
        self.delete_selected.connect(self.schedule_view.deleteSelected)

    def createDashWindow(self):
        dash_window = DashWindow()
        dash_window.rootContext().setContextProperty(
            "ScheduleModel", self.proxyModel
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


class DeletionBox(QMessageBox):

    def __init__(self, parent: Optional[MainWindow] = None) -> None:
        super().__init__(parent=parent)
        self.setWindowTitle(self.tr('Delete'))
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    def getMessageBody(self) -> Optional[str]:
        prefix = 'Are you sure about deletion of below items?\n'
        titles = self.itemTitleList()
        if titles:
            for title in titles:
                prefix += '-' + title + '\n'
            return prefix
        else:
            return None

    def itemTitleList(self) -> List[str]:
        title_list = list()
        indexes_to_delete = self.parent().schedule_view.getSelected()
        for index in indexes_to_delete:
            name = index.data(ScheduleModel.NameRole)
            if name is None or name == "":
                title_list.append("(Empty Item)")
            else:
                title_list.append(name)
        return title_list

    def ask(self) -> QMessageBox.StandardButton:
        body = self.getMessageBody()
        if body:
            self.setText(body)
            return self.question(
                self.parent(),
                self.windowTitle(),
                self.text(),
                self.standardButtons()
            )
