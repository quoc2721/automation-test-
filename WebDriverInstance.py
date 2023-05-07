from selenium import webdriver

class WebDriverInstance:
   __instance__ = None
   webdriver = None
   def __init__(self):
       """ Constructor.
       """
       
       self.webdriver = webdriver.Chrome()
       # self.webdriver = webdriver.Chrome(ChromeDriverManager().install())
       self.webdriver.implicitly_wait(100)

       if WebDriverInstance.__instance__ is None:
           WebDriverInstance.__instance__ = self
       else:
           raise Exception("You cannot create another SingletonGovt class")

   @staticmethod
   def get_instance():
       """ Static method to fetch the current instance.
       """
       if not WebDriverInstance.__instance__:
           WebDriverInstance()
       return WebDriverInstance.__instance__

   def getWebDriver(self):
        return self.webdriver
        