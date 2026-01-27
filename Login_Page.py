import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium.webdriver.common.by import By
import allure

def test_shop_pages():
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# перейти на сайт_подождать подгрузку_развернуть окно
    browser.get("https://www.saucedemo.com")
    browser.implicitly_wait(4)
    browser.maximize_window()
    el=browser.find_element(By.CSS_SELECTOR, '#user-name')
    el.click
    el.send_keys("standard_user")

    el1=browser.find_element(By.CSS_SELECTOR, '#password')
    el1.click()
    el1.send_keys('secret_sauce')

    bt=browser.find_element(By.CSS_SELECTOR, '#login-button')
    bt.click()

    browser.quit()