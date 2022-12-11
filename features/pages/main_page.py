from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from pages.base_page import BasePage 
from pages.tickets_page import TicketPage

from utilities.utills import Utils
import logging

class MainPage(BasePage):
    logger = Utils.logger(log_level=logging.DEBUG)

    def __init__(self,driver):
        super(MainPage,self).__init__(driver)
        self.wait = WebDriverWait(self.driver,10)

    # LOCATORS
        self.profile = (By.XPATH,"//div[@class='font-600 text-overflow w-100']")
        self.profile_locator_loggedin = (By.XPATH,"//button[@class='size-5 rounded square overflow-h t-btn-atomic cursor-pointer theme-default']")

        self.profile_locator = (By.XPATH,"//div[contains(text(),'Мой билет')]")
        self.login_locator = (By.XPATH,"//input[@name='email']")
        self.password_locator = (By.CSS_SELECTOR,"input[name='password']")
        self.submit_btn_locator = (By.XPATH,"//button[@type='submit'][contains(text(),'Вход')]")

        self.aviatickets_btn = (By.XPATH,"//button[@data-uil='service-avia']")
        self.from_station_btn = (By.XPATH,"//div[@class='t-menu t-select selected big t-autocomplete-v2 double-autocomplete__input departure ltr theme-default']//div[@class='t-select__block-activator']//button[@type='button']")
        self.from_city_station_btn = (By.XPATH,"//div[@class='t-menu open t-select selected big t-autocomplete-v2 double-autocomplete__input departure ltr theme-default']//input[@type='text']")


        self.to_station_btn = (By.XPATH,"//div[@class='t-menu t-select selected big t-autocomplete-v2 double-autocomplete__input arrival ltr theme-default']//div[@class='t-select__block-activator']//button[@type='button']")
        self.to_city_station = (By.XPATH,"//div[@class='t-menu open t-select selected big t-autocomplete-v2 double-autocomplete__input arrival ltr theme-default']//input[@type='text']")
    
        self.date_picker_btn = (By.XPATH,"//div[@class='t-date-picker__inner']")
        
        
        # self.next_date_btn = (By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today'] + div")
        # self.next_weekend_date_btn = (By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today weekend'] + div")

        # self.next_month_btn = (By.XPATH,f"//div[@class='t-calendar__month__week__day ltr theme-default']//button[@type='button'][normalize-space()='{self.do_get_text(self.next_date_btn)}']")
        # self.next_month_weekend_btn = (By.XPATH,f"//div[@class='t-calendar__month__week__day ltr theme-default weekend']//button[@type='button'][normalize-space()='{self.next_weekend_date_btn}']")

        self.find_flight_btn = (By.XPATH,"//button[contains(text(),'Найти')]")    


    def login_to_website(self,login,password):
        self.do_click(self.profile_locator)
        self.do_send_keys(self.login_locator,login)
        self.logger.info("Entered email")
        self.do_send_keys(self.password_locator,password)
        self.logger.info("Entered password")
        self.do_click(self.submit_btn_locator)
    
    def check_login(self):
        self.do_long_click(self.profile_locator_loggedin)
        try:
            text = self.do_get_text(self.profile_locator)
        except:
            text = self.do_get_text(self.profile)
        if text.split()[0] == "Приветствуем":
            return 1
        elif text == "Мой билет":
            return 0 

    def order_ticket(self,from_city,to_city):
        self.do_click(self.aviatickets_btn)
        self.do_click(self.from_station_btn)
        self.do_clear(self.from_city_station_btn)
        self.do_send_keys(self.from_city_station_btn,from_city)
        self.logger.info("Entered from City")

        self.do_click(self.to_station_btn)
        self.do_clear(self.to_city_station)
        self.do_send_keys(self.to_city_station,to_city)
        # self.do_submit(self.to_city_station)
        self.logger.info("Entered To City")
        time.sleep(2)


        self.do_long_click(self.date_picker_btn)
        try:
            day = self.driver.find_element(By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today'] + div").text
            self.driver.find_element(By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today'] + div").click()
        except:
            day = self.driver.find_element(By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today weekend'] + div").text
            self.driver.find_element(By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today weekend'] + div").click()
        self.logger.info("Day:" + day)
        # print(day)
        try:
            self.driver.find_element(By.XPATH,f"//div[@class='t-calendar__month__week__day ltr theme-default weekend']//button[@type='button'][normalize-space()='{day}']").click()
        except:
            self.driver.find_element(By.XPATH,f"//div[@class='t-calendar__month__week__day ltr theme-default']//button[@type='button'][normalize-space()='{day}']").click()
        self.logger.info("Entered dates")

        self.do_click(self.find_flight_btn)

        ticketpage = TicketPage(self.driver)
        return ticketpage

       