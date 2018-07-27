
"""
=============================================================================
Name of Software: jobCrawler
Author: Abhi Kapoor and Sultan Sidhu
Date: July 25th, 2018
USE OF PYTHON 3.6 OR HIGHER IS RECOMMENDED
=============================================================================
"""

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *
from PyQt5.QtGui import QIcon, QPixmap
import JobCrawlerMain

class WelcomeWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """
        Initializes a new MainWindow object, and creates the display screen
        """

        super(WelcomeWindow, self).__init__()
        self.setGeometry(50,50,700,400)
        self.setWindowTitle("pyWeather - Enter City and Units")

        label2 = QtWidgets.QLabel(self)
        label2.setGeometry(0,0,700,400)
        label2.setPixmap(QPixmap("background.jpg"))

        lblLogo = QtWidgets.QLabel(self)
        lblLogo.setGeometry(55,2,300,70)
        lblLogo.setPixmap(QPixmap("logo.png"))

        self.city_entry = QtWidgets.QLineEdit(self)
        self.city_entry.setGeometry(5,370,350,20)

        font = QtGui.QFont()
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(12)

        lblCopyrightInfo = QtWidgets.QLabel("© Copyright Sultan Sidhu and Abhi Kapoor 2018", self)
        lblCopyrightInfo.setGeometry(405, 0, 300, 30)
        lblCopyrightInfo.setFont(font)

        self.lbl_enter_city = QtWidgets.QLabel(self)
        self.lbl_enter_city.setText("Enter a City: ")
        self.lbl_enter_city.setGeometry(5,342,350,25)
        self.lbl_enter_city.setFont(font)

        button_new = QtWidgets.QPushButton("Search", self)
        button_new.setGeometry(360,362,100,38)
        button_new.clicked.connect(self.display_options)

        self.show()


    def display_options(self):
        """
        This method saves the user-entered city and launches the new screen, which displays the
        job fields and connects to the internet
        :return: None
        """

        city = self.city_entry.text().strip()
        self.city_entry.setText("")

        self.screen2 = JobCrawlerMain.MainWindow(city)
        self.screen2.show()
        self.screen2.setWindowTitle("JobCrawler - Home")
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = WelcomeWindow()

    sys.exit(app.exec_())
