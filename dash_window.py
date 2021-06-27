import os, sys
from PySide2.QtCore import QAbstractListModel, QModelIndex, QUrl, Qt, Slot
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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.dat = []

    def rowCount(self, index=QModelIndex()):
        return len(self.dat)

    def data(self, index: QModelIndex(), role: Qt.ItemDataRole):

        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return self.dat[index.row()]

    @Slot()
    def insertRows(self, dix):
        self.beginInsertRows(QModelIndex(), 0, len(dix))
        for index, item in enumerate(dix):
            self.dat.insert(index, item.dict)
        self.endInsertRows()

    # TODO: find a method for using this slot. Kill yourself if you have to
    # Because you're an idiot who deserves no better.
    @Slot(dict)
    def setData(self, item_dict, role=Qt.EditRole):

        for i, dix in enumerate(self.dat):
            # print(dix)
            # print(item_dict)
            if dix["item_name"] == item_dict["item_name"]:
                self.dat[i] == item_dict
        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount(), 0),
                              Qt.DisplayRole)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    widget = DashWindow()
    window.setCentralWidget(widget)

    window.show()
    app.exec_()