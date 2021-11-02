from datetime import datetime, time, timedelta

from PySide2.QtCore import (QDate, QModelIndex, QRect, QSize, Qt, QTime,
                            Signal, Slot)
from PySide2.QtGui import QBrush, QColor, QPainter, QPainterPath, QPen
from PySide2.QtWidgets import (QComboBox, QDateEdit, QGridLayout, QLineEdit,
                               QListView, QPushButton, QStyle,
                               QStyledItemDelegate, QStyleOptionViewItem,
                               QTimeEdit, QWidget)

from view import ScheduleView
from model import ScheduleModel
from scheduleclasses import Status, TestItem
from xlsIO import tick


class ItemEditor(QWidget):
    editing_finished = Signal()
    attendance_dict = {
        '-': ' ',
        'A': 'Approval',
        'NA': 'Not Applicable',
        'R': 'Review',
        'W': 'Witness',
        tick: 'tick'
    }

    def __init__(self,
                 parent: QWidget,
                 option: QStyleOptionViewItem,
                 index: QModelIndex) -> None:

        super().__init__(parent=parent)
        self.index = index
        self.setAutoFillBackground(True)

        self.setGeometry(option.rect)

        self.edit_layout = QGridLayout()
        self.setLayout(self.edit_layout)
        self.edit_layout.setSpacing(3)
        self.edit_layout.setMargin(0)

        self.sfi_edit = QLineEdit(parent=self)
        self.sfi_edit.setMaximumWidth(40)
        self.edit_layout.addWidget(self.sfi_edit, 1, 0, 3, 1)
        self.edit_layout.setAlignment(self.sfi_edit, Qt.AlignBottom)

        self.name_edit = QLineEdit(parent=self)
        self.edit_layout.addWidget(self.name_edit, 0, 1, 3, 2)
        self.edit_layout.setAlignment(self.name_edit, Qt.AlignBottom)
        # self.name_edit.setMinimumWidth(100)

        self.dept_edit = QComboBox(parent=self)
        self.dept_edit.setEditable(True)
        self.edit_layout.addWidget(self.dept_edit, 3, 1, 3, 1)

        self.resp_name_edit = QLineEdit(parent=self)
        self.edit_layout.addWidget(self.resp_name_edit, 3, 2, 3, 1)

        self.state_edit = QComboBox(self)
        combo_items = [
            Status.NOT_STARTED.value,
            Status.ACTIVE.value,
            Status.PASSED.value,
            Status.FAILED.value,
        ]
        self.state_edit.addItems(combo_items)
        self.edit_layout.addWidget(self.state_edit, 0, 3, 3, 1)

        self.save_button = QPushButton('Save Changes', parent=self)
        self.edit_layout.addWidget(self.save_button, 3, 3, 3, 1)

        self.cls_edit = QComboBox(parent=self)
        self.cls_edit.addItems(
            ['C: ' + i for i in self.attendance_dict.keys()]
            )
        self.edit_layout.addWidget(self.cls_edit, 0, 4, 2, 1)
        self.cls_edit.setFixedWidth(55)

        self.flag_edit = QComboBox(parent=self)
        self.flag_edit.addItems(
            ['F: ' + i for i in self.attendance_dict.keys()]
            )
        self.edit_layout.addWidget(self.flag_edit, 2, 4, 2, 1)
        self.flag_edit.setFixedWidth(55)

        self.owner_edit = QComboBox(parent=self)
        self.owner_edit.addItems(
            ['O: ' + i for i in self.attendance_dict.keys()]
            )
        self.edit_layout.addWidget(self.owner_edit, 4, 4, 2, 1)
        self.owner_edit.setFixedWidth(55)

        self.date_edit = QDateEdit(parent=self, calendarPopup=True)
        self.date_edit.setDisplayFormat('dd-MM-yyyy')
        self.date_edit.setFixedWidth(100)
        self.edit_layout.addWidget(self.date_edit, 0, 5, 3, -1)

        self.hour_edit = QTimeEdit(parent=self)
        self.hour_edit.setDisplayFormat('HH:mm')
        self.edit_layout.addWidget(self.hour_edit, 3, 5, 3, 1)

        self.duration_edit = QTimeEdit(parent=self)
        self.duration_edit.setDisplayFormat('HH:mm')
        self.edit_layout.addWidget(self.duration_edit, 3, 6, 3, 1)

        self.save_button.clicked.connect(self.saveButton)

    def saveButton(self):
        if self.dept_edit.findText(self.dept_edit.currentText()) == -1:
            self.dept_edit.addItem(self.dept_edit.currentText())
        view: QListView = self.parent().parent()
        view.closeEditor(self, QStyledItemDelegate.SubmitModelCache)
        view.model().check_activated()


class TestItemDelegate(QStyledItemDelegate):
    """A delegate to show test items in listview in qt side"""

    COLORS = {
        'Set State': Qt.white,
        'Not Started': Qt.lightGray,
        'Active': QColor(0, 114, 206),
        'Passed': QColor(68, 214, 44),
        'Failed': QColor(227, 120, 120)
    }

    def __init__(self, parent: ScheduleView) -> None:
        super().__init__(parent)
        self.model: ScheduleModel = self.parent().model()

        return None

    def paint(self, painter: QPainter,
              option: QStyleOptionViewItem, index: QModelIndex):

        painter.setRenderHint(QPainter.Antialiasing, on=True)

        # Supplying data from model
        sfi = index.data(ScheduleModel.SfiRole)
        name = index.data(ScheduleModel.NameRole)
        cls_att = index.data(ScheduleModel.ClsRole)
        flg_att = index.data(ScheduleModel.FlagRole)
        ownr_att = index.data(ScheduleModel.OwnrRole)
        resp_dept = index.data(ScheduleModel.DeptRole)
        date_str = index.data(ScheduleModel.DateStrRole)
        hour_str = index.data(ScheduleModel.HourRole)
        est_duration = index.data(ScheduleModel.EstTimeRole)
        status = index.data(ScheduleModel.StatusRole)
        resp_name = index.data(ScheduleModel.RespNameRole)

        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        # Frame and Background(s)

        # background color for delegate rectangle
        back_brush = QBrush()
        back_brush.setStyle(Qt.SolidPattern)

        back_brush.setColor(self.COLORS[status])

        rect_path = QPainterPath()
        r = option.rect
        rect_path.addRoundedRect(
            r.x()+3, r.y()+3, r.width()-6, r.height()-6, 10, 10
        )
        pen = QPen()
        pen.setColor("Black")
        pen.setWidth(1)
        painter.setPen(pen)
        painter.fillPath(rect_path, back_brush)
        painter.drawPath(rect_path)

        # painter.fillRect(option.rect, back_brush)

        painter.setPen(Qt.black)
        # Coordinates for delegate background
        x, y, w, h = option.rect.getRect()

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
            QRect(x+50+w//3, y+h//2, w//3, h//2),
            Qt.AlignVCenter, resp_name
        )

        painter.drawText(
            QRect(x+w-100, y, 100, h//2),
            Qt.AlignCenter, date_str.strftime('%d-%m-%Y')
        )

        painter.drawText(
            QRect(x+w-100, y+h//2, 50, h//2),
            Qt.AlignCenter, hour_str.strftime('%H:%M')
        )

        if type(est_duration) is time:
            est_str = est_duration.strftime('%H:%M')
        else:
            est_str = est_duration

        painter.drawText(
            QRect(x+w-50, y+h//2, 50, h//2),
            Qt.AlignCenter,
            est_str
        )

    def createEditor(self, parent, option, index):
        editor = ItemEditor(parent, option, index)
        return editor

    def sizeHint(self, option: QStyleOptionViewItem, index):
        size = QSize(option.rect.width(), 70)
        return size

    def updateEditorGeometry(self, editor: QWidget, option, index):

        if index.isValid():
            x, y, w, h = option.rect.getRect()
            editor.setGeometry(x+6, y+6, w-12, h-12)

            return None

        # else:
        #     return super().updateEditorGeometry(editor, option, index)

    def setEditorData(self, editor: ItemEditor, index: QModelIndex):
        if index.isValid():
            editor.dept_edit.addItems(index.data(
                ScheduleModel.RespSelectionRole)
            )
            if editor.isHidden():
                editor.sfi_edit.setText(index.data(ScheduleModel.SfiRole))
                editor.name_edit.setText(index.data(ScheduleModel.NameRole))

                dept_index = editor.dept_edit.findText(
                    index.data(ScheduleModel.DeptRole))
                editor.dept_edit.setCurrentIndex(dept_index)

                editor.resp_name_edit.setText(
                    index.data(ScheduleModel.RespNameRole)
                )

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
                editor.date_edit.setDate(
                    QDate(date.year, date.month, date.day)
                )

                hour = index.data(ScheduleModel.HourRole)
                editor.hour_edit.setTime(QTime(hour.hour, hour.minute))

                est_dur = index.data(ScheduleModel.EstTimeRole)
                if type(est_dur) is time or type(est_dur) is datetime:
                    editor.duration_edit.setTime(
                        QTime(est_dur.hour, est_dur.minute)
                    )
                else:
                    editor.duration_edit.hide()

                state = index.data(ScheduleModel.StatusRole)
                state_ind = editor.state_edit.findText(state)
                editor.state_edit.setCurrentIndex(state_ind)

                # Changing editor's background color according to the state
                new_pallete = editor.palette()
                new_pallete.setColor(
                    editor.backgroundRole(), self.COLORS[state])
                editor.setPalette(new_pallete)

    def setModelData(
            self,
            editor: ItemEditor,
            model: ScheduleModel,
            index: QModelIndex) -> None:

        if index.isValid():

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
                editor.duration_edit.time().toPython(),
                ScheduleModel.EstTimeRole
            )

            model.setData(
                index,
                editor.state_edit.currentText(),
                ScheduleModel.StatusRole
            )

            model.setData(
                index,
                editor.resp_name_edit.text(),
                ScheduleModel.RespNameRole
            )

            # Signal for updating dash and qt side at the same time
            model.dataChanged.emit(index, index, [])

    @Slot()
    def newItem(self):
        self.model.beginInsertRows(
            QModelIndex(),
            self.model.rowCount(),
            self.model.rowCount(),
        )
        self.model._data.append(TestItem(
            sfi='',
            item_name='',
            class_attendance='-',
            flag_attendance='-',
            owner_attendance='-',
            record_status='',
            responsible_dept='Quality',
            date=datetime.today(),
            start_hour=(datetime.now()+timedelta(hours=3)).time(),
            est=time()
            )
        )
        self.model.endInsertRows()
        parr: ScheduleView = self.parent()
        parr.edit(self.model.index(self.model.rowCount()-1))
