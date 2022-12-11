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

import pytest_check as check


# To use local Chrome Driver #
# driver = webdriver.Chrome(executable_path=r"D:\IDE Projects\VS Code Projects\Selenium_Python\chrome-driver\chromedriver.exe")
# driver.get("https://tickets.kz/")
# driver.maximize_window()
@pytest.mark.usefixtures("setUp_tests")
@ddt
class TestFlightSearch(unittest.TestCase):
    logger = Utils.logger(log_level=logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.orderticket = MainPage(self.driver)    

    # @data(*Utils.read_data_from_excel(r"D:\IDE Projects\VS Code Projects\QA_Selenium\Assignment_5\testdata\test_data_for_login.xlsx","Лист1"))

    @data(("t1mb3rmn@gmail.com","Register125"))
    @unpack
    def test_login_tickets(self,login,password):
        self.logger.info("<------------Test Login Started----------------->")
        self.driver.get("https://tickets.kz/")
        loginpage = MainPage(self.driver)
        loginpage.login_to_website(login,password)
        # profile_text = loginpage.check_login()
        # loginpage.login_to_website("t1mb3rmn@gmail.com","Register125")
        time.sleep(5)
        # assert profile_text == 1
        title = self.orderticket.do_get_title()
        assert title == "Купить авиабилеты в Казахстане: дешевые авиабилеты онлайн - Tickets.kz"
        self.logger.info("<------------Test Login Ended------------------->")

   
    

    # @pytest.mark.parametrize("from_city,to_city", [("Astana", "Almaty"), ("Taraz", "Almaty")])
    # @data(("Almaty","Astana"),("Астана","Тараз"))
    # @unpack
    # @file_data("../testdata/test_data.json")
    @data(*Utils.read_data_from_excel(r"D:\IDE Projects\VS Code Projects\QA_Selenium\Assignment_5\testdata\test_data.xlsx","Лист1"))
    @unpack
    def test_order_ticket(self,from_city,to_city,row):
        self.logger.info("<------------Test Order Ticket Started----------------->")
        self.driver.get("https://tickets.kz/")
        self.orderticket.order_ticket(from_city,to_city)
        time.sleep(5)

        title = self.orderticket.do_get_title()
        # self.soft_assert(self.assertEqual, title,"Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
        check.equal(title, "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
        # assert title == "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz"
        # self.assertEqual(title,"Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
        if title == "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz":
            self.logger.info("Test Passed")    
            result = "test passed"
        else:
            self.logger.info("Test Failed")
            result = "test failed"
        
        Utils.write_data_to_excel(r"D:\IDE Projects\VS Code Projects\QA_Selenium\Assignment_5\testdata\test_data.xlsx","Лист1",result,row)
        self.logger.info("<------------Test Order Ticket Ended------------------->")
        # self.assert_all()

    @data(("Almaty","Astana"))
    @unpack  
    def test_full_order_ticket(self,from_city,to_city):
        self.logger.info("<------------Test Order Ticket Started----------------->")
        self.orderticket.order_ticket(from_city,to_city)
        self.logger.info("Logined")
        self.driver.get("https://tickets.kz/")
        ticket_page = self.orderticket.order_ticket(from_city,to_city)
        # time.sleep(20)
        title = ticket_page.do_get_title()


        # self.soft_assert(self.assertEqual, title,"Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz")
        assert title == "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz"
        if title == "Бронирование авиабилетов онлайн - Tickets.kz / Tickets.kz":
            self.logger.info("Test Passed")    
            
        else:
            self.logger.info("Test Passed")

        ticket_page.choose_flight_settings()
        orderticket = ticket_page.choose_ticket()
        orderticket.fill_credentials()


        time.sleep(20)
        

        self.logger.info("<------------Test Order Ticket Ended------------------->")