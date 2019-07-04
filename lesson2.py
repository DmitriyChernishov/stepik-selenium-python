from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_class_name("trollface").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element_by_id("input_value").text
print(calc(x))
input = browser.find_element_by_id("answer")
input.click()
input.send_keys(calc(x))
button = browser.find_element_by_class_name("btn")
button.click()

time.sleep(6)
browser.stop_client()
browser.quit()