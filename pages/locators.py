from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.TAG_NAME, "h1")
    NOTIFICATION_ITEM_ADDED = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) >.alertinner > strong")
    ITEM_PRICE = (By.CSS_SELECTOR, "p.price_color")
    NOTIFICATION_PRICE_ADDED = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) >.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")

class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")