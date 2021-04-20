from PySide2.QtWidgets import (QApplication,
                               QGridLayout,
                               QLabel,
                               QMainWindow,
                               QPushButton,
                               QWidget)
from parse import parse_SAT_doc
import datetime as dt


class TestItem(QWidget):
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
        sfi_label.setMaximumWidth(70)
        name_label = QLabel(self.item_name)
        class_label = QLabel('C:{}'.format(self.class_attendance))
        owner_label = QLabel('O:{}'.format(self.class_attendance))
        resp_label = QLabel(self.responsible)
        start_label = QLabel(self.start_dt.strftime('%d/%m%Y, %H:%M')
                             if self.start_dt is not None else '')
        finish_label = QLabel(self.finnish_dt.strftime('%d/%m/%Y, %H:%M')
                              if self.finnish_dt is not None else '')
        done_button = QPushButton('Done')
        done_button.setMaximumWidth(40)

        super().__init__()
        layout = QGridLayout()
        layout.addWidget(sfi_label, 0, 0, 2, 1)
        layout.addWidget(name_label, 0, 1, 1, 4)
        layout.addWidget(resp_label, 1, 1)
        layout.addWidget(class_label, 1, 2)
        layout.addWidget(owner_label, 1, 3)
        layout.addWidget(start_label, 0, 4, 1, 5)
        layout.addWidget(finish_label, 1, 4, 2, 5)
        layout.addWidget(done_button, 0, 5, 2, 6)
        layout.setColumnMinimumWidth(4, 150)

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
        self.setLayout(layout)


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
