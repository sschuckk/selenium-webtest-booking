import pytest
from utils.base import BaseClass
import datetime


class TestSuite(BaseClass):

    def test_language(self):
        self.base_homepage().get_language()

    def test_currency(self):
        self.base_homepage().get_currency()

    def test_destination(self):
        self.base_homepage().get_destination("New York")

    def test_dates(self):
        check_in = datetime.date.today() + datetime.timedelta(days=1)
        check_out = datetime.date.today() + datetime.timedelta(days=3)
        self.base_homepage().get_dates(check_in, check_out)

    def test_occupancy(self):
        self.base_homepage().get_occupancy()
