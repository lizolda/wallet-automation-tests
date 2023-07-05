import pytest
import os
import selenium.webdriver as webdriver


@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(20)
    b.maximize_window()
    yield b
    b.quit()


@pytest.fixture
def url():
    url = os.getenv(
        "WALLET_APP_URL", "http://qa-hiring-test.s3-website.us-east-2.amazonaws.com/")

    return url

