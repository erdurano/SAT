import typing
from PySide2.QtCore import QItemSelectionModel, Signal
from PySide2.QtGui import QCloseEvent
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

    window_closed = Signal()

    def __init__(self):
        super().__init__()

        self.dash_button = QPushButton("Dash It!")
        self.import_button = QPushButton("Import .xls")

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        self.schedule_view = ScheduleView(self)
        main_layout.addWidget(self.schedule_view)
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

    def closeEvent(self, event: QCloseEvent) -> None:
        self.window_closed.emit()
        return super().closeEvent(event)


class ScheduleView(QListView):

    def __init__(self, parent: typing.Optional[QWidget]) -> None:
        super().__init__(parent=parent)
        self.setSpacing(4)

    def commitData(self, editor: QWidget) -> None:
        # Holds the view from updating the model when exiting the item
        # else passes the commitData slot
        if type(self.sender()) == QItemSelectionModel:
            return None
        return super().commitData(editor)


if __name__ == "__main__":
    app = QApplication()

    win = MainWindow()

    win.show()

    app.exec_()
