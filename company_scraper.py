from hmac import new
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time 
import os
from threading import Thread
import var
import shutil
from pyautogui import alert, write, press


class comapny_scrape():
    def __init__(self):
        print("inside the company scraper")

    def scrap(self):
        links = []
        print("starting to scrape....")
        # start_time = time()
        limit = var.page_number
        profile_count = 0
        var.profile_count = profile_count
        step = var.scrolling_step
        try_count = var.try_count
        delay_time = var.delay
        self.driver = var.driver
        count = 0
        try:
           
            # looping through every page
            for count3 in range(0,limit):
                if var.stop == True:
                    break

                if(var.pause_option == True):
                    var.pause_option = False
                    print("\n Program Paused \n")
                    os.system("pause")

                # Scrolling Down

                for i in range(try_count):
                    if(var.pause_option == True):
                        var.pause_option = False
                        print("\n Program Paused \n")
                        os.system("pause")

                    count = count + step
                    self.driver.execute_script("document.querySelector('#content-main > div > div.full-width > div.p4._vertical-scroll-results_1igybl').scrollTop={}".format(count))
                    time.sleep(0.75)


                try:
                        count = 0
                        temp = list()
                        elem = self.driver.find_elements_by_css_selector('a[data-anonymize="company-name"]')  
                    
                         
                        for item in elem:
                                if var.stop == True:
                                    break
                                link = item.get_attribute("href")
                                links.append(link)
                            
                except Exception as e:
                            print("can't get links")
            
                # Going to Next Page by clicking the Next button, Here Limit is The Total Number of Pages To Scrape

                if(count3<(limit-1)):
                    
                    try: 
                        next_btn = self.driver.find_element_by_css_selector('button[aria-label="Next"]')
                        next_btn.click()
                    except Exception as e:
                            print("no more page exist")
                            break
                time.sleep(4)
                
            #looping through each elements in One item

            for link in links:
                                if var.stop == True:
                                  break
                                if(var.pause_option == True):
                                    var.pause_option = False
                                    print("\n Program Paused \n")
                                    os.system("pause")

                                self.driver.get(link)

                                profile_count += 1
                                var.profile_count = profile_count
                                var.remaining_page = (len(links) - profile_count)

                                time.sleep(delay_time)

                                try:
                                    # getting Company Name
                                    try:
                                        name = self.driver.find_element_by_css_selector('div[data-anonymize="company-name"]').get_attribute('innerHTML').strip()
                                    except Exception as e:
                                        name = "not available"
                                    
                                    # getting Company Industry

                                    try:   
                                        job_title = self.driver.find_element_by_css_selector('span[data-anonymize="industry"]').get_attribute('innerHTML').strip()
                                    except Exception as e:
                                        job_title = "not available"

                                    # getting Company Location

                                    try:   
                                        location = self.driver.find_element_by_css_selector('div[data-anonymize="location"]').text
                                    except Exception as e:
                                        location = "not available"

                                    time.sleep(2)
                                    
                                    # getting Company Website Link
                                    try:
                                        website_link_div = self.driver.find_element_by_css_selector('a[data-control-name="visit_company_website"]')
                                        website_link = website_link_div.get_attribute("href")
                                    except:
                                        website_link = "not available"

                                    # getting Company All Employee Info
                                    try:
                                        all_count_links = self.driver.find_elements_by_class_name(
                                            'link-without-visited-and-hover-state')

                                        new_value = []

                                        # getting Company Employees

                                        # so "all_count_links" is the Tag that contains All the  3 info i.e.  no. of empyees, no. of decision makers,  no. of teamlink connection,  so there  is no way to get them seprately, &  not  every Company has all the 3 info, so we can't take value serialy,  so  after getting all 3 data, we are splitiing it, then searching  using "keywords" to identify them idivually

                                        for link in all_count_links:
                                            value = link.text
                                            op_value = value.split("See ")[0]
                                            new_value.append(op_value)

                                        for values in new_value:
                                            if "All" in values:
                                                employee_count = values.strip('\n')
                                                break
                                            else:
                                                employee_count = 'not available'

                                        # getting Company Decision Makers

                                        for values in new_value:
                                            if "Decision" in values:
                                                decision_makers = values.strip('\n')
                                                break
                                            else:
                                                decision_makers = 'not available'

                                        # getting Company teamlink Connetions

                                        for values in new_value:
                                            if "TeamLink" in values:
                                                team_link = values.strip('\n')
                                                break
                                            else:
                                                team_link = 'not available'

                                            
                                        
                                    except:
                                        employee_count = 'not available'
                                        decision_makers = 'not available'
                                        team_link = 'not available'
                                            

                                    tempDict = {
                                                "Company": name,
                                                "Industry": job_title,
                                                "Headquater": location,
                                                "Website": website_link,
                                                "All_Employees": employee_count,
                                                "Decision_makers": decision_makers,
                                                "TeamLink_connections": team_link
                                            }
                                    temp.append(tempDict.copy())
                                    elem.remove(item)

                                    
                                except Exception as e:
                                    # print("error at getting profile")
                                    pass
 
               

            for item in temp:
                        var.scrap_data.append(item)

            
            var.remaining_page = limit - (count3+1)
            var.profile_count = profile_count

            print("  Page Count : {} \n  Profile Count : {} ".format(count3+1, len(temp)))

            var.initial_option = var.option_type
            alert(text='Total Profile : {}'.format(profile_count), title='', button='OK')
           

        except Exception as e:
            print("Exeception occured at scrap : {} ".format(e))
            var.status = False
            var.stop = True

        finally:
            var.scarp_start = False
            print("scrap func finished")

    