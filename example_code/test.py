import sys
from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt
from PySide2.QtGui import QGuiApplication

from PySide2.QtQml import QQmlApplicationEngine


class Model (QAbstractListModel):
    def __init__(self, items, parent=None):
        super(Model, self).__init__(parent)
        self ._items = items

    def rowCount(self, parent=None):
        return len(self._items)

    def data(self, index, role=None):
        role = role or QModelIndex()

        if role == Qt.UserRole + 0:
            return self ._items[index.row()]["type"]

        if role == Qt.UserRole + 1:
            return self ._items[index.row()]["name"]

        if role == Qt.UserRole + 2:
            return self ._items[index.row()]["path"]

        if role == Qt.UserRole + 3:
            return self ._items[index.row()]["versions"]

    def roleNames(self):
        return {
            Qt.UserRole + 0: b"itemType",
            Qt.UserRole + 1: b"itemName",
            Qt.UserRole + 2: b"itemPath",
            Qt.UserRole + 3: b"itemVersions",
                }


if __name__ == "__main__":

    items = [
        {
            "type": "asset",
            "name": "shapes",
            "path": "c:/users/Roy/Desktop/shapes.ma",
            "versions": ["v001", "v002", "v003"]
        },
        {
            "type": "asset",
            "name": "shapes1",
            "path": "c:/users/Roy/Desktop/shapes.ma",
            "versions": ["v001", "v002", "v003", "v004"]
        },
        {
            "type": "asset",
            "name": "shapes2",
            "path": "c:/users/Roy/Desktop/shapes.ma",
            "versions": ["v001", "v002", "v003"]
        },
    ]

model = Model(items)

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty("mymodel", model)
engine.load("test.qml")
roots = engine.rootObjects()
if not roots:
    sys.exit(-1)
sys.exit(app.exec_())
