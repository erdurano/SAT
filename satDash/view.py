from typing import List, Optional

from PySide6.QtCore import QItemSelectionModel, QModelIndex, Slot
from PySide6.QtWidgets import QListView, QStyledItemDelegate, QWidget


class ScheduleView(QListView):

    def __init__(self, parent: Optional[QWidget]) -> None:
        super().__init__(parent=parent)

        self.setVerticalScrollMode(
            self.ScrollPerPixel
        )

        self.setSelectionMode(self.ExtendedSelection)
        self.setSelectionRectVisible(True)

    def commitData(self, editor: QWidget) -> None:
        # Holds the view from updating the model when exiting the item
        # else passes the commitData slot
        if type(self.sender()) == QItemSelectionModel or\
                type(self.sender()) is None:
            return None
        else:
            return super().commitData(editor)

    def closeEditor(self,
                    editor: QWidget,
                    hint: QStyledItemDelegate.EndEditHint) -> None:
        if hint == QStyledItemDelegate.SubmitModelCache:
            self.commitData(editor)
        elif hint == QStyledItemDelegate.RevertModelCache:
            pass
        super().closeEditor(editor, hint)

    def getSelected(self) -> List[QModelIndex]:
        return self.selectionModel().selectedRows()

    @Slot()
    def newItem(self):
        end = self.model().sourceModel().rowCount()
        self.model().sourceModel().insertRow(end)
        self.edit(self.model().index(end, 0))

    @Slot()
    def deleteSelected(self):
        rows_to_del = self.getSelected()
        rows_to_del.sort(key=QModelIndex.row)
        for index in rows_to_del[::-1]:
            ind_to_del = self.model().mapToSource(index)
            self.model().sourceModel().removeRow(ind_to_del.row())
