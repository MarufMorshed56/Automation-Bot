# import collections
import profile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# import clipboard
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow


import time
from threading import Thread
import var
import shutil
from pyautogui import alert, write, press, confirm


from profile_scraper import profile_scrape
from company_scraper import comapny_scrape
from updater import update
from job_scraper import job_scrape
from connect_message import connect_msg_bot


class Scraper():
    def __init__(self):
        self.email = var.email
        self.password = var.password
        Thread(target=self.stop, daemon=True).start()

    def run(self):
        try:
            # login handle
            """ There was three case in total here.
            1. Remember me : true
            2. Remember me : true different account
            3. Remember me : false """

            if var.remember_me:
                chrome_options = Options()
                try:
                    chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                except:
                    chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                chrome_options.add_argument("user-data-dir=selenium")

                if self.email == var.cookies_of:

                    var.driver = self.driver = webdriver.Chrome(
                        executable_path='chromedriver.exe', chrome_options=chrome_options)
                    # changed this line from => executable_path='chromedriver', chrome_options=chrome_options)
                    self.driver.get(var.primary_link)
                    try:
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(
                                (By.ID, "global-typeahead-search-input")))
                        self.driver.find_element_by_id(
                            "global-typeahead-search-input")

                    except:
                        print("Logging in....")
                        self.login()

                else:
                    try:
                        shutil.rmtree("selenium")
                    except:
                        print("Can't delete")
                    chrome_options = Options()
                    try:
                        chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                    except:
                        chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                    a = self.driver = webdriver.Chrome(
                        executable_path='chromedriver', chrome_options=chrome_options)
                    self.login()

                var.cookies_of = self.email

            else:
                chrome_options = Options()
                chrome_options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                var.driver = self.driver = webdriver.Chrome(
                    executable_path='chromedriver.exe', chrome_options=chrome_options)
                # changed this line from => self.driver = webdriver.Chrome(executable_path='chromedriver')
                self.login()

            var.driver = self.driver
            # wait till start button is pushed
            # while var.status == True:
            #     sleep(1)

            # var.status = True
            # self.scrap()
            print("Login Done ...")
        except Exception as e:
            print("Exeception occured at scraper init :{}".format(e))
            var.status = False
            var.stop = True

        # finally:
        #     print("closing the thread")

    def login(self):
        self.driver.get(var.primary_link)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "body")))
        # print("1")
        time.sleep(2)

        self.driver.find_element_by_tag_name("body").send_keys(
            Keys.TAB + self.email + Keys.TAB + self.password + Keys.ENTER)
        # email_field = self.driver.find_element_by_id("username")
        # print("3")
        # email_field.send_keys(Keys.TAB + self.email + Keys.TAB + self.password + Keys.ENTER)

        time.sleep(1)

    def scrap(self):
        if(var.current_tab == 0):
            choosen_option = var.option_type

            if(choosen_option == 1):
                print("choosen option: 1")
                profile_scrape().scrap()
            elif(choosen_option == 2):
                print("choosen option: 2")
                comapny_scrape().scrap()

        elif(var.current_tab == 1):
            update().scrap()

        elif(var.current_tab == 2):
            job_scrape().scrap()

        elif(var.current_tab == 3):
            connect_msg_bot().scrap()

    def stop(self):
        while True:
            time.sleep(1)
            if var.stop == True:
                try:
                    var.status = False
                    self.driver.quit()
                    print("Process : Closing the browser")
                except Exception as e:
                    print("Exeception occured at stop : {} ".format(e))
                finally:
                    break


def run():
    #   if(var.option_type == 1):
    scraper = Scraper()
    scraper.run()
    while var.status == True:
        time.sleep(1)
        if var.scarp_start == True:
            scraper.scrap()
            print("out of scrap func")
    var.status = False
    var.scarp_start = False
    print("Closing the thread")
# def scrap():
#     scraper = Scraper()
#     scraper.scrap()


if __name__ == "__main__":
    pass
