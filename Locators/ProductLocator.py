from selenium.webdriver.common.by import By

class ProductLocators:

    Product_Button = (By.XPATH, "//a[@href='/products']")
    Search_Box = (By.ID, "search_product")
    Search_Button = (By.ID, "submit_search")
    Cart_Button = (By.LINK_TEXT, "Cart")
    Product_Verification = (By.XPATH, "//div[@class='productinfo text-center']/p")
    Add_To_Cart = (By.XPATH, "//a[contains(@class, 'btn btn-default add-to-cart')]")
    Continue_Shopping = (By.XPATH, "//button[contains(@class, ' btn-block')]")
    Product_In_Cart_Verification = (By.XPATH, "//table[@id='cart_info_table']//td[@class='cart_description']//h4/a")