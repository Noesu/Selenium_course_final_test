from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")


class BasketPageLocators():
    BASKET_NOT_EMPTY = (By.CLASS_NAME, "basket-items")


class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    PROMO_ADD_TO_BASKET_LINK = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
    BASKET_PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, ".alertinner:first-of-type strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")




