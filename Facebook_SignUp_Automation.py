from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
browser = webdriver.Firefox()

browser.get("https://facebook.com")
fname = browser.find_element_by_name("firstname")
fname.clear()
fname.send_keys("your first name")

lname = browser.find_element_by_name("lastname")
lname.clear()
lname.send_keys("your last name")

email = browser.find_element_by_name("reg_email__")
email.clear()
email.send_keys("test@mail.com")

conf_email = browser.find_element_by_name("reg_email_confirmation__")
conf_email.clear()
conf_email.send_keys("test@mail.com")

passwd = browser.find_element_by_name("reg_passwd__")
passwd.clear()
passwd.send_keys("test123")

dob = Select(browser.find_element_by_name("birthday_day"))
dob.select_by_value("3")

mob = Select(browser.find_element_by_name("birthday_month"))
mob.select_by_value("3")

yob = Select(browser.find_element_by_name("birthday_year"))
yob.select_by_value("1992")

gender = browser.find_element_by_id("u_0_7")
gender.click()

submit = browser.find_element_by_name("websubmit")
submit.click()