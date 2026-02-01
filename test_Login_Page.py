# import allure
# import pytest
# import subprocess
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from Pages.Login_Page import Login_Page
#
#
# @allure.suite('Login Page Tests')
# class TestLoginPage:
#
#     @allure.title('Test Login with valid and invalid credentials')
#     @allure.step("Запускаем тест входа")
#     def test_login_page(self):
#         # Устанавливаем драйвер для Firefox
#         with allure.step("Инициализация браузера"):
#             browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#
#         # Создаем экземпляр страницы логина
#         login_page = Login_Page(browser)
#
#         with allure.step("Проверка валидных данных"):
#             login_page.test_login('standard_user')
#
#         with allure.step("Проверка пустого поля логина"):
#             login_page.test_login_err('')
#
#         with allure.step("Проверка с неправильным паролем"):
#             login_page.test_password_err('secretsauce')
#
#         with allure.step("Проверка заблокированного юзера"):
#             login_page.test_blocked_user('locked_out_user')
#
#         with allure.step("Проверка входа с высокой нагрузкой"):
#             login_page.test_perfomanse_user('performance_glitch_user')
#
#         with allure.step("Закрытие браузера"):
#             browser.quit()
#
# if __name__ == "__main__":
#     pytest_result = subprocess.run(["pytest", "--alluredir=allure-results"])
#
#     if pytest_result.returncode == 0:
#         allure_result = subprocess.run(["allure", "serve", "allure-results"])
#
#         if allure_result.returncode != 0:
#             print("Не удалось запустить сервер Allure")
#     else:
#         print("Тесты завершились с ошибками. Проверьте логи для деталей.")


import allure
import pytest
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Pages.Login_Page import Login_Page


@allure.suite('Login Page Tests')
class TestLoginPage:

    @allure.title('Test Login with valid and invalid credentials')
    @allure.step("Запускаем тест входа")
    def test_login_page(self):
        with allure.step("Инициализация браузера"):
            browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        login_page = Login_Page(browser)

        with allure.step("Проверка валидных данных"):
            login_page.test_login('standard_user')

        with allure.step("Проверка пустого поля логина"):
            login_page.test_login_err('')

        with allure.step("Проверка с неправильным паролем"):
            login_page.test_password_err('secretsauce')

        with allure.step("Проверка заблокированного юзера"):
            login_page.test_blocked_user('locked_out_user')

        with allure.step("Проверка входа с высокой нагрузкой"):
            login_page.test_perfomanse_user('performance_glitch_user')

        with allure.step("Закрытие браузера"):
            browser.quit()


if __name__ == "__main__":
    # Запускаем pytest и сохраняем результаты в allure-results
    pytest_result = subprocess.run(
        ["pytest", "C:/Users/SMART/Documents/Technical_Task1/test_Login_Page.py", "--alluredir=allure-results"])

    # Если тесты прошли успешно, запускаем Allure
    if pytest_result.returncode == 0:
        subprocess.run(["allure", "serve", "allure-results"])
    else:
        print("Тесты завершились с ошибками. Проверьте логи для деталей.")
