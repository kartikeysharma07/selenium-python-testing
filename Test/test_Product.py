from Test.test_base import BaseTest
from Utilities.ReadExcelData import DataProvider
from Pages.ProductPage import Product

class Test_Product(BaseTest):

    data_provider=DataProvider()

    def setup_method(self):
        self.product=Product(self.driver)

    def test_verify_page_title(self):
        self.product.get_page_title()

    def test_search_product(self):
        products=self.data_provider.get_products()
        login_credentials = self.data_provider.get_login_credentials()
        for product in products:
            self.product.search_product(product)
            for username, password in login_credentials:
                self.product.verify_product_in_cart_after_login(product,username,password)