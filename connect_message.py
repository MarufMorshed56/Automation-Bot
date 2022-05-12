# import collections
from cgitb import text
import csv
import pandas as pd
from gettext import find
from glob import escape
from lib2to3.pgen2 import driver
from select import select
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# import clipboard
import os
import time 
from threading import Thread
import var
import shutil
from pyautogui import alert, write, press

class connect_msg_bot():
    def __init__(self):
        print("inside the Profile Info updater")


    def scrap(self):        
        name = []
        pro_link = []
        profile_open = []
        all_profile = []
        msg_status = []
        connect_status = []
        print("starting to scrape....")
        limit = var.page_number
        profile_count = 0
        var.remaining_page = limit
        var.profile_count = profile_count
        filepath = var.file_path
        choosen_option = var.option_type_2

        self.driver = var.driver
    
        delay_time = var.delay
        # count3 = 0

        acc_value = var.acc_select

        j = 0
        l = 0
        try:
                     # .csv format
            # with open(filepath,'r', errors='ignore') as csv_file:
            #     file = csv.reader(csv_file)
            #     for link in file:
            #         j+=1

                     # .xlsx format
                     
            #  counting the Number of rows
            file = pd.read_excel(r'{}'.format(filepath), engine='openpyxl')
            for k, rows in file.iterrows():
                j += 1
        except:
            print("")

        print("\n total number of Profiles to be Scrapped: {}".format(j))

            
        print("\n choosen account: {}".format(acc_value))
        if(choosen_option == 1):
            print("\n Choosen Connect & Message option \n")
        if(choosen_option == 2):
            print("\n Choosen Only Connect option \n")
        if(choosen_option == 3):
            print("\n Choosen Only Message option \n")

        print("........................................... \n ")
        print("\n ")


        # if(var.pause_option == True):
        #     var.pause_option = False
        #     os.system("pause")

        try:
            # with open(filepath,'r', errors='ignore') as csv_file:
            #     file = csv.reader(csv_file)
            
            file = pd.read_excel(r'{}'.format(filepath), engine='openpyxl')
                  
            self.driver.maximize_window()
            time.sleep(1)
                # print(delay_time)
                
            for z, link in file.iterrows():
                    if var.stop == True:
                            break
                #   if(l<1):
                #       l += 1
                #       print("\n Row No: {} \n".format(l))
                #       print("\n")
                #       print("Reading Header Column")
                #       print("\n ............................. \n \n \n")
                #   else:
                    
                    # if( l == 3):
                    #     break

                    l += 1
                    print("Row No: {} \n".format(l))
                    print("\n")

                    name_value = link[0]
                    name.append(name_value)

                    profile_link = link[4]
                    pro_link.append(profile_link)
                    # Getting into each profile link
                    self.driver.get(profile_link)

                    profile_count += 1
                    var.profile_count = profile_count
                    var.remaining_page = (j - (profile_count))  

                    time.sleep(3)
                    
                    if(var.pause_option == True):
                        var.pause_option = False
                        print("\n Program Paused \n")
                        os.system("pause")

                
                    try:
                        if(acc_value == "Normal"):
                            if(choosen_option == 1):
                                # print("accessed Connect & Message option")

                             #  trying Connect..............................................

                                try:
                                    try:
                                        try:
                                            btn = self.driver.find_element_by_class_name("artdeco-button--primary").get_attribute("innerHTML")     
                                            new_value = btn.split("<")[-2]
                                            value = new_value.split(">")[1]
                                            final_value=value.strip()
                                            
                                            # checking if Connect Btn is there or not
                                            if(final_value == 'Connect'):
                                                

                                                # print("found connect btn div")

                                                # time.sleep(0.5)
                                                
                                                connect_btn = self.driver.find_element_by_css_selector('button[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view pvs-profile-actions__action"]')
                                                
                                                # time.sleep(2)
                                                
                                                self.driver.execute_script("arguments[0].click();",connect_btn)
                                                
                                                
                                                time.sleep(0.5)
                            
                                                # print("clicked connect btn")
                                                
                                                add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                                add_note_btn.click()

                                                time.sleep(0.5)

                                                # print("clicked add note btn")
                                                
                                                msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                                # msg = "Hello " + link[0] + link[7]
                                                # msg_area.send_keys(link[8])
                                                text = link[8]
                                                for character in text:
                                                    msg_area.send_keys(character)
                                                    time.sleep(0.01) 

                                                time.sleep(0.5)

                                                if(var.pause_option == True):
                                                    print("\n Program Paused \n")
                                                    var.pause_option = False
                                                    os.system("pause")

                                                send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                                self.driver.execute_script("arguments[0].click();",send_btn)
                                                # send_btn.click()
                                                print("Sent Connect Request to {}".format(link[0]))
                                                connect_status.append('sent')
                                                time.sleep(1)
                                            else:
                                                # checking for follow btn. if available then go inside more_btn
                                                
                                                # time.sleep(2)
                                            
                                                more_btn = self.driver.find_element_by_css_selector('button[aria-label="More actions"]')

                                                # time.sleep(0.5)
                                
                                                self.driver.execute_script("arguments[0].click();",more_btn)

                                                time.sleep(0.5)
                                                
                                                # print("clicked more btn")

                                                divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')

                                                i = 1
                                                for div in divs:
                                                    if(i == 3):
                                                        self.driver.execute_script("arguments[0].click();",div)
                                                        # print(div.get_attribute("innerHTML"))
                                                        # print("break")
                                                        break
                                                    i += 1


                                                # print("clicked connect option btn")

                                                time.sleep(0.5)

                                                connect_btn = self.driver.find_element_by_css_selector('button[aria-label="Connect"]')
                                                connect_btn.click()
                                                add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                                add_note_btn.click()

                                                time.sleep(0.5)
                                                
                                                msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                                # msg = "Hello " + link[0] + link[7]
                                                # msg_area.send_keys(link[8])
                                                text = link[8]
                                                for character in text:
                                                    msg_area.send_keys(character)
                                                    time.sleep(0.01)

                                                time.sleep(0.5)

                                                if(var.pause_option == True):
                                                    print("\n Program Paused \n")
                                                    var.pause_option = False
                                                    os.system("pause")

                                                send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                                self.driver.execute_script("arguments[0].click();",send_btn)
                                                # send_btn.click()
                                                # print("found send_btn")
                                                print("Sent Connect Request to {}".format(link[0]))
                                                connect_status.append('sent')

                                                time.sleep(1)

                                        except Exception as e:
                                                    more_btn = self.driver.find_element_by_css_selector('button[aria-label="More actions"]')

                                                    # time.sleep(0.5)
                                    
                                                    self.driver.execute_script("arguments[0].click();",more_btn)

                                                    time.sleep(0.5)
                                                    
                                                    

                                                    divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')
                                                    
                                                    # i = 1
                                                    for div in divs:
                                                        value = div.text 
                                                        nv = (value.split(" ")[0])
                                                        nvv = (nv[0])
                                                        # print(nvv)
                                                        # print(".......")
                                                        if(nvv == "C"):
                                                            self.driver.execute_script("arguments[0].click();",div)
                                                            # print(div.get_attribute("innerHTML"))
                                                            # print("break")
                                                            break
                                                    

                                                    # print("clicked connect option btn")
                                                    time.sleep(0.5)


                                                    # print("clicked connect option btn")

                                                    time.sleep(0.5)

                                                    connect_btn = self.driver.find_element_by_css_selector('button[aria-label="Connect"]')
                                                    connect_btn.click()
                                                    add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                                    add_note_btn.click()

                                                    time.sleep(0.5)
                                                    
                                                    msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                                    # msg = "Hello " + link[0] + link[7]
                                                    # msg_area.send_keys(link[8])
                                                    text = link[8]
                                                    for character in text:
                                                        msg_area.send_keys(character)
                                                        time.sleep(0.01)

                                                    time.sleep(0.5)

                                                    if(var.pause_option == True):
                                                        print("\n Program Paused \n")
                                                        var.pause_option = False
                                                        os.system("pause")

                                                    send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                                    self.driver.execute_script("arguments[0].click();",send_btn)
                                                    # send_btn.click()
                                                    # print("found send_btn")
                                                    print("Sent Connect Request to {}".format(link[0]))
                                                    connect_status.append('sent')

                                                    time.sleep(1)
                                        
                                    except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        connect_status.append('not sent')
                                        
                                except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        connect_status.append('not sent')

                             # Trying Messaging...............................................
                                
                                time.sleep(1)

                                try:
                                    # checking if profile is Locked Or Not
                                    lock_icon = self.driver.find_element_by_css_selector('li-icon[type="lock-icon"]')
                                    status = "Msg option is locked "
                                    print("Msg option is locked for {}".format(link[0]))
                                    msg_status.append("closed")
                                    time.sleep(delay_time)
                                except:
                                    try:
                                        msg_btn = self.driver.find_element_by_class_name('message-anywhere-button')
                                        # msg_btn.click()
                                        self.driver.execute_script("arguments[0].click();",msg_btn)

                                        # print("msg btn clicked")
                                        time.sleep(0.5)

                                        subject = self.driver.find_element_by_css_selector('input[placeholder="Subject (optional)"]')
                                        subject.send_keys(link[6])

                                        # print("subject added")

                                        time.sleep(0.5)

                                        text_area = self.driver.find_element_by_css_selector('div[aria-label="Write a message…"]')
                                        # text_area.send_keys(link[7])
                                        text = link[7]
                                        for character in text:
                                            text_area.send_keys(character)
                                            time.sleep(0.01)

                                        # print("msg body added")

                                        time.sleep(1)

                                        if(var.pause_option == True):
                                                var.pause_option = False
                                                print("\n Program Paused \n")
                                                os.system("pause")

                                        msg_send_btn = self.driver.find_element_by_class_name('msg-form__send-button')
                                        self.driver.execute_script("arguments[0].click();",msg_send_btn)
                                        # msg_send_btn.click()
                                        # print("msg sent ")
                                        msg_status.append("sent")
                                        print("Sent Message to {}".format(link[0]))
                                        time.sleep(delay_time)

                                    except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        msg_status.append("not sent")
                                        time.sleep(delay_time)

                            


                            if(choosen_option == 2):
                                # only connect
                                # print("accessed connect option")

                                # time.sleep(2)
                                try:
                                    try:
                                        try:
                                            btn = self.driver.find_element_by_class_name("artdeco-button--primary").get_attribute("innerHTML")     
                                            new_value = btn.split("<")[-2]
                                            value = new_value.split(">")[1]
                                            final_value=value.strip()
                                            
                                            # checking if Connect Btn is there or not
                                            if(final_value == 'Connect'):
                                                

                                                # print("found connect btn div")

                                                # time.sleep(0.5)
                                                
                                                connect_btn = self.driver.find_element_by_css_selector('button[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view pvs-profile-actions__action"]')
                                                
                                                # time.sleep(2)
                                                
                                                self.driver.execute_script("arguments[0].click();",connect_btn)
                                                
                                                
                                                time.sleep(0.5)
                            
                                                # print("clicked connect btn")
                                                
                                                add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                                add_note_btn.click()

                                                time.sleep(0.5)

                                                # print("clicked add note btn")
                                                
                                                msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                                # msg = "Hello " + link[0] + link[7]
                                                # msg_area.send_keys(link[8])
                                                text = link[8]
                                                for character in text:
                                                    msg_area.send_keys(character)
                                                    time.sleep(0.01)
                                                

                                                time.sleep(0.5)

                                                if(var.pause_option == True):
                                                    print("\n Program Paused \n")
                                                    var.pause_option = False
                                                    os.system("pause")

                                                send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                                self.driver.execute_script("arguments[0].click();",send_btn)
                                                # send_btn.click()
                                                print("Sent Connect Request to {}".format(link[0]))
                                                connect_status.append('sent')
                                                time.sleep(1)
                                            else:
                                                # checking for follow btn. if available then go inside more_btn
                                                
                                                # time.sleep(2)
                                            
                                                more_btn = self.driver.find_element_by_css_selector('button[aria-label="More actions"]')

                                                # time.sleep(0.5)
                                
                                                self.driver.execute_script("arguments[0].click();",more_btn)

                                                time.sleep(0.5)
                                                
                                                # print("clicked more btn")

                                                divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')

                                                i = 1
                                                for div in divs:
                                                    if(i == 3):
                                                        self.driver.execute_script("arguments[0].click();",div)
                                                        # print(div.get_attribute("innerHTML"))
                                                        # print("break")
                                                        break
                                                    i += 1


                                                # print("clicked connect option btn")

                                                time.sleep(0.5)

                                                connect_btn = self.driver.find_element_by_css_selector('button[aria-label="Connect"]')
                                                connect_btn.click()
                                                add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                                add_note_btn.click()

                                                time.sleep(0.5)
                                                
                                                msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                                # msg = "Hello " + link[0] + link[7]
                                                # msg_area.send_keys(link[8])
                                                text = link[8]
                                                for character in text:
                                                    msg_area.send_keys(character)
                                                    time.sleep(0.01)

                                                time.sleep(0.5)

                                                if(var.pause_option == True):
                                                    print("\n Program Paused \n")
                                                    var.pause_option = False
                                                    os.system("pause")

                                                send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                                self.driver.execute_script("arguments[0].click();",send_btn)
                                                # send_btn.click()
                                                # print("found send_btn")
                                                print("Sent Connect Request to {}".format(link[0]))
                                                connect_status.append('sent')

                                                time.sleep(1)

                                        except Exception as e:
                                                    more_btn = self.driver.find_element_by_css_selector('button[aria-label="More actions"]')

                                                    # time.sleep(0.5)
                                    
                                                    self.driver.execute_script("arguments[0].click();",more_btn)

                                                    time.sleep(0.5)
                                                    
                                                   
                                                    divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')
                                                    
                                                    # i = 1
                                                    for div in divs:
                                                        value = div.text 
                                                        nv = (value.split(" ")[0])
                                                        nvv = (nv[0])
                                                        # print(nvv)
                                                        # print(".......")
                                                        if(nvv == "C"):
                                                            self.driver.execute_script("arguments[0].click();",div)
                                                            # print(div.get_attribute("innerHTML"))
                                                            # print("break")
                                                            break
                                                    

                                                    # print("clicked connect option btn")
                                                    # time.sleep(0.5)


                                                    # print("clicked connect option btn")

                                                    time.sleep(0.5)

                                                    connect_btn = self.driver.find_element_by_css_selector('button[aria-label="Connect"]')
                                                    connect_btn.click()
                                                    add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                                    add_note_btn.click()

                                                    time.sleep(0.5)
                                                    
                                                    msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                                    # msg = "Hello " + link[0] + link[7]
                                                    # msg_area.send_keys(link[8])
                                                    text = link[8]
                                                    for character in text:
                                                        msg_area.send_keys(character)
                                                        time.sleep(0.01)

                                                    time.sleep(0.5)

                                                    if(var.pause_option == True):
                                                        print("\n Program Paused \n")
                                                        var.pause_option = False
                                                        os.system("pause")

                                                    send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                                    self.driver.execute_script("arguments[0].click();",send_btn)
                                                    # send_btn.click()
                                                    # print("found send_btn")
                                                    print("Sent Connect Request to {}".format(link[0]))
                                                    connect_status.append('sent')

                                                    time.sleep(1)
                                        
                                    except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        connect_status.append('not sent')
                                        time.sleep(delay_time)
                                        
                                except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        connect_status.append('not sent')
                                        time.sleep(delay_time)


                            if(choosen_option == 3):
                                # only msg
                                try:
                                    # checking if profile is Locked Or Not
                                    lock_icon = self.driver.find_element_by_css_selector('li-icon[type="lock-icon"]')
                                    status = "Msg option is locked "
                                    print("Msg option is locked for {}".format(link[0]))
                                    msg_status.append("closed")
                                    time.sleep(delay_time)
                                except:
                                    try:
                                        msg_btn = self.driver.find_element_by_class_name('message-anywhere-button')
                                        # msg_btn.click()
                                        self.driver.execute_script("arguments[0].click();",msg_btn)

                                        # print("msg btn clicked")
                                        time.sleep(0.5)

                                        subject = self.driver.find_element_by_css_selector('input[placeholder="Subject (optional)"]')
                                        subject.send_keys(link[6])

                                        # print("subject added")

                                        time.sleep(0.5)

                                        text_area = self.driver.find_element_by_css_selector('div[aria-label="Write a message…"]')
                                        # text_area.send_keys(link[7])
                                        text = link[7]
                                        for character in text:
                                            text_area.send_keys(character)
                                            time.sleep(0.01) 
                                        # pause for 0.3 seconds

                                        # print("msg body added")

                                        time.sleep(1)

                                        if(var.pause_option == True):
                                                var.pause_option = False
                                                print("\n Program Paused \n")
                                                os.system("pause")

                                        msg_send_btn = self.driver.find_element_by_class_name('msg-form__send-button')
                                        self.driver.execute_script("arguments[0].click();",msg_send_btn)
                                        # msg_send_btn.click()
                                        # print("msg sent ")
                                        print("Sent Message to {}".format(link[0]))
                                        msg_status.append("sent")
                                        time.sleep(delay_time)
                                    except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        msg_status.append("not sent")
                                        time.sleep(delay_time)



                        #.......................... Salas Navigator Account......................




                        if(acc_value == "Sales_Navigator"):
                            # print("sales")

                            if(choosen_option == 1):
                                # print("accessed Connect & Message option")



                                # Trying connect Option
                        
                                
                                try:
                                    try:
                                        btn = self.driver.find_element_by_class_name("artdeco-button--primary").get_attribute("innerHTML")     

                                        new_value = btn.split("<")[-2]
                                        value = new_value.split(">")[1]
                                        final_value=value.strip()
                                        # print("first value {}".format(final_value))
                                        # print("got in")
                                        
                                        # checking Checking Connect at option 1
                                        if(final_value == 'Connect'):
                                            

                                            # print("found connect btn div")
                                            # time.sleep(0.5)
                                            
                                            connect_btn = self.driver.find_element_by_css_selector('button[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view pvs-profile-actions__action"]')
                                            
                                            # time.sleep(2)
                                            
                                            self.driver.execute_script("arguments[0].click();",connect_btn)
                                            
                                            # print("clicked connect btn")
                                            
                                            time.sleep(0.5)

                                            
                                            add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                            add_note_btn.click()

                                            # print("clicked add note btn")

                                            time.sleep(0.5)
                                            
                                            msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                            # msg = "Hello " + link[0] + link[7]
                                            # msg_area.send_keys(link[8])
                                            text = link[8]
                                            for character in text:
                                                msg_area.send_keys(character)
                                                time.sleep(0.01)

                                            time.sleep(1)

                                            if(var.pause_option == True):
                                                var.pause_option = False
                                                print("\n Program Paused \n")
                                                os.system("pause")

                                            send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                            self.driver.execute_script("arguments[0].click();",send_btn)
                                            # send_btn.click()
                                            # print("clicked send btn")
                                            print("Sent Connect Request to {}".format(link[0]))
                                            connect_status.append('sent')
                                            time.sleep(delay_time)
                                        else:
                                            # checking for follow btn. if available then go inside more_btn
                                            # print("got into else caause  connect not in position 1")
                                            more_btn = self.driver.find_element_by_css_selector('button[aria-label="More actions"]')

                                            # time.sleep(1)
                            
                                            self.driver.execute_script("arguments[0].click();",more_btn)

                                            # print("clicked more btn")
                                            
                                            time.sleep(0.5)

                                            # divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')
                                            
                                            
                                            divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')
                                            # i = 1
                                            for div in divs:
                                                value = div.text 
                                                nv = (value.split(" ")[0])
                                                nvv = (nv[0])
                                                # print(nvv)
                                                # print(".......")
                                                if(nvv == "C"):
                                                    self.driver.execute_script("arguments[0].click();",div)
                                                    # print(div.get_attribute("innerHTML"))
                                                    # print("break")
                                                    break
                                            

                                            # print("clicked connect option btn")
                                            time.sleep(0.5)

                                            connect_btn = self.driver.find_element_by_css_selector('button[aria-label="Connect"]')
                                            connect_btn.click()
                                            add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                            add_note_btn.click()

                                            time.sleep(0.5)
                                            
                                            msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                            # msg = "Hello " + link[0] + link[7]
                                            # msg_area.send_keys(link[8])
                                            text = link[8]
                                            for character in text:
                                                msg_area.send_keys(character)
                                                time.sleep(0.01)

                                            time.sleep(1)

                                            if(var.pause_option == True):
                                                var.pause_option = False
                                                print("\n Program Paused \n")
                                                os.system("pause")

                                            send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                            self.driver.execute_script("arguments[0].click();",send_btn)
                                            # send_btn.click()
                                            # print("found send_btn")
                                            print("Sent Connect Request to {}".format(link[0]))
                                            connect_status.append('sent')
                                            time.sleep(delay_time)
                                            
                                                

                                    except Exception as e:
                                        
                                        try:
                                            # print("went inside exception")
                                             # checking for follow btn. if available then go inside more_btn
                                            more_btn = self.driver.find_element_by_css_selector('button[aria-label="More actions"]')

                                            # time.sleep(1)
                            
                                            self.driver.execute_script("arguments[0].click();",more_btn)

                                            # print("clicked more btn")
                                            
                                            time.sleep(0.5)

                                            divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')
                                            # i = 1
                                            for div in divs:
                                                value = div.text 
                                                nv = (value.split(" ")[0])
                                                nvv = (nv[0])
                                                # print(nvv)
                                                # print(".......")
                                                if(nvv == "C"):
                                                    self.driver.execute_script("arguments[0].click();",div)
                                                    # print(div.get_attribute("innerHTML"))
                                                    # print("break")
                                                    break
                                            
                                            # print("clicked connect option btn")

                                            time.sleep(0.5)

                                            connect_btn = self.driver.find_element_by_css_selector('button[aria-label="Connect"]')
                                            connect_btn.click()
                                            add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                            add_note_btn.click()

                                            time.sleep(0.5)
                                            
                                            msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                            # msg = "Hello " + link[0] + link[7]
                                            # msg_area.send_keys(link[8])
                                            text = link[8]
                                            for character in text:
                                                msg_area.send_keys(character)
                                                time.sleep(0.01)

                                            time.sleep(1)

                                            if(var.pause_option == True):
                                                var.pause_option = False
                                                print("\n Program Paused \n")
                                                os.system("pause")

                                            send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                            self.driver.execute_script("arguments[0].click();",send_btn)
                                            # send_btn.click()
                                            # print("found send_btn")
                                            print("Sent Connect Request to {}".format(link[0]))
                                            connect_status.append('sent')
                                            time.sleep(1)
                                        except Exception as e:
                                            print("Exeception occured at scrap : {} ".format(e))
                                            connect_status.append('not sent')
                                            time.sleep(delay_time)

                                except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        connect_status.append('not sent')
                                        time.sleep(delay_time) 








                            #   Trying Message option

                                original_window = self.driver.current_window_handle


                                # print("original window :{}".format(original_window))
                                try:
                                    try:
                                            msg_btn = self.driver.find_element_by_css_selector('a[class="message-anywhere-button pvs-profile-actions__action artdeco-button "]')
                                            
                                            # time.sleep(0.5)
                                            
                                            self.driver.execute_script("arguments[0].click();",msg_btn)
                                            
                                            # print("clicked msg btn")
                                            
                                            time.sleep(0.5)

                                            all_windows = self.driver.window_handles

                                            total_window = len(all_windows)

                                            # print("total windows {}".format(total_window))

                                            if(total_window < 2):
                                                
                                                time.sleep(0.5)
                                                subject = self.driver.find_element_by_css_selector('input[placeholder="Subject (optional)"]')
                                                subject.send_keys(link[6])

                                                # print("subject added")

                                                time.sleep(0.5)

                                                text_area = self.driver.find_element_by_css_selector('div[aria-label="Write a message…"]')
                                                # text_area.send_keys(link[7])
                                                text = link[7]
                                                for character in text:
                                                    msg_area.send_keys(character)
                                                    time.sleep(0.01)

                                                # print("msg body added")

                                                time.sleep(1)

                                                if(var.pause_option == True):
                                                    var.pause_option = False
                                                    print("\n Program Paused \n")
                                                    os.system("pause")

                                                msg_send_btn = self.driver.find_element_by_class_name('msg-form__send-button')
                                                self.driver.execute_script("arguments[0].click();",msg_send_btn)
                                                # msg_send_btn.click()
                                                # print("msg sent ")
                                                print("Sent Message to {}".format(link[0]))
                                                msg_status.append("sent")
                                                time.sleep(delay_time)
                                            else:
                                                # print(self.driver.current_window_handle)
                                                self.driver.switch_to.window(all_windows[1])
                                                time.sleep(0.5)
                                                # print("went into unwanted window")
                                                self.driver.close()
                                                time.sleep(0.5)
                                                # print("window closed")
                                                self.driver.switch_to.window(all_windows[0])
                                                time.sleep(0.5)
                                                print("Message Option is Locked for {}".format(link[0]))
                                                msg_status.append("closed")
                                                # print("going back to original window")

                                                time.sleep(delay_time)

                                    except:
                                        

                                        try:

                                            msg_btn = self.driver.find_element_by_css_selector('button[class="pvs-compose-option-action__dropdown-item "]')

                                            # for div in divs:
                                            #     print(div.get_attribute("innerHTML"))
                                            self.driver.execute_script("arguments[0].click();",msg_btn)
                                            # print("msg btn clicked")

                                            time.sleep(1)

                                            all_windows = self.driver.window_handles

                                            total_window = len(all_windows)

                                            # print("total windows {}".format(total_window))

                                            if(total_window < 2):
                                                
                                                time.sleep(0.5)

                                                subject = self.driver.find_element_by_css_selector('input[placeholder="Subject (optional)"]')
                                                subject.send_keys(link[6])

                                                # print("subject added")

                                                time.sleep(0.5)

                                                text_area = self.driver.find_element_by_css_selector('div[aria-label="Write a message…"]')
                                                # text_area.send_keys(link[7])
                                                text = link[7]
                                                for character in text:
                                                    text_area.send_keys(character)
                                                    time.sleep(0.01)

                                                # print("msg body added")

                                                time.sleep(1)

                                                if(var.pause_option == True):
                                                    var.pause_option = False
                                                    print("\n Program Paused \n")
                                                    os.system("pause")

                                                msg_send_btn = self.driver.find_element_by_class_name('msg-form__send-button')
                                                self.driver.execute_script("arguments[0].click();",msg_send_btn)
                                                # msg_send_btn.click()
                                                # print("msg sent ")
                                                print("Sent Message to {}".format(link[0]))
                                                msg_status.append("sent")
                                                time.sleep(delay_time)

                                            else:
                                                # print(self.driver.current_window_handle)
                                                self.driver.switch_to.window(all_windows[1])
                                                time.sleep(0.5)
                                                # print("went into unwanted window")
                                                self.driver.close()
                                                time.sleep(0.5)
                                                # print("window closed")
                                                self.driver.switch_to.window(all_windows[0])
                                                time.sleep(0.5)
                                                print("Message Option is Locked for {}".format(link[0]))
                                                msg_status.append("closed")
                                                # print("going back to original window")

                                                time.sleep(delay_time)
                                        
                                        except Exception as e:
                                            print("Exeception occured at scrap : {} ".format(e))
                                            msg_status.append("not sent")

                                except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        msg_status.append("not sent")
                                        time.sleep(delay_time)






                            if(choosen_option == 2):
                                # only connect
                                # print("accessed connect option")
                                # time.sleep(2)
                                try:
                                    try:
                                        btn = self.driver.find_element_by_class_name("artdeco-button--primary").get_attribute("innerHTML")     

                                        new_value = btn.split("<")[-2]
                                        value = new_value.split(">")[1]
                                        final_value=value.strip()
                                        # print("first value {}".format(final_value))
                                        # print("got in")
                                        
                                        # checking Checking Connect at option 1
                                        if(final_value == 'Connect'):
                                            

                                            # print("found connect btn div")
                                            # time.sleep(0.5)
                                            
                                            connect_btn = self.driver.find_element_by_css_selector('button[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view pvs-profile-actions__action"]')
                                            
                                            # time.sleep(2)
                                            
                                            self.driver.execute_script("arguments[0].click();",connect_btn)
                                            
                                            # print("clicked connect btn")
                                            
                                            time.sleep(0.5)

                                            
                                            add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                            add_note_btn.click()

                                            # print("clicked add note btn")

                                            time.sleep(0.5)
                                            
                                            msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                            # msg = "Hello " + link[0] + link[7]
                                            # msg_area.send_keys(link[8])
                                            text = link[8]
                                            for character in text:
                                                    msg_area.send_keys(character)
                                                    time.sleep(0.01)
                                            

                                            time.sleep(1)

                                            if(var.pause_option == True):
                                                    var.pause_option = False
                                                    print("\n Program Paused \n")
                                                    os.system("pause")

                                            send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                            self.driver.execute_script("arguments[0].click();",send_btn)
                                            # send_btn.click()
                                            # print("clicked send btn")
                                            print("Sent Connect Request to {}".format(link[0]))
                                            connect_status.append('sent')
                                            time.sleep(delay_time)
                                        else:
                                            # checking for follow btn. if available then go inside more_btn
                                            # print("got into else caause  connect not in position 1")
                                            more_btn = self.driver.find_element_by_css_selector('button[aria-label="More actions"]')

                                            # time.sleep(1)
                            
                                            self.driver.execute_script("arguments[0].click();",more_btn)

                                            # print("clicked more btn")
                                            
                                            time.sleep(0.5)

                                            # divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')
                                            
                                            
                                            divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')
                                            # i = 1
                                            for div in divs:
                                                value = div.text 
                                                nv = (value.split(" ")[0])
                                                nvv = (nv[0])
                                                # print(nvv)
                                                # print(".......")
                                                if(nvv == "C"):
                                                    self.driver.execute_script("arguments[0].click();",div)
                                                    # print(div.get_attribute("innerHTML"))
                                                    # print("break")
                                                    break
                                            

                                            # print("clicked connect option btn")
                                            time.sleep(0.5)

                                            connect_btn = self.driver.find_element_by_css_selector('button[aria-label="Connect"]')
                                            connect_btn.click()
                                            add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                            add_note_btn.click()

                                            time.sleep(0.5)
                                            
                                            msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                            # msg = "Hello " + link[0] + link[7]
                                            # msg_area.send_keys(link[8])
                                            text = link[8]
                                            for character in text:
                                                    msg_area.send_keys(character)
                                                    time.sleep(0.01)

                                            time.sleep(1)

                                            if(var.pause_option == True):
                                                    var.pause_option = False
                                                    print("\n Program Paused \n")
                                                    os.system("pause")

                                            send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                            self.driver.execute_script("arguments[0].click();",send_btn)
                                            # send_btn.click()
                                            # print("found send_btn")
                                            print("Sent Connect Request to {}".format(link[0]))
                                            connect_status.append('sent')
                                            time.sleep(delay_time)
                                            
                                                

                                    except Exception as e:
                                        
                                        try:
                                            # print("went inside exception")
                                             # checking for follow btn. if available then go inside more_btn
                                            more_btn = self.driver.find_element_by_css_selector('button[aria-label="More actions"]')

                                            # time.sleep(1)
                            
                                            self.driver.execute_script("arguments[0].click();",more_btn)

                                            # print("clicked more btn")
                                            
                                            time.sleep(0.5)

                                            divs = self.driver.find_elements_by_css_selector('div[class="display-flex align-items-center  artdeco-dropdown__item artdeco-dropdown__item--is-dropdown ember-view"]')
                                            # i = 1
                                            for div in divs:
                                                value = div.text 
                                                nv = (value.split(" ")[0])
                                                nvv = (nv[0])
                                                # print(nvv)
                                                # print(".......")
                                                if(nvv == "C"):
                                                    self.driver.execute_script("arguments[0].click();",div)
                                                    # print(div.get_attribute("innerHTML"))
                                                    # print("break")
                                                    break
                                            
                                            # print("clicked connect option btn")

                                            time.sleep(0.5)

                                            connect_btn = self.driver.find_element_by_css_selector('button[aria-label="Connect"]')
                                            connect_btn.click()
                                            add_note_btn = self.driver.find_element_by_css_selector('button[aria-label="Add a note"]')
                                            add_note_btn.click()

                                            time.sleep(0.5)
                                            
                                            msg_area = self.driver.find_element_by_css_selector('textarea[name="message"]')
                                            # msg = "Hello " + link[0] + link[7]
                                            # msg_area.send_keys(link[8])
                                            text = link[8]
                                            for character in text:
                                                    msg_area.send_keys(character)
                                                    time.sleep(0.01)

                                            time.sleep(1)

                                            if(var.pause_option == True):
                                                    var.pause_option = False
                                                    print("\n Program Paused \n")
                                                    os.system("pause")

                                            send_btn = self.driver.find_element_by_css_selector('button[aria-label="Send now"]')
                                            self.driver.execute_script("arguments[0].click();",send_btn)
                                            # send_btn.click()
                                            # print("found send_btn")
                                            print("Sent Connect Request to {}".format(link[0]))
                                            connect_status.append('sent')
                                            time.sleep(1)
                                        except Exception as e:
                                            print("Exeception occured at scrap : {} ".format(e))
                                            connect_status.append('not sent')
                                            time.sleep(delay_time)

                                except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        connect_status.append('not sent')
                                        time.sleep(delay_time) 





                            if(choosen_option == 3):
                                # only msg
                                # self.driver.switch_to(original_window)
                                original_window = self.driver.current_window_handle


                                # print("original window :{}".format(original_window))
                                try:
                                    try:
                                            msg_btn = self.driver.find_element_by_css_selector('a[class="message-anywhere-button pvs-profile-actions__action artdeco-button "]')
                                            
                                            # time.sleep(0.5)
                                            
                                            self.driver.execute_script("arguments[0].click();",msg_btn)
                                            
                                            # print("clicked msg btn")
                                            
                                            time.sleep(0.5)

                                            all_windows = self.driver.window_handles

                                            total_window = len(all_windows)

                                            # print("total windows {}".format(total_window))

                                            if(total_window < 2):
                                                
                                                time.sleep(0.5)
                                                subject = self.driver.find_element_by_css_selector('input[name="subject"]')
                                                subject.send_keys(link[6])

                                                # print("subject added")

                                                time.sleep(0.5)

                                                text_area = self.driver.find_element_by_css_selector('div[aria-label="Write a message…"]')
                                                # text_area.send_keys(link[7])
                                                text = link[7]
                                                for character in text:
                                                    text_area.send_keys(character)
                                                    time.sleep(0.01)

                                                # print("msg body added")

                                                time.sleep(1)

                                                if(var.pause_option == True):
                                                    var.pause_option = False
                                                    print("\n Program Paused \n")
                                                    os.system("pause")

                                                msg_send_btn = self.driver.find_element_by_class_name('msg-form__send-button')
                                                self.driver.execute_script("arguments[0].click();",msg_send_btn)
                                                # msg_send_btn.click()
                                                # print("msg sent ")
                                                print("Sent Message to {}".format(link[0]))
                                                msg_status.append("sent")
                                                time.sleep(delay_time)
                                            else:
                                                # print(self.driver.current_window_handle)
                                                self.driver.switch_to.window(all_windows[1])
                                                time.sleep(0.5)
                                                # print("went into unwanted window")
                                                self.driver.close()
                                                time.sleep(0.5)
                                                # print("window closed")
                                                self.driver.switch_to.window(all_windows[0])
                                                time.sleep(0.5)
                                                print("Message Option is Locked for {}".format(link[0]))
                                                msg_status.append("closed")
                                                # print("going back to original window")

                                                time.sleep(delay_time)

                                    except:
                                        

                                        try:

                                            msg_btn = self.driver.find_element_by_css_selector('button[class="pvs-compose-option-action__dropdown-item "]')

                                            # for div in divs:
                                            #     print(div.get_attribute("innerHTML"))
                                            self.driver.execute_script("arguments[0].click();",msg_btn)
                                            # print("msg btn clicked")

                                            time.sleep(1)

                                            all_windows = self.driver.window_handles

                                            total_window = len(all_windows)

                                            # print("total windows {}".format(total_window))

                                            if(total_window < 2):
                                                
                                                time.sleep(0.5)

                                                subject = self.driver.find_element_by_css_selector('input[placeholder="Subject (optional)"]')
                                                subject.send_keys(link[6])

                                                # print("subject added")

                                                time.sleep(0.5)

                                                text_area = self.driver.find_element_by_css_selector('div[aria-label="Write a message…"]')
                                                # text_area.send_keys(link[7])
                                                text = link[7]
                                                for character in text:
                                                    text_area.send_keys(character)
                                                    time.sleep(0.01)

                                                # print("msg body added")

                                                time.sleep(1)

                                                if(var.pause_option == True):
                                                    var.pause_option = False
                                                    print("\n Program Paused \n")
                                                    os.system("pause")

                                                msg_send_btn = self.driver.find_element_by_class_name('msg-form__send-button')
                                                self.driver.execute_script("arguments[0].click();",msg_send_btn)
                                                # msg_send_btn.click()
                                                # print("msg sent ")
                                                print("Sent Message to {}".format(link[0]))
                                                msg_status.append("sent")
                                                time.sleep(delay_time)

                                            else:
                                                # print(self.driver.current_window_handle)
                                                self.driver.switch_to.window(all_windows[1])
                                                time.sleep(0.5)
                                                # print("went into unwanted window")
                                                self.driver.close()
                                                time.sleep(0.5)
                                                # print("window closed")
                                                self.driver.switch_to.window(all_windows[0])
                                                time.sleep(0.5)
                                                print("Message Option is Locked for {}".format(link[0]))
                                                msg_status.append("closed")
                                                # print("going back to original window")

                                                time.sleep(delay_time)
                                        
                                        except Exception as e:
                                            print("Exeception occured at scrap : {} ".format(e))
                                            msg_status.append("not sent")

                                except Exception as e:
                                        print("Exeception occured at scrap : {} ".format(e))
                                        msg_status.append("not sent")
                                        time.sleep(delay_time)
                                



                        print("..............................................")
                        print(" \n ")
                    except:
                        print("choose an option")


            temp = list()

            for i in range(len(pro_link)):
                try:
                    if(choosen_option == 1): 
                        try:
                            tempDict = {
                                    "Name": name[i],
                                    "Link": pro_link[i],
                                    "Message": msg_status[i],
                                    "Connect": connect_status[i]
                                            }
                            
                            temp.append(tempDict.copy())
                            
                        except Exception as e:
                            # print("Exeception occured at scrap : {} ".format(e))
                            pass
                    if(choosen_option == 2): 
                        try:
                            tempDict = {
                                    "Name": name[i],
                                    "Link": pro_link[i],
                                    "Message": "",
                                    "Connect": connect_status[i]
                                            }
                            
                            temp.append(tempDict.copy())
                            
                        except Exception as e:
                            # print("Exeception occured at scrap : {} ".format(e))
                            pass
                    if(choosen_option == 3): 
                        try:
                            tempDict = {
                                    "Name": name[i],
                                    "Link": pro_link[i],
                                    "Message": msg_status[i],
                                    "Connect": ""
                                            }
                            
                            temp.append(tempDict.copy())
                            
                        except Exception as e:
                            # print("Exeception occured at scrap : {} ".format(e))
                            pass
                except:
                    print("Exeception occured at scrap : {} ".format(e))

            for item in temp:
                    var.scrap_data.append(item)

            alert(text='Total Profile : {}'.format(profile_count), title='', button='OK')
           


        except Exception as e:
            print("Exeception occured at scrap : {} ".format(e))
            var.status = False
            var.stop = True

        finally:
            var.scarp_start = False
            print("scrap func finished")


            


   