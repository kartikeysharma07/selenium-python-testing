from configparser import ConfigParser


class Configuration:
    config_file_path = "../Configuration/config.ini"
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(self.config_file_path)

    def get_browser(self):
        browser = self.config.get('url info', 'browser')
        return browser

    def get_url(self):
        base_url = self.config.get('url info', 'url')
        return base_url

    def get_headless_info(self):
        headless_info=self.config.get('url info','headless_mode')
        return headless_info

    def get_wait_time(self):
        return int(self.config.get('url info', 'Wait_Duration'))