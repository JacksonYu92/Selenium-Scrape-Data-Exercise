from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# number_of_articles = driver.find_element_by_css_selector("#articlecount a")
# # number_of_articles.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

#
# driver.quit()

driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element_by_name("fName")
l_name= driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
sign_up_button = driver.find_element_by_xpath("/html/body/form/button")

f_name.send_keys("Jackson")
l_name.send_keys("Yu")
email.send_keys("jackson@email.com")
sign_up_button.click()