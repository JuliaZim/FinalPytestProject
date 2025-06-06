from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'URL некорректный'
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),  'Форма логина отутствует'
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма регистрации отсутствует'
        assert True