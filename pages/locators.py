from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
    LOGIN_USERNAME_FORM = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS_FORM = (By.CSS_SELECTOR, "#id_login-password")
    REG_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2_FORM = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MES_AFTER_ADDING_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
	
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")