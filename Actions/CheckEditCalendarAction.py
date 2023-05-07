import time
from selenium.webdriver.common.by import By
from WebDriverInstance import WebDriverInstance
import os

class CheckEditCalendarsAction:
  def __init__(self, select_task_1, select_edit, id_title_2, value_edit, save_2,
               select_task_2, select_delete, delete_task):
    self.select_task_1 = select_task_1
    self.select_edit = select_edit
    self.id_title_2 = id_title_2
    self.value_edit = value_edit
    self.save_2 = save_2
    self.select_task_2 = select_task_2
    self.select_delete = select_delete
    self.delete_task = delete_task

  @staticmethod
  def getActionName():
    return 'Check Edit Calendar'

  def doAction(self):
    chromeDriver = WebDriverInstance.get_instance().getWebDriver()

    chromeDriver.find_element(By.XPATH, self.select_task_1).click()
    chromeDriver.find_element(By.XPATH, self.select_edit).click()
    time.sleep(2)

    chromeDriver.find_element(By.XPATH, self.id_title_2).send_keys(self.value_edit)
    time.sleep(1)
    chromeDriver.find_element(By.XPATH, self.save_2).click()
    time.sleep(3)

    chromeDriver.find_element(By.XPATH, self.select_task_2).click()
    time.sleep(2)
    chromeDriver.find_element(By.XPATH, self.select_delete).click()
    time.sleep(1)
    chromeDriver.save_screenshot(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkEditCalendarScreenShoot.png'))
    chromeDriver.find_element(By.XPATH, self.delete_task).click()


















