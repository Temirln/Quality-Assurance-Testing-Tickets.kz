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

        # self.aviatickets_btn = (By.XPATH,"//button[@data-uil='service-avia']")
        self.aviatickets_btn = (By.XPATH,"//button[@class='t-btn-atomic cursor-pointer theme-default font-size-13 font-bold pl-2 pr-2 size-4 rounded no-wrap f-center-center color-1 bg-hover-1 color-hover-29 bg-1 color-29']")
        
        # self.from_station_btn = (By.XPATH,"//div[@class='t-menu t-select selected big t-autocomplete-v2 double-autocomplete__input departure ltr theme-default']//div[@class='t-select__block-activator']//button[@type='button']")
        self.from_station_btn = (By.XPATH,"//label[@class='search-form-activator display-f valued cursor-text theme-default size-8 size-m-9 size-xl-10 border-radius-4-tl border-radius-4-tr border-radius-m-0-tr border-radius-xl-4-bl']")
        # self.from_city_station_btn = (By.XPATH,"//div[@class='t-menu open t-select selected big t-autocomplete-v2 double-autocomplete__input departure ltr theme-default']//input[@type='text']")
        self.from_city_station_btn = (By.XPATH,"//input[@class='search-form-activator__input w-100 h-100 bg-transparent color-inherit cursor-inherit valued focused ltr']")

        # self.to_station_btn = (By.XPATH,"//div[@class='t-menu t-select selected big t-autocomplete-v2 double-autocomplete__input arrival ltr theme-default']//div[@class='t-select__block-activator']//button[@type='button']")
        self.to_station_btn = (By.XPATH,"//label[@class='search-form-activator display-f cursor-text theme-default size-8 size-m-9 size-xl-10 border-radius-xl-0-tr border-radius-m-4-tr']//div[@class='rel display-f w-100']")
        # self.to_city_station = (By.XPATH,"//div[@class='t-menu open t-select selected big t-autocomplete-v2 double-autocomplete__input arrival ltr theme-default']//input[@type='text']")
        self.to_city_station = (By.XPATH,"//input[@class='search-form-activator__input w-100 h-100 bg-transparent color-inherit cursor-inherit ltr']")
        # self.date_picker_btn = (By.XPATH,"//div[@class='t-date-picker__inner']")
        self.date_picker_btn = (By.XPATH,"//label[@class='search-form-activator display-f readonly cursor-pointer theme-default size-8 size-m-9 size-xl-10 border-radius-m-4-bl border-radius-xl-0-bl']//div[@class='rel display-f w-100']")
        
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
        # try:
        from datetime import date

        today = date.today()
        day = today.strftime("%d")
        print(day)
        # day = self.driver.find_element(By.XPATH,f"//*[contains(text(), "{d2}")]")
        # day = self.driver.find_element(By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today'] + div").text
        self.driver.find_element(By.XPATH,f'//*[contains(text(), "{day}")]').click()
        # self.driver.find_element(By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today'] + div").click()
        # except:
        #     day = self.driver.find_element(By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today weekend'] + div").text
        #     self.driver.find_element(By.CSS_SELECTOR,"div[class='t-calendar__month__week__day ltr theme-default today weekend'] + div").click()
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

       