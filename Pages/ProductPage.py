import time
from Utilities.AssertMessage import AssertTitle as info
from Pages.BasePage import BasePage
from Pages.LoginPage import Login
from Utilities import ReadConfigurations as rc
from Locators.ProductLocator import ProductLocators as pc
from Utilities.AssertMessage import ErrorMessage as error
class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        config = rc.Configuration()
        self.url = config.get_url()
        self.driver.get(self.url)
        self.loginPage = Login(driver)

    def get_page_title(self):
        self.assert_equal_title(info.home_page_title, error.title_error_message)

    def login(self, email, password):
        self.loginPage.get_login(email, password)

    def search_product(self,product):
        self.do_click(pc.Product_Button)
        self.assert_equal_title(info.product_page_title,error.product_page_error_message)
        self.do_send_keys(pc.Search_Box,product)
        self.do_click(pc.Search_Button)
        # get_product=self.get_element_text(pc.Product_Verification)
        # assert get_product == product,error.search_error_message
        self.assert_equal_check_element(pc.Product_Verification,product,error.search_error_message)
        self.do_click(pc.Add_To_Cart)
        self.do_click(pc.Continue_Shopping)
        self.do_click(pc.Cart_Button)
        # item=self.get_element_text(pc.Product_In_Cart_Verification)
        # assert item == product, error.product_error_message
        self.assert_equal_check_element(pc.Product_In_Cart_Verification,product,error.product_error_message)

    def verify_product_in_cart_after_login(self,product,email,password):
        self.login(email, password)
        self.do_click(pc.Cart_Button)
        # item = self.get_element_text(pc.Product_In_Cart_Verification)
        # assert item == product, error.product_login_error_message
        self.assert_equal_check_element(pc.Product_In_Cart_Verification,product,error.product_login_error_message)



