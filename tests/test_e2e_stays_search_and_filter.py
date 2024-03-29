import pytest
import datetime
from utils.base import BaseClass
from time import sleep

class TestSuite(BaseClass):
    """An E2E Test Suite for testing various functionalities of the www.booking.com website.

    This test suite adopts an end-user perspective, simulating real-user scenarios that cover different aspects of the
    hotel booking application. These aspects include language selection, currency selection, city destination search,
    date selection, occupancy management, search options, and the application of filters to show personalized results.
    """
    def test_language(self):
        """Test language selection choosing US as option."""
        self.base_homepage().get_select_language().click()
        self.base_homepage().get_us_language().click()

    def test_currency(self):
        """Test currency selection choosing US Dollar as option."""
        self.base_homepage().get_select_currency().click()
        self.base_homepage().get_us_currency().click()

    def test_city_destination(self):
        """Test destination input field by passing a city name."""
        destination = "New York"
        self.base_homepage().get_destination().send_keys(destination)
        self.base_homepage().get_city_destination(destination).click()

    def test_dates(self):
        """Test check-in and check-out dates using the current date + delta date."""
        check_in = datetime.date.today() + datetime.timedelta(days=1)
        check_out = datetime.date.today() + datetime.timedelta(days=3)
        self.base_homepage().get_date_box().click()
        self.base_homepage().get_date_picker(check_in).click()
        self.base_homepage().get_date_picker(check_out).click()

    def test_occupancy(self):
        """Test occupancy configuration by setting the number of adult by increasing and decreasing the count."""
        self.base_homepage().get_occupancy_box().click()
        self.base_homepage().get_increase_occupancy_adult().click()
        self.base_homepage().get_increase_occupancy_adult().click()
        self.base_homepage().get_decrease_occupancy_adult().click()
        self.base_homepage().get_occupancy_button_done().click()

    def test_search_options(self):
        """Test the click at search button"""
        self.base_homepage().get_button_search().click()

    @pytest.mark.parametrize("star", ["3", "4", "5"])
    def test_filter_rating(self, star):
        """Test the selection of filters by star ratings with parameterized multiple input values."""
        self.base_results().filter_by_rating(star).click()

    def test_filter_distance(self):
        """Test the filter by distance functionality with a specified distance"""
        self.base_results().filter_by_distance(distance="3220").click()

    def test_sort_by_price(self):
        """Test the sorting of hotel results by selecting 'sort by price' from a dropdown menu."""
        self.base_results().sort_dropdown_trigger().click()
        self.base_results().sort_by_price().click()

    def test_city_destination_result(self):
        """Verify if the city destination is the same after search action."""
        destination = "New York"
        assert self.base_homepage().get_destination_value() == destination

    def test_dates_result(self):
        """Verify if the check-in and check-out dates is the same after search action."""
        check_in = datetime.date.today() + datetime.timedelta(days=1)
        check_out = datetime.date.today() + datetime.timedelta(days=3)
        self.base_homepage().get_date_box().click()
        assert self.base_homepage().get_date_picker(check_in).get_attribute('aria-checked') == "true"
        assert self.base_homepage().get_date_picker(check_out).get_attribute('aria-checked') == "true"

    def test_adult_number_result(self):
        """Verify if the number of adults is the same after search action."""
        self.base_homepage().get_occupancy_box().click()
        assert self.base_homepage().get_number_adults() == "3"

    def test_result_list(self):
        """Verify hotel list results"""
        hotel_lst = self.base_results().get_result_list()
        self.html_pandas(hotel_lst)
