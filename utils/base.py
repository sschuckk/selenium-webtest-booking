import pytest
import pandas as pd
from datetime import datetime
from pages.home import HomePage
from pages.results import ResultsPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def base_homepage(self):
        return HomePage(self.driver)

    def base_results(self):
        return ResultsPage(self.driver)

    def html_pandas(self, data):
        df = pd.DataFrame(data, columns=['Hotel Name', 'Price (USD)', 'User Score'])

        styled_df = df.style.highlight_max(color='lightgreen', subset=["User Score"])
        html = styled_df.to_html(index=False, classes='table', border=0, escape=False)

        # write html to file
        filename = f"../reports/search-result_{datetime.now().strftime('%Y-%m-%d_%H-%M%p')}.html"
        with open(filename, "w") as f:
            f.write(html)
            f.close()
