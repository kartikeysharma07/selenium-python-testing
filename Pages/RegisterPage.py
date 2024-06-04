from Pages.BasePage import BasePage
from Utilities import ReadConfigurations as rc
from Locators.RegisterLocator import RegisterLocators as rl
from Utilities.AssertMessage import AssertTitle as info
from Utilities.AssertMessage import User_Query as user
from Utilities.AssertMessage import ErrorMessage as error
class Register(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        config = rc.Configuration()
        self.url = config.get_url()
        self.driver.get(self.url)

    def get_page_title(self):
        self.assert_equal_title(info.home_page_title, error.title_error_message)

    def verify_page_url(self,expected_url,message):
        self.assert_equal_url(expected_url,message)

    def get_register(self, credential):
        self.do_click(rl.SignUp)
        self.verify_page_url(user.expected_url,error.signup_error_message)
        self.do_send_keys(rl.Name, credential['name'])
        self.do_send_keys(rl.Email, credential['email'])
        self.do_click(rl.Signup_Button)
        # get_title=self.get_title()
        # assert get_title != info.signup_page_title, error.signup_error_message
        self.assert_notequal_title(info.signup_page_title,error.signup_error_message)
        self.do_send_keys(rl.Password, credential['password'])
        self.do_click(rl.Newsletter)
        self.do_send_keys(rl.FirstName, credential['firstname'])
        self.do_send_keys(rl.LastName, credential['lastname'])
        self.do_send_keys(rl.Address, credential['address'])
        self.do_send_keys(rl.State, credential['state'])
        self.do_send_keys(rl.City, credential['city'])
        self.do_send_keys(rl.Zip, credential['zipcode'])
        self.do_send_keys(rl.Mobile, credential['mobile'])
        self.do_click(rl.Create_Account)
        self.verify_page_url(user.account_action,error.account_error_message)
        self.do_click(rl.Continue_Button)
        self.do_click(rl.logout_button)



