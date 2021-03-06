from selenium import webdriver
import pytest
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"								  

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    browser.get(link)
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_button_add_to_basket()
    product_page.add_product_to_basket()
    product_page.should_added_product_name_equal_product_name()
    product_page.should_added_product_price_equal_product_price()

@pytest.mark.xfail	
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.get(link)
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_button_add_to_basket()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message_after_adding_product_to_basket()
	
def test_guest_cant_see_success_message(browser):
    browser.get(link)
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message_after_adding_product_to_basket()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.get(link)
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_button_add_to_basket()
    product_page.add_product_to_basket()
    product_page.message_should_disappear_after_adding_product_to_basket()
	
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_your_cart_is_empty_text()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "ThisIsMyPass"
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        browser.get(link)
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message_after_adding_product_to_basket()

    @pytest.mark.need_review   
    def test_user_can_add_product_to_basket(self, browser):
        browser.get(link)
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_button_add_to_basket()
        product_page.add_product_to_basket()
        product_page.should_added_product_name_equal_product_name()
        product_page.should_added_product_price_equal_product_price()
