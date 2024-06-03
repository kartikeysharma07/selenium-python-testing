from selenium.webdriver.common.by import By

class OrderLocators:
    Product = (By.XPATH, "//p[text()='Green Side Placket Detail T-Shirt']")
    Add_To_Cart = (By.XPATH, "//a[@data-product-id=29]")
    View_Cart = (By.XPATH, "//a[@href='/view_cart']")
    Product_Added = (By.XPATH, "//*[@id='cartModal']/div/div/div[2]/p[1]")
    Continue_Shopping = (By.XPATH, "//*[@id='cartModal']/div/div/div[3]/button")
    Checkout = (By.XPATH, "//a[text()='Proceed To Checkout']")
    Place_Order = (By.XPATH, "//a[@href='/payment']")
    Cart = (By.LINK_TEXT, "Cart")
    Name_On_Card = (By.NAME, "name_on_card")
    Card_Number = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    Expiry_Month = (By.NAME, "expiry_month")
    Expiry_Year = (By.NAME, "expiry_year")
    Submit = (By.ID, "submit")
    Continue = (By.XPATH, "//a[@data-qa='continue-button']")
    Logout = (By.LINK_TEXT, "Logout")