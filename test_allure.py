import subprocess

# Запускаем скрипт test_Login_Page.py
test_process = subprocess.Popen(
    ["python", "C:/Users/SMART/Documents/Technical_Task1/test_Login_Page.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Ждем завершения процесса
stdout, stderr = test_process.communicate()

# Выводим результаты
if test_process.returncode == 0:
    print("Тесты успешно завершены.")
    print(stdout.decode())  # Выводим стандартный вывод тестов
else:
    print("Ошибка при выполнении тестов.")
    print(stderr.decode())  # Выводим ошибки, если есть

# Запускаем Allure для отображения результатов
allure_process = subprocess.Popen(
    ["cmd.exe", "/c", "start", "C:\\Users\\SMART\\Desktop\\allure-2.35.1\\bin\\allure.bat", "serve", "allure-results"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("Allure запущен. Для завершения закройте окно Allure.")

# Ожидаем завершения процесса Allure
try:
    allure_process.wait()
except KeyboardInterrupt:
    allure_process.terminate()
    print("Allure закрыт.")


