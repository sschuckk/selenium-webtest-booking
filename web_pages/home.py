from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class HomePage(object):
    """Represents the home page of the www.booking.com web application and provides methods to interact with its
    principal elements.
    """
    def __init__(self, driver: WebDriver):
        """Initializes the HomePage object with a WebDriver instance.

        Args:
            driver (WebDriver): The WebDriver instance used for web automation.
        """
        self.driver = driver

    def get_select_language(self):
        """Finds and returns the 'Select Language' button element on the page."""
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-language-picker-trigger']")

    def get_us_language(self):
        """Finds and returns the 'English (US)' language option element."""
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='English (US)']")

    def get_select_currency(self):
        """Finds and returns the 'Select Currency' button element."""
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")

    def get_us_currency(self):
        """Finds and returns the 'USD' currency option element."""
        return self.driver.find_element(By.XPATH, "//div[normalize-space()='USD']")

    def get_destination(self):
        """Finds and returns the destination input field element."""
        return self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Where are you going?']")

    def get_destination_value(self):
        """Finds and returns the attribute value of destination input field."""
        return self.driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Where are you going?']").get_attribute('value')

    def get_city_destination(self, destination):
        """Find and return the web element corresponding to the given city destination.

        Args:
            destination (str): The name of the city destination to locate.

        Returns:
            WebElement: The web element representing the specified city destination.
        """
        destination = "//div[normalize-space()='" + destination + "']"
        return self.driver.find_element(By.XPATH, destination)

    def get_date_box(self):
        """Find and return the date box web element for selecting dates.

        This function first attempts to locate the date box using a CSS selector. If the element is not found,
        it prints a warning message and then tries to locate the date box using a button element.

        Returns:
            WebElement: The date box web element for selecting dates.

        Raises:
            NoSuchElementException: If the date box cannot be found by default.
        """
        try:
            self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='searchbox-datepicker']")
        except NoSuchElementException:
            print("Warning: Element not found by default!")
            return self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='date-display-field-start']")

    def get_date_picker(self, date):
        """Find and return the date picker element for the specified date.

        Args:
            date (str): The target date in the format YYYY/MM/DD.

        Returns:
            WebElement: The date picker element for the specified date.
        """
        pick_date = f"span[data-date='{date}']"
        return self.driver.find_element(By.CSS_SELECTOR, pick_date)

    def get_occupancy_box(self):
        """Find and return the occupancy box element."""
        return self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='occupancy-config']")

    def get_increase_occupancy_adult(self):
        """Find and return the button to increase the number of adult occupants."""
        return self.driver.find_element(By.XPATH, "(//button[@type='button'])[8]")

    def get_decrease_occupancy_adult(self):
        """Find and return the button to decrease the number of adult occupants."""
        return self.driver.find_element(By.XPATH, "(//button[@type='button'])[7]")

    def get_number_adults(self):
        """Get the current number of adult occupants from the occupancy box element."""
        return int(self.driver.find_element(By.ID, "group_adults").get_attribute('value'))

    def get_occupancy_button_done(self):
        """Find and return the 'Done' button element in the occupancy box configuration."""
        return self.driver.find_element(By.XPATH, "(//button[@type='button'])[13]")

    def get_button_search(self):
        """Find and return the search button element on the web page."""
        return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'] span")
