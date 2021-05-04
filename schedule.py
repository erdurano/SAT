from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import (QApplication, QFrame,
                               QGridLayout,
                               QLabel,
                               QMainWindow,
                               QPushButton,
                               QWidget)
from parse import parse_SAT_doc
import datetime as dt


class TestItem(QFrame):
    # Constructor class for managing test items.
    item_data = Signal(dict)

    def __init__(self, item_dict):
        self.dict = item_dict
        self.dict["active_stat"] = False
        self.dict["done_stat"] = False
        self.dict.update({'active_stat': self.dict["active_stat"],
                          "done_stat": self.dict["done_stat"]})

    def get_item_widget(self):

        sfi_label = QLabel(self.dict["sfi"])
        sfi_label.setAlignment(Qt.AlignLeft)
        sfi_label.setAlignment(Qt.AlignVCenter)

        name_label = QLabel(self.dict["item_name"])
        name_label.setWordWrap(True)
        name_label.setAlignment(Qt.AlignLeft)

        class_label = QLabel('Class:{}'.format(self.dict["class_att"]))

        owner_label = QLabel('Owner:{}'.format(self.dict["owner_att"]))

        resp_label = QLabel(self.dict["resp_dept"])

        start_label = QLabel(
            self.dict["start_datetime"].strftime('%d/%m%Y, %H:%M')
            if self.dict["start_datetime"] is not None else ''
            )

        finish_label = QLabel(
            self.dict["estimated_finish"].strftime('%d/%m/%Y, %H:%M')
            if self.dict["estimated_finish"] is not None else ''
            )

        done_button = QPushButton('Done')
        done_button.setMaximumWidth(40)
        done_button.clicked.connect(self.doneButtonHandler)

        super().__init__()
        layout = QGridLayout()
        layout.addWidget(sfi_label, 0, 0, 2, 1)
        layout.addWidget(name_label, 0, 1, 1, 3)
        layout.addWidget(resp_label, 1, 1)
        layout.addWidget(class_label, 1, 2)
        layout.addWidget(owner_label, 1, 3)
        layout.addWidget(start_label, 0, 4)
        layout.addWidget(finish_label, 1, 4)
        layout.addWidget(done_button, 0, 5, 2, 1)

        self.getActiveStat()
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(1)

        layout.setRowStretch(0, 2)
        layout.setColumnStretch(0, 0)
        self.setLayout(layout)
        # self.item_data.connect(self.parent_window.dash_window.model.setData)

    def getActiveStat(self):
        now = dt.datetime.now()
        if now > self.dict["start_datetime"]:
            self.dict["active_stat"] = True
            self.setStyleSheet('QFrame {background-color: #4d97f2}')

    def doneButtonHandler(self):

        if self.dict["active_stat"] is True and self.dict["done_stat"] is True:

            self.dict["done_stat"] = False
            self.getActiveStat()

        elif self.dict["active_stat"] is False\
                and self.dict["done_stat"] is True:

            self.dict["done_stat"] = False
            self.setStyleSheet('')

        elif self.dict["done_stat"] is False:

            self.dict["done_stat"] = True
            self.setStyleSheet('QFrame {background-color: #61f34b}')

        self.item_data.emit(self.dict)


class Schedule():
    # A class for creating and managing test items

    def __init__(self):
        self.scheduleItems = []
        self.activeItems = []
        self.upcomingItems = []
        self.completedItems = []

    def imprt_data(self, xldata):
        self.scheduleItems = []
        for item_dict in xldata:
            test_item = TestItem(item_dict)
            test_item.get_item_widget()
            self.scheduleItems.append(test_item)


if __name__ == '__main__':
    app = QApplication()
    filename = './example/5_NB67_SAT_Schedule_Rev_3.xlsx'

    xldata = parse_SAT_doc(filename)
    container = QWidget()
    schedule = Schedule()
    schedule.imprt_data(xldata)
    grid = QGridLayout()

    for row, test_item in enumerate(schedule.scheduleItems):
        for column, item in enumerate(test_item.widgets):
            grid.addWidget(item, row, column)
    grid.setSpacing(5)
    container.setLayout(grid)

    window = QMainWindow()
    window.setCentralWidget(container)
    window.show()

    app.exec_()
