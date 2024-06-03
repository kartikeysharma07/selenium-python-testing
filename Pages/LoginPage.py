from Pages.BasePage import BasePage
from Utilities import ReadConfigurations as rc
from Locators.LoginLocators import LoginLocators as lc
from Utilities.AssertMessage import AssertTitle as info
from Utilities.AssertMessage import ErrorMessage as error

class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        config = rc.Configuration()
        self.url = config.get_url()
        self.driver.get(self.url)

    def get_page_title(self):
        title=self.get_title()
        assert title == info.home_page_title,error.title_error_message

    def get_login(self, email, password):
        self.do_click(lc.Login)
        self.do_send_keys(lc.Email, email)
        self.do_send_keys(lc.Password, password)
        self.do_click(lc.login_button)
        self.do_click(lc.logout_button)

