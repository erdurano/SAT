from PySide2.QtCore import QModelIndex, QSize
from PySide2.QtWidgets import (QFrame, QHBoxLayout, QLabel, QSizePolicy,
                               QStyledItemDelegate)


class TestItemDelegate(QStyledItemDelegate):
    """A delegate to show test items in listview in qt side"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.model = self.parent().model()

    def paint(self, painter, option, index):

        if index.isValid() and index != QModelIndex():
            widget = DelegateWidget(self.model, index, self.parent())
            widget.setGeometry(option.rect)
            self.parent().setIndexWidget(index, widget)
        else:
            return super().paint(painter, option, index)

    def sizeHint(self, option, index):
        size = QSize(self.parent().size().width(), 30)
        return size


class DelegateWidget(QFrame):
    def __init__(self, model, index, parent=None):
        super().__init__(parent=parent)
        # self.text = 'WhadUp!'
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.model = model
        self.index = index
        self.setFrameShape(self.Box)
        self.setLineWidth(1)

        self.sfiLabel = QLabel(
            text=str(self.index.row())
            )
        layout = QHBoxLayout()
        layout.addWidget(self.sfiLabel)
        self.setLayout(layout)
