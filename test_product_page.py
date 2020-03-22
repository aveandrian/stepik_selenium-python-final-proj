from selenium import webdriver
import pytest
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

'''
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])    
'''								  

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

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_your_cart_is_empty_text()
    
