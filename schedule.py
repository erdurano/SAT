from PySide2.QtCore import Qt
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
    def __init__(self, item_dict):
        self.sfi = item_dict["sfi"]
        self.item_name = item_dict["item_name"]
        self.class_attendance = item_dict["class_att"]
        self.flag_attendance = item_dict["flag_att"]
        self.owner_attendance = item_dict["owner_att"]
        self.to_be_followed = item_dict["rec_stat"]
        self.responsible = item_dict["resp_dept"]
        self.start_dt = item_dict["start_datetime"]
        self.finnish_dt = item_dict["estimated_finish"]
        self.active_stat = False
        self.done_stat = False

    def get_item_widget(self):

        sfi_label = QLabel(self.sfi)
        sfi_label.setAlignment(Qt.AlignLeft)
        sfi_label.setAlignment(Qt.AlignVCenter)

        name_label = QLabel(self.item_name)
        name_label.setWordWrap(True)
        name_label.setAlignment(Qt.AlignLeft)

        class_label = QLabel('Class:{}'.format(self.class_attendance))

        owner_label = QLabel('Owner:{}'.format(self.owner_attendance))

        resp_label = QLabel(self.responsible)

        start_label = QLabel(self.start_dt.strftime('%d/%m%Y, %H:%M')
                             if self.start_dt is not None else '')

        finish_label = QLabel(self.finnish_dt.strftime('%d/%m/%Y, %H:%M')
                              if self.finnish_dt is not None else '')

        done_button = QPushButton('Done')
        done_button.setMaximumWidth(40)
        done_button.clicked.connect(self.doneHandler)

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

        self.widgets = [
                        QLabel(self.sfi),
                        QLabel(self.item_name),
                        QLabel(self.class_attendance),
                        QLabel(self.flag_attendance),
                        QLabel(self.owner_attendance),
                        QLabel(self.to_be_followed),
                        QLabel(self.responsible),
                        QLabel(self.start_dt.strftime('%d/%m%Y, %H:%M')
                               if self.start_dt is not None else ''),
                        QLabel(self.finnish_dt.strftime('%d/%m/%Y, %H:%M')
                               if self.finnish_dt is not None else ''),
                        QPushButton('Done')
                        ]
        self.getActiveStat()
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(1)

        layout.setRowStretch(0, 2)
        layout.setColumnStretch(0, 0)
        self.setLayout(layout)

    def getActiveStat(self):
        now = dt.datetime.now()
        if now > self.start_dt:
            self.active_stat = True
            self.setStyleSheet('QFrame {background-color: #4d97f2}')

    def doneHandler(self):
        if self.active_stat is True and self.done_stat is True:
            self.done_stat = False
            self.getActiveStat()
        elif self.active_stat is False and self.done_stat is True:
            self.done_stat = False
            self.setStyleSheet('')
        elif self.done_stat is False:
            self.done_stat = True
            self.setStyleSheet('QFrame {background-color: #61f34b}')


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

        # self.sortItemsByStatus()

    def sortItemsByStatus(self):
        now = dt.datetime.now()
        # print(self.scheduleItems)
        for item in self.scheduleItems:
            if item.finnish_dt is None:
                if item.start_dt >= now:
                    self.upcomingItems.append(item)
                if item.start_dt <= now:
                    self.completedItems.append(item)
            else:
                if item.start_dt <= now <= item.finnish_dt:
                    self.activeItems.append(item)
                elif item.start_dt >= now:
                    self.upcomingItems.append(item)
                elif item.start_dt <= now:
                    self.completedItems.append(item)


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
