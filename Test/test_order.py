from Pages.LoginPage import Login
from Pages.OrderPage import OrderPage
from Test.test_base import BaseTest
from Utilities.ReadExcelData import DataProvider

class Test_Order(BaseTest):
    data_provider=DataProvider()
    def test_page_title(self):
        self.order=OrderPage(self.driver)
        self.order.get_page_title()

    def test_login(self):
        self.order = OrderPage(self.driver)
        login_credentials = self.data_provider.get_login_credentials()
        for email,password in login_credentials:
            self.order.get_login(email,password)

    def test_order(self):
        self.order=OrderPage(self.driver)
        self.order.scroll_to_product()
        title=self.order.add_to_cart()
        assert title == "Your product has been added to cart.", "Page not loaded completely"
        payments=self.data_provider.get_payment_details()
        for payment in payments:
            self.order.place_order(payment)