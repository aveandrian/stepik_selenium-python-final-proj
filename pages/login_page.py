from .base_page import BasePage
from .locators import LoginPageLocators
import time # в начале файла

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login page not open"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_FORM) and self.is_element_present(*LoginPageLocators.LOGIN_PASS_FORM), "Login or pass form is not presented"
		
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_FORM) and self.is_element_present(*LoginPageLocators.REG_PASS1_FORM) and self.is_element_present(*LoginPageLocators.REG_PASS2_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS1_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS2_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
        
