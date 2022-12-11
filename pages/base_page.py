from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class BasePage():

    def __init__(self,driver):
        self.driver = driver
        self.wait_explicity = WebDriverWait(self.driver,10)
        self.wait_fluent = WebDriverWait(self.driver,50,10,ignored_exceptions=[TimeoutException])

    def do_click(self,locator):
        self.wait_explicity.until(EC.element_to_be_clickable(locator)).click()
    
    def do_send_keys(self,locator,text):
        self.wait_explicity.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def do_clear(self,locator):
        self.wait_explicity.until(EC.visibility_of_element_located(locator)).clear()

    def do_get_text(self,locator):
        return self.wait_explicity.until(EC.visibility_of_element_located(locator)).text

    def do_long_click(self,locator):
        self.wait_fluent.until(EC.presence_of_element_located(locator)).click()

    def do_submit(self,locator):
        self.wait_explicity.until(EC.element_to_be_clickable(locator)).submit()

    def do_get_title(self):
        return self.driver.title