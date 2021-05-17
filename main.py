from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

driver.maximize_window()

times = driver.find_elements_by_css_selector(".event-widget time")
names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": names[n].text,
    }
print(events)
driver.quit()