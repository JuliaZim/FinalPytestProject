from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_for")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class BookPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_TEXT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    BOOK_LINK2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


