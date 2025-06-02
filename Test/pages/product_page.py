from urllib3 import request
from selenium.webdriver.chrome.options import Options
from .base_page import BasePage
from .locators import BookPageLocators
from ..conftest import browser



class BookPage(BasePage):
    def prepare_expected_result(self, field_name=""):
        if field_name == "name": expected_result = self.browser.find_element(
            *BookPageLocators.EXPECTED_NAME_OF_BOOK).text
        if field_name == "price": expected_result = self.browser.find_element(
            *BookPageLocators.EXPECTED_PRICE_OF_BOOK).text
        return expected_result
    #Добавить в корзину
    def add_book_to_basket(self):
        add_button = self.browser.find_element(*BookPageLocators.ADD_BUTTON)
        add_button.click()

    def add_value_to_popup(self):
        BasePage.solve_quiz_and_get_code(self)
    #Проверить, что появилась надпись о добавлении в корзину
    def should_be_message_book(self):
        assert self.is_element_present(
            *BookPageLocators.MESSAGE_BOOK_IN_BASKET), 'Message about adding book to basket is not presented'
    #Проверка соответствия книги в сообщении
    def should_be_name_of_book(self, expected_book):
        actual_name = self.browser.find_element(*BookPageLocators.ACTUAL_NAME_OF_BOOK).text
        assert actual_name == expected_book, f"фактическое имя '{actual_name}' не соответствует ожидаемому '{expected_book}'"

    def should_be_message_price(self):
        assert self.is_element_present(
            *BookPageLocators.MESSAGE_PRICE_OF_BASKET).text, 'Message about price in basket is not presented'

    def should_be_price_of_book(self, expected_price):
        actual_price = self.browser.find_element(*BookPageLocators.ACTUAL_PRICE_OF_BOOK).text
        assert actual_price == expected_price, f"The price {actual_price} in basket doesn't equal {expected_price}"

    def should_be_expected_item_in_basket(self, actual_name="", actual_price=""):
        self.should_be_message_book()
        self.should_be_name_of_book(actual_name)
        self.should_be_message_price()
        self.should_be_price_of_book(actual_price)
