from selenium.webdriver.common.by import By

class MainPageLocators:
    pass
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR,"div.alertinner>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert-success")
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")