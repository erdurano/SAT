from scheduleclasses import Status, TestItem
import typing
from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, Slot
from datetime import datetime


class ScheduleModel(QAbstractListModel):

    SfiRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2
    ClsRole = Qt.UserRole + 3
    FlagRole = Qt.UserRole + 4
    OwnrRole = Qt.UserRole + 5
    RecordRole = Qt.UserRole + 6
    DeptRole = Qt.UserRole + 7
    DateStrRole = Qt.UserRole + 8
    HourRole = Qt.UserRole + 9
    EstTimeRole = Qt.UserRole + 10
    StatusRole = Qt.UserRole + 11
    QmlDateRole = Qt.UserRole + 12
    QmlHourRole = Qt.UserRole + 13

    state_list = [
        'Passive',
        'Active',
        'Passed',
        'Failed',
        ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self._data: list[TestItem] = []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    @Slot()
    def updateSchedule(self, schedule_items: list):
        self.beginResetModel()
        self._data = schedule_items
        self.endResetModel()
        self.check_activated()

    def data(self, index=QModelIndex(), role: int = Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._data[index.row()]

            if role == self.SfiRole:
                return item.sfi
            elif role == self.NameRole:
                return item.item_name
            elif role == self.ClsRole:
                return item.class_attendance
            elif role == self.FlagRole:
                return item.flag_attendance
            elif role == self.OwnrRole:
                return item.owner_attendance
            elif role == self.RecordRole:
                return item.record_status
            elif role == self.DeptRole:
                return item.responsible_dept
            elif role == self.DateStrRole:
                return item.date
            elif role == self.HourRole:
                return item.start_hour
            elif role == self.EstTimeRole:
                return item.est
            elif role == self.StatusRole:
                return item.status.value
            elif role == self.QmlDateRole:
                return item.date.strftime('%d/%m/%Y') \
                    if item.date is not None else ' '
            elif role == self.QmlHourRole:
                return item.start_hour.strftime('%H:%M')

        else:
            return None

    def setData(
            self,
            index: QModelIndex,
            value: typing.Any,
            role: int) -> bool:

        if index.isValid():
            if role == self.SfiRole:
                self._data[index.row()].sfi = value
            elif role == self.NameRole:
                self._data[index.row()].item_name = value
            elif role == self.DeptRole:
                self._data[index.row()].responsible_dept = value
            elif role == self.ClsRole:
                self._data[index.row()].class_attendance = value
            elif role == self.FlagRole:
                self._data[index.row()].flag_attendance = value
            elif role == self.OwnrRole:
                self._data[index.row()].owner_attendance = value
            elif role == self.DateStrRole:
                self._data[index.row()].date = value
            elif role == self.HourRole:
                self._data[index.row()].start_hour = value
            elif role == self.EstTimeRole:
                self._data[index.row()].est = value
            elif role == self.StatusRole:
                self._data[index.row()].status = Status(value)

            return True

        else:
            return False

    def roleNames(self):
        roles = dict()

        roles[self.SfiRole] = b'sfiRole'
        roles[self.NameRole] = b'nameRole'
        roles[self.ClsRole] = b'clsRole'
        roles[self.FlagRole] = b'flagRole'
        roles[self.OwnrRole] = b'ownrRole'
        roles[self.RecordRole] = b'recordRole'
        roles[self.DeptRole] = b'deptRole'
        roles[self.DateStrRole] = b'dateStrRole'
        roles[self.HourRole] = b'hourRole'
        roles[self.EstTimeRole] = b'estTimeRole'
        roles[self.StatusRole] = b'statusRole'
        roles[self.QmlDateRole] = b'qmlDateRole'
        roles[self.QmlHourRole] = b'qmlHourRole'

        return roles

    def flags(self, index):
        if index.isValid():
            return (Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

        return super().flags(index)

    def check_activated(self):
        now = datetime.now()
        for rown in range(self.rowCount()):
            index = self.index(rown)
            year, month, day = (
                self.data(index, self.DateStrRole).year,
                self.data(index, self.DateStrRole).month,
                self.data(index, self.DateStrRole).day,
            )
            hour, minute = (
                self.data(index, self.HourRole).hour,
                self.data(index, self.HourRole).minute,
            )
            dt = datetime(year, month, day, hour, minute)

            if now > dt and\
                    self.data(index, self.StatusRole) ==\
                    Status.NOT_STARTED.value:
                self.setData(
                    index,
                    Status.ACTIVE.value,
                    self.StatusRole
                )

            self.dataChanged.emit(
                index,
                index
            )
