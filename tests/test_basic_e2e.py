import pytest
from utils.base import BaseClass


class TestSuite(BaseClass):

    def test_language(self):
        self.base_homepage().get_language()

    def test_currency(self):
        self.base_homepage().get_currency()
