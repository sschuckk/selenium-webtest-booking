import datetime

import pytest

from utils.base import BaseClass
import time

class TestSuite(BaseClass):

    def test_language(self):
        self.base_homepage().get_select_language().click()
        self.base_homepage().get_us_language().click()

    def test_currency(self):
        self.base_homepage().get_select_currency().click()
        self.base_homepage().get_us_currency().click()

    def test_destination(self):
        destination = "New York"
        self.base_homepage().get_destination().send_keys(destination)
        self.base_homepage().get_city_destination(destination).click()

    def test_dates(self):
        time.sleep(2)
        check_in = datetime.date.today() + datetime.timedelta(days=1)
        check_out = datetime.date.today() + datetime.timedelta(days=3)
        self.base_homepage().get_date_box().click()
        self.base_homepage().get_date_picker(check_in).click()
        self.base_homepage().get_date_picker(check_out).click()

    def test_occupancy(self):
        self.base_homepage().get_occupancy_box().click()
        self.base_homepage().get_increase_occupancy_adult().click()
        self.base_homepage().get_increase_occupancy_adult().click()
        self.base_homepage().get_decrease_occupancy_adult().click()
        self.base_homepage().get_occupancy_button_done().click()

    def test_search(self):
        self.base_homepage().get_button_search().click()

    @pytest.mark.parametrize("star", ["3", "4", "5"])
    def test_filter_rating(self, star):
        self.base_results().filter_by_rating(star).click()

    def test_filter_distance(self):
        self.base_results().filter_by_distance(distance="3220")

    def test_sort_by(self):
        self.base_results().sort_by_price()

    def test_result_list(self):
        hotel_lst = self.base_results().get_result_list()
        self.html_pandas(hotel_lst)
