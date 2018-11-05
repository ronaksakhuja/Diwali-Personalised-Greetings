from selenium import webdriver
from time import sleep
import pickle
import filter_contacts

wishing_contacts=filter_contacts.filter_contacts("google.csv")

driver=webdriver.Chrome('/Users/ronaksakhuja/AnacondaProjects/Data Science Course/scraping/books_crawler/chromedriver')

driver.get('https://web.whatsapp.com')
sleep(15)
contacts=dict()
# contacts['Saani']="Saanidhi"

for key,value in wishing_contacts.items():
    pre_msg="TESTING Dear "
    post_msg=" I wish you a very happy diwali"
    input_box=driver.find_element_by_css_selector("input[type='text']")
    input_box.click()
    input_box.send_keys(key)
    sleep(1)
    userbox=driver.find_element_by_css_selector("span[title='"+key+"']")
    userbox.click()
    inputbox=driver.find_element_by_css_selector("div[data-tab='1']")

    inputbox.click()
    inputbox.send_keys(pre_msg+value+post_msg)
    send_button=driver.find_element_by_css_selector("span[data-icon='send']")
    send_button.click()
    sleep(1)