import pytest
from utils.base import BaseClass


class TestSuite(BaseClass):

    def test_language(self):
        self.base_homepage().get_language()

    def test_currency(self):
        self.base_homepage().get_currency()

    def test_destination(self):
        self.base_homepage().get_destination("New York")

    def test_dates(self):
        self.base_homepage().get_dates()

    def test_occupancy(self):
        self.base_homepage().get_occupancy()
