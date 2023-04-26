import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def tear_up():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    service = Service(r"..selenium-webtest-booking\drivers")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.booking.com/")

    try:
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        driver.find_element(By.XPATH, "//button[@aria-label='Ignorar informações de login.']").click()
    except WebDriverWait:
        print("Pop-up not detected")
    #yield
    tear_down(driver)

def tear_down(driver):
    driver.close()
