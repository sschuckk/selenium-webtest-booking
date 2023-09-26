from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class HomePage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_select_language(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-language-picker-trigger']")

    def get_us_language(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='English (US)']")

    def get_select_currency(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")

    def get_us_currency(self):
        return self.driver.find_element(By.XPATH, "//div[normalize-space()='USD']")

    def get_destination(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Where are you going?']")

    def get_city_destination(self, destination):
        destination = "//div[normalize-space()='" + destination + "']"
        return self.driver.find_element(By.XPATH, destination)

    def get_date_box(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='searchbox-datepicker']")
        except NoSuchElementException:
            print("Warning: Element not found by default!")
            return self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='date-display-field-start']")

    def get_date_picker(self, date):
        pick_date = f"span[data-date='{date}']"
        return self.driver.find_element(By.CSS_SELECTOR, pick_date)

    def get_occupancy_box(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='occupancy-config']")

    def get_increase_occupancy_adult(self):
        return self.driver.find_element(By.XPATH, "(//button[@type='button'])[8]")

    def get_decrease_occupancy_adult(self):
        return self.driver.find_element(By.XPATH, "(//button[@type='button'])[7]")

    def get_number_adults(self):
        return int(self.driver.find_element(By.ID, "group_adults").get_attribute('value'))

    def get_button_done(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Done']")

    def get_search(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'] span").click()
