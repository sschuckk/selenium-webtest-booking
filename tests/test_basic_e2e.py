import pytest
from pages.home import HomePage


@pytest.mark.usefixtures("setup")
class TestSuite:

    def test_case1(self):
        homepage = HomePage(self.driver)
        homepage.get_language()
        homepage.get_currency()

