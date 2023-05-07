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

class CheckEditorsAction:
  def __init__(self, click_editor, clear_input, add_content):
    self.click_editor = click_editor
    self.clear_input = clear_input
    self.add_content = add_content

  @staticmethod
  def getActionName():
    return 'Check Editor'

  def doAction(self):
    chromeDriver = WebDriverInstance.get_instance().getWebDriver()

    chromeDriver.find_element(By.XPATH, self.click_editor).click()
    time.sleep(2)

    inputContent = chromeDriver.find_element(By.XPATH, self.clear_input)
    inputContent.clear()
    inputContent.send_keys(self.add_content)

    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkEditContentScreenShoot.png'))
    time.sleep(4)



















