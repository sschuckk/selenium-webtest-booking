from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_language(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-language-picker-trigger']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='English (US)']").click()

    def get_currency(self):
        self.driver.find_element(By.XPATH, "(//span[@class='cb5ebe3ffb'])[1]").click()
        self.driver.find_element(By.XPATH, "//div[normalize-space()='USD']").click()

    def get_destination(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Where are you going?']")

    def get_dates(self):
        pass

    def get_occupancy(self):
        pass
