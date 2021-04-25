import os

from parse import parse_SAT_doc
from schedule import Schedule
from PySide2.QtCore import QUrl, Qt
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QListView,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget
    )
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout()
        main_widget = QWidget()
        button_layout = QHBoxLayout()
        self.item_view = QListView()
        self.schedule = Schedule()

        import_button = QPushButton("Import SAT")
        import_button.setFixedWidth(70)
        import_button.clicked.connect(self.get_excel_file)

        dash_button = QPushButton("Dash It!")
        dash_button.setFixedWidth(70)
        dash_button.clicked.connect(self.get_dash_window)

        button_layout.addWidget(dash_button)
        verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                     QSizePolicy.Minimum)
        button_layout.addItem(verticalSpacer)
        button_layout.addWidget(import_button)
        self.main_layout.addWidget(self.get_scrollview())
        self.main_layout.addLayout(button_layout)
        main_widget.setLayout(self.main_layout)

        self.setMinimumSize(600, 480)
        self.setWindowTitle("SATDash")
        self.setCentralWidget(main_widget)

    def get_scrollview(self):

        self.container = QWidget()
        self.scr_area = QScrollArea()
        self.widget = QWidget()
        self.grid = QVBoxLayout()
        for row, test_item in enumerate(self.schedule.scheduleItems):
            self.grid.addWidget(test_item)

        self.widget.setLayout(self.grid)

        # Scroll Area Properties
        self.scr_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scr_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scr_area.setWidgetResizable(True)
        self.scr_area.setWidget(self.widget)

        return self.scr_area

    def get_excel_file(self):
        filename, _ = QFileDialog.\
            getOpenFileName(self, self.tr('Load SAT file'),
                            self.tr("Desktop"),
                            self.tr("Excel files, (*.xlsx)"))

        xldata = parse_SAT_doc(filename)
        self.schedule.imprt_data(xldata)
        self.main_layout.replaceWidget(self.scr_area, self.get_scrollview())

    def get_dash_window(self):
        dash_widget = QWidget()
        self.qmlView = QQuickView()
        url = QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__),
                                              "qml/Dash.qml"))
        self.qmlView.setSource(url)
        self.qmlView.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()
