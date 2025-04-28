from selenium.webdriver.common.by import By

from .conftest import browser
from .pages.product_page import BookPage

def test_add_book_to_basket(browser):
    book_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    book_page = BookPage(browser, book_link)
    book_page.open()
    book_page.add_book_to_basket()
    book_page.solve_quiz_and_get_code()
