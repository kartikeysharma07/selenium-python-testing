import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.ReadConfigurations import Configuration as config
from selenium.webdriver.chrome.options import Options
@pytest.fixture(params=[config().get_browser()],scope='class')
def init__driver(request):
    if request.param=="chrome":
        if config().get_headless_info()=="True":
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            web_driver = webdriver.Chrome(options=chrome_options)
        else:
            web_driver = webdriver.Chrome()

    elif request.param=="firefox":
        if config().get_headless_info()=="True":
            firefox_options=Options()
            firefox_options.add_argument("--headless")
            web_driver=webdriver.Firefox(options=firefox_options)
        else:
            web_driver=webdriver.Firefox()

    request.cls.driver=web_driver
    yield
    web_driver.close()