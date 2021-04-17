import sys
import os
from PySide2.QtCore import QObject, QUrl, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from parse import parse_SAT_doc
from schedule import Schedule


class Helper(QObject):
    @Slot(QUrl)
    def read_file(self, url):
        filename = url.toLocalFile()
        active_schedule = Schedule(parse_SAT_doc(filename))
        for items in active_schedule.completedItems:
            print(items.item_name)
        print(len(active_schedule.completedItems))
    # TODO: write a elper method for setting texts and positioning
    # them


def run():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))
    engine.quit.connect(app.quit)
    helper = Helper()
    engine.rootContext().setContextProperty("helper", helper)

    if not engine.rootObjects():
        sys.exit(-1)

    return app.exec_()


if __name__ == "__main__":

    sys.exit(run())
