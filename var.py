from json import load
import os
import sys

global driver
# scrap_data = [{'name':'abc','position':'gfdsgsd','location':"fdgsdfg", 'Company':'fdgsdfg', 'profile_link':'dsfgsdf'}]
scrap_data = []
remaining_page = 0
profile_count = 0

remember_me = False


cookies_of = ""
directory = ""

status = False
scarp_start = False
stop = False

initial_option = ''

driver = ''

current_tab = 0
scrolling_step = 0
try_count = 5

option_type = ''
option_type_2 = ''

file_path = ""
option_type = ""
acc_select = ""

pause_option = False

email = "jawadkhan@hotmail.co.uk"
password = "TLpassword@111"
filename = "demo.csv"
delay = 0
page_number = 1
primary_link = "https://www.linkedin.com/sales/homepage"
login_link = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

try:
    with open('config.json') as json_file:
        data = load(json_file)
    config = data['config']
    email = config['email']
    password = config['password']
    filename = config['filename']
    delay = config['delay']
    page_number = config['page_number']
    primary_link = config['primary_link']
    login_link = config['login_link']
    cookies_of = config['cookies_of']
    scrolling_step = config['scrolling_step']
    try_count = config['try_count']
    directory = config['directory']
except Exception as e:
    print("Exeception occured at config loading:{}".format(e))
# pyinstaller --onedir --icon=icons/exe.ico --noconfirm main.py