import var
import time
import os
import shutil
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyautogui import alert, write, press


class profile_scrape():
    def __init__(self):
        print("inside the profile scraper")

    def scrap(self):

        links = []
        Name = []
        CompanyName = []
        Designation = []
        Location = []
        normal_link = []
        
        limit = var.page_number
        profile_count = 0
        var.remaining_page = limit
        var.profile_count = profile_count
        step = var.scrolling_step
        try_count = var.try_count
        link = 0
        b = 0
        c = 0
        self.driver = var.driver

        delay_time = var.delay
        count3 = 0

        print("starting to scrape....")
        try:
           
            # looping through every page

            self.driver.maximize_window()
            time.sleep(1)
            # print(delay_time)

            for count3 in range(0, limit):
                count3 = (count3 + 1)
                # limit is total page number & count3 is the iterator
                if var.stop == True:
                    break
                count = 0

                normal_link = []
                link = 0
                b = 0
                c = 0

                for i in range(try_count):
                    count = count + step
                    self.driver.execute_script(
                        "document.querySelector('#content-main > div > div.full-width > div.p4._vertical-scroll-results_1igybl').scrollTop={}".format(count))
                    time.sleep(0.5)

                    if(var.pause_option == True):
                        var.pause_option = False
                        print("\n Program Paused \n")
                        os.system("pause")
                # runs the scrolling action, try_count = number of scrolls, count = number of pixels to scroll per time

                temp = list()
                try:
                    try:

                        all_lists = self.driver.find_elements_by_css_selector(
                            'a[data-anonymize="person-name"]')
                        print("links {}".format(len(all_lists)))
                        for lists in all_lists:
                            if var.stop == True:
                                break
                            profile_count += 1
                            var.profile_count = profile_count

                            if(var.pause_option == True):
                                var.pause_option = False
                                print("\n Program Paused \n")
                                os.system("pause")

                            #  updates the gui profile variable , Scrapping the lnkedin_sales_navigator urls of each profile


                            #  Getting the Normal Profile Link Out of Sales Link
                            try:
                                link = lists.get_attribute("href")
                                links.append(link)

                                b = link.split(',')[0]

                                # print(b)

                                c = b.replace("/sales/lead/", "/in/")

                                # print(c)

                                normal_link.append(c)

                            except Exception as e:
                                links.append("not available")
                    except Exception as e:
                        print("can't get links")

                    # Getting Profile Name          
                    try:
                        names = self.driver.find_elements_by_css_selector(
                            'a[data-anonymize="person-name"]')

                        for item in names:
                            if var.stop == True:
                                break
                            try:
                                Name.append(item.text)
                            except Exception as e:
                                Name.append("not available")
                        print("Name {}".format(len(names)))
                    except Exception as e:
                        print("can't get Names")

                    # Getting Profile's Company name 

                    try:
                        #  Scrapes the total "Company_name & position" div then  splits the inner info into chunks & gets the Array which contains the "Company Name" information
                        company_names = self.driver.find_elements_by_css_selector(
                            'div[data-test-lead-result-entity="title-at-company"]')
                        for item in company_names:
                            if var.stop == True:
                                break
                            try:
                                try:
                                    link = item.find_element_by_class_name(
                                        "ember-view")
                                    CompanyName.append(link.text)

                                except Exception as e:
                                    str = item.get_attribute('innerHTML')
                                    # print("0")
                                    # print(str)
                                    str_1 = (str.split('>'))
                                    # print("1")
                                    # print(str_1)
                                    str_2 = ''
                                    # print(new_str)
                                    for sentence in str_1:
                                        if 'aria-label' in sentence:
                                            str_2 = sentence

                                    str_3 = (str_2.split('"')[0])
                                    # print("3")
                                    # print(str_3)
                                    company_op = (str_3.split('<')[0])
                                    # print("4")
                                    # print(company)

                                    company_op2 = company_op.strip()
                                # apostophe S  gets  misinterpreted to "amp;" thats why replacing it
                                    company_name = company_op2.replace(
                                        "amp;", "")

                                    # print("5")
                                    # print(company_name)
                                    CompanyName.append(company_name)

                            except Exception as e:
                                CompanyName.append("not found")
                        print("company_names {}".format(len(company_names)))

                    except Exception as e:
                        print("Exeception occured at scrap : {} ".format(e))
                        # print("can't get Company Names")

                    # Getting Profile's Position

                    try:
                        lists = self.driver.find_elements_by_css_selector(
                            'div[data-test-lead-result-entity="title-at-company"]')
                        #  Scrapes the total "Company_name & position" div then  splits the inner info into chunks & gets the Array which contains the "position" information
                        for item in lists:
                            try:
                                str = item.get_attribute('innerHTML')
                                position_str = (str.split('<span>')[-1])
                                designation_op = (position_str.split('<')[0])

                                designation = designation_op.replace(
                                    "amp;", "")

                                Designation.append(designation)
                            except:
                                Designation.append("not available")
                        print("lists {}".format(len(lists)))

                    except Exception as e:
                        print("can't get position")


                    # Getting Profile's Location

                    try:
                        locations = self.driver.find_elements_by_css_selector(
                            'div[data-test-lead-result-entity="geo"]')

                        for item in locations:
                            try:
                                Location.append(item.text)
                            except Exception as e:
                                Location.append("not available")
                        print("locations {}".format(len(locations)))
                    except Exception as e:
                        print("can't get positions")


                    # Linkedin Changed  & Does not show The "premium Info" any more so this section does not work
                    try:
                        # Scrapes the linkedin Premium icon data: boolean(true / false)
                        premium_divs = self.driver.find_elements_by_css_selector(
                            'div[class="artdeco-entity-lockup__content ember-view"]')
                        # for i in range(1,26):
                        for premium_div in premium_divs:
                            try:
                                
                                profile_status = premium_div.find_element_by_css_selector(
                                    'li-icon[type="linkedin-premium-gold-icon"]')
                                
                                ProfileStatus.append("Premium")
                            except:
                                ProfileStatus.append("Not")
                        x = len(ProfileStatus)
                        print('profile_status {}'.format(len(ProfileStatus)))

                    except Exception as e:
                        print("can't get profile premium info")

                    for i in range(len(Name)):
                        # combining each profile's [total = 25] different Data in one row
                        # if not ProfileStatus[i]:
                        #     ProfileStatus[i] = "this 25 data may be corrupted"

                        try:
                            tempDict = {
                                'Name': Name[i],
                                "Company": CompanyName[i],
                                "Job_title": Designation[i],
                                "Location": Location[i],
                                "Linkedin_Link": normal_link[i],
                                "Sales_nav_link": links[i]
                            }

                            temp.append(tempDict.copy())
                            # print(Name[i])
                            # print( Location[i])
                            # print( Designation[i])
                            # print( CompanyName[i])
                            # print( links[i])
                            # print(ProfileStatus[i])
                            # print(i)
                            # print("\n")
                            # collection.append(tempDict.copy())
                            # elem.remove(item)
                        except Exception as e:
                            print("Exeception occured at scrap : {} ".format(e))
                            print("can't scrape data")
                            pass

                except Exception as e:
                    print("Exeception occured at scrap : {} ".format(e))

                for item in temp:
                    var.scrap_data.append(item)

                var.remaining_page = limit - (count3)

                # profile_count = (len(ProfileStatus))

                var.profile_count = profile_count
                print("  Page Count : {} \n  Profile Count : {} ".format(
                    count3, profile_count))
                # print("  Page Count : {} \n  Profile Count : {} ".format(count3, len(temp)))

                Name = []
                Designation = []
                Location = []
                CompanyName = []
                links = []
                ProfileStatus = []

                if(count3 < (limit)):
                    time.sleep(1)
                    try:
                        next_btn = self.driver.find_element_by_css_selector(
                            'button[aria-label="Next"]')
                        next_btn.click()
                    except Exception as e:
                        print("no more page exist")
                        break

                time.sleep(delay_time)

            # for item in temp:
            #         var.scrap_data.append(item)

            # time_taken = (time() - start_time)/60
            var.initial_option = var.option_type
            alert(text='Total Profile : {}'.format(
                profile_count), title='', button='OK')

        except Exception as e:
            print("Exeception occured at scrap : {} ".format(e))
            var.status = False
            var.stop = True

        finally:
            var.scarp_start = False
            print("scrap func finished")
