from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ya():
    # Перешли на ya.ru
    ya_url = 'https://ya.ru/'
    driver = webdriver.Chrome()
    driver.get(ya_url)

    # Нашли поле поиска и написали привет мир
    search_field = driver.find_element(By.ID, "text")
    search_field.send_keys("Hello world")

    # Кнопки "Найти" на яндексе нет, поэтому просто отправим энтер
    search_field.send_keys(Keys.ENTER)

    driver.quit()


test_ya()
