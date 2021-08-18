
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_not_be_items()
        self.should_be_empty_message()

    def should_not_be_items(self):
        assert self.is_element_not_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty, but it should be'

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No 'empty basket' message present"
