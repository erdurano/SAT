from PySide2.QtCore import QModelIndex, QRect, QSize, Qt
from PySide2.QtGui import QPainter, QPen
from PySide2.QtWidgets import (QStyledItemDelegate, QStyleOptionViewItem)


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
        sfi = model_ind.data(index, model_ind.SfiRole)
        name = model_ind.data(index, model_ind.NameRole)
        cls_att = model_ind.data(index, model_ind.ClsRole)
        flg_att = model_ind.data(index, model_ind.FlagRole)
        ownr_att = model_ind.data(index, model_ind.OwnrRole)
        rec_stat = model_ind.data(index, model_ind.RecordRole)
        resp_dept = model_ind.data(index, model_ind.DeptRole)
        date_str = model_ind.data(index, model_ind.DateStrRole)
        hour_str = model_ind.data(index, model_ind.HourRole)
        est_duration = model_ind.data(index, model_ind.EstTimeRole)
        status = model_ind.data(index, model_ind.StatusRole)

        # Frame and Background(s)
        pen = QPen()
        pen.setColor("Black")
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRoundedRect(option.rect, 25, 25)

        print(canvas)
        painter.setPen(Qt.blue)
        # Coordinates for delegate background
        x, y, w, h = canvas

        # Drawing of the texts
        painter.drawText(
            QRect(x + 50, y, w//3, h//2),
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

    def sizeHint(self, option, index):
        size = QSize(self.parent().size().width(), 50)
        return size
