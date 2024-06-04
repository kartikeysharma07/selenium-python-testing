from Utilities import ReadConfigurations as rc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        config = rc.Configuration()
        self.duration = config.get_wait_time()

    def do_click(self, by_locator):
        WebDriverWait(self.driver, self.duration).until(ec.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, self.duration).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.duration).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, self.duration).until(ec.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_url(self):
        return self.driver.current_url

    def assert_equal_title(self, expected_title, error_message):
        actual_title = self.get_title()
        assert actual_title == expected_title, error_message

    def assert_equal_url(self, expected_url, error_message):
        current_url = self.get_url()
        assert expected_url in current_url, error_message

    def assert_equal_check_element(self, text_locator, expected_text, error_message):
        text = self.get_element_text(text_locator)
        assert text.lower() == expected_text.lower(), error_message

    def assert_notequal_title(self,expected_title,error_message):
        get_title = self.get_title()
        assert get_title != expected_title, error_message
