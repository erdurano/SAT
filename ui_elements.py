import sys
from PySide2.QtWidgets import (
    QApplication, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QWidget)


class test_item(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.widgets = [
                        QLabel('sfi'),
                        QLabel("test_item"),
                        QLabel('class_att'),
                        QLabel('flag_att'),
                        QLabel('owner_att'),
                        QLabel('rec_stat'),
                        QLabel('resp_dept'),
                        QPushButton('Done')
                        ]
        for prop in self.widgets:
            layout.addWidget(prop)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setCentralWidget(test_item())
    window.show()

    app.exec_()
