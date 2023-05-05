import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(autouse=True, scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    service = Service(r"..selenium-webtest-booking\drivers")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.booking.com/")
    request.cls.driver = driver

    try:
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        driver.find_element(By.CLASS_NAME,
                            "fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.ae1678b153").click()
    except WebDriverWait:
        print("Pop-up not detected")

    yield
    driver.close()
