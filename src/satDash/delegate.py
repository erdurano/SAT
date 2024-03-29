from datetime import datetime, time

from PySide6.QtCore import QDate, QModelIndex, QRect, QSize, Qt, QTime, Signal
from PySide6.QtGui import QBrush, QColor, QPainter, QPainterPath, QPaintEvent, QPen
from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QStyle,
    QStyledItemDelegate,
    QStyleOptionViewItem,
    QTimeEdit,
    QWidget,
)

from .model import ScheduleModel
from .scheduleclasses import Status
from .view import ScheduleView
from .xlsIO import tick


class ItemEditor(QWidget):
    editing_finished = Signal()
    attendance_dict = {
        "-": " ",
        "A": "Approval",
        "NA": "Not Applicable",
        "R": "Review",
        "W": "Witness",
        tick: "tick",
    }

    def __init__(
        self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex
    ) -> None:

        super().__init__(parent=parent)
        self.index: QModelIndex = index

        self.option = option

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.edit_layout = QGridLayout()
        self.setLayout(self.edit_layout)
        self.edit_layout.setSpacing(2)

        self.sfi_edit = QLineEdit(parent=self)
        self.sfi_edit.setMaximumWidth(40)
        self.edit_layout.addWidget(self.sfi_edit, 1, 0, 3, 1)
        self.edit_layout.setAlignment(self.sfi_edit, Qt.AlignmentFlag.AlignBottom)

        self.name_edit = QLineEdit(parent=self)
        self.edit_layout.addWidget(self.name_edit, 0, 1, 3, 2)
        self.edit_layout.setAlignment(self.name_edit, Qt.AlignBottom)  # type: ignore
        # self.name_edit.setMinimumWidth(100)

        self.dept_edit = QComboBox(parent=self)
        self.dept_edit.setEditable(True)
        self.edit_layout.addWidget(self.dept_edit, 3, 1, 3, 1)

        self.resp_name_edit = QLineEdit(parent=self)
        self.edit_layout.addWidget(self.resp_name_edit, 3, 2, 3, 1)

        self.state_edit = QComboBox(self)
        combo_items = [
            "Not Done",
            Status.PASSED.value,
            Status.COMMENTED.value,
            Status.FAILED.value,
        ]
        self.state_edit.addItems(combo_items)
        self.edit_layout.addWidget(self.state_edit, 0, 3, 3, 1)

        self.save_button = QPushButton("Save Changes", parent=self)
        self.edit_layout.addWidget(self.save_button, 3, 3, 3, 1)

        self.cls_edit = QComboBox(parent=self)
        self.cls_edit.addItems([f"C: {i}" for i in self.attendance_dict.keys()])
        self.edit_layout.addWidget(self.cls_edit, 0, 4, 2, 1)
        self.cls_edit.setFixedWidth(55)

        self.flag_edit = QComboBox(parent=self)
        self.flag_edit.addItems([f"F: {i}" for i in self.attendance_dict.keys()])
        self.edit_layout.addWidget(self.flag_edit, 2, 4, 2, 1)
        self.flag_edit.setFixedWidth(55)

        self.owner_edit = QComboBox(parent=self)
        self.owner_edit.addItems([f"O: {i}" for i in self.attendance_dict.keys()])
        self.edit_layout.addWidget(self.owner_edit, 4, 4, 2, 1)
        self.owner_edit.setFixedWidth(55)

        self.date_edit = QDateEdit(parent=self)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd-MM-yyyy")
        self.date_edit.setFixedWidth(100)
        self.edit_layout.addWidget(self.date_edit, 0, 5, 3, -1)

        self.hour_edit = QTimeEdit(parent=self)
        self.hour_edit.setDisplayFormat("HH:mm")
        self.edit_layout.addWidget(self.hour_edit, 3, 5, 3, 1)

        self.duration_edit = QTimeEdit(parent=self)
        self.duration_edit.setDisplayFormat("HH:mm")
        self.edit_layout.addWidget(self.duration_edit, 3, 6, 3, 1)

        x, y, w, h = self.rect().getCoords()

        self.setGeometry(x, y, w, h)

        self.save_button.clicked.connect(self.saveButton)

    def paintEvent(self, event: QPaintEvent) -> None:

        x, y, w, h = self.option.rect.getRect()

        status = self.index.data(ScheduleModel.StatusRole)
        color = QColor(TestItemDelegate.COLORS[status])

        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(color)
        painter.drawRect(QRect(0 + 6, 0 + 6, w - 12, h - 12))
        painter.end()
        # return super().paintEvent(event)

    def saveButton(self):
        if self.dept_edit.findText(self.dept_edit.currentText()) == -1:
            self.dept_edit.addItem(self.dept_edit.currentText())
        view = self.parent().parent()
        view.closeEditor(self, QStyledItemDelegateSubmitModelCache)
        view.model().sourceModel().check_activated()


class TestItemDelegate(QStyledItemDelegate):
    """A delegate to show test items in listview in qt side"""

    COLORS = {
        "Set State": Qt.GlobalColor.white,
        "Not Started": Qt.GlobalColor.lightGray,
        "Active": QColor(0, 114, 206),
        "Passed": QColor(68, 214, 44),
        "Failed": QColor(227, 120, 120),
        "Commented": QColor(255, 255, 49),
    }

    def __init__(self, parent: ScheduleView) -> None:
        super().__init__(parent)
        self.model: ScheduleModel = self.parent().model()

        return None

    def paint(
        self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex
    ):

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
            r.x() + 3, r.y() + 3, r.width() - 6, r.height() - 6, 10, 10
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
        painter.drawText(QRect(x + 50, y, w - 200, h // 2), Qt.AlignVCenter, name)

        painter.drawText(QRect(x, y, h, h), Qt.AlignCenter, sfi)

        painter.drawText(
            QRect(x + w - 150, y, 50, h // 3),
            Qt.AlignVCenter,
            f'C:{"-" if cls_att == "" else cls_att}',
        )

        painter.drawText(
            QRect(x + w - 150, y + h // 3, 50, h // 3),
            Qt.AlignVCenter,
            f'F:{"-" if flg_att == "" else flg_att}',
        )

        painter.drawText(
            QRect(x + w - 150, y + 2 * h // 3, 50, h // 3),
            Qt.AlignVCenter,
            f'O:{"-" if ownr_att == "" else ownr_att}',
        )

        painter.drawText(
            QRect(x + 50, y + h // 2, w // 3, h // 2), Qt.AlignVCenter, resp_dept
        )

        painter.drawText(
            QRect(x + 50 + w // 3, y + h // 2, w // 3, h // 2),
            Qt.AlignVCenter,
            resp_name,
        )

        painter.drawText(
            QRect(x + w - 100, y, 100, h // 2),
            Qt.AlignmentFlag.AlignCenter,
            date_str.strftime("%d-%m-%Y"),
        )

        painter.drawText(
            QRect(x + w - 100, y + h // 2, 50, h // 2),
            Qt.AlignmentFlag.AlignCenter,
            hour_str.strftime("%H:%M"),
        )

        if type(est_duration) is time:
            est_str = est_duration.strftime("%H:%M")
        else:
            est_str = est_duration

        painter.drawText(
            QRect(x + w - 50, y + h // 2, 50, h // 2),
            Qt.AlignmentFlag.AlignCenter,
            est_str,
        )

    def createEditor(self, parent, option, index):
        editor = ItemEditor(parent, option, index)
        self.updateEditorGeometry(editor, option, index)
        return editor

    def sizeHint(self, option: QStyleOptionViewItem, index):
        if index.isValid():
            return QSize(option.rect.width(), 70)

    def updateEditorGeometry(self, editor: ItemEditor, option, index):

        if index.isValid():
            x, y, w, h = option.rect.getRect()
            editor.setGeometry(x, y, w, h)
            editor.update()

    def setEditorData(self, editor: ItemEditor, index: QModelIndex):
        if not index.isValid():
            return
        editor.dept_edit.addItems(index.data(ScheduleModel.RespSelectionRole))
        if index.data(ScheduleModel.DeptRole) not in index.data(
            ScheduleModel.RespSelectionRole
        ):
            editor.dept_edit.addItems(
                [
                    index.data(ScheduleModel.DeptRole),
                ]
            )

        if editor.isHidden():
            self._extracted_from_setEditorData_13(editor, index)

    # TODO Rename this here and in `setEditorData`
    def _extracted_from_setEditorData_13(self, editor, index):
        editor.sfi_edit.setText(index.data(ScheduleModel.SfiRole))
        editor.name_edit.setText(index.data(ScheduleModel.NameRole))

        dept_index = editor.dept_edit.findText(index.data(ScheduleModel.DeptRole))
        editor.dept_edit.setCurrentIndex(dept_index)

        editor.resp_name_edit.setText(index.data(ScheduleModel.RespNameRole))

        bodies_prefix = ["C: ", "F: ", "O: "]
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

        est_dur = index.data(ScheduleModel.EstTimeRole)
        if type(est_dur) is time or type(est_dur) is datetime:
            editor.duration_edit.setTime(QTime(est_dur.hour, est_dur.minute))
        else:
            editor.duration_edit.hide()

        state = index.data(ScheduleModel.StatusRole)
        if state in ["Not Started", "Active"]:
            state = "Not Done"
        state_ind = editor.state_edit.findText(state)
        editor.state_edit.setCurrentIndex(state_ind)

    def setModelData(
        self, editor: ItemEditor, model: ScheduleModel, index: QModelIndex
    ) -> None:

        if index.isValid():

            model.setData(index, editor.sfi_edit.text(), ScheduleModel.SfiRole)
            model.setData(index, editor.name_edit.text(), ScheduleModel.NameRole)

            if editor.dept_edit.currentText() == "":
                editor.dept_edit.removeItem(
                    editor.dept_edit.findText(index.data(ScheduleModel.DeptRole))
                )
                nl = model.data(index, ScheduleModel.RespSelectionRole)
                if model.data(index, ScheduleModel.DeptRole) in model.data(
                    index, ScheduleModel.RespSelectionRole
                ):
                    nl.remove(model.data(index, ScheduleModel.DeptRole))
                model.setData(index, nl, ScheduleModel.RespSelectionRole)

            elif editor.dept_edit.currentText() not in model.data(
                index, ScheduleModel.RespSelectionRole
            ):
                nl = model.data(index, ScheduleModel.RespSelectionRole)
                nl.append(editor.dept_edit.currentText())
                model.setData(index, nl, ScheduleModel.RespSelectionRole)

            model.setData(index, editor.dept_edit.currentText(), ScheduleModel.DeptRole)

            model.setData(
                index,
                editor.cls_edit.currentText().split(" ")[-1],
                ScheduleModel.ClsRole,
            )

            model.setData(
                index,
                editor.flag_edit.currentText().split(" ")[-1],
                ScheduleModel.FlagRole,
            )

            model.setData(
                index,
                editor.owner_edit.currentText().split(" ")[-1],
                ScheduleModel.OwnrRole,
            )

            model.setData(
                index,
                datetime.combine(
                    editor.date_edit.date().toPython(), datetime.min.time()
                ),
                ScheduleModel.DateStrRole,
            )

            model.setData(
                index, editor.hour_edit.time().toPython(), ScheduleModel.HourRole
            )

            model.setData(
                index, editor.duration_edit.time().toPython(), ScheduleModel.EstTimeRole
            )

            model.setData(
                index, editor.state_edit.currentText(), ScheduleModel.StatusRole
            )

            model.setData(
                index, editor.resp_name_edit.text(), ScheduleModel.RespNameRole
            )

            # Signal for updating dash and qt side at the same time
            model.dataChanged.emit(index, index, [])
