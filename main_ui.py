from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication,
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
from ui_elements import test_item


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_widget = QWidget()
        button_layout = QHBoxLayout()
        self.item_view = QListView()

        import_button = QPushButton("Import SAT")
        import_button.setFixedWidth(70)

        dash_button = QPushButton("Dash It!")
        dash_button.setFixedWidth(50)
        dash_button.clicked.connect(self.hey)

        button_layout.addWidget(dash_button)
        verticalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                     QSizePolicy.Minimum)
        button_layout.addItem(verticalSpacer)
        button_layout.addWidget(import_button)
        main_layout.addWidget(self.get_scrollview())
        main_layout.addLayout(button_layout)
        main_widget.setLayout(main_layout)

        self.setFixedSize(640, 480)
        self.setWindowTitle("SATDash")
        self.setCentralWidget(main_widget)

    def get_scrollview(self):

        self.container = QWidget()
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        for i in range(1, 50):
            object = test_item()
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        return self.scroll

    def hey(self):
        print('yeeeeey')

    # def get_excel_file(self):


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()
