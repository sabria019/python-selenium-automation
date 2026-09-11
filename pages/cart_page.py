from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    # Strings:
    cart_empty_txt = 'Your cart is empty'

    def verify_empty_cart_msg(self):
        actual_text = self.get_element_text(*self.CART_EMPTY_MSG)
        assert actual_text == self.cart_empty_txt, f'Expected {self.cart_empty_txt}, but got {actual_text}'