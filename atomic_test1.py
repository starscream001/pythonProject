import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://atomicwallet.io/awc-staking")
time.sleep(10)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
calcul = driver.find_element(By.CSS_SELECTOR, ".slider-calc-field__val")

# Напишем текст ответа в найденное поле
calcul.send_keys("22222")
time.sleep(15)

# Найдем кнопку, которая отправляет введенное решение
stake_button = driver.find_element(By.XPATH, "/html/body/main/section/section[1]/div/div[2]/form/a")


# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
stake_button.click()
time.sleep(5)

# Поиск и проверка попадания на главную страницу
title_text = driver.find_element(By.XPATH, "/html/body/main/section/div/div/div[1]/h2")
if title_text.text == "4 steps to get your AWC rewards":
    print("Мы попали на главную страницу")
else:
    print("Ошибка поиска элемента")

time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()