from selenium.webdriver.common.by import By

class RegisterLocators:
    SignUp = (By.LINK_TEXT, "Signup / Login")
    Name = (By.NAME, "name")
    Email = (By.XPATH, "//input[@data-qa='signup-email']")
    Password = (By.ID, "password")
    Newsletter = (By.XPATH, "//input[@id='newsletter' and @value='1']")
    FirstName = (By.ID, "first_name")
    LastName = (By.ID, "last_name")
    Address = (By.ID, "address1")
    State = (By.ID, "state")
    City = (By.ID, "city")
    Zip = (By.ID, "zipcode")
    Mobile = (By.ID, "mobile_number")
    Signup_Button = (By.XPATH, "//button[@data-qa='signup-button']")
    Element = (By.XPATH, "//h2//b")
    Create_Account = (By.XPATH, "//button[@data-qa='create-account']")
    Continue_Button=(By.XPATH,"//*[@id='form']/div/div/div/div/a")