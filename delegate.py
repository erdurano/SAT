from PySide2.QtWidgets import QStyledItemDelegate


class TestItemDelegate(QStyledItemDelegate):
    """A delegate to show test items in listview in qt side"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
