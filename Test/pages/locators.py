from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_for")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class BookPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")

    EXPECTED_NAME_OF_BOOK = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    EXPECTED_PRICE_OF_BOOK = (By.CSS_SELECTOR, "p.price_color")


    MESSAGE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner")
    ACTUAL_NAME_OF_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner strong")
    MESSAGE_PRICE_OF_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p")
    ACTUAL_PRICE_OF_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p strong")

    BOOK_LINK2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    BOOK_LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
