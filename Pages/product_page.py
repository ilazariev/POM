
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_added_correctly(self):
        self.should_be_correct_name()
        self.should_be_correct_basket_total()

    def should_be_correct_name(self):
        correct_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        gotten_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert correct_name == gotten_name, f'Wrong item added to the basket. \
        Expected {correct_name}, got {gotten_name}.'

    def should_be_correct_basket_total(self):
        correct_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        gotten_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert correct_price == gotten_price, f'Wrong basket total. \
        Expected {correct_price}, got {gotten_price}.'
