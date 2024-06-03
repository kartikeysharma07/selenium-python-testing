from Pages.BasePage import BasePage
from Utilities import ReadConfigurations as rc
from Locators.SubscriptonLocator import SubscriptionLocators as sl
from Utilities.AssertMessage import AssertTitle as info
from Utilities.AssertMessage import ErrorMessage as error

class Subscription(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        config = rc.Configuration()
        self.url = config.get_url()
        self.driver.get(self.url)

    def get_page_title(self):
        title=self.get_title()
        assert title == info.home_page_title,error.title_error_message

    def scroll_to_subscription(self):
        self.scroll_to_element(sl.Subscription_Box)
        text = self.get_element_text(sl.Subscription_Text)
        assert text.lower() == info.subscription,error.subscription_error_message

    def get_subscription(self):
        self.do_send_keys(sl.Subscription_Box, "kartikeysharma@gmail.com")
        self.do_click(sl.Subscription_Button)

    def get_text(self):
        return self.get_element_text(sl.Subscription_Text)
