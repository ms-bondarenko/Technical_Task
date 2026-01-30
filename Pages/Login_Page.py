from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import base_url
import allure

class Login_Page:
    def __init__(self, driver):
        self._url = base_url
        self._driver = driver

    def test_login(self, term):
        self._driver.get(self._url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

        # Вводим логин и пароль
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        current_url = self._driver.current_url
        assert current_url == "https://www.saucedemo.com/inventory.html", (
            f"Expected URL: 'https://www.saucedemo.com/inventory.html', "
            f"but got: '{current_url}'"
        )

            # Проверяем, что заголовок страницы корректный
        try:
            title_element = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'title'))
            )
            assert title_element.text == 'Products', (
                f"Expected text: 'Products', but got: '{title_element.text}'"
            )
            print("URL и текст на странице соответствуют ожиданиям.")
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Ошибка: {str(e)}")  # Обрабатываем исключения


    def test_login_err(self, term):
        self._driver.get(self._url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

        # Вводим логин и пароль
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        try:
            # Проверка на наличие сообщения об ошибке
            error_element = WebDriverWait(self._driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.error-message-container'))
            )
            print(f"Неверный логин: {error_element.text}")  # Выводим сообщение об ошибке
            print("Тест признан положительным, так как произошла ошибка входа.")
            return  # Завершаем функцию без выброса ошибки
        except TimeoutException:
            # Если ошибок не оказалось, проверяем, что страницы указаны правильно
            current_url = self._driver.current_url
            if current_url == "https://www.saucedemo.com/inventory.html":
                print("Не должно было пройти авторизацию, но она прошла. Провал теста.")
            else:
                print(f"Ожидаемый URL: 'https://www.saucedemo.com/inventory.html', "
                      f"но получили: '{current_url}'")

    def test_password_err(self, term):
        self._driver.get(self._url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        try:
            # Проверка на наличие сообщения об ошибке
            error_element = WebDriverWait(self._driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.error-message-container'))
            )
            print(f"Неверный пароль: {error_element.text}")  # Выводим сообщение об ошибке
            print("Тест признан положительным, так как произошла ошибка входа.")

        except TimeoutException:
            # Если ошибок не оказалось, проверяем текущий URL
            current_url = self._driver.current_url
            if current_url == "https://www.saucedemo.com/inventory.html":
                print("Авторизация прошла успешно, хотя этого не должно было произойти. Провал теста.")
            else:
                print(f"Ожидаемый URL: 'https://www.saucedemo.com/inventory.html', "
                      f"но получили: '{current_url}'")

    def test_blocked_user(self, term):

        self._driver.get(self._url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

        # Вводим логин и пароль
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        try:
            # Проверка на наличие сообщения об ошибке
            error_element = WebDriverWait(self._driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.error-message-container'))
            )
            error_text = error_element.text

            if "Epic sadface: Sorry, this user has been locked out." in error_text:
                print("Пользователь заблокирован. Тест признан положительным.")
            else:
                print(f"Неверный логин: {error_text}")  # Выводим другое сообщение об ошибке

        except TimeoutException:
            # Если ошибок не оказалось, проверяем текущий URL
            current_url = self._driver.current_url
            if current_url == "https://www.saucedemo.com/inventory.html":
                print("Авторизация прошла успешно, хотя этого не должно было произойти. Провал теста.")
            else:
                print(f"Ожидаемый URL: 'https://www.saucedemo.com/inventory.html', "
                      f"но получили: '{current_url}'")

    def test_perfomanse_user(self, term):
        self._driver.get(self._url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

        # Вводим логин и пароль
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

        WebDriverWait(self._driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#shopping_cart_container')))
        current_url = self._driver.current_url
        assert current_url == "https://www.saucedemo.com/inventory.html", (
            f"Expected URL: 'https://www.saucedemo.com/inventory.html', "
            f"but got: '{current_url}'"
        )
        print('тест с задержкой признан положительным')






