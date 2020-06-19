from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



from selenium.webdriver.common.keys import Keys ##KEYBOARD KEYS & FUCTIONS##

driver = webdriver.Chrome("C:/Users/Niku/Downloads/chromedriver_win32/chromedriver.exe")##NEEDS PATH FOR DRIVER##
driver.implicitly_wait(5) ##IMPLICITY WAIT: WAITS SET TIME###
driver.get("http://www.instagram.com")
assert "Instagram" in driver.title

SEle = driver.find_element_by_name("username")
SEle.clear()
SEle.send_keys("USERNAME")

SEle = driver.find_element_by_name("password")
SEle.clear()
SEle.send_keys("PASSWORD")
SEle.send_keys(Keys.ENTER)
driver.implicitly_wait(5)

SEle = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")[0]
SEle.click()


my_element_id = 'eyXLr wUAXj '
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
your_element = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))
SEle.click()
SEle.send_keys("Test search")
SEle.send_keys(Keys.ENTER)
