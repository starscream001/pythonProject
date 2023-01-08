import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element_by_id("//*[@id=\"user-name\"]")
    input_password = driver.find_element_by_id("//*[@id=\"password\"]")
    login_button = driver.find_element_by_id("//*[@id=\"login-button\"]")

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element_by_id("//*[@id=\"header_container\"]/div[2]/span")
    if title_text.text == "PRODUCTS":
        print("Мы попали на главную страницу")
    else:
        print("Ошибка поиска элемента")

    time.sleep(5)


if __name__ == '__main__':
    first_test()