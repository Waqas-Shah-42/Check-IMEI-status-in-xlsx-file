import os
from selenium import webdriver
from tkinter import messagebox
from selenium.webdriver.common.by import By

os.chdir(os.path.dirname(os.path.realpath(__file__)))

class Drs:

    def __init__(self):
      super().__init__()
      self.loginDRS()


    def loginDRS(self):

        # login information
        email = 'Please input email'
        password = 'Please input password'

        # getting to the starting point
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dirbs.pta.gov.pk/drs")

        # waiting for the page to load
        self.driver.implicitly_wait(2)

        # logging in
        self.driver.find_element(By.ID, "identity").send_keys(email)
        self.driver.find_element(By.ID, "login_password").send_keys(password)

        # wait to complete captcha
        messagebox.showinfo(title='Captcha', message='Finish CAPTCHA, and then click OK.')

        return self.driver


    def getDeviceDetails(self, IMEI):
        self.driver.get('https://dirbs.pta.gov.pk/drs/search/tac')

        # waiting for the page to load
        # self.driver.implicitly_wait(1)

        tac = int(str(IMEI)[:8])

        self.driver.find_element(By.ID, "search_tac").send_keys(tac)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div[1]/form/div/span/button").click()

        # waiting for the page to load
        # self.driver.implicitly_wait(3)

        modelNumber = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]").get_attribute('innerHTML')
        manufacturer = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/section[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]').get_attribute('innerHTML')

        return modelNumber, manufacturer

    def IMEIStatus(self, IMEI):
      # opening the relevant web page
      self.driver.get('https://dirbs.pta.gov.pk/drs/search/imei')

      # waiting for page to open    
      # self.driver.implicitly_wait(2)

      self.driver.find_element(By.ID, "imei").send_keys(IMEI)

      self.driver.find_element(By.NAME, "imei_submit").click()

      status = "error please try again"

      try:
        status = self.driver.find_element(By.ID, "infoMessage").get_attribute('innerHTML')
        
      except:
        status = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div[3]/div/table/tbody/tr[2]/td[2]").get_attribute('innerHTML')


      finally:
        pass

      return status


    def quit(self):
      self.driver.quit()