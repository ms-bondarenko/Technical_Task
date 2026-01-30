# import selenium
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# import pytest
# import allure
# from Pages.Login_Page import Login_Page
#
# def test_Login_Page():
#     browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#
#     login_page = Login_Page(browser)
#
#     login_page.test_login('standard_user')
#     login_page.test_login_err('')
#     login_page.test_password_err('secretsauce')
#     login_page.test_blocked_user('locked_out_user')
#     login_page.test_perfomanse_user('performance_glitch_user')
#
#     browser.quit()
import subprocess

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Pages.Login_Page import Login_Page


@allure.suite('Login Page Tests')
class TestLoginPage:

    @allure.title('Test Login with valid and invalid credentials')
    def test_login_page(self):
        # Устанавливаем драйвер для Firefox
        with allure.step("Initialize the browser"):
            browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        # Создаем экземпляр страницы логина
        login_page = Login_Page(browser)

        with allure.step("Проверка валидных данных"):
            login_page.test_login('standard_user')

        with allure.step("Проверка пустого поля логина"):
            login_page.test_login_err('')

        with allure.step("Проверка с кривым паролем"):
            login_page.test_password_err('secretsauce')

        with allure.step("Проверка заблокированного юзера"):
            login_page.test_blocked_user('locked_out_user')

        with allure.step("Проверка входа с высокой нагрузкой"):
            login_page.test_perfomanse_user('performance_glitch_user')

        with allure.step("Закрытие браузера"):
            browser.quit()

if __name__ == "__main__":
    # Формируем результаты и запускаем сервер Allure
    subprocess.run(["pytest", "--alluredir=allure-results"])
    subprocess.run(["allure", "serve", "allure-results"])

