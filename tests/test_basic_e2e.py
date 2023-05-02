import pytest
import datetime
from utils.base import BaseClass


class TestSuite(BaseClass):

    def test_language(self):
        self.base_homepage().get_language()

    def test_currency(self):
        self.base_homepage().get_currency()

    def test_destination(self):
        self.base_homepage().get_destination(destination="New York")

    def test_dates(self):
        check_in = datetime.date.today() + datetime.timedelta(days=1)
        check_out = datetime.date.today() + datetime.timedelta(days=3)
        self.base_homepage().get_dates(check_in, check_out)

    def test_occupancy(self):
        # The occupancy value must be the range of 1~30
        self.base_homepage().get_occupancy(adults=4)

    def test_search(self):
        self.base_homepage().get_search()

    def test_filter_rating(self):
        self.base_results().filter_by_rating(stars=["3", "4", "5"])

    def test_filter_distance(self):
        self.base_results().filter_by_distance(distance="5000")

    def test_sort_by(self):
        self.base_results().sort_by_price()

    def test_result_list(self):
        self.base_results().get_result_list()