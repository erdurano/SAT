import sys
import os
from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from parse import parse_SAT_doc


class Helper(QObject):
    @pyqtSlot(QUrl)
    def read_file(self, url):
        filename = url.toLocalFile()
        print(parse_SAT_doc(filename))


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
