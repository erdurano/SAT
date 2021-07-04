import os
import sys

from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, QUrl, Slot
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2.QtWidgets import QApplication, QMainWindow


class DashWindow(QQuickWidget):

    def __init__(self):
        super().__init__()
        self.model = ItemModel()
        self.rootContext().setContextProperty("itemModel", self.model)
        self.setSource(QUrl.fromLocalFile(
            os.path.join(os.path.dirname(__file__), 'qml/Dash.qml')
            ))
        self.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.setWindowTitle('Dash')


class ItemModel(QAbstractListModel):

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

    def data(self, index: QModelIndex(), role=Qt.DisplayRole):

        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._data[index.row()]

            if role == ItemModel.SfiRole:
                return item['sfi']

            if role == ItemModel.NameRole:
                return item['item_name']

            if role == ItemModel.DateStrRole:
                return item['date_str']

            if role == ItemModel.ClsRole:
                return item['class_att']

            if role == ItemModel.FlagRole:
                return item['flag_att']

            if role == ItemModel.OwnrRole:
                return item['owner_att']

            if role == ItemModel.DeptRole:
                return item['resp_dept']

            if role == ItemModel.StatusRole:
                return item['active_stat']

    def roleNames(self):
        roles = dict()

        roles[ItemModel.SfiRole] = b'sfiStr'
        roles[ItemModel.NameRole] = b'testStr'
        roles[ItemModel.DateStrRole] = b'dateStr'
        roles[ItemModel.ClsRole] = b'clsStr'
        roles[ItemModel.FlagRole] = b'flgStr'
        roles[ItemModel.OwnrRole] = b'OwnrStr'
        roles[ItemModel.DeptRole] = b'DeptStr'
        roles[ItemModel.StatusRole] = b'statStr'

        return roles

    @Slot()
    def insertRows(self, dix):
        self.beginInsertRows(QModelIndex(), self.rowCount(), len(dix))
        for item in dix:
            self._data.append(item.dict)
        self.endInsertRows()

    # TODO: find a method for using this slot. Kill yourself if you have to
    # Because you're an idiot who deserves no better.
    @Slot(dict)
    def setData(self, item_dict, role=Qt.EditRole):

        for i, dix in enumerate(self.item_dict):
            # print(dix)
            # print(item_dict)
            if dix["item_name"] == item_dict["item_name"]:
                self._data[i] == item_dict
        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount(), 0),
                              Qt.DisplayRole)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    widget = DashWindow()
    window.setCentralWidget(widget)

    window.show()
    app.exec_()
