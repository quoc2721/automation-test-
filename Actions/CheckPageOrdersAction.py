
import time
from selenium.webdriver.common.by import By
from WebDriverInstance import WebDriverInstance
import os

class CheckPageOrdersAction:
  def __init__(self, click_order, click_page_2):
    self.click_order = click_order
    self.click_page_2 = click_page_2


  @staticmethod
  def getActionName():
    return 'Check Page Order'

  def doAction(self):
    chromeDriver = WebDriverInstance.get_instance().getWebDriver()

    chromeDriver.find_element(By.XPATH, self.click_order).click()
    time.sleep(2)

    chromeDriver.save_screenshot(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'pageOrderScreenShoot.png'))

    chromeDriver.find_element(By.XPATH, self.click_page_2).click()
    time.sleep(3)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'page2OrderScreenShoot.png'))







