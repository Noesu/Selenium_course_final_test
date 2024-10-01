from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators:
    PROMO_ADD_TO_BASKET_LINK = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
    BASKET_PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, ".alertinner:first-of-type strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".basket-mini")



