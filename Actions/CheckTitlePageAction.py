from WebDriverInstance import WebDriverInstance
import os

class CheckTitlePageAction:
  def __init__(self, titlePage):
    self.titlePage = titlePage    

  @staticmethod
  def getActionName():
    return 'Check Title Page'

  def doAction(self):            
      chromeDriver = WebDriverInstance.get_instance().getWebDriver()
      print(chromeDriver.title)
      assert chromeDriver.title == self.titlePage, "title page is incorrect!"
      #chromeDriver.save_screenshot("ScreenShoots/checkPageTitleScreenShoot.png")
      chromeDriver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ScreenShoots', 'checkPageTitleScreenShoot.png'))
    #   driver = webdriver.Chrome()
    #   driver.implicitly_wait(60)
