import os

from PySide2.QtCore import Property, QAbstractListModel, QModelIndex, QObject, QUrl, Qt, Signal
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2.QtWidgets import QApplication, QMainWindow


class MockModel(QAbstractListModel):
    role1 = Qt.UserRole + 1000
    role2 = Qt.UserRole + 1001
    role3 = Qt.UserRole + 1002

    def __init__(self, parent=None):
        super.__init__(parent)
        self._data = []

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._data[index.row()]

            if role == MockModel.role1:
                return item['role1']

            elif role == MockModel.role2:
                return item['role2']

            elif role == MockModel.role3:
                return item['role3']

    def roleNames(self):
        roles = dict()
        roles[MockModel.role1] = b'role1'
        roles[MockModel.role2] = b'role2'
        roles[MockModel.role3] = b'role3'

        return roles

    def appendRow(self, role1str, role2str, role3str):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._dat.append({'role1': role1str, 'role2': role2str, 'role2': role2str,})
        self.endInsertRows()


class Backend(QObject):
    modelChanged = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._model = MockModel()

    @Property(QObject, constant=False, notify=modelChanged)
    def model(self):
        return self._model

def add_item(model):
    model.appendRow()

if __name__ == "__main__":
    app = QApplication()
    window = QMainWindow()
    widget = QQuickWidget()
    widget.setSource(QUrl(os.path.dirname(__file__) + "qml/test.qml"))
    
    window.setCentralWidget(widget)
    window.show()

    app.exec_()
