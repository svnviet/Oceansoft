from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/bin/chromedriver')


url = "https://cm.litextension.com/login"
driver.get(url)

email = driver.find_element_by_id("email")
email.clear()
email.send_keys("test1@test.com")

password= driver.find_element_by_id("password")
password.clear()
password.send_keys('aA123456')

driver.find_elements_by_xpath("""//*[@id="app"]/div/div/div/div/div[2]/div/div[1]/form/div[5]/div/button""")[0].click()


print('Name = ',driver.find_elements_by_id("navbarDropdown2")[0].text)
