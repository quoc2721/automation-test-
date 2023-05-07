import time
from selenium.webdriver.common.by import By
from WebDriverInstance import WebDriverInstance
import os

class CheckNavbarAction:
  def __init__(self, click_cart, click_erase, click_chat, click_notification,
               click_profile, click_erase_2):
    self.click_cart = click_cart
    self.click_erase = click_erase
    self.click_chat = click_chat
    self.click_notification = click_notification
    self.click_profile = click_profile
    self.click_erase_2 = click_erase_2

  @staticmethod
  def getActionName():
    return 'Check Navbar'

  def doAction(self):
    chromeDriver = WebDriverInstance.get_instance().getWebDriver()

    chromeDriver.find_element(By.XPATH, self.click_cart).click()
    time.sleep(2)
    chromeDriver.save_screenshot(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'clickCartScreenShoot.png'))
    chromeDriver.find_element(By.XPATH, self.click_erase).click()
    chromeDriver.find_element(By.XPATH, self.click_chat).click()
    time.sleep(2)

    chromeDriver.save_screenshot(os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'ScreenShoots', 'clickChatScreenShoot.png'))

    chromeDriver.find_element(By.XPATH, self. click_notification).click()
    time.sleep(2)
    chromeDriver.save_screenshot(os.path.join(os.path.dirname(
          os.path.realpath(__file__)), 'ScreenShoots', 'clickNotiScreenShoot.png'))

    chromeDriver.find_element(By.XPATH, self.click_profile). click()
    time.sleep(2)
    chromeDriver.save_screenshot(os.path.join(os.path.dirname(
          os.path.realpath(__file__)), 'ScreenShoots', 'clickProfileScreenShoot.png'))

    chromeDriver.find_element(By.XPATH, self.click_erase_2).click()







