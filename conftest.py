from selene import browser
import pytest


@pytest.fixture
def browser_open():
    browser.open('https://google.com')


@pytest.fixture
def browser_screen_resolution(browser_open):
    browser.driver.set_window_size(1600, 900)
