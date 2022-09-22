import sys, os

from PyQt5 import QtGui, QtWidgets

from glassman_hv import HV_Gui


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle("ANL NEXT Lab Control System")
        # self.setStyleSheet("background:white")
        layout = QtWidgets.QHBoxLayout()

        self.hv_gui = HV_Gui()

        layout.addWidget(self.hv_gui)

        self.setLayout(layout)


        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
