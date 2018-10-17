from PyQt5 import QtWidgets
import sys

from src.main_view import MainView


if __name__ == "__main__":
    qt_app = QtWidgets.QApplication(sys.argv)
    main_window = MainView()
    main_window.show()
    sys.exit(qt_app.exec_())
