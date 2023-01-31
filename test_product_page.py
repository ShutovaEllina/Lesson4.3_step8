import time

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
   # link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    #page = ProductPage(browser, link)
    #page.open()
    #page.add_to_cart_page()
    #assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

#def test_guest_cant_see_success_message(browser):
    #link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    #page = ProductPage(browser, link)
    #page.open()
    #assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

#def test_message_disappeared_after_adding_product_to_basket(browser):
#    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
 #   page = ProductPage(browser, link)
  #  page.open()
   # page.add_to_cart_page()
    #assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Sucsess messege isnt disappeared'

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

