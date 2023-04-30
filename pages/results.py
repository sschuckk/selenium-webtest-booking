from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class ResultsPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def filter_by_rating(self, stars):
        for star in stars:
            self.driver.find_element(By.XPATH, f"(//div[@data-filters-item='class:class={star}'])[1]").click()

    def filter_by_distance(self, distance):
        self.driver.find_element(By.XPATH, f"(//div[@data-filters-item='distance:distance={distance}'])[1]").click()
        sleep(10)
    def sort_by_price(self):
        pass
