import time
from selenium.webdriver.common.by import By
from WebDriverInstance import WebDriverInstance
import os

class CheckChartsAction:
  def __init__(self, select_line, select_bar, select_pie, select_financial):
    self.select_line = select_line
    self.select_bar = select_bar
    self.select_pie = select_pie
    self.select_financial = select_financial

  @staticmethod
  def getActionName():
    return 'Check Charts'

  def doAction(self):
    chromeDriver = WebDriverInstance.get_instance().getWebDriver()

    chromeDriver.find_element(By.XPATH, self.select_line).click()
    time.sleep(3)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkLineChartsScreenShoot.png'))
    chromeDriver.find_element(By.XPATH, self.select_bar).click()
    time.sleep(2)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkBarChartsScreenShoot.png'))
    chromeDriver.find_element(By.XPATH, self.select_pie).click()
    time.sleep(3)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkPieChartsScreenShoot.png'))
    chromeDriver.find_element(By.XPATH, self.select_financial).click()
    time.sleep(3)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkFinancialChartsScreenShoot.png'))



















