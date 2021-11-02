from typing import List, Optional

from PySide2.QtCore import QItemSelectionModel, QModelIndex
from PySide2.QtWidgets import QListView, QStyledItemDelegate, QWidget


class ScheduleView(QListView):

    def __init__(self, parent: Optional[QWidget]) -> None:
        super().__init__(parent=parent)
        self.setSpacing(1)

        self.setVerticalScrollMode(
            self.ScrollPerPixel
        )
        self.setSelectionMode(self.ExtendedSelection)

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
