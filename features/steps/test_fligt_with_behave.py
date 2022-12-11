from behave import given, when, then, step

from dotenv import load_dotenv

import time

from utilities.utills import Utils
import logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.main_page import MainPage

import pytest_check as check
from selenium.common.exceptions import InvalidSessionIdException



@given('I am on Ticket Search Page')
def step_impl(context):
    context.driver = webdriver.Chrome(service = ChromeService(r"D:\IDE Projects\VS Code Projects\QA_Selenium\webdrivers\chrome-driver\chromedriver.exe"))
    context.driver.implicitly_wait(10)
    context.wait = WebDriverWait(context.driver,10)
    context.driver.maximize_window()
    context.orderticket = MainPage(context.driver)
    context.logger = Utils.logger(log_level=logging.DEBUG)

@when('I enter from {from_city} to {to_city}')
def step_impl(context, from_city,to_city):
    context.logger.info("<------------Test Order Ticket Started----------------->")
    context.driver.get("https://tickets.kz/")
    context.orderticket.order_ticket(from_city,to_city)
    time.sleep(5)

    title = context.orderticket.do_get_title()
    # context.soft_assert(context.assertEqual, title,"Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
    check.equal(title, "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
    # assert title == "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz"
    # context.assertEqual(title,"Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
    if title == "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz":
        context.logger.info("Test Passed")    
        result = "test passed"
        # context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
          
    else:
        context.logger.info("Test Failed")
        result = "test failed"
        # context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Oops! my sample test failed"}}')
        
    # Utils.write_data_to_excel(r"D:\IDE Projects\VS Code Projects\QA_Selenium\Assignment_5\testdata\test_data.xlsx","Лист1",result,row)
    context.logger.info("<------------Test Order Ticket Ended------------------->")
    # context.assert_all()print(from_city,to_city)

# @then('I should be on the Tickets Page')
# def step_impl(context):
#     print("I am on Ticket Page")

@then("Close Browser")
def step_iml(context):
    context.driver.close()
    context.driver.quit()


    