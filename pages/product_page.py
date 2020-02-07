from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
    def should_be_notification_title(self): #уведомление о том, что товар добавлен в корзину
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        notification_item_added = self.browser.find_element(*ProductPageLocators.NOTIFICATION_ITEM_ADDED).text
        assert item_name == notification_item_added, "item name is not correct"
    def should_be_notification_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        notification_price_added = self.browser.find_element(*ProductPageLocators.NOTIFICATION_PRICE_ADDED).text
        assert item_price == notification_price_added, "price is different"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    def success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should disappear"

    