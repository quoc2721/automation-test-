import time
from selenium.webdriver.common.by import By
from WebDriverInstance import WebDriverInstance
import os

class CheckPageEmployeesAction:
  def __init__(self, click_employees, click_page_employees):
    self.click_employees = click_employees
    self.click_page_employees = click_page_employees


  @staticmethod
  def getActionName():
    return 'Check Page Employees'

  def doAction(self):
    chromeDriver = WebDriverInstance.get_instance().getWebDriver()

    chromeDriver.find_element(By.XPATH, self.click_employees).click()
    time.sleep(2)

    chromeDriver.save_screenshot(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkEmployeesScreenShoot.png'))

    chromeDriver.find_element(By.NAME, self.click_page_employees).click()
    time.sleep(3)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'page2EmployeesScreenShoot.png'))







