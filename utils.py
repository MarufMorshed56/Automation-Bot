import var
import json
import csv
from os import path
from pyautogui import alert


def update_config_json():
    try:
        data = {
            "config": {
                "email": var.email,
                "password": var.password,
                "filename": var.filename,
                "delay": var.delay,
                "page_number": var.page_number,
                "primary_link": var.primary_link,
                "login_link": var.login_link,
                "cookies_of": var.cookies_of,
                "scrolling_step": var.scrolling_step,
                "try_count": var.try_count,
                "directory": var.directory
            }
        }

        with open('config.json', 'w') as json_file:
            json.dump(data, json_file)

    except Exception as e:
        print("Exeception occured at update_config_json : {}".format(e))


def export_data_to_csv():

    if(var.current_tab == 0):
        if (var.option_type == 1):
            csv_columns = ['Name',"Company","Job_title","Location","Linkedin_Link","Sales_nav_link"]
        if(var.option_type == 2):
            csv_columns = ['Company', 'Industry', 'Headquater',
                        'Website', "All_Employees", "Decision_makers", "TeamLink_connections"]
    elif(var.current_tab == 1):
        csv_columns = ["Name", "Comapny", "Job_title", "Location", "LinkedIn_Link",
                       "Sales_nav_link", "Name_status", "Company_status", "Job_title_status", "Location_status"]
    elif(var.current_tab == 2):
        csv_columns = ['Title', 'Company', 'Place', 'Number of Applicants', 'Date', 'Date_s', 'link', 'Desciption',
                       'DescriptionHTML', 'Seniority Level', "Employment type", "Industry", "Size of Company", "Job ID"]

    elif(var.current_tab == 3):
        csv_columns = ['Name', 'Link', 'Message', 'Connect']


    if ".csv" in var.filename:
            csv_file = var.filename
    else:
            csv_file = var.filename + ".csv"
    #     if os.path.isfile(csv_file):
        # csv_path = var.directory + "/" + csv_file
        # csv_path = path.join(*var.directory.split("/"), csv_file)
    csv_path = path.join(var.directory, csv_file)
    with open(csv_path, 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for item in var.scrap_data:
                try:
                    writer.writerow(item)
                except Exception as e:
                    print("Exeception occured at export_data_to_csv : {} ".format(e))

    alert(text='Exported to: {} Done'.format(
            csv_path), title='Export file', button='OK')

