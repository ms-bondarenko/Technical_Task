import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import allure
from Pages.Login_Page import Login_Page

def test_Login_Page():
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    login_page = Login_Page(browser)

    login_page.test_login('standard_user')
    login_page.test_login_err('')
    login_page.test_password_err('secretsauce')
    login_page.test_blocked_user('locked_out_user')
    login_page.test_perfomanse_user('performance_glitch_user')

    browser.quit()

