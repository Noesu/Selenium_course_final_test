from .base_page import BasePagefrom .locators import LoginPageLocatorsclass LoginPage(BasePage):    def register_new_user(self, email: str, password: str):        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)        email_field.send_keys(email)        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_FIELD)        password1_field.send_keys(password)        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_FIELD)        password2_field.send_keys(password)        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)        register_button.click()    def should_be_login_form(self):        assert self.is_element_present(            *LoginPageLocators.LOGIN_EMAIL_FIELD), "Login email field is not presented"        assert self.is_element_present(            *LoginPageLocators.LOGIN_PASSWORD_FIELD), "Login password field is not presented"    def should_be_login_page(self):        self.should_be_login_url()        self.should_be_login_form()        self.should_be_register_form()    def should_be_login_url(self):        assert self.browser.current_url == self.url    def should_be_register_form(self):        assert self.is_element_present(            *LoginPageLocators.REGISTRATION_EMAIL_FIELD), "Registration email field is not presented"        assert self.is_element_present(            *LoginPageLocators.REGISTRATION_PASSWORD1_FIELD), "Registration password1 field is not presented"        assert self.is_element_present(            *LoginPageLocators.REGISTRATION_PASSWORD2_FIELD), "Registration password2 field is not presented"