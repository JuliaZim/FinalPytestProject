from urllib3 import request
from selenium.webdriver.chrome.options import Options
from .base_page import BasePage
from .locators import BookPageLocators
from ..conftest import browser



class BookPage(BasePage):
    def add_book_to_basket(self):
        add_button = self.browser.find_element(*BookPageLocators.ADD_BUTTON)
        add_button.click()
    def should_be_add_to_basket(self, book_name):
        book_name = self.browser.find_element(*BookPageLocators.BOOK_NAME).text
        success_text = book_name + " был добавлен в вашу корзину."
        success_text_en = book_name + " has been added to your basket."
        print(success_text)
        print(self.browser.find_element(*BookPageLocators.SUCCESS_TEXT).text)
        assert success_text in self.browser.find_element(*BookPageLocators.SUCCESS_TEXT).text, "Текст несовпадает"
        #assert success_text_en in self.browser.find_element(*BookPageLocators.SUCCESS_TEXT).text, "Текст несовпадает"
    def search_book_name(self):
        book_name = self.browser.find_element(*BookPageLocators.BOOK_NAME).text
        return book_name

