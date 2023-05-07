import time

from selenium.webdriver.common.by import By

from WebDriverInstance import WebDriverInstance
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os

class CheckPageCustomersAction:
  def __init__(self, click_customer, item_1, item_2, item_3, delete_1, delete_all, click_ok, customer_page,
               select_all, delete_2):
    self.click_customer = click_customer
    self.item_1 = item_1
    self.item_2 = item_2
    self.item_3 = item_3
    self.delete_1 = delete_1
    self.delete_all = delete_all
    self.click_ok = click_ok
    self.customer_page = customer_page
    self.select_all = select_all
    self.delete_2 = delete_2


  @staticmethod
  def getActionName():
    return 'Check Page Customers'

  def doAction(self):
    chromeDriver = WebDriverInstance.get_instance().getWebDriver()

    chromeDriver.find_element(By.XPATH, self.click_customer).click()
    time.sleep(2)
    chromeDriver.save_screenshot(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkCustomersScreenShoot.png'))

    chromeDriver.find_element(By.XPATH, self.item_1).click()
    time.sleep(1)
    chromeDriver.find_element(By.XPATH, self.item_2).click()
    time.sleep(1)
    chromeDriver.find_element(By.XPATH, self.item_3).click()
    time.sleep(1)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkSelectItemScreenShoot.png'))
    chromeDriver.find_element(By.XPATH, self.delete_1).click()
    time.sleep(2)

    chromeDriver.find_element(By.XPATH, self.delete_all).click()
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'deleteAllScreenShoot.png'))
    time.sleep(3)
    chromeDriver.find_element(By.XPATH, self.click_ok).click()

    chromeDriver.find_element(By.XPATH, self.customer_page).click()
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'pageCustomerScreenShoot.png'))
    time.sleep(3)

    chromeDriver.find_element(By.XPATH, self.select_all).click()
    chromeDriver.find_element(By.XPATH, self.delete_2).click()
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'deleteCustomerAllScreenShoot.png'))













