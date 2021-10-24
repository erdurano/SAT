import typing
from PySide2.QtCore import QModelIndex, QObject, QAbstractTableModel, QSize, Qt
from PySide2.QtGui import QImage, qGray


class ImageModel(QAbstractTableModel):

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent=parent)
        self.modelImage: QImage = QImage()

    
    def setImage(self, image: QImage) -> None:
        self.beginResetModel()
        self.modelImage = image
        self.endResetModel()

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return self.modelImage.height()

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return self.modelImage.width()
    
    def data(self, index: QModelIndex = QModelIndex(), role: int = ...) -> typing.Any:
        if (index.isValid() is False) and (role != Qt.DisplayRole):
            return None
        return qGray(self.modelImage.pixel(index.column(), index.row()))

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.SizeHintRole:
            return QSize(1, 1)
        return None