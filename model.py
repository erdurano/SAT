import typing
from datetime import datetime, time, timedelta

from PySide6.QtCore import (QAbstractListModel, QModelIndex, Qt, Slot)

from scheduleclasses import Schedule, Status, TestItem


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
    QmlEstRole = Qt.UserRole + 14
    RespNameRole = Qt.UserRole + 15
    RespSelectionRole = Qt.UserRole + 16
    IsNearRole = Qt.UserRole + 17

    state_list = [
        'Passive',
        'Active',
        'Passed',
        'Failed',
        ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self._data: list[TestItem] = []
        self.schedule = Schedule()

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()) -> int:
        return 0

    @Slot()
    def updateSchedule(self, schedule: Schedule):
        self.beginResetModel()
        self.schedule = schedule
        self._data = self.schedule.agenda_items
        self.sort()
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
                return item.date.strftime('%d-%m-%Y')
            elif role == self.QmlHourRole:
                return item.start_hour.strftime('%H:%M')
            elif role == self.QmlEstRole:
                return item.est.strftime('%H:%M')\
                    if isinstance(item.est, time) else item.est
            elif role == self.RespNameRole:
                return item.responsible_name
            elif role == self.RespSelectionRole:
                if hasattr(self.schedule, 'responsible_selection'):
                    return self.schedule.responsible_selection
                else:
                    return ['Quality']
            elif role == self.IsNearRole:
                t_date = item.date
                t_hour = item.start_hour
                dt = datetime(
                    t_date.year,
                    t_date.month,
                    t_date.day,
                    t_hour.hour,
                    t_hour.minute
                )
                isNear = (dt - datetime.now()) <= timedelta(hours=2)
                return isNear

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
                self._data[index.row()].est = ScheduleModel.correct_est_value(
                    self._data[index.row()].est, value
                )
            elif role == self.StatusRole:
                self._data[index.row()].status = Status(value)
            elif role == self.RespNameRole:
                self._data[index.row()].responsible_name = value
            self.sort()

            return True

        else:
            return False

    def sort(self,
             column: int = 0,
             order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:

        if self.columnCount() < column:
            return
        elif order == Qt.SortOrder.DescendingOrder:
            self._data.sort(key=TestItem.dt, reverse=True)
        elif order == Qt.SortOrder.AscendingOrder:
            self._data.sort(key=TestItem.dt, reverse=False)
        else:
            return super().sort(column, order=order)

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
        roles[self.QmlEstRole] = b'qmlEstRole'
        roles[self.RespNameRole] = b'respNameRole'
        roles[self.IsNearRole] = b'isNearRole'

        return roles

    @staticmethod
    def correct_est_value(record, new_value):
        if isinstance(record, time):
            return new_value
        if isinstance(record, str):
            return record

    def flags(self, index):
        if index.isValid():
            return (Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

        return super().flags(index)

    def check_activated(self):
        now = datetime.now()
        roles_to_change = [self.StatusRole, self.IsNearRole]
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
                self.dataChanged.emit(index, index, roles_to_change[0:1])

            elif now < dt and\
                    self.data(index, self.StatusRole) ==\
                    Status.ACTIVE.value:

                self.setData(
                    index,
                    Status.NOT_STARTED.value,
                    self.StatusRole
                )
                self.dataChanged.emit(index, index, roles_to_change[0:1])

            if index.isValid():
                self.dataChanged.emit(
                    index, index,
                    roles_to_change[1:]
                )

    def removeRow(self, row: int, parent: QModelIndex = QModelIndex()) -> bool:
        if self.index(row).isValid():
            self.beginRemoveRows(
                QModelIndex(),
                row,
                row
            )
            self._data.pop(row)
            self.endRemoveRows()
            return True
        return False
