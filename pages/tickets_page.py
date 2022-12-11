from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.base_page import BasePage
from pages.order_page import OrderPage

class TicketPage(BasePage):
    
    def __init__(self,driver):
        super(TicketPage,self).__init__(driver)
        self.wait = WebDriverWait(self.driver,10)
        self.cheapest_tickets_btn = (By.XPATH,"//body/main[@class='app-avia display-f f--column']/section[@class='page-avia-results']/div[@class='container']/div[@class='row']/div[@class='col-24 col-xl-18']/div[@class='mb-2 avia-results-top']/div[@class='row']/div[@class='col-24']/div[@class='theme-default block']/div[@class='row f-center-space-between']/div[@class='col']/div[@class='t-tabs-v2 avia-results-sorter pl-2 pr-2']/div[@class='f-center-center rel']/div[@class='t-tabs-v2__inner rel ltr']/div[@class='t-tabs-v2__carriage scrolled hide-scroll ltr']/div[2]")
        self.first_ticket_btn = (By.XPATH,"//body/main[@class='app-avia display-f f--column']/section[@class='page-avia-results']/div[@class='container']/div[@class='row']/div[@class='col-24 col-xl-18']/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]")

    def choose_flight_settings(self):
        self.do_long_click(self.cheapest_tickets_btn)
        
    def choose_ticket(self):
        self.do_long_click(self.first_ticket_btn)
    
        orderticket = OrderPage(self.driver)
        return orderticket
