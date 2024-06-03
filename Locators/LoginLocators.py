from selenium.webdriver.common.by import By

class LoginLocators:
    Login = (By.LINK_TEXT, "Signup / Login")
    Email = (By.NAME, "email")
    Password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    logout_button=(By.XPATH,"//a[@href='/logout']")