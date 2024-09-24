import sys

from PySide2 import QtCore, QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("test app")

        label = QtWidgets.QLabel(self)
        label.setFixedWidth(100)
        label.setStyleSheet("background-color: rgb(200, 50, 8)")

        lineedit = QtWidgets.QLineEdit()
        lineedit.setFixedWidth(180)

        button = QtWidgets.QPushButton("Fixed Button size!")
        button.setFixedSize(110, 25)
        button.setStyleSheet(
            """
        background-color: #4CAF50;
        border: none;
        color: white;
        text-align: center;
        font-size: 12px;
        font-family: Arial
        """
        )

        widget = QtWidgets.QLabel()
        widget.setFixedSize(180, 180)
        widget.setStyleSheet("background-color: rgb(250, 255, 250)")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        right_container = QtWidgets.QWidget()

        bottom_widget = QtWidgets.QWidget()
        bottom_widget.setContentsMargins(0, 0, 0, 0)
        bottom_widget.setFixedWidth(180)
        hlay2 = QtWidgets
        hlay2.setContentsMargins(0, 0, 0, 0)
        hlay2.addStretch()
        hlay2.addWidget(button)

        glay = QtWidgets
        glay.addWidget(QtWidgets.QWidget(), 0, 0, 5, 1)
        glay.addWidget(lineedit, 0, 1)
        glay.addWidget(QtWidgets.QWidget(), 1, 1)
        glay.addWidget(widget, 2, 1, QtCore.Qt.AlignCenter)
        glay.addWidget(QtWidgets.QWidget(), 3, 1)
        glay.addWidget(QtWidgets.QWidget(), 0, 2, 5, 1)
        glay.addWidget(bottom_widget, 4, 1)

        hlay = QtWidgets
        hlay.setContentsMargins(0, 0, 0, 0)
        hlay.addWidget(label)
        hlay.addWidget(right_container)


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
