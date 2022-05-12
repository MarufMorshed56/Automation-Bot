# import collections
import os
import profile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# import clipboard
from datetime import datetime, timedelta
import csv
import time
from threading import Thread
import var
import shutil
from pyautogui import alert, write, press


class job_scrape():
    def __init__(self):
        print("inside job scrapper")

    def scrap(self):

        print("starting to scrape....")

        limit = var.page_number
        profile_count = 0
        var.remaining_page = limit
        var.profile_count = profile_count
        step = var.scrolling_step
        try_count = var.try_count

        job_ids = []
        job_titles = []
        job_links = []
        company_names = []
        job_locations = []
        job_types = []
        job_dates = []
        job_dates_converted = []
        applicant_numbers = []
        employment_types = []
        seniority_levels = []
        company_sizes = []
        industry_types = []

        description = []
        description_HTML = []

        total_page_available = 10
        delay_time = var.delay
        count3 = 0
        j = 1

        Job_ID_rows = []
        
        self.driver = var.driver

        # .................... Opening the Csv file containg the Job Id database................#
        with open("Job_ID_Database.csv", 'r') as file:
            csvreader = csv.reader(file)
            for data in csvreader:
                Job_ID_rows.append(data[0])

        try:
            self.driver.maximize_window()
            time.sleep(1)
            # print(delay_time)

            for count3 in range(0, limit):

                count3 = (count3 + 1)
                # limit is total page number & count3 is the iterator
                if var.stop == True:
                    break
                count = 0

              
                temp = list()
                try:

                    try:
                        #  getting all the Job_id Liat to loop through them one by one
                        all_jobs = self.driver.find_elements_by_class_name(
                            "jobs-search-results__list-item")

                        for jobs in all_jobs:
                            job_div = jobs.find_element_by_class_name(
                                "job-card-container--clickable")
                            job_id = job_div.get_attribute("data-job-id")

                            # Logic matching Job id with Data base to see if it was already scraped or not goes here, if Job Id matches then we ignore all the section from here ( if else condition)

                            if(var.pause_option == True):
                                var.pause_option = False
                                print("\n Program Paused \n")
                                os.system("pause")

                            if job_id in Job_ID_rows:

                                job_div.click()
                                time.sleep(1)
                                print("already scraped this job")

                            else:
                                job_div.click()
                                time.sleep(3)

                                Job_ID_rows.append(job_id)
                                # appending job Id
                                job_ids.append(job_id)
                                print("\n \n ............... \n \n")
                                print(job_id)
                                # print(job_ids)


# .............................. appending job details.........................

                                #  getting job section on the right side

                                try:
                                    right_section = self.driver.find_element_by_class_name(
                                        'jobs-search__right-rail')

                                    main_div = right_section.find_element_by_class_name(
                                        "jobs-unified-top-card__content--two-pane")
                                    # getting Job header section
                                    header = main_div.find_element_by_css_selector(
                                        'a[class="ember-view"]')

                        # ................ Job Link .................
                                    try:
                                        link = header.get_attribute("href")
                                        # print(link)
                                        job_links.append(link)

                                    except Exception as e:
                                        # print("Exeception occured at scraper init :{}".format(e))
                                        job_links.append(
                                            " job link not available")

                                    # print("........... \n")

                        # ................ Job Title .................

                                    try:
                                        job_title = header.text
                                        job_titles.append(job_title)

                                        print(
                                            "\n job title {}".format(job_title))

                                    except Exception as e:
                                        # print(
                                        #     "Exeception occured at scraper init :{}".format(e))
                                        print(
                                            "\n job title not available")
                                        job_titles.append("not available")

                        # ................ Company Name .................

                                    try:
                                        company_name = main_div.find_element_by_class_name(
                                            "jobs-unified-top-card__company-name").text

                                        company_names.append(company_name)
                                        print(
                                            "\n job title {}".format(company_name))

                                    except Exception as e:
                                        print("\n company name not available")
                                        company_names.append("not available")

                        # ................ Job Location .................

                                    try:
                                        job_location = main_div.find_element_by_class_name(
                                            "jobs-unified-top-card__bullet").text
                                        job_locations.append(job_location)

                                        print(
                                            "\n job location {}".format(job_location))

                                    except Exception as e:
                                        print("\n job location not availabe")
                                        job_locations.append("not availabe")

                        # ................ Job Type .................

                                    try:
                                        job_type = main_div.find_element_by_class_name(
                                            "jobs-unified-top-card__workplace-type").text

                                        job_types.append(job_type)

                                        print(
                                            "\n job type {}".format(job_type))

                                    except Exception as e:
                                        print("\n job_type not available")
                                        job_types.append("not available")

                        # ................ Total  Applicant .................
                                    try:
                                        applicant_number = main_div.find_element_by_class_name(
                                            "jobs-unified-top-card__applicant-count").text

                                        applicant_numbers.append(
                                            applicant_number)

                                        print(
                                            "\n total aplicants {}".format(applicant_number))

                                    except Exception as e:
                                        print(
                                            "\n applicant number not available")
                                        applicant_numbers.append(
                                            "not available")

                        # ................ Job Posted at ................

                                    try:
                                        job_date = main_div.find_element_by_class_name(
                                            "jobs-unified-top-card__posted-date").text

                                        job_dates.append(job_date)

                                        print(
                                            "\n job posted at {}".format(job_date))

                                    except Exception as e:
                                        print("\n  job date not available")
                                        job_dates.append("not available")

                    #  ..... Job date Conversion..............
                                    try:
                                        a = 0
                                        int_date = 0
                                        job_time = 0
                                        job_date_unconverted =0


                                        job_date_unconverted = main_div.find_element_by_class_name(
                                            "jobs-unified-top-card__posted-date").text
                        # date is in format like this "1 hour ago"  or "1 days ago" etc, so we are spliting the string based on "space"  & taking the number

                                        a = job_date_unconverted.split()
                                        int_date = int(a[0])
                                        
                                        if 'hour' in job_date_unconverted:
                                            job_time = datetime.now() - timedelta(hours=int_date)
                                            print(job_time.strftime(
                                                '\n %d/%m/%Y | %H:%M:%S'))

                                            job_dates_converted.append(
                                                job_time.strftime(
                                                    '%d/%m/%Y | %H:%M:%S'))

                                        elif 'hours' in job_date_unconverted:
                                            job_time = datetime.now() - timedelta(hours = int_date)
                                            print(job_time.strftime(
                                                '\n %d/%m/%Y | %H:%M:%S'))

                                            job_dates_converted.append(
                                                job_time.strftime(
                                                    '%d/%m/%Y | %H:%M:%S'))

                                        elif 'day' in job_date_unconverted:
                                            job_time = datetime.now() - timedelta(days=int_date)
                                            print(job_time.strftime(
                                                '\n %d/%m/%Y | %H:%M:%S'))

                                            job_dates_converted.append(
                                                job_time.strftime(
                                                    '%d/%m/%Y | %H:%M:%S'))
                                        elif 'days' in job_date_unconverted:
                                            job_time = datetime.now() - timedelta(days=int_date)
                                            print(job_time.strftime(
                                                '\n %d/%m/%Y | %H:%M:%S'))

                                            job_dates_converted.append(
                                                job_time.strftime(
                                                    '%d/%m/%Y | %H:%M:%S'))
                                        elif 'week' in job_date_unconverted:
                                            job_time = datetime.now() - timedelta(weeks=int_date)
                                            print(job_time.strftime(
                                                '\n %d/%m/%Y | %H:%M:%S'))

                                            job_dates_converted.append(
                                                job_time.strftime(
                                                    '%d/%m/%Y | %H:%M:%S'))

                                        elif 'weeks' in job_date_unconverted:
                                            job_time = datetime.now() - timedelta(weeks = int_date)
                                            print(job_time.strftime(
                                                '\n %d/%m/%Y | %H:%M:%S'))

                                            job_dates_converted.append(
                                                job_time.strftime(
                                                    '%d/%m/%Y | %H:%M:%S'))

                                        else:
                                            job_time = datetime.now()
                                            print(job_time.strftime(
                                                '\n %d/%m/%Y | %H:%M:%S'))
                                            job_dates_converted.append(
                                                job_time.strftime(
                                                    '%d/%m/%Y | %H:%M:%S'))

                                    except:
                                        print("\n cant get job posting time ")
                                        job_dates_converted.append(
                                            "not available")

# ................ Employment type, Seniority Level ................

                                    try:
                                        job_details = main_div.find_elements_by_class_name(
                                            "jobs-unified-top-card__job-insight")

                                        ll = 0
                                        no_of_employs__company_type = 0

                                        # print(len(job_details))

                                        for job_detail in job_details:
                                            ll += 1
                                            if(ll > 2):
                                                break
                                            elif(ll == 1):
                                                employment_type__job_position = job_detail.text
                                            else:
                                                no_of_employs__company_type = job_detail.text

                                        x = 0
                                        x = employment_type__job_position.split(
                                            " · ")

                                        try:
                                            if(len(x) > 1):
                                                employment_type = x[0]
                                                employment_types.append(
                                                    employment_type)

                                                seniority_level = x[1]
                                                seniority_levels.append(
                                                    seniority_level)
                                            else:
                                                employment_type = x[0]
                                                employment_types.append(
                                                    employment_type)

                                                seniority_level = " "
                                                seniority_levels.append(
                                                    "not available")

                                            print(
                                                "\n employment type at {}".format(employment_type))
                                            print(
                                                "\n seniority level {}".format(seniority_level))
                                        except:
                                            print(
                                                "\n employment_type not available \n serniority not available")
                                            employment_types.append(
                                                "not available")
                                            seniority_levels.append(
                                                "not available")

# ................ Companhy_sizes , Industry_type ................

                                        y = 0
                                        y = no_of_employs__company_type.split(
                                            " · ")

                                        try:
                                            if(len(y) > 1):
                                                company_size = y[0]
                                                company_sizes.append(
                                                    company_size)

                                                industry_type = y[1]
                                                industry_types.append(
                                                    industry_type)

                                            else:
                                                company_size = y[0]
                                                company_sizes.append(
                                                    company_size)

                                                industry_type = ''
                                                industry_types.append(
                                                    "not available")

                                            print(
                                                "\n Industry type at {}".format(industry_type))
                                            print(
                                                "\n company size {}".format(company_size))

                                        except:
                                            company_sizes.append(
                                                "not available")

                                            industry_types.append(
                                                "not available")

                                    except Exception as e:
                                        # print(
                                        #     "Exeception occured at scraper init :{}".format(e))
                                        print("\n employment not available")
                                        print("\n seniority not available")
                                        print("\n company_size not available")
                                        print("\n industry not available")
                                        employment_types.append(
                                            "not available")
                                        seniority_levels.append(
                                            "not available")
                                        company_sizes.append(
                                            "not available")
                                        industry_types.append(
                                            "not available")


# ................ Description , Description HTML ................

                                    try:
                                        job_description_div = self.driver.find_element_by_class_name(
                                            "jobs-description__container")

                                        badtext = job_description_div.find_element_by_class_name(
                                            "jobs-box__html-content").text

                                        
                                        job_description = badtext

                                        description.append(job_description)
                                        

                                        badtext_HTML = job_description_div.find_element_by_class_name(
                                            "jobs-box__html-content").get_attribute('innerHTML')
                                        
                                        job_description_HTML = badtext_HTML

                                        # job_description_HTML = badtext_HTML.replace(
                                        #     "'", "`")
                                        description_HTML.append(
                                            job_description_HTML)
                                        # description_HTML.append(
                                        #     job_description_html)

                                    except Exception as e:
                                        # print(
                                        #     "Exeception occured at scraper init :{}".format(e))
                                        description.append(
                                            " not available")
                                        description_HTML.append(
                                            "not available")

                                except Exception as e:
                                    print(e)

                                print("\n \n .................. \n \n")

                    except Exception as e:
                        print(e)

                    for i in range(len(job_ids)):
                        # combining each profile's [total = 25] different Data in one row
                        # if not ProfileStatus[i]:
                        #     ProfileStatus[i] = "this 25 data may be corrupted"

                        try:
                            tempDict = {
                                'Title': job_titles[i],
                                'Company': company_names[i],
                                'Place': job_locations[i],
                                'Number of Applicants': applicant_numbers[i],
                                'Date': job_dates[i],
                                'Date_s': job_dates_converted[i],
                                'link': job_links[i],
                                'Desciption': description[i],
                                'DescriptionHTML': description_HTML[i],
                                'Seniority Level': seniority_levels[i],
                                "Employment type": employment_types[i],
                                "Industry": industry_types[i],
                                "Size of Company": company_sizes[i],
                                "Job ID": job_ids[i],
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
                profile_count = profile_count + len(job_ids)
                var.profile_count = profile_count
                print("  Page Count : {} \n  Profile Count : {} ".format(
                    count3, profile_count))
                # print("  Page Count : {} \n  Profile Count : {} ".format(count3, len(temp)))

                job_ids = []
                job_titles = []
                job_links = []
                company_names = []
                job_locations = []
                job_types = []
                job_dates = []
                applicant_numbers = []
                employment_types = []
                seniority_levels = []
                company_sizes = []
                industry_types = []
                description = []
                description_HTML = []
                job_dates_converted = []

                total_page = []

                current_page = 1
#  as by Just Clicking the  next Job-div the  Page Auto-scrolls Down so We dont need any addition "scrolling logic" aprt from the last part, where for the "page Number" to be visible we need scrolling logic

#  The Number of pages in the Searcg Result will vary, so we are Scrapping the "Total Number of Pages" from the "buttons" that says the page number, inside,  we are getting all the buttons &  then looping through them to get the Last Button which states the last Page Number, we are doing this only for the  one time /First time, that why the logic (coun3 < 2 ) meaning just for the first page do this.., we are then using the "last page" number to limit our bot,   
                try:
                 if(count3 < 2):
                    if(var.pause_option == True):
                        var.pause_option = False
                        print("\n Program Paused \n")
                        os.system("pause")

                    pagination = self.driver.find_element_by_css_selector(
                        'section[aria-label="pagination"]')

                    pagination_lists = pagination.find_elements_by_class_name(
                        "artdeco-pagination__indicator")

                    for page in pagination_lists:
                        value = page.text
                        total_page.append(value)

                    print(total_page)
                    print(".................")

                    total_page_available = int(total_page[-1]) + 1
                    current_page_btn = pagination.find_element_by_css_selector(
                        'button[aria-current="true"]')


                    current_page_str = current_page_btn.text
                    current_page = int(current_page_str)

                 if((count3 < (limit)) and (count3 < total_page_available)):
                    time.sleep(0.5)
                    if(var.pause_option == True):
                        var.pause_option = False
                        print("\n Program Paused \n")
                        os.system("pause")

        # Scrolling Logic  to make the "next page" button visible 
                    try:
                        self.driver.execute_script(
                            'document.querySelector("body > div.application-outlet > div.authentication-outlet > div.job-search-ext > div.jobs-search-two-pane__wrapper > div > section.jobs-search__left-rail > div > div").scrollTop={}'.format(4000))
                        time.sleep(1)

        #  There isn't any "next page" button, linkedin makes it so that "each page button" is diffrent & the page number is in the button CSS name, thus  we  added the logic to Dynamically Chnage the "CSS Selector" Name, So lets say we want to go to page no. 2,  So the  css_selector needs to be  'button[aria-label="Page 2"', so we are Dynamically adding this using the following Logic, very handy Stuff

                        if (current_page < 2 ):
                            j += 1
                            pagination = self.driver.find_element_by_css_selector(
                            'section[aria-label="pagination"]')

                            next_btn = pagination.find_element_by_css_selector(
                            F'button[aria-label="Page {j}"]')
                            next_btn.click()
                        else:
                            j = current_page + 1
                            # j += 1
                            pagination = self.driver.find_element_by_css_selector(
                                'section[aria-label="pagination"]')

                            next_btn = pagination.find_element_by_css_selector(
                                F'button[aria-label="Page {j}"]')
                            next_btn.click()
                    except Exception as e:
                        print("no more page exist")
                        break

                 time.sleep(delay_time)
                except:
                    print('no more page available')

            # for item in temp:
            #         var.scrap_data.append(item)

            # time_taken = (time() - start_time)/60

# ............. Updating  csv File with new Job Ids..............
#  for this we need to create dictionaries, as  [csv.writer => writerows] can't writenormal data  rows wise without the data being a dictionary.. a dictionary looks like this  tempp = [{1:'a'},{2:'b'}]  ..... now "writerows" will take the first number meaning "1" , "2" instead of 'a' , 'b', so we take "Job Id" in the first position...#

            tempp = []
            for i in range(len(Job_ID_rows)):
                tempD = {Job_ID_rows[i]: i, }
                tempp.append(tempD.copy())

            # now tempp has become a dictionary, now to write the csv file containing the values

            # first deleting the old file to create a new file containing the updated data
            os.remove('Job_ID_Database.csv')

            with open("Job_ID_Database.csv", 'a', newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(tempp)

# ...........now the writing is complete.............

            alert(text='Total Profile : {}'.format(
                profile_count), title='', button='OK')

        except Exception as e:
            print("Exeception occured at scrap : {} ".format(e))
            var.status = False
            var.stop = True

        finally:
            var.scarp_start = False
            print("scrap func finished")

    
