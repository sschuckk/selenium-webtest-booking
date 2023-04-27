from selenium.webdriver.common.by import By

class HomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_language(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-language-picker-trigger']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='English (US)']").click()

    def get_currency(self):
        self.driver.find_element(By.XPATH, "(//span[@class='cb5ebe3ffb'])[1]").click()
        self.driver.find_element(By.XPATH, "//div[normalize-space()='USD']").click()

    def get_destination(self, destination):
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Where are you going?']").send_keys(destination)
        destination = "//div[normalize-space()='" + destination + "']"
        self.driver.find_element(By.XPATH, destination).click()

    def get_dates(self):
        pass

    def get_occupancy(self):
        pass
