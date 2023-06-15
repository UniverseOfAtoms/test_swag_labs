from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class HomePage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, 60)
       
    def open_website(self):
        self.selenium_driver.get("https://www.saucedemo.com/")
        self.selenium_driver.maximize_window()
    
    def login(self, username, password):
        username_field = self.wait.until(ec.element_to_be_clickable((By.ID, "user-name")))
        username_field.click()
        username_field.send_keys(username)

        password_field = self.selenium_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.send_keys(password)

        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()
    
    def is_on_page(self):
        page = self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "title")))
        return page.text
    
    def add_to_cart(self):
        add_bike_light = self.wait.until(ec.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        add_bike_light.click()

        add_backpack = self.selenium_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_backpack.click()
      
    def go_to_your_cart_page(self):
        your_cart = self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        your_cart.click()

    def is_first_item_here(self):
        first_item = self.wait.until(ec.element_to_be_clickable((By.ID, "item_0_title_link")))
        return first_item.text
    
    def is_second_item_here(self):
        scnd_item = self.wait.until(ec.element_to_be_clickable((By.ID, "item_4_title_link")))
        return scnd_item.text
    
    def go_to_checkout(self):
        checkout_button = self.wait.until(ec.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

    def checkout_informations(self, first_name, last_name, zip):
        first_name_field = self.wait.until(ec.element_to_be_clickable((By.ID, "first-name")))
        first_name_field.click()
        first_name_field.send_keys(first_name)

        last_name_field = self.selenium_driver.find_element(By.ID, "last-name")
        last_name_field.click()
        last_name_field.send_keys(last_name)

        zip_field = self.selenium_driver.find_element(By.ID, "postal-code")
        zip_field.click()
        zip_field.send_keys(zip)

    def go_to_continue(self):
        continue_button = self.wait.until(ec.element_to_be_clickable((By.ID, "continue")))
        continue_button.click()

    def go_to_finish(self):
        finish_button = self.wait.until(ec.element_to_be_clickable((By.ID, "finish")))
        finish_button.click()
    
    def go_to_logout(self):
        dropdown_list = self.wait.until(ec.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        dropdown_list.click()
        logout =  self.wait.until(ec.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout.click()
    
    def is_on_login_page(self):
        login_page = self.wait.until(ec.element_to_be_clickable((By.ID, "login_credentials")))
        return login_page.get_attribute("class")

    




