from selene import be, have, browser
import pytest


def test_google_search_find(browser_screen_resolution):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_not_find(browser_screen_resolution):
    browser.element('[name="q"]').should(be.blank).type('lfhslfhslhfsdf;oisdi2388392392').press_enter()
    browser.element('.card-section [role="heading"]').should(have.text('ничего не найдено'))