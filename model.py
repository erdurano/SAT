from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, Slot


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

    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    @Slot()
    def updateSchedule(self, schedule_items: list):
        self.beginResetModel()
        self._data = schedule_items
        self.endResetModel()

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
                return "Passive"

        else:
            return None

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

        return roles
