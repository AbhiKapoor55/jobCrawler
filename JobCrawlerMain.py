
"""
=============================================================
Name of Software: jobCrawler
Author: Abhi Kapoor and Sultan Sidhu
Date: July 25th, 2018
USE OF PYTHON 3.6 OR HIGHER IS RECOMMENDED
=============================================================
"""

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *
from PyQt5.QtGui import QIcon, QPixmap
import requests
from bs4 import BeautifulSoup
import random


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, city):
        """
        Initializes a new MainWindow object, and creates the display screen
        """

        super(MainWindow, self).__init__()
        self.setGeometry(50,50,700,400)
        self.setWindowTitle("pyWeather - Enter City and Units")

        self.city = city

        label2 = QtWidgets.QLabel(self)
        label2.setGeometry(0,0,700,400)
        label2.setPixmap(QPixmap("background.jpg"))

        lblLogo = QtWidgets.QLabel(self)
        lblLogo.setGeometry(55, 2, 300, 70)
        lblLogo.setPixmap(QPixmap("logo.png"))

        self.opts_lbl = QtWidgets.QLabel(self)
        self.opts_lbl.setGeometry(55, 0, 700, 400)

        self.logOutput = QtWidgets.QTextEdit(self)
        self.logOutput.setGeometry(25,70,640,270)
        self.logOutput.setVisible(False)

        self.city_entry = QtWidgets.QLineEdit(self)
        self.city_entry.setGeometry(5,370,350,20)

        self.new = QtWidgets.QLineEdit(self)
        self.new.setGeometry(5,370,350,20)
        self.new.setVisible(False)

        self.font = QtGui.QFont()
        self.font.setItalic(True)
        self.font.setBold(True)
        self.font.setPointSize(12)

        lblCopyrightInfo = QtWidgets.QLabel("© Copyright Sultan Sidhu and Abhi Kapoor 2018", self)
        lblCopyrightInfo.setGeometry(405, 0, 300, 30)
        lblCopyrightInfo.setFont(self.font)

        self.lbl_enter_city = QtWidgets.QLabel(self)
        self.lbl_enter_city.setText("Choose a Job Field from Above: ")
        self.lbl_enter_city.setGeometry(5,342,350,25)
        self.lbl_enter_city.setFont(self.font)

        button_new = QtWidgets.QPushButton("Search", self)
        button_new.setGeometry(360,362,100,38)
        button_new.clicked.connect(self.connect)
        self._display_job_fields()

        self.show()


    def _display_job_fields(self):
        """
        This function displays all the possible job fields on the GUI in a visually appealing fashion
        :return: None
        """

        lst = ['engineering and architecture', 'software', 'accounting', 'finance', 'administration', 'office',
                'art', 'media', 'design', 'biotech', 'science', 'business', 'management', 'customer service', 'hr',
                'education', 'miscellaneous', 'food', 'hospitality', 'general', 'labour', 'government']
        str = ""
        for x in range(len(lst)):
            if x % 4 == 0:
                str += lst[x]+"\n\n"
            else:
                str += random.choice([2,3,4]) * "   " +lst[x]+ "   " * random.choice([2,3,4,5,6,7,8,9])

        rfont = QtGui.QFont()
        rfont.setItalic(True)
        rfont.setBold(True)
        rfont.setPointSize(14)

        self.opts_lbl.setText(str)
        self.opts_lbl.setFont(rfont)


    def _jobchecker(self, choice: str):
        """
        This function takes the user-entered job choice and returns the code word related to that job choice.
        The code word is then used in forming the URL
        :param choice: str
        :return: None
        """

        if choice == 'engineering and architecture':
            return 'egr'
        elif choice == 'software':
            return 'sof'
        elif choice == "accounting" or "finance":
            return "acc"
        elif choice == "administration" or "admin" or "office":
            return "ofc"
        elif choice == "art" or "media" or "design":
            return "med"
        elif choice == "biotech" or "science":
            return "sci"
        elif choice == "business" or "management":
            return "bus"
        elif choice == "customer service" or "hr":
            return "csr"
        elif choice == "education" or "teaching":
            return "edu"
        elif choice == "miscellaneous":
            return "etc"
        elif choice == "food" or "hospitality":
            return "fbh"
        elif choice == "general" or "labour" or "general labour":
            return "lab"
        elif choice == "government":
            return "gov"
        else:
            raise Exception("invalid job choice entered.")


    def connect(self):
        """
        This function connects to the Craigslist website using the BeautifulSoup library
        and extracts useful information from it
        :return: None
        """

        job_choice = self.city_entry.text().lower()
        job_code = self._jobchecker(job_choice)
        url = "http://" + str(self.city) + ".craigslist.org/search/" + str(job_code)

        self.lbl_enter_city.setText("CONNECTING.....")
        self.lbl_enter_city.setFont(self.font)
        self.lbl_enter_city.repaint()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        soup.prettify()
        dictionary = {"class": "result-title hdrlnk"}
        answer = soup.find_all('a', attrs=dictionary)
        names = []
        links = []
        for thing in answer:
            names.append(thing.string)
            links.append(thing.attrs["href"])

        self.display_answer(names, links)


    def display_answer(self, names, links):
        """
        Displays the links and the names of the jobs, found by parsing Craigslist
        :param names: List
        :param links: List
        :return: None
        """

        results = ""
        if len(names) == len(links):
            for i in range(len(names)):
                results += "\n"
                #print("\n")
                nameres = "Job: " + names[i]
                results + "\n"
                results += nameres
                #print(nameres)
                lnk = "URL: " + links[i]
                results += "\n"
                results += lnk
                #print(lnk)
                results += "\n\n"
                #print("\n\n\n")
                print(results)
                self.logOutput.setVisible(True)
                self.logOutput.setText(results)
                self.opts_lbl.setText("")
                self.lbl_enter_city.setText("CONNECTION SUCCESSFUL")
                self.lbl_enter_city.setFont(self.font)
                self.lbl_enter_city.repaint()

        else:
            raise Exception("Incompatible data")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = MainWindow()

    sys.exit(app.exec_())
