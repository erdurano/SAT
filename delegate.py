from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QFrame, QHBoxLayout, QLabel, QSizePolicy,
                               QStyledItemDelegate)


class TestItemDelegate(QStyledItemDelegate):
    """A delegate to show test items in listview in qt side"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.model = self.parent().model()

    def paint(self, painter: QPainter, option, index):
        model_ind = index.model()

        name = model_ind.data(index, model_ind.NameRole)
        sfi = model_ind.data(index, model_ind.SfiRole)
        painter.setPen(Qt.black)
        painter.drawRect(option.rect)

        painter.setPen(Qt.blue)
        painter.drawText(option.rect, Qt.AlignCenter, name)
        painter.drawText(option.rect, Qt.AlignLeft, sfi)

        #     widget = DelegateWidget(self.model, index, self.parent())
        #     widget.setGeometry(option.rect)
        #     self.parent().setIndexWidget(index, widget)
        # else:
        #     return super().paint(painter, option, index)

    def sizeHint(self, option, index):
        size = QSize(self.parent().size().width(), 50)
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
