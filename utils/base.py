import pytest
from pages.home import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def base_homepage(self):
        return HomePage(self.driver)

    def base_results(self):
        pass
