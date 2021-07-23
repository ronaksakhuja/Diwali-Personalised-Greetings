from selenium import webdriver
from time import sleep
import filter_contacts


wishingContacts = filter_contacts.filter_contacts("google.csv")
driver = webdriver.Firefox('C:\webdrivers')
driver.get('https://web.whatsapp.com')
sleep(30)
contacts = dict()

for key, value in wishingContacts.items():
    pre_msg = "Namaskar *"
    post_msg = "* Bit by bit, may every cracker cracked on the evening of Diwali bring light to your life, darkness to your IDE, sweet free shwags, gits of joy, colours of RGB, arrays of prosperity and drive away bugs of hopelessness from your life. May the time limit of your life be exceeded, the errors fixed and your joys increment multiflops. *Wish you a very Happy Diwali*"
    input_box = driver.find_element_by_css_selector("div[data-tab='3']")
    input_box.click()
    input_box.send_keys(key)
    sleep(0.7)
    userbox = driver.find_element_by_css_selector("span[title='"+key+"']")
    userbox.click()
    inputbox = driver.find_element_by_css_selector("div[data-tab='6']")
    inputbox.click()
    inputbox.send_keys(pre_msg+value+post_msg+'\n')
