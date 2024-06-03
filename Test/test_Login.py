from Pages.LoginPage import Login
from Test.test_base import BaseTest
from Utilities.ReadExcelData import DataProvider


class Test_Login(BaseTest):

    data_provider = DataProvider()

    def test_page_title(self):
        self.loginPage = Login(self.driver)
        self.loginPage.get_page_title()

    def test_login(self):
        self.loginPage = Login(self.driver)
        login_credentials = self.data_provider.get_login_credentials()
        for username, password in login_credentials:
            self.loginPage.get_login(username, password)
