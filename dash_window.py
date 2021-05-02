import os
from PySide2.QtCore import QAbstractListModel, QModelIndex, QUrl, Qt
from PySide2.QtQuickWidgets import QQuickWidget


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
        self.schedule_data = [{"sfi": "123"}]
        super().__init__(parent)
        self.dat = self.schedule_data

    def rowCount(self, index=QModelIndex()):
        return len(self.dat)

    def data(self, index: QModelIndex(), role: Qt.ItemDataRole):

        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return self.dat[index.row()]
