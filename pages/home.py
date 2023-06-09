from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class HomePage(object):

    def __init__(self, driver: WebDriver):
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
        check_in = f"span[data-date='{check_in}']"
        check_out = f"span[data-date='{check_out}']"

        # Verify if the element already exist and click to open/show if not
        try:
            self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='searchbox-datepicker']")
        except NoSuchElementException:
            print("Warning: Element not found by default!")
            self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='date-display-field-start']").click()

        self.driver.find_element(By.CSS_SELECTOR, check_in).click()
        self.driver.find_element(By.CSS_SELECTOR, check_out).click()

    def get_occupancy(self, adults):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='occupancy-config']").click()
        increase_adult = self.driver.find_element(By.XPATH, "(//button[@type='button'])[8]")
        decrease_adult = self.driver.find_element(By.XPATH, "(//button[@type='button'])[7]")
        while True:
            current_adults = int(self.driver.find_element(By.ID, "group_adults").get_attribute('value'))
            if adults > current_adults:
                increase_adult.click()
            elif adults < current_adults:
                decrease_adult.click()
            else:
                break

        self.driver.find_element(By.XPATH, "//span[normalize-space()='Done']").click()

    def get_search(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'] span").click()
