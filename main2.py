import sys
import os
from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from parse import parse_SAT_doc
from schedule import Schedule


class Helper(QObject):
    @pyqtSlot(QUrl)
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
    engine.load(os.path.join(os.path.dirname(__file__), "qml/Dash.qml"))
    engine.quit.connect(app.quit)
    helper = Helper()
    engine.rootContext().setContextProperty("helper", helper)

    if not engine.rootObjects():
        sys.exit(-1)

    return app.exec_()


if __name__ == "__main__":

    sys.exit(run())
