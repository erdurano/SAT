from PySide2.QtWidgets import QAbstractItemDelegate


class TestItemDelegate(QAbstractItemDelegate):
    """A delegate to show test items in listview in qt side"""

    def __init__(self) -> None:
        super().__init__()
