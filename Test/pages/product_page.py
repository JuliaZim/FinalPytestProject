from .base_page import BasePage
from .locators import BookPageLocators


class BookPage(BasePage):
    def add_book_to_basket(self):
        add_button = self.browser.find_element(*BookPageLocators.ADD_BUTTON)
        add_button.click()

