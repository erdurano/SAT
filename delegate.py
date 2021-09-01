from PySide2.QtCore import QModelIndex, QRect, QSize, Qt, Signal
from PySide2.QtGui import QPainter, QPen
from PySide2.QtWidgets import (QComboBox, QFrame, QGridLayout,
                               QLineEdit, QStyledItemDelegate,
                               QStyleOptionViewItem, QWidget)


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
        editor = ItemEditor(parent, option, index)
        return editor

    def sizeHint(self, option, index):
        size = QSize(300, 75)
        return size


class ItemEditor(QFrame):
    editing_finished = Signal()
    attendance_dict = {
        '-': ' ',
        'A': 'Approval',
        'NA': 'Not Applicable',
        'R': 'Review',
        'W': 'Witness',
    }

    departments = [
        ' ',
        'Commissioning',
        'Electricity',
        'Quality',
        'Hull',
        'Piping',
    ]

    def __init__(self,
                 parent: QWidget,
                 option: QStyleOptionViewItem,
                 index: QModelIndex) -> None:

        super().__init__(parent=parent)
        self.setFrameShape(QFrame.Box)
        self.setAutoFillBackground(True)
        self.setLineWidth(2)
        self.resize(self.width(), self.height()*3//2)

        self.edit_layout = QGridLayout()
        self.setLayout(self.edit_layout)
        self.edit_layout.setSpacing(3)
        self.edit_layout.setMargin(3)

        self.sfi_edit = QLineEdit(parent=self)
        self.sfi_edit.setMaximumWidth(40)
        self.edit_layout.addWidget(self.sfi_edit, 1, 0, 3, 1)
        self.edit_layout.setAlignment(self.sfi_edit, Qt.AlignBottom)

        self.name_edit = QLineEdit(parent=self)
        self.edit_layout.addWidget(self.name_edit, 0, 1, 3, 1)
        self.edit_layout.setAlignment(self.name_edit, Qt.AlignBottom)
        self.name_edit.setMinimumWidth(100)

        self.dept_edit = QComboBox(parent=self)
        self.dept_edit.addItems([i + ' Dept.' if i != ' ' else ' '
                                for i in self.departments])
        self.edit_layout.addWidget(self.dept_edit, 3, 1, 3, 1)
        self.edit_layout.setAlignment(self.dept_edit, Qt.AlignBottom)

        self.cls_edit = QComboBox(parent=self)
        self.cls_edit.addItems(self.attendance_dict.keys())
        self.edit_layout.addWidget(self.cls_edit, 0, 2, 2, 1)
        self.cls_edit.setMaximumWidth(100)

        self.flag_edit = QComboBox(parent=self)
        self.flag_edit.addItems(self.attendance_dict.keys())
        self.edit_layout.addWidget(self.flag_edit, 2, 2, 2, 1)
        self.flag_edit.setMaximumWidth(100)

        self.owner_edit = QComboBox(parent=self)
        self.owner_edit.addItems(self.attendance_dict.keys())
        self.edit_layout.addWidget(self.owner_edit, 4, 2, 2, 1)
        self.owner_edit.setMaximumWidth(100)
