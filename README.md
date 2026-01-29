# ТЕХНИЧЕСКОЕ ЗАДАНИЕ ДЛЯ Effective Mobile НА ВАКАНСИЮ JUNIOR AQA PYTHON

## Автотесты для Страницы входа(https://www.saucedemo.com/), в рамках ui теста произведен серия тестов Авторизаия 

### Для UI тестов применено Page Object
   

### Шаги
1. Склонировать проект 'git clone https://github.com/ms-bondarenko/Technical_Task.git'
2. Установить все зависимости из requirements.txt командой pip install -r requirements.txt
3. 1)Создать виртуальное окружение и 2)активировать его: 1)python -m venv venv, 2)venv\scripts\activate # Windows
4. Если pytest не запускает проект то установите переменную окружения
- "$env:PYTHONPATH = "путь к корневой директории проекта"
- например ($env:PYTHONPATH="C:\Users\SMART\Dcuments\Technical_Task1")

### Запуск тестов
- UI тесты: pytest test_Login_page.py #--alluredir=allure-results пока не пришит
### Просмотр Allure отчёта
#- Сформировать результаты: pytest --alluredir=allure-results
#- Запустить сервер Allure: allure serve allure-results

### Стек:
- pytest
- selenium
- allure

### Структура:
- ./pages - описание страниц

### Полезные ссылки
- [Подсказка по Markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)

### Библиотеки
- allure-pytest==2.15.0
- pytest==8.4.1
- selenium==4.34.2
- webdriver-manager==4.0.2
- allure-python-commons~=2.15.0