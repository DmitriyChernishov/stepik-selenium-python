import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# this code for unittest and PyTest
class TestAbs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_link1(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration1.html")
        input1 = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Dima")
        input2 = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Chernishov")
        input3 = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("mail@mail.com")
        ''' Отправляем заполненную форму '''
        button = driver.find_element_by_class_name("btn-default")
        button.click()
        ''' Проверяем, что смогли зарегистрироваться ждем загрузки страницы'''
        time.sleep(1)
        ''' находим элемент, содержащий текст'''
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        '''записываем в переменную welcome_text текст из элемента welcome_text_elt'''
        welcome_text1 = welcome_text_elt.text
        '''с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта'''
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text1
        time.sleep(5)

    def test_link2(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration2.html")
        input1 = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Dima")
        input2 = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Chernishov")
        input3 = driver.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("mail@mail.com")
        ''' Отправляем заполненную форму '''
        button = driver.find_element_by_class_name("btn-default")
        button.click()
        ''' Проверяем, что смогли зарегистрироваться ждем загрузки страницы'''
        time.sleep(1)
        ''' находим элемент, содержащий текст'''
        welcome_text = driver.find_element_by_tag_name("h1")
        '''записываем в переменную welcome_text текст из элемента welcome_text_elt'''
        '''с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта'''
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        time.sleep(5)
        self.assertEqual(welcome_text1, welcome_text)


if __name__ == "__main__":
    unittest.main()