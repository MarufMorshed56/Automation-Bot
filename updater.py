# import collections
from cgitb import text
import csv
import pandas as pd
from gettext import find
from glob import escape
from lib2to3.pgen2 import driver
from select import select
from turtle import pos
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


class update():
    def __init__(self):
        print("inside profile updater \n")

    def scrap(self):

        name = []
        pro_link = []
        msg_status = []
        location = []
        company = []
        connect_status = []
        position = []
        sales_nav_link = []
        normal_link = []
        name_status = []
        org_status = []
        job_title_status = []
        location_status = []

        print("starting to Update....")
        limit = var.page_number
        profile_count = 0
        var.remaining_page = limit
        var.profile_count = profile_count
        filepath = var.file_path

        self.driver = var.driver

        delay_time = var.delay
        # count3 = 0
        j = 1
        l = 0
        try:
            
            file = pd.read_excel(r'{}'.format(filepath), engine='openpyxl')
            # file = pd.DataFrame(csv_file)
            for k, rows in file.iterrows():
                j += 1
        except:
            print("")

        print("\n total number of Profiles to be Scrapped: {}".format(j))

        # if(var.pause_option == True):
        #     var.pause_option = False
        #     os.system("pause")

        try:
            file = pd.read_excel(r'{}'.format(filepath), engine='openpyxl')
            

            self.driver.maximize_window()

            time.sleep(1)
            # print(delay_time)

            for i, link in file.iterrows():
                if var.stop == True:
                    break
                

                print("\n ............................. \n \n \n")
                l += 1
                print("Row No: {} \n".format(l))
                print("\n")

                
                sales_profile_link = link[5]
                pro_link.append(sales_profile_link)
                # Getting into each profile link
                self.driver.get(sales_profile_link)

                profile_count += 1
                var.profile_count = profile_count
                var.remaining_page = (j - (profile_count+1))

                time.sleep(2)

                if(var.pause_option == True):
                    var.pause_option = False
                    print("\n Program Paused \n")
                    os.system("pause")

                time.sleep(delay_time)

                try:
                    # trying to Get Name
                    try:
                        person_name = self.driver.find_element_by_css_selector(
                            'h1[data-anonymize="person-name"]').text
                        prev_name = link[0]

                        print("prev name {}".format(prev_name))
                        print("cur  {}".format(person_name))

                        if (prev_name == person_name):
                            n_status = "."
                            name_status.append(n_status)
                            name.append(prev_name)

                        elif(person_name == 'LinkedIn Member'):
                            n_status = "."
                            name_status.append(n_status)
                            name.append(prev_name)
                        else:
                            n_status = "changed"
                            name_status.append(n_status)
                            name.append(person_name)

                        print("n_status {}".format(n_status))
                        print('\n')

                    except Exception as e:
                        name_status('changed')
                        name.append("not available")
                        print("can't get name")

                    #  getting Location
                    try:
                        person_location = self.driver.find_element_by_css_selector(
                            'a[data-test-lockup-link="location"]').text
                        location.append(person_location)

                        prev_location = link[3]

                        print("prev loc {}".format(prev_location))
                        print("cur  {}".format(person_location))

                        if (prev_location == person_location):
                            loc_status = "."
                            location_status.append(loc_status)
                        else:
                            loc_status = "changed"
                            location_status.append(loc_status)

                        print("loc_status {}".format(loc_status))
                        print('\n')

                    except Exception as e:
                        location.append("not available")
                        print("can't get location")

                    #  geting Company Name &  getting Job Title

                    com_value = 0
                    job_value = 0
                    print('\n')
                    current_company_info = self.driver.find_element_by_css_selector(
                        'div[data-test-current-role]')
                    prev_company = link[1]
                    prev_title = link[2]

                    try:
                        try:
                            # 
                            company_info_lists = current_company_info.find_elements_by_css_selector(
                                'p[data-test-current-role-item]')
                            # print("inside option 1")

                            for item in company_info_lists:
                                try:
                                    curr_job_title = item.find_element_by_css_selector(
                                        'span[data-anonymize="job-title"]').text
                                    if(prev_title == curr_job_title):
                                        job_value = 1
                                        position.append(curr_job_title)
                                    try:
                                        company_name = item.find_element_by_css_selector(
                                            'a[data-anonymize="company-name"]').text
                                        # print("inside option 1 comapny _1")
                                        if(prev_company == company_name):
                                            # print("inside option 1 comapny_1 condition")
                                            com_value = 1
                                            company.append(company_name)
                                    except:
                                        company_name = item.find_element_by_css_selector(
                                            'span[data-anonymize="company-name"]').text
                                        # print("inside option 1 comapny _2")
                                        if(prev_company == company_name):
                                            # print("inside option 1 comapny_2 condition")
                                            com_value = 1
                                            company.append(company_name)

                                except Exception as e:
                                    print(
                                        "Exeception occured at scraper init :{}".format(e))
                                    # print("except 1")
                                    break
                        except:
                            ##########......... this part is unnecessary.................##############
                            # print("inside option 2")
                            current_info_div = self.driver.find_element_by_css_selector(
                                'p[data-test-current-role-item]')
                            job_title = current_info_div.find_element_by_css_selector(
                                'span[data-anonymize="job-title"]').text

                            if(prev_title == job_title):
                                job_value = 1
                                position.append(prev_title)
                            try:
                                # print("inside option 2 comapny _1")
                                company_name = current_info_div.find_element_by_css_selector(
                                    'span[data-anonymize="company-name"]').text
                                if(prev_company == company_name):
                                    # print("inside option 2 comapny_1 condition")
                                    com_value = 1
                                    company.append(prev_company)
                            except:
                                # print("inside option 2 comapny _2")
                                company_name = current_info_div.find_element_by_css_selector(
                                    'a[data-anonymize="company-name"]').text
                                if(prev_company == company_name):
                                    # print("inside option 2 comapny_2 condition")
                                    com_value = 1
                                    company.append(prev_company)

                        #  if job value  & Com_value  is 1 that means they are unchanged... & if Job_title is changed then we can get it easily from 'span[data-anonymize="job-title"]', 
                        if(job_value == 1):
                            j_status = "."
                            job_title_status.append(j_status)
                            print("prev title {}".format(prev_title))
                            print("cur title {}".format(prev_title))
                            print("j_status {}".format(j_status))
                        else:
                            j_status = "changed"
                            job_title_status.append(j_status)
                            print("prev title {}".format(prev_title))
                            current_info_div = self.driver.find_element_by_css_selector(
                                'p[data-test-current-role-item]')
                            position_title = current_info_div.find_element_by_css_selector(
                                'span[data-anonymize="job-title"]').text
                            position.append(position_title)
                            print("cur title {}".format(position_title))
                            print("j_status {}".format(j_status))

                        print('\n')

                        if(com_value == 1):
                            com_status = "."
                            org_status.append(com_status)
                            print("prev company {}".format(prev_company))
                            print("cur company  {}".format(prev_company))
                            print("org_status {}".format(com_status))

                        #  Company Name Can be both  'a[data-anonymize="company-name"]'  OR                            'span[data-anonymize="company-name"]',  "a" is clikable & "span" is not.  we are basically getting the  First "Company name" from the "Current Section/ Div" out of many "companies" which a profile might have...
                        else:
                            com_status = "changed"
                            print("org_status {}".format(com_status))
                            org_status.append(com_status)
                            print("prev company {}".format(prev_company))
                            current_info_div = self.driver.find_element_by_css_selector(
                                'p[data-test-current-role-item]') 
                                #  current_info_div takes the section/paragraph that lists the current Company & Job titile, & out of it we are taking the first one... This is how we are getting the First Job_Title & First Company Name, so it matches
                            try:
                                company_name = current_info_div.find_element_by_css_selector(
                                    'a[data-anonymize="company-name"]').text

                            except:
                                company_name = current_info_div.find_element_by_css_selector(
                                    'span[data-anonymize="company-name"]').text
                            company.append(company_name)
                            print("cur company  {}".format(company_name))

                        print('\n')

                    except Exception as e:
                        company.append("not available")
                        print("can't get company name")

                    print('\n')

                    #  Appending Sales Navlink

                    try:
                        sales_nav_link.append(link[5])
                    except Exception as e:
                        sales_nav_link.append("not available")
                        # print("can't get sales nav link")

                    try:
                        normal_link.append(link[4])
                    except Exception as e:
                        normal_link.append("not available")
                        print("can't get sales nav link")

                    print("..............................................")
                    print(" \n ")
                except Exception as e:
                    print("Exeception occured at scraper init :{}".format(e))

            temp = list()

            print("\n /////////////////////////////")
            print(len(name_status))
            print(len(org_status))
            print(len(job_title_status))
            print(len(location_status))
            print(" \n  /////////////////////////////")

            for i in range(len(pro_link)):
                try:
                    try:
                        tempDict = {
                            "Name": name[i],
                            "Comapny": company[i],
                            "Job_title": position[i],
                            "Location": location[i],
                            "LinkedIn_Link": normal_link[i],
                            "Sales_nav_link": sales_nav_link[i],
                            "Name_status": name_status[i],
                            "Company_status": org_status[i],
                            "Job_title_status": job_title_status[i],
                            "Location_status": location_status[i]
                        }

                        temp.append(tempDict.copy())

                    except Exception as e:
                        # print("Exeception occured at scrap : {} ".format(e))
                        pass
                except:
                    print("Exeception occured at scrap : {} ".format(e))

            for item in temp:
                var.scrap_data.append(item)

            alert(text='Total Profile : {}'.format(
                profile_count), title='', button='OK')

        except Exception as e:
            print("Exeception occured at scrap : {} ".format(e))
            var.status = False
            var.stop = True

        finally:
            var.scarp_start = False
            print("scrap func finished")




