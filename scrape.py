from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time
from ics import Calendar, Event
import datetime
from datetime import timedelta

# set your username and password
username = "username"
password = "password"

# open Chrome and navigate to the login page
# driver = webdriver.Chrome('/Users/jnunn1/Downloads/chromedriver_mac64/chromedriver')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://login.colesgroup.com.au/nidp/saml2/sso?sid=0&option=credential")

# find the username and password fields and enter your credentials
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.ID, "Ecom_User_ID"))
)
username_field = driver.find_element(By.ID, "Ecom_User_ID")
password_field = driver.find_element(By.ID, "Ecom_Password")
username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.CLASS_NAME, "login-button")
login_button.click()

elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.CLASS_NAME, "quickLinkTile"))
)

driver.get('https://colesgroup.sharepoint.com/sites/mycoles/work/hours/Pages/default.aspx')

elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle"))
)

time.sleep(4)

nextWeek = driver.find_element(By.XPATH, "/html/body/form/div[3]/main/div/div/div/div[1]/div[2]/div/div[3]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[4]/ul/li[2]/a")

nextWeek.click()
time.sleep(2)

allDays = driver.find_elements(By.CLASS_NAME, "weeklycalendar-daycolumn")

for day in allDays:
    try:
        day.find_element(By.CLASS_NAME, "roster-timeblock-time-wrapper")
    except:
        noShift = day.get_attribute("data-date")
        print(f'No Shift on {noShift}')
    else:
        shift = day.find_element(By.CLASS_NAME, "roster-timeblock")
        wrongDate = shift.get_attribute("data-date")
        yearForm, dayForm, monthForm = wrongDate.split('-')
        date = f'{yearForm}-{monthForm}-{dayForm}'
        times = shift.find_element(By.CLASS_NAME, "roster-timeblock-time").text
        begin, end = times.split("\n")
        beginHour, beginMinute = begin.split(":")
        endHour, endMinute = end.split(":")

        beginBrisTime = datetime.datetime(int(yearForm), int(monthForm), int(dayForm), int(beginHour), int(beginMinute), 0)
        endBrisTime = datetime.datetime(int(yearForm), int(monthForm), int(dayForm), int(endHour), int(endMinute), 0)
        zBeginTime = beginBrisTime - datetime.timedelta(hours=10)
        zEndTime = endBrisTime - datetime.timedelta(hours=10)

        c = Calendar()
        e = Event()
        e.name = "James Work"
        e.begin = zBeginTime
        e.end = zEndTime
        e.description = 'I have work in department...'
        e.location = 'Redbank Plaza, 1 Collingwood Park Drv, Redbank QLD 4301'
        c.events.add(e)
        c.events
        try:
            with open(f'myShifts/{dayForm}.ics', 'w') as my_file:
                my_file.writelines(c.serialize_iter())
            print(f'Shift event for {dayForm} Saved')
        except:
            print('didnt work')

        finally:
            time.sleep(1)

print('Week Completed see the myShifts file')

time.sleep(1000)
driver.quit()


# index = 0


#
# allDays = driver.find_elements(By.CLASS_NAME, "weeklycalendar-daycolumn")
#
# for day in allDays:
#     try:
#         day.find_element(By.CLASS_NAME, "roster-timeblock-time-wrapper")
#     except:
#         print('No Shift')
#     else:
#         index += 1
#
# header = driver.find_elements(By.CLASS_NAME, "weeklycalendar-dayheader")
#
# for h in header:
#     p = h.find_element(By.CLASS_NAME, "view-details")
#     h.click()
#     time.sleep(1)
#     p.click()
#     print("clicked")
#
#     while index > 0:
#         b = driver.find_element(By.CLASS_NAME, "roster-header-right")
#         time.sleep(1)
#         b.click()
#         index -= 1
#
#     close = find_element(By.XPATH, """//*[@id="roster-view"]/div/div/div[2]/div/button""")
#     close.click()
#     time.sleep(5)
