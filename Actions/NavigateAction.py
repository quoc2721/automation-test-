from WebDriverInstance import WebDriverInstance

class NavigateAction:
  def __init__(self, url):
    self.url = url    

  @staticmethod
  def getActionName():
    return 'Navigate'

  def doAction(self):
      print('Navigate to URL')
      print(self.url)

      chromeDriver = WebDriverInstance.get_instance().getWebDriver()
      chromeDriver.maximize_window()
      print(chromeDriver)
      chromeDriver.get(self.url)
    #   driver = webdriver.Chrome()
    #   driver.implicitly_wait(60)
