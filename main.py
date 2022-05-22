import datetime
from threading import Thread
from time import sleep
import var
import os
import sys
from selenium import webdriver
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import encodings.idna
from utils import update_config_json, export_data_to_csv
# from utils_2 import update_config_json, export_data_to_csv
import scraper

from pyautogui import confirm


print("App started....")


class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)


def set_icon(obj):
    try:
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        p = resource_path('icons/icon.png')
        obj.setWindowIcon(QtGui.QIcon(p))
    except Exception as e:
        print(e)


class myMainClass():
    def __init__(self):

        #  gui for Sales Navigator People &  Comapny Profile Scraper
        #     GUI.lineEdit_email.setText(var.email)
        #     GUI.lineEdit_password.setText(var.password)
        #     GUI.pushButton_login.clicked.connect(self.start)
        GUI.tabWidget.setCurrentIndex(0)
        GUI.tabWidget.currentChanged.connect(self.current_tab_no)

        GUI.spinBox_speed.valueChanged.connect(self.update_speed)
        GUI.spinBox_try_count.valueChanged.connect(self.update_try_count)
        # GUI.checkBox_remember_me.stateChanged.connect(
        #     self.update_remember_me)

    # current_tab = GUI.tabWidget.currentIndex()

    # if(GUI.tabWidget.currentIndex() == 0):
        GUI.lineEdit_filename.setText(var.filename)
        GUI.lineEdit_delay.setText(str(var.delay))
        GUI.lineEdit_page_number.setText(str(var.page_number))
        GUI.spinBox_speed.setValue(var.scrolling_step)
        GUI.spinBox_try_count.setValue(var.try_count)
        GUI.pushButton_start.clicked.connect(self.start_scrap)
        GUI.pushButton_export.clicked.connect(self.export)
        GUI.pushButton_close.clicked.connect(self.stop)
        GUI.pause_btn.clicked.connect(self.pause_action)
        # selection one of the options of Tab 0 i.e. profile / company scrape
        GUI.people_option.clicked.connect(self.start_people_scrape)
        GUI.company_option.clicked.connect(self.start_company_scrape)

    # if(GUI.tabWidget.currentIndex() == 1):
        GUI.lineEdit_filename_2.setText(var.filename)
        GUI.lineEdit_delay_2.setText(str(var.delay))
        GUI.pushButton_export_2.clicked.connect(self.export)
        GUI.pushButton_start_2.clicked.connect(self.start_scrap)
        GUI.pushButton_close_2.clicked.connect(self.stop)
        GUI.browse.clicked.connect(self.browsefiles)
        GUI.pause_btn_2.clicked.connect(self.pause_action)

    # if(GUI.tabWidget.currentIndex() == 2):
        GUI.lineEdit_filename_3.setText(var.filename)
        GUI.lineEdit_delay_3.setText(str(var.delay))
        GUI.lineEdit_page_number_2.setText(str(var.page_number))
        GUI.pushButton_export_3.clicked.connect(self.export)
        GUI.pushButton_start_3.clicked.connect(self.start_scrap)
        GUI.pushButton_close_3.clicked.connect(self.stop)
        GUI.pause_btn_3.clicked.connect(self.pause_action)

    # if(GUI.tabWidget.currentIndex() == 3):
        GUI.lineEdit_filename_4.setText(var.filename)
        GUI.lineEdit_delay_4.setText(str(var.delay))
        GUI.browse_2.clicked.connect(self.browsefiles)
        GUI.pushButton_export_4.clicked.connect(self.export)
        GUI.pushButton_start_4.clicked.connect(self.start_scrap)
        GUI.pushButton_close_4.clicked.connect(self.stop)
        GUI.pause_btn_4.clicked.connect(self.pause_action)
        GUI.select_btn.clicked.connect(self.combo_select)

        GUI.connect_message.clicked.connect(self.connectMsg)
        GUI.only_connect.clicked.connect(self.onlyConnect)
        GUI.only_message.clicked.connect(self.onlyMsg)




        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)

    # input Xlsx File Logic:
    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            None, "Open File", "", "XLSX files (*.xlsx)")
        current_tab = GUI.tabWidget.currentIndex()
        if(current_tab == 1):
            GUI.filename.setText(fname[0])
            var.file_path = (fname[0])
            print(var.file_path)
        if(current_tab == 3):
            GUI.filename_2.setText(fname[0])
            var.file_path = (fname[0])
            print(var.file_path)
    
    # account-type selection & "function" selection for "connect & message" bot
    def combo_select(self):
        var.acc_select = GUI.comboX.currentText()
    
    def connectMsg(self):
        var.option_type_2 = 1

    def onlyConnect(self):
        var.option_type_2 = 2

    def onlyMsg(self):
        var.option_type_2 = 3
    # ...............................................
    
    def pause_action(self):
        var.pause_option = True

    def update_try_count(self):
        print("try count : {}".format(GUI.spinBox_try_count.value()))
        var.try_count = GUI.spinBox_try_count.value()

    def update_speed(self):
        print("speed : {}".format(GUI.spinBox_speed.value()))
        var.scrolling_step = GUI.spinBox_speed.value()

    def update_label(self):
        text = "Remaining: {} | Profile: {} | Total Profile: {}".format(
            var.remaining_page, var.profile_count, len(var.scrap_data))
        if( var.current_tab == 0):    
            GUI.label_status.setText(text)
        if(var.current_tab == 1):
            GUI.label_status_2.setText(text)
        if(var.current_tab == 2):
            GUI.label_status_3.setText(text)
        if( var.current_tab == 3): 
            GUI.label_status_4.setText(text)



    def start_people_scrape(self):
        var.initial_option = var.option_type or 0
        var.option_type = 1
        print("choosen option: People's Profile Scraping")

    def start_company_scrape(self):
        var.initial_option = var.option_type or 0
        var.option_type = 2
        print("choosen option: Comapny's Profile Scraping")
    
    def current_tab_no(self):
        current_tab = GUI.tabWidget.currentIndex()
        # var.current_tab = current_tab
        print("current tab", current_tab)

        


    def start(self):
        self.validation()
        update_config_json()
        if not var.status:
            var.status = True
            var.stop = False
            Thread(target=scraper.run, daemon=True).start()

        
    def start_scrap(self):
        current_tab = GUI.tabWidget.currentIndex()
        if not (current_tab == var.current_tab):
            var.current_tab = current_tab
            var.scrap_data = []

        self.validation()
        update_config_json()
      

        # making sure that the User selects one of the options before starting
         # for Tab no. 0  i.e.  profile scrape or company scrape
        if (current_tab == 0):
            choosen_option = var.option_type
            if not (choosen_option == 1 or choosen_option == 2):
                confirm_return = confirm(text='Please Select one of the options\nBefore Starting',
                                        title='Confirm', buttons=['person scraper', 'comapany scraper'])
                if confirm_return == "person scraper":
                    GUI.people_option.setChecked(True)
                    GUI.company_option.setChecked(False)
                    self.start_people_scrape()
                if confirm_return == "comapany scraper":
                    GUI.people_option.setChecked(True)
                    GUI.company_option.setChecked(True)
                    self.start_company_scrape()

        elif(current_tab == 3):
            # for Tab no. 3  i.e. connect & message
            choosen_option_2 = var.option_type_2
            choosen_acc = var.acc_select
            if not (choosen_option_2 == 1 or choosen_option_2 == 2 or choosen_option_2 == 3):
                confirm_return = confirm(text='Please Select one of the options\n\nOnly After Selecting Press The Button bellow',
                                         title='Confirm', buttons=['I Have Selected, Now Start'])
                if confirm_return == "I understand":
                    pass
            
                
            elif not (choosen_acc == 'Normal' or choosen_acc == 'Sales_Navigator'):
                confirm_return = confirm(text='Please Select your Account Type\n\nOnly After Selecting Press The Button bellow',
                                         title='Confirm', buttons=['I Have Selected, Now Start'])
                if confirm_return == "I Have Selected Now Start":
                    pass
                    
                    

        # confirmation code to  Keep th Old data or not . 
            #   for Tab = 0
        if (current_tab == 0): 
            if not (var.initial_option == var.option_type or var.initial_option == 0):
                confirm_return = confirm(text='You have changed the selected Option...\n',
                                        title='Confirm', buttons=['I Understand'])
                if confirm_return == "I Understand":
                    var.initial_option = choosen_option
                    var.status = True
                    var.scarp_start = False
                    var.stop = False
                    var.scrap_data = []

            else:
                var.status = True
                var.stop = False
                if var.status == True and var.scarp_start == False:
                    if len(var.scrap_data) > 0:
                        confirm_return = confirm(text='Do you want to keep data\'s from previous scrap?',
                                            title='Confirm', buttons=['yes', 'no'])
                    
                        if confirm_return == "yes":
                            pass
                        else:
                            var.scrap_data = []
                
                
                var.scarp_start = True

            #   for all the rest of the tabs
        else:
            if var.status == True and var.scarp_start == False:
                if len(var.scrap_data) > 0:
                        confirm_return = confirm(text='Do you want to keep data\'s from previous scrap?',
                                                title='Confirm', buttons=['yes', 'no'])

                        if confirm_return == "yes":
                            pass
                        else:
                            var.scrap_data = []
                var.scarp_start = True

        

    def stop(self):
        var.stop = True

    def export(self):

        dialog = QFileDialog()
        dialog.setDirectory(var.directory)
        csvPath = dialog.getExistingDirectory(None, "File saving window")
        if csvPath:
            print(csvPath)
            var.directory = csvPath
            self.validation()
            update_config_json()
            print("Total Data : {}".format(len(var.scrap_data)))
            Thread(target=export_data_to_csv, daemon=True).start()
        else:
            print("Exporting Cancelled")

    def update_remember_me(self, checked):
        if checked:
            var.remember_me = True
        else:
            var.remember_me = False
        print("Remember me : {}".format(var.remember_me))

    def validation(self):

        if GUI.lineEdit_email.text():
            var.email = GUI.lineEdit_email.text()
        else:
            GUI.lineEdit_email.setText(var.email)

        if GUI.lineEdit_password.text():
            var.password = GUI.lineEdit_password.text()
        else:
            GUI.lineEdit_password.setText(var.password)

        current_tab = GUI.tabWidget.currentIndex()

        if GUI.lineEdit_delay.text() and GUI.lineEdit_delay.text().isnumeric():
            if(var.current_tab == 0):
                var.delay = int(GUI.lineEdit_delay.text())
            if(var.current_tab == 1):
                var.delay = int(GUI.lineEdit_delay_2.text())
            if(var.current_tab == 2):
                var.delay = int(GUI.lineEdit_delay_3.text())
            if(var.current_tab == 3):
                var.delay = int(GUI.lineEdit_delay_4.text())
        else:
            if(var.current_tab == 0):
                var.delay = int(GUI.lineEdit_delay.setText(str(var.delay)))
            if(var.current_tab == 1):
                var.delay = int(GUI.lineEdit_delay_2.setText(str(var.delay)))
            if(var.current_tab == 2):
                var.delay = int(GUI.lineEdit_delay_3.setText(str(var.delay)))
            if(var.current_tab == 3):
                var.delay = int(GUI.lineEdit_delay_4.setText(str(var.delay)))


        if(var.current_tab == 0):
            if GUI.lineEdit_page_number.text() and GUI.lineEdit_page_number.text().isnumeric():
                var.page_number = int(GUI.lineEdit_page_number.text())
            else:
                GUI.lineEdit_page_number.setText(str(var.page_number))
        
        if(var.current_tab == 2):
            if GUI.lineEdit_page_number_2.text() and GUI.lineEdit_page_number_2.text().isnumeric():
                var.page_number = int(GUI.lineEdit_page_number_2.text())
            else:
                GUI.lineEdit_page_number.setText(str(var.page_number))

        if(var.current_tab == 0):
            if GUI.lineEdit_filename.text():
                var.filename = GUI.lineEdit_filename.text()
            else:
                GUI.lineEdit_filename.setText(var.filename)
        if(var.current_tab == 1):
            if GUI.lineEdit_filename_2.text():
                var.filename = GUI.lineEdit_filename_2.text()
            else:
                GUI.lineEdit_filename_2.setText(var.filename)
        if(var.current_tab == 2):
            if GUI.lineEdit_filename_3.text():
                var.filename = GUI.lineEdit_filename_3.text()
            else:
                GUI.lineEdit_filename_3.setText(var.filename)
        if(var.current_tab == 3):
            if GUI.lineEdit_filename_4.text():
                var.filename = GUI.lineEdit_filename_4.text()
            else:
                GUI.lineEdit_filename_4.setText(var.filename)

        # print("Config {0} {1} {2} {3} {4}".format(
        #     var.email, var.password, var.delay, var.page_number, var.filename))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    set_icon(mainWindow)

    mainWindow.setWindowFlags(mainWindow.windowFlags(
    ) | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowSystemMenuHint)

    GUI = MyGui(mainWindow)
    # mainWindow.showMaximized()
    mainWindow.show()

    myMC = myMainClass()

    app.exec_()
    print("Exit")
    sys.exit()
