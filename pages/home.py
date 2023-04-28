from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_language(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-language-picker-trigger']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='English (US)']").click()

    def get_currency(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']").click()
        self.driver.find_element(By.XPATH, "//div[normalize-space()='USD']").click()

    def get_destination(self, destination):
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Where are you going?']").send_keys(destination)
        destination = "//div[normalize-space()='" + destination + "']"
        self.driver.find_element(By.XPATH, destination).click()

    def get_dates(self, check_in, check_out):
        check_in = "span[data-date='" + str(check_in) + "']"
        check_out = "span[data-date='" + str(check_out) + "']"

        # Verify if the element already exist and click to open if not
        try:
            self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='searchbox-datepicker']")
        except NoSuchElementException:
            self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='date-display-field-start']").click()

        self.driver.find_element(By.CSS_SELECTOR, check_in).click()
        self.driver.find_element(By.CSS_SELECTOR, check_out).click()

    def get_occupancy(self):
        pass
