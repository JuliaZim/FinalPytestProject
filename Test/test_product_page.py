from selenium.webdriver.common.by import By

from .conftest import browser
from .pages.locators import BookPageLocators
from .pages.product_page import BookPage

def test_add_book_to_basket(browser):
    book_link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    book_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    book_page = BookPage(browser, BookPageLocators.BOOK_LINK)
    book_page.open()
    name = book_page.prepare_expected_result("name")
    price = book_page.prepare_expected_result("price")
    book_page.add_book_to_basket()
    book_page.add_value_to_popup()
    book_page.should_be_message_book()
    book_page.should_be_expected_item_in_basket(name, price)