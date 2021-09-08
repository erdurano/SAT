from datetime import datetime
from PySide2.QtCore import (QDate, QModelIndex, QRect, QSize, Qt, QTime,
                            Signal)
from PySide2.QtGui import QBrush, QPainter, QPainterPath, QPen
from PySide2.QtWidgets import (QComboBox, QDateEdit, QGridLayout, QLineEdit,
                               QPushButton, QStyledItemDelegate,
                               QStyleOptionViewItem, QTimeEdit, QWidget)

from model import ScheduleModel


class ItemEditor(QWidget):
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
        # self.setFrameShape(QFrame.Box)
        self.setAutoFillBackground(True)
        # self.setLineWidth(2)

        self.edit_layout = QGridLayout()
        self.setLayout(self.edit_layout)
        self.edit_layout.setSpacing(3)
        self.edit_layout.setMargin(0)

        self.sfi_edit = QLineEdit(parent=self)
        self.sfi_edit.setMaximumWidth(40)
        self.edit_layout.addWidget(self.sfi_edit, 1, 0, 3, 1)
        self.edit_layout.setAlignment(self.sfi_edit, Qt.AlignBottom)

        self.name_edit = QLineEdit(parent=self)
        self.edit_layout.addWidget(self.name_edit, 0, 1, 3, 1)
        self.edit_layout.setAlignment(self.name_edit, Qt.AlignBottom)
        # self.name_edit.setMinimumWidth(100)

        self.dept_edit = QComboBox(parent=self)
        self.dept_edit.addItems([i + ' Dept.' if i != ' ' else ' '
                                for i in self.departments])
        self.edit_layout.addWidget(self.dept_edit, 3, 1, 3, 1)

        self.state_edit = QComboBox(self)
        states = index.model().state_list
        combo_items = ['Set State', ] + states
        self.state_edit.addItems(combo_items)
        self.edit_layout.addWidget(self.state_edit, 0, 2, 3, 1)

        self.save_button = QPushButton('Save Changes', parent=self)
        self.edit_layout.addWidget(self.save_button, 3, 2, 3, 1)

        self.cls_edit = QComboBox(parent=self)
        self.cls_edit.addItems(
            ['C: ' + i for i in self.attendance_dict.keys()]
            )
        self.edit_layout.addWidget(self.cls_edit, 0, 3, 2, 1)
        self.cls_edit.setFixedWidth(50)

        self.flag_edit = QComboBox(parent=self)
        self.flag_edit.addItems(
            ['F: ' + i for i in self.attendance_dict.keys()]
            )
        self.edit_layout.addWidget(self.flag_edit, 2, 3, 2, 1)
        self.flag_edit.setFixedWidth(50)

        self.owner_edit = QComboBox(parent=self)
        self.owner_edit.addItems(
            ['O: ' + i for i in self.attendance_dict.keys()]
            )
        self.edit_layout.addWidget(self.owner_edit, 4, 3, 2, 1)
        self.owner_edit.setFixedWidth(50)

        self.date_edit = QDateEdit(parent=self, calendarPopup=True)
        self.date_edit.setDisplayFormat('dd-MM-yyyy')
        self.date_edit.setFixedWidth(100)
        self.edit_layout.addWidget(self.date_edit, 0, 4, 3, -1)

        self.hour_edit = QTimeEdit(parent=self)
        self.hour_edit.setDisplayFormat('HH:mm')
        self.edit_layout.addWidget(self.hour_edit, 3, 4, 3, 1)

        self.duration_edit = QLineEdit(parent=self)
        self.duration_edit.setFixedWidth(50)
        self.edit_layout.addWidget(self.duration_edit, 3, 5, 3, 1)


class TestItemDelegate(QStyledItemDelegate):
    """A delegate to show test items in listview in qt side"""

    COLORS = {
        'Passive': Qt.lightGray,
        'Active': Qt.blue,
        'Passed': Qt.green,
        'Failed': Qt.red
    }

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
        resp_dept = index.data(model_ind.DeptRole)
        date_str = index.data(model_ind.DateStrRole)
        hour_str = index.data(model_ind.HourRole)
        est_duration = index.data(model_ind.EstTimeRole)
        status = model_ind.data(index, model_ind.StatusRole)

        # Frame and Background(s)

        # background color for delegate rectangle
        back_brush = QBrush()
        back_brush.setStyle(Qt.SolidPattern)

        back_brush.setColor(self.COLORS[status])

        rect_path = QPainterPath()
        rect_path.addRoundedRect(option.rect, 10, 10)
        pen = QPen()
        pen.setColor("Black")
        pen.setWidth(1)
        painter.setPen(pen)
        painter.fillPath(rect_path, back_brush)
        painter.drawPath(rect_path)

        # painter.fillRect(option.rect, back_brush)

        painter.setPen(Qt.black)
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
        size = QSize(300, 60)
        return size

    def updateEditorGeometry(self, editor: QWidget, option, index):

        if index.isValid():
            x, y, w, h = option.rect.getRect()
            editor.setGeometry(x+3, y+3, w-6, h-6)

        else:
            return super().updateEditorGeometry(editor, option, index)

    def setEditorData(self, editor: ItemEditor, index: QModelIndex):
        if index.isValid():
            editor.sfi_edit.setText(index.data(ScheduleModel.SfiRole))
            editor.name_edit.setText(index.data(ScheduleModel.NameRole))

            dept_index = editor.dept_edit.findText(
                index.data(ScheduleModel.DeptRole))
            editor.dept_edit.setCurrentIndex(dept_index)

            bodies_prefix = ['C: ', 'F: ', 'O: ']
            roles = [
                ScheduleModel.ClsRole,
                ScheduleModel.FlagRole,
                ScheduleModel.OwnrRole,
                ]

            for i, p in enumerate(bodies_prefix):
                if i == 0:
                    widget = editor.cls_edit
                elif i == 1:
                    widget = editor.flag_edit
                else:
                    widget = editor.owner_edit

                sel_index = widget.findText(p + index.data(roles[i]))
                widget.setCurrentIndex(sel_index)

            date = index.data(ScheduleModel.DateStrRole)
            editor.date_edit.setDate(QDate(date.year, date.month, date.day))

            hour = index.data(ScheduleModel.HourRole)
            editor.hour_edit.setTime(QTime(hour.hour, hour.minute))

            editor.duration_edit.setText(
                index.data(ScheduleModel.EstTimeRole))

            state = index.data(ScheduleModel.StatusRole)
            state_ind = editor.state_edit.findText(state)
            editor.state_edit.setCurrentIndex(state_ind)

            # TODO: Find a method for painting the background of the editor
            # according to the item state
            # editor.palette().setColor(QPalette.Window, self.COLORS[state])

        else:
            return super().setEditorData(editor, index)

    def setModelData(
            self,
            editor: ItemEditor,
            model: ScheduleModel,
            index: QModelIndex) -> None:

        if index.isValid():
            model = index.model()
            model.setData(
                index,
                editor.sfi_edit.text(),
                ScheduleModel.SfiRole
            )
            model.setData(
                index,
                editor.name_edit.text(),
                ScheduleModel.NameRole
            )

            model.setData(
                index,
                editor.dept_edit.currentText(),
                ScheduleModel.DeptRole)

            model.setData(
                index,
                editor.cls_edit.currentText().split(' ')[-1],
                ScheduleModel.ClsRole
            )

            model.setData(
                index,
                editor.flag_edit.currentText().split(' ')[-1],
                ScheduleModel.FlagRole
            )

            model.setData(
                index,
                editor.owner_edit.currentText().split(' ')[-1],
                ScheduleModel.OwnrRole
            )

            model.setData(
                index,
                datetime.combine(
                    editor.date_edit.date().toPython(),
                    datetime.min.time()
                ),
                ScheduleModel.DateStrRole
            )

            model.setData(
                index,
                editor.hour_edit.time().toPython(),
                ScheduleModel.HourRole
            )

            model.setData(
                index,
                editor.duration_edit.text(),
                ScheduleModel.EstTimeRole
            )

            model.setData(
                index,
                editor.state_edit.currentText(),
                ScheduleModel.StatusRole
            )
