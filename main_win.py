from PySide2.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QListView,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """MainWindow class to import, see and adjust test items"""

    def __init__(self):
        super().__init__()

        self.dash_button = QPushButton("Dash It!")
        self.import_button = QPushButton("Import .xls")

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(QListView())
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.dash_button)
        button_layout.addItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )
        button_layout.addWidget(self.import_button)

        main_layout.addLayout(button_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.setMinimumSize(762, 480)


if __name__ == "__main__":
    app = QApplication()

    win = MainWindow()

    win.show()

    app.exec_()
