from selenium.webdriver.common.by import By

from .conftest import browser
from .pages.locators import BookPageLocators
from .pages.product_page import BookPage

def test_add_book_to_basket(browser):
    book_link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    book_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    book_page = BookPage(browser, BookPageLocators.BOOK_LINK2)
    book_page.open()
    book_page.add_book_to_basket()
    book_page.solve_quiz_and_get_code()
    book_name = book_page.search_book_name()
    book_page.should_be_add_to_basket(book_name)
