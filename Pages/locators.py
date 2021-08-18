
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages div:first-child div strong')
    BASKET_TOTAL = (By.CSS_SELECTOR, '#messages div:nth-child(3) p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success:first-child')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, 'div.basket_items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner > p')
