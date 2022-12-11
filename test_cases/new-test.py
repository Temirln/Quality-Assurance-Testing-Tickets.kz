from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': 'latest',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      },
      {
      'device': 'Google Pixel 5',
      'os_browser': '11.0',
      'real_mobile': 'true',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'device': 'iPhone 12 Pro',
      'os_browser': '14',
      'real_mobile': 'true',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
}]   
#run_session function searches for 'BrowserStack' on google.com
def run_session(desired_cap):
  driver = webdriver.Remote(
      command_executor='https://tnma_Wc4uog:pPCfZz9oPSjniGuUippt@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)
  driver.get("https://www.google.com")
  if not "Google" in driver.title:
      raise Exception("Unable to load google page!")
  elem = driver.find_element_by_name("q")
  elem.send_keys("BrowserStack")
  elem.submit()
  try:
      WebDriverWait(driver, 5).until(EC.title_contains("BrowserStack"))
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
  except TimeoutException:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
  print(driver.title)
  driver.quit()
#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()