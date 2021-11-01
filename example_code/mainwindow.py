from typing import ItemsView, Optional

from PySide2 import QtWidgets
from PySide2.QtCore import QAbstractItemModel, QDir, QModelIndex, QRect, Qt, Slot
from PySide2.QtGui import QImage, QKeySequence, QPainter
from PySide2.QtPrintSupport import QPrintDialog, QPrinter
from PySide2.QtWidgets import (QAction, QApplication, QDialog,
                               QFileDialog, QHBoxLayout, QLabel, QMainWindow,
                               QMenu, QMessageBox, QProgressDialog, QSpinBox, QStyleOptionViewItem, QStyledItemDelegate,
                               QTableView, QVBoxLayout, QWidget)

from imagemodel import ImageModel
from pixeldelegate import PixelDelegate, ItemSize


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget= None, flags: Qt.WindowFlags = None) -> None:
        super().__init__()
        self.printAction: Optional(QAction) = None
        self.model: Optional(QAbstractItemModel) = ImageModel(self)
        self.currentPath: Optional(str) = QDir().homePath()
        self.view: QTableView = None


        self.centralWidget = QWidget()

        self.view = QTableView()
        self.view.setShowGrid(False)
        self.view.horizontalHeader().hide()
        self.view.horizontalHeader().setMinimumSectionSize(1)
        self.view.verticalHeader().hide()
        self.view.verticalHeader().setMinimumSectionSize(1)
        self.view.setModel(self.model)

        self.delegate: QStyledItemDelegate = PixelDelegate(self)
        self.view.setItemDelegate(self.delegate)

        pixelSizeLabel = QLabel(self.tr('Pixel size:'))
        pixelSizeSpinBox = QSpinBox()
        pixelSizeSpinBox.setMinimum(4)
        pixelSizeSpinBox.setMaximum(32)
        pixelSizeSpinBox.setValue(12)

        fileMenu = QMenu(self.tr('&File'), self)
        openAction: QAction = fileMenu.addAction(self.tr('&Open'))
        openAction.setShortcuts(QKeySequence.Open)

        self.printAction: QAction= fileMenu.addAction(self.tr("&Print"))
        self.printAction.setEnabled(False)
        self.printAction.setShortcuts(QKeySequence.Print)

        quitAction: QAction= fileMenu.addAction(self.tr('E&xit'))
        quitAction.setShortcuts(QKeySequence.Quit)

        helpMenu = QMenu(self.tr('&help'), self)
        aboutAction: QAction = helpMenu.addAction(self.tr('&About'))

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(helpMenu)

        openAction.triggered.connect(self.chooseImage)
        self.printAction.triggered.connect(self.printImage)
        quitAction.triggered.connect(QApplication.instance().quit)
        aboutAction.triggered.connect(self.showAboutBox)
        pixelSizeSpinBox.valueChanged.connect(self.delegate.setPixelSize)
        pixelSizeSpinBox.valueChanged.connect(self.updateView)

        controlsLayout = QHBoxLayout()
        controlsLayout.addWidget(pixelSizeLabel)
        controlsLayout.addWidget(pixelSizeSpinBox)
        controlsLayout.addStretch(1)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.view)
        mainLayout.addLayout(controlsLayout)
        self.centralWidget.setLayout(mainLayout)

        self.setCentralWidget(self.centralWidget)

        self.setWindowTitle(self.tr('Pixelator'))

    @Slot(str)
    def openImage(self, fileName: str) -> None:
        
        image = QImage()
        print(fileName)
        print(image.load(fileName))

        if image.load(fileName):
            
            self.model.setImage(image)
            if fileName[:2] != ":/":
                self.currentPath = fileName
                self.setWindowTitle(self.tr('{} - Pixelator'.format(self.currentPath)))

            self.printAction.setEnabled(True)
            self.updateView()

    @Slot()
    def chooseImage(self) -> None:
        fileName, _ = QFileDialog().getOpenFileName(self, self.tr("Choose an image"), self.currentPath, "*")

        if fileName is not None:
            self.openImage(fileName)

    @Slot()
    def printImage(self) -> None:
        if self.model.rowCount(QModelIndex()) *\
            self.model.columnCount(QModelIndex()) > 90000:

            answer = QMessageBox().question(
                self,
                self.tr("Large Image Size"),
                self.tr("The printed image may be very large. Are you sure that",
                        "you want to print it?"),
                QMessageBox.Yes|QMessageBox.No
            )

            if answer == answer.No:
                return

        printer = QPrinter(QPrinter.HighResolution)
        dlg = QPrintDialog(printer, self)
        dlg.setWindowTitle(self.tr("Print Image"))

        if dlg.exec_() != QDialog.Accepted:
            return

        painter = QPainter()
        painter.begin(printer)

        rows = self.model.rowCount(QModelIndex())
        columns = self.model.columnCount(QModelIndex())
        sourceWidth = (columns + 1) * ItemSize
        sourceHeight = (rows + 1) * ItemSize

        painter.save()

        xscale = printer.pageRect(QPrinter.DevicePixel).width() / sourceWidth
        yscale = printer.pageRect(QPrinter.DevicePixel).height() / sourceHeight
        scale = min(xscale,yscale)

        painter.translate(
            printer.paperRect(QPrinter.DevicePixel).x() + printer.pageRect(QPrinter.DevicePixel).width() / 2,
            printer.paperRect(QPrinter.DevicePixel).y() + printer.pageRect(QPrinter.DevicePixel).height() / 2
        )

        painter.scale(scale, scale)
        painter.transtale(-sourceWidth/2, -sourceHeight/2)

        option = QStyleOptionViewItem()
        parent = QModelIndex()

        progress = QProgressDialog(self.tr("Printing..."), self.tr("Cancel"), 0, rows, self)
        progress.setWindowModality(Qt.ApplicationModal)
        y = ItemSize/2

        for row in range(rows):
            progress.setValue(row)
            QApplication.instance().processEvents()
            if  progress.wasCanceled():
                break

            x = ItemSize/2

            for col in range(columns):
                option.rect = QRect(x, y, ItemSize, ItemSize)

                self.view.itemDelegate().paint(painter, option, self.model.index(row, col, parent))

                x += ItemSize
            
            y += ItemSize
        
        progress.setValue(rows)

        painter.restore()
        painter.end()

        if progress.wasCanceled():
            information = QMessageBox(self, self.tr("Printing canceled"),
            self.tr("Printing process was cancelld"), QMessageBox.Cancel
            )

        

    @Slot()
    def showAboutBox(self) -> None:
        about = QMessageBox.About(self, self.tr("About the pixelator"),
        self.tr("This example demonstrates how a standart view and a custom delegate can be used to produced a specialized representation of in a simple custom model"))

    @Slot()
    def updateView(self) -> None:
        self.view.resizeColumnsToContents()
        self.view.resizeRowsToContents()
