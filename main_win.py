from typing import List, Optional
from PySide2.QtCore import QItemSelectionModel, QModelIndex, Signal
from PySide2.QtGui import QCloseEvent, QIcon, QPixmap
from PySide2.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QListView,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStyledItemDelegate,
    QVBoxLayout,
    QWidget,
)
from model import ScheduleModel


class MainWindow(QMainWindow):
    """MainWindow class to import, see and adjust test items"""

    window_closed = Signal()

    def __init__(self):
        super().__init__()

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
        self.schedule_view.setSelectionRectVisible(True)
        self.delete_button.clicked.connect(self.delete_handler)

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


class ScheduleView(QListView):

    def __init__(self, parent: Optional[QWidget]) -> None:
        super().__init__(parent=parent)
        self.setSpacing(1)

        self.setVerticalScrollMode(
            self.ScrollPerPixel
        )
        self.setSelectionMode(self.ExtendedSelection)

    def commitData(self, editor: QWidget) -> None:
        # Holds the view from updating the model when exiting the item
        # else passes the commitData slot
        if type(self.sender()) == QItemSelectionModel or\
                type(self.sender()) is None:
            return None
        else:
            return super().commitData(editor)

    def closeEditor(self,
                    editor: QWidget,
                    hint: QStyledItemDelegate.EndEditHint) -> None:
        if hint == QStyledItemDelegate.SubmitModelCache:
            self.commitData(editor)
        elif hint == QStyledItemDelegate.RevertModelCache:
            pass
        super().closeEditor(editor, hint)

    def getSelected(self) -> List[QModelIndex]:
        return self.selectionModel().selectedRows()


if __name__ == "__main__":
    app = QApplication()

    win = MainWindow()

    win.show()

    app.exec_()
