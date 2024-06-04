from Pages.LoginPage import Login
from Test.test_base import BaseTest
from Utilities.ReadExcelData import DataProvider


class Test_Login(BaseTest):

    data_provider = DataProvider()

    def setup_method(self):
        self.loginPage = Login(self.driver)

    def test_page_title(self):
        self.loginPage.get_page_title()

    def test_login(self):
        login_credentials = self.data_provider.get_login_credentials()
        for username, password in login_credentials:
            self.loginPage.get_login(username, password)

    def test_logout(self):
        self.loginPage.get_logout()
