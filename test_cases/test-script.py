import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
options = Options()

load_dotenv()

username = os.getenv('BROWSERSTACK_USERNAME')
accessKey = os.getenv('BROWSERSTACK_ACCESS_KEY')

desired_cap = {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': 'latest',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1', # Your tests will be organized within this build
}
    
command_executor='https://'+username+':'+accessKey+'@hub-cloud.browserstack.com/wd/hub'
# command_executor = "https://tnma_Wc4uog:pPCfZz9oPSjniGuUippt@hub-cloud.browserstack.com/wd/hub"
print(command_executor)
options.set_capability('bstack:options', desired_cap)
driver = webdriver.Remote(
    command_executor='https://'+username+':'+accessKey+'@hub.browserstack.com/wd/hub',
    desired_capabilities=desired_cap 
)
# Rest of the test case goes here



# from browserstack.local import Local
  
# # Creates an instance of Local
# bs_local = Local()
  
# # You can also use the environment variable - "BROWSERSTACK_ACCESS_KEY".
# bs_local_args = { "key": accessKey }
  
# # Starts the Local instance with the required arguments
# bs_local.start(**bs_local_args)
  
# # Check if BrowserStack local instance is running
# print(bs_local.isRunning())
  
# Your test code goes here, from creating the driver instance till the end.
driver.get("https://www.youtube.com/")
driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
driver.quit()
# Stop the Local instance after your test run is completed. 
# bs_local.stop()