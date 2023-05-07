import time
from selenium.webdriver.common.by import By
from WebDriverInstance import WebDriverInstance
import os

class CheckAddCalendarsAction:
  def __init__(self, click_calendar, add_task, select_details, id_title, id_location, id_description, title,
               location, description, save_1):
    self.click_calendar = click_calendar
    self.add_task = add_task
    self.select_details = select_details
    self.id_title = id_title
    self.id_location = id_location
    self.id_description = id_description
    self.title = title
    self.location = location
    self.description = description
    self.save_1 = save_1


  @staticmethod
  def getActionName():
    return 'Check Add Calendar'

  def doAction(self):
    chromeDriver = WebDriverInstance.get_instance().getWebDriver()

    chromeDriver.find_element(By.XPATH, self.click_calendar).click()
    time.sleep(1)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkCalendarScreenShoot.png'))

    chromeDriver.find_element(By.XPATH, self.add_task).click()
    time.sleep(2)
    chromeDriver.find_element(By.XPATH, self.select_details).click()

    chromeDriver.find_element(By.ID, self.id_title).send_keys(self.title)
    time.sleep(1)
    chromeDriver.find_element(By.ID, self.id_location).send_keys(self.location)
    time.sleep(1)
    chromeDriver.find_element(By.ID, self.id_description).send_keys(self.description)
    time.sleep(1)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkFormTaskScreenShoot.png'))
    chromeDriver.find_element(By.XPATH, self.save_1).click()
    time.sleep(2)

















