from PySide2.QtCore import QModelIndex, QRect, QSize, Qt
from PySide2.QtGui import QPainter, QPen
from PySide2.QtWidgets import (QStyledItemDelegate, QStyleOptionViewItem,
                               QWidget)


class TestItemDelegate(QStyledItemDelegate):
    """A delegate to show test items in listview in qt side"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.model = self.parent().model()

    def paint(self, painter: QPainter,
              option: QStyleOptionViewItem, index: QModelIndex):

        model_ind = index.model()
        canvas = option.rect.getRect()

        painter.setRenderHint(QPainter.Antialiasing, on=True)

        # Supplying data from model
        sfi = index.data(model_ind.SfiRole)
        name = index.data(model_ind.NameRole)
        cls_att = index.data(model_ind.ClsRole)
        flg_att = index.data(model_ind.FlagRole)
        ownr_att = index.data(model_ind.OwnrRole)
        # rec_stat = index.data(model_ind.RecordRole)
        resp_dept = index.data(model_ind.DeptRole)
        date_str = index.data(model_ind.DateStrRole)
        hour_str = index.data(model_ind.HourRole)
        est_duration = index.data(model_ind.EstTimeRole)
        # status = model_ind.data(index, model_ind.StatusRole)

        # Frame and Background(s)
        pen = QPen()
        pen.setColor("Black")
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRoundedRect(option.rect, 10, 10)

        painter.setPen(Qt.blue)
        # Coordinates for delegate background
        x, y, w, h = canvas

        # Drawing of the texts
        painter.drawText(
            QRect(x + 50, y, w-200, h//2),
            Qt.AlignVCenter, name)

        painter.drawText(
            QRect(x, y, h, h),
            Qt.AlignCenter, sfi)

        painter.drawText(
            QRect(x+w-150, y, 50, h//3),
            Qt.AlignVCenter,
            "C:{}".format('-' if cls_att == '' else cls_att))

        painter.drawText(
            QRect(x+w-150, y+h//3, 50, h//3),
            Qt.AlignVCenter,
            "F:{}".format('-' if flg_att == '' else flg_att))

        painter.drawText(
            QRect(x+w-150, y + 2*h//3, 50, h//3),
            Qt.AlignVCenter,
            "O:{}".format('-' if ownr_att == '' else ownr_att))

        painter.drawText(
            QRect(x+50, y+h//2, w//3, h//2),
            Qt.AlignVCenter, resp_dept)

        painter.drawText(
            QRect(x+w-100, y, 100, h//2),
            Qt.AlignCenter, date_str.strftime('%d-%m-%Y')
        )

        painter.drawText(
            QRect(x+w-100, y+h//2, 50, h//2),
            Qt.AlignCenter, hour_str.strftime('%H:%M')
        )

        painter.drawText(
            QRect(x+w-50, y+h//2, 50, h//2),
            Qt.AlignCenter, est_duration
        )

    def createEditor(self, parent, option, index):
        print(type(parent))

    def sizeHint(self, option, index):
        size = QSize(300, 50)
        return size


class ItemEditor(QWidget):
    pass
