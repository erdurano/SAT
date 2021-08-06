from scheduleclasses import TestItem
from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt


class ScheduleModel(QAbstractListModel):

    SfiRole = Qt.UserRole + 1001
    NameRole = Qt.UserRole + 1002
    DateStrRole = Qt.UserRole + 1003
    ClsRole = Qt.UserRole + 1004
    FlagRole = Qt.UserRole + 1005
    OwnrRole = Qt.UserRole + 1006
    DeptRole = Qt.UserRole + 1007
    StatusRole = Qt.UserRole + 1008

    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = []

    def rowCount(self, index=QModelIndex()):
        return len(self._data)

    def roleNames(self):
        roles = dict()

        roles[ScheduleModel.SfiRole] = b'sfiStr'
        roles[ScheduleModel.NameRole] = b'testStr'
        roles[ScheduleModel.DateStrRole] = b'dateStr'
        roles[ScheduleModel.ClsRole] = b'clsStr'
        roles[ScheduleModel.FlagRole] = b'flgStr'
        roles[ScheduleModel.OwnrRole] = b'OwnrStr'
        roles[ScheduleModel.DeptRole] = b'DeptStr'
        roles[ScheduleModel.StatusRole] = b'statStr'

        return roles

    # TODO: Upwards is boiler plate but as you might've guessed, below still
    # needs implementation

    def insertRows(self, row: int, count: int, parent: QModelIndex) -> bool:
        pass

    def setData(self, index: QModelIndex, value: TestItem, role: int) -> bool:
        return super().setData(index, value, role=role)
