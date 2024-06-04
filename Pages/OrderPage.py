from Utilities.AssertMessage import AssertTitle as info
from Pages.BasePage import BasePage
from Utilities import ReadConfigurations as rc
from Pages.LoginPage import Login
from Locators.OrderLocator import OrderLocators as oc
from Utilities.AssertMessage import User_Query as user
from Utilities.AssertMessage import ErrorMessage as error
class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        config = rc.Configuration()
        self.url = config.get_url()
        self.driver.get(self.url)
        self.loginPage = Login(driver)

    def login(self, email, password):
        self.loginPage.get_login(email, password)

    def get_page_title(self):
        self.assert_equal_title(info.home_page_title,error.title_error_message)
    def scroll_to_product(self):
        self.scroll_to_element(oc.Product)

    def add_to_cart(self):
        self.do_click(oc.Add_To_Cart)
        # return self.get_element_text(oc.Product_Added)
        # title=self.get_element_text(oc.Product_Added)
        self.assert_equal_check_element(oc.Product_Added,info.add_to_cart_title, error.cart_error_message)


    def place_order(self, payment):
        self.do_click(oc.Continue_Shopping)
        self.do_click(oc.Cart)
        self.assert_equal_url(user.cart,error.order_page_error_message)
        self.do_click(oc.Checkout)
        self.do_click(oc.Place_Order)
        self.do_send_keys(oc.Name_On_Card, payment['name'])
        self.do_send_keys(oc.Card_Number, payment['card number'])
        self.do_send_keys(oc.CVC, payment['cvc'])
        self.do_send_keys(oc.Expiry_Month, payment['expiry-month'])
        self.do_send_keys(oc.Expiry_Year, payment['expiry-year'])
        self.do_click(oc.Submit)
        self.assert_equal_url(user.payment,error.payment_error_message)
        self.do_click(oc.Continue)
        self.assert_equal_title(info.home_page_title,error.title_error_message)

    def get_login(self,email,password):
        self.login(email, password)
        logout=self.get_element_text(oc.Logout)
        assert logout==info.logout

