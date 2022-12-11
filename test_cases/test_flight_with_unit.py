import unittest
import pytest
import softest
import time

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.main_page import MainPage

from ddt import ddt , unpack ,data ,file_data

from utilities.utills import Utils
import logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService

import pytest_check as check
from selenium.common.exceptions import InvalidSessionIdException

from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager


@ddt
class TestFlightUnit(unittest.TestCase):
    logger = Utils.logger(log_level=logging.DEBUG)
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(service = ChromeService(r"D:\IDE Projects\VS Code Projects\QA_Selenium\webdrivers\chrome-driver\chromedriver.exe"))

    #     # cls.driver = webdriver.Firefox(service = FirefoxService(r"D:\IDE Projects\VS Code Projects\QA_Selenium\webdrivers\firefoxdriver\geckodriver.exe"))
    #     cls.driver.implicitly_wait(10)
    #     cls.wait = WebDriverWait(cls.driver,10)
    #     # cls.driver.get("https://kaspi.kz/")
    
    @classmethod
    def setUp(self):
        
        load_dotenv()

        username = os.getenv('BROWSERSTACK_USERNAME')
        accessKey = os.getenv('BROWSERSTACK_ACCESS_KEY')

        # desired_cap = {
        #     'os_version': '10',
        #     'os': 'Windows',
        #     'browser': 'chrome',
        #     'browser_version': 'latest',
        #     'name': 'Parallel Test1', # test name
        #     'build': 'browserstack-build-1', # Your tests will be organized within this build
        # }
        # self.driver = webdriver.Remote(
        #     command_executor='https://'+username+':'+accessKey+'@hub.browserstack.com/wd/hub',
        #     desired_capabilities=desired_cap 
        # )

        # time.sleep(5)
        self.driver = webdriver.Chrome(service = ChromeService(r"D:\IDE Projects\VS Code Projects\QA_Selenium\webdrivers\chrome-driver\chromedriver.exe"))
        # self.driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver,10)
        # self.driver.switch_to.new_window('tab')
        # self.driver.get("https://tickets.kz/")
        # except Exception as e:
        #     print(e.message)
        
        self.driver.maximize_window()
    # @pytest.fixture(autouse=True)
    # def class_setup(self):
        self.orderticket = MainPage(self.driver) 

    @data(*Utils.read_data_from_excel(r"D:\IDE Projects\VS Code Projects\QA_Selenium\Assignment_5\testdata\test_data.xlsx","Лист1"))
    @unpack
    def test_order_ticket(self,from_city,to_city,row):
        self.logger.info("<------------Test Order Ticket Started----------------->")
        self.driver.get("https://tickets.kz/")
        self.orderticket.order_ticket(from_city,to_city)
        time.sleep(15)

        title = self.orderticket.do_get_title()
        # self.soft_assert(self.assertEqual, title,"Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
        check.equal(title, "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
        # assert title == "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz"
        # # self.assertEqual(title,"Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
        if title == "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz":
            self.logger.info("Test Passed")    
            result = "test passed"
            # self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')

        else:
            self.logger.info("Test Failed")
            result = "test failed"
            # self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Oops! my sample test failed"}}')
        
        Utils.write_data_to_excel(r"D:\IDE Projects\VS Code Projects\QA_Selenium\Assignment_5\testdata\test_data.xlsx","Лист1",result,row)
        self.logger.info("<------------Test Order Ticket Ended------------------->")
        self.assert_all()


    def test_login_tickets(self):
        # self.logger.info("<------------Test Login Started----------------->")
        # self.driver.get("https://tickets.kz/")
        loginpage = MainPage(self.driver)
        # loginpage.login_to_website(login,password)
        # profile_text = loginpage.check_login()
        loginpage.login_to_website("t1mb3rmn@gmail.com","Register125")
        time.sleep(5)
        # assert profile_text == 1
        title = loginpage.do_get_title()
        assert title == "Купить авиабилеты в Казахстане: дешевые авиабилеты онлайн - Tickets.kz"
        # self.logger.info("<------------Test Login Ended------------------->")

    def test_login_tickets_2(self):
        # self.logger.info("<------------Test Login Started----------------->")
        self.driver.get("https://tickets.kz/")
        loginpage = MainPage(self.driver)
        # loginpage.login_to_website(login,password)
        # profile_text = loginpage.check_login()
        loginpage.login_to_website("t1mb3rmn@gmail.com","Register125")
        time.sleep(5)
        # assert profile_text == 1
        title = loginpage.do_get_title()
        assert title == "Купить авиабилеты в Казахстане: дешевые авиабилеты онлайн - Tickets.kz"
        # self.logger.info("<------------Test Login Ended------------------->")
    

    @classmethod
    def tearDown(self):
        self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.quit()

    

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()



if __name__ == "__main__":
    unittest.main()