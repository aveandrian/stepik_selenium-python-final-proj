from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_LIST), "Items list is presented"

    def should_be_your_cart_is_empty_text(self):
        basket_text = self.browser.find_element(*BasketPageLocators.CART_IS_EMPTY_TEXT).text
        language = self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
        if(language == "ru"):
           assert basket_text == "Ваша корзина пуста Продолжить покупки", language
        if(language == "en"):
           assert basket_text == "Your basket is empty. Continue shopping", language
       

