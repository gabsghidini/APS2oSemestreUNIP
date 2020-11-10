import loginPage
import welcomePage
import substancesDataList
import crewDataList
import sys

from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication( [] )
form = uic.loadUi("loginPage.ui")

def callLoginPage():
    loginPage.callLoginPage()
    form.close()    

def callSubstancesDataList():
    substancesDataList.callSubstancesDataList()
    form.close()

def callWelcomePage():
    welcomePage.callWelcomePage()
    form.close()

def callCrewDataList():
    crewDataList.callCrewDataList()
    form.close


