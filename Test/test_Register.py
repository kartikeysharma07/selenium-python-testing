from Pages.RegisterPage import Register
from Test.test_base import BaseTest
from Utilities.ReadExcelData import DataProvider


class Test_Register(BaseTest):
    data_provider = DataProvider()

    def test_signup(self):
        self.signup = Register(self.driver)
        signup_credentials = self.data_provider.get_register_credentials()
        for credential in signup_credentials:
            self.signup.get_register(credential)
