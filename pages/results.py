from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep


class ResultsPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def filter_by_rating(self, star):
        """
        Find and returns the first search result element matching the specified star rating for Property Rating.

        Args:
            star (int): The star rating (1 to 5) to filter the results.

        Returns:
             WebElement: The first search result element matching the specified star rating.
        """
        return self.driver.find_element(By.XPATH, f"(//div[@data-filters-item='class:class={star}'])[1]")

    def filter_by_distance(self, distance):
        self.driver.find_element(By.XPATH, f"(//div[@data-filters-item='distance:distance={distance}'])[1]").click()

    def sort_by_price(self):
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='sorters-dropdown-trigger']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[data-id='price']").click()

    def get_result_list(self):
        sleep(3)
        hotel_lst = []
        result_list = self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")

        for i in result_list:
            name = i.find_element(By.CSS_SELECTOR,
                                  "div[data-testid='title']").get_attribute('innerHTML').strip()
            price = i.find_element(By.CSS_SELECTOR,
                                   "span[data-testid='price-and-discounted-price']").get_attribute('innerHTML').strip()

            try:
                score = i.find_element(
                    By.CSS_SELECTOR, "div[data-testid='review-score']").find_element(
                    By.CLASS_NAME, 'b5cd09854e').get_attribute('innerHTML').strip()
            except NoSuchElementException:
                score = " "

            hotel_lst.append([name, price, score])

        for i in hotel_lst:
            print(i)

        return hotel_lst
