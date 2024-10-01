from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_link(self):
        assert self.is_element_present(
            *ProductPageLocators.PROMO_ADD_TO_BASKET_LINK), "No 'Add to basket' link for NewYear promo found!"

    def get_product_name(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.split(', ')[-1]

    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.PROMO_ADD_TO_BASKET_LINK)
        add_to_basket_link.click()

    def check_product_name(self, product_name: str):
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME_ALERT).text
        assert basket_product_name == product_name, "Product name in basket doesn`t match"

    def check_product_price(self, product_price: str):
        basket_price_text = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
        basket_price = basket_price_text.splitlines()[0].split(":")[-1].strip()
        assert product_price == basket_price, "Basket price doesn`t match product price"

