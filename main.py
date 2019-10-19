import os
import time
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from ReadContacts import ReadingCSV

browser = wd.Chrome('/Path/chromedriver')
browser.get(f'https://api.whatsapp.com/send?phone=5512981215691&text=permita')


def getMessage():
    text = ''    
    message = input("Message: ").split(' ')
    for x in message:
        text = text + x + '%20'
    return text

def checkLogon(code):
    if code.find_elements_by_id('side'):
        return True
    else:
        return False

def getNumber():
    pass

def sendMessage(text, number):
    browser.get(f'https://api.whatsapp.com/send?phone=55{number}&text={text}')
    notification = browser.find_element_by_id('action-button')
    notification.click()
    time.sleep(5.0)
    send = browser.find_elements_by_class_name('hnQHL')
    send[1].click()
    time.sleep(1.5)

#Check if o the WhatsApp is connected
while checkLogon(browser) != True:
    time.sleep(3.0)
    print("Connecting...")

#Check if has an image
image = input("This massege has an imagen within it ? s/n: ")
if image == 's':
    path_image = (input("Path: "))

#send Message
contacts_list = ReadingCSV
contacts = contacts_list.getNumbersPhones()
for x in range(0, len(contacts)):
    try: 
        sendMessage(getMessage(), contacts[x])
    except:
        pass

t = input("pause...")
        