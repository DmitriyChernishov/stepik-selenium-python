import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_links(browser, links):
    link = "https://stepik.org/lesson/{}/step/1".format(links)
    browser.get(link)
    answer = math.log(int(time.time()))
    input = browser.find_element_by_class_name("textarea")
    input.click()
    print(str(answer))
    input.send_keys(str(answer))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    actual = browser.find_element_by_class_name("smart-hints__hint")
    actual.text
    time.sleep(3)
    assert actual == "Correct!"
