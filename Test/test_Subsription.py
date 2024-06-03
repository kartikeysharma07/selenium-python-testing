from Pages.SubscriptionPage import Subscription
from Test.test_base import BaseTest
from Utilities.ReadExcelData import DataProvider

class Test_Subscribe(BaseTest):

    data_provider=DataProvider()

    def test_get_title(self):
        self.subscriptionPage=Subscription(self.driver)
        self.subscriptionPage.get_page_title()

    def test_subscribe(self):
        self.subscriptionPage = Subscription(self.driver)
        self.subscriptionPage.scroll_to_subscription()
        self.subscriptionPage.get_subscription()

