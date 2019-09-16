from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
#        self.solve_quiz_and_get_code()
		
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
	
    def should_added_product_name_equal_product_name(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert added_product_name.text == product_name.text, "Added product name is not equal product name on the page"
		
    def should_added_product_price_equal_product_price(self):
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert added_product_price.text == product_price.text, "Added product price is not equal product price on the page"
	
    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MES_AFTER_ADDING_TO_BASKET), "Success message after adding product to basket is presented"
		
    def message_should_disappear_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MES_AFTER_ADDING_TO_BASKET), "Success message after adding product to basket is not disappeared"