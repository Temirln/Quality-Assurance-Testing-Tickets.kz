from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select


import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.base_page import BasePage
from utilities.utills import Utils
import logging

class OrderPage(BasePage):
    logger = Utils.logger(log_level=logging.DEBUG)

    def __init__(self,driver):
        super(OrderPage,self).__init__(driver)
        self.wait = WebDriverWait(self.driver,50)

        self.gender = (By.XPATH,"//body[1]/main[1]/section[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/label[1]/button[1]")
        
        

        self.choose_gender = (By.XPATH,"//button[contains(text(),'Мужской')]")
        self.surname_input = (By.CSS_SELECTOR,"input[name='lastName']")


        self.name_input = (By.CSS_SELECTOR,"input[name='firstName']")



        self.surname = "Toleubekov"
        self.name = "Temirlan"

        self.birthday = (By.CSS_SELECTOR,"div:nth-child(5) div:nth-child(1) label:nth-child(1)")
        self.birthday_date_input = (By.CSS_SELECTOR,"input[name='birthday']")
        self.birthday_date = "05.11.2002"
        self.identify_by_btn = (By.CSS_SELECTOR,"div[class='t-menu-v2 t-select-v2 avia-passengers-doctype fields-builder-v2__element'] label[class='input-wrapper']")
        self.identify_by_id = (By.XPATH,"//button[contains(text(),'Удостоверение личности')]")
        self.identity_card_number_btn = (By.CSS_SELECTOR,".bg-inherit.input-wrapper.t-input-v2.size-6.theme-default.t-input-masked")
        self.identity_card_number = (By.CSS_SELECTOR,"input[name='docnum']")
        self.card_number = "044108621"


        self.card_number_expire_date_btn = (By.CSS_SELECTOR,"div:nth-child(5) div:nth-child(1) label:nth-child(1)")
        self.card_number_expire_date = (By.CSS_SELECTOR,"input[name='docExpireDate']")
        self.card_number_expire_date_number = "25.02.2029"
        self.iin_btn = (By.CSS_SELECTOR,".input-wrapper.t-input-v2.size-6.theme-default.t-input-masked.fields-builder-v2__element")
        self.iin_input = (By.CSS_SELECTOR,"input[name='ipn']")
        self.iin_number = "021105501563"

        self.continue_btn = (By.XPATH,"//button[contains(text(),'Продолжить')]")


    def fill_credentials(self):
        # select = Select(self.wait.until(EC.presence_of_element_located(((By.XPATH,"/html/body/main/section/div/div[2]/div/form/div/div[1]/div[2]/div")))))
        # select.select_by_visible_text("Мужской")   
        
        self.do_long_click(self.gender)
        self.do_click(self.choose_gender)   
        self.logger.info("Choosed Gender")
                 
        self.do_send_keys(self.surname_input,self.surname)
        self.logger.info("Entered surname")
        self.do_send_keys(self.name_input,self.name)
        self.logger.info("Entered Name")
        self.do_click(self.birthday)
        self.do_send_keys(self.birthday_date_input,self.birthday_date)
        self.logger.info("Entered Birthday")
        self.do_click(self.identify_by_btn)
        self.do_click(self.identify_by_id)
        self.do_click(self.identity_card_number_btn)
        self.do_send_keys(self.identity_card_number,self.card_number)
        self.logger.info("Entered Card Number")
        self.do_click(self.card_number_expire_date_btn)
        self.do_send_keys(self.card_number_expire_date,self.card_number_expire_date_number)

        self.do_click(self.iin_btn)
        self.do_send_keys(self.iin_input,self.iin_number)
        self.logger.info("IIN Number")

        self.do_click(self.continue_btn)
