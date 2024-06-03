from selenium.webdriver.common.by import By

class SubscriptionLocators:

    Subscription_Box = (By.XPATH, "//input[@id='susbscribe_email']")
    Subscription_Button = (By.XPATH, "//button[@id='subscribe']")
    Subscription_Text = (By.XPATH, "//*[@id='footer']/div[1]/div/div/div[2]/div/h2")