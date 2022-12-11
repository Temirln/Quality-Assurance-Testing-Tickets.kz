import datetime
import os
from time import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from dotenv import load_dotenv



@pytest.fixture(scope="class")
def setUp_tests(request,browser):
    load_dotenv()
    BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "tnma_Wc4uog"
    BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "pPCfZz9oPSjniGuUippt"
    URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
    BUILD_NAME = "browserstack-build-1"
    capabilities = [
        {
            "browserName": "Chrome",
            "browserVersion": "103.0",
            "os": "Windows",
            "osVersion": "11",
            "sessionName": "BStack Python sample parallel", # test name
            "buildName": BUILD_NAME,  # Your tests will be organized within this build
        },
        {
            "browserName": "Firefox",
            "browserVersion": "102.0",
            "os": "Windows",
            "osVersion": "10",
            "sessionName": "BStack Python sample parallel",
            "buildName": BUILD_NAME,
        },
        {
            "browserName": "Safari",
            "browserVersion": "14.1",
            "os": "OS X",
            "osVersion": "Big Sur",
            "sessionName": "BStack Python sample parallel",
            "buildName": BUILD_NAME,
        },
    ]
        

    global driver
    if browser == "fox":
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver = webdriver.Firefox(service = FirefoxService(r"D:\IDE Projects\VS Code Projects\QA_Selenium\webdrivers\firefoxdriver\geckodriver.exe"))
    elif browser == "chrome":
        # driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service = ChromeService(r"D:\IDE Projects\VS Code Projects\QA_Selenium\webdrivers\chrome-driver\chromedriver.exe"))
    elif browser == "edge":
        # driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()))
        driver = webdriver.Edge(service = EdgeService(r"D:\IDE Projects\VS Code Projects\QA_Selenium\webdrivers\edgedriver\msedgedriver.exe"))
    else:
        driver = webdriver.Chrome(service = ChromeService(r"D:\IDE Projects\VS Code Projects\QA_Selenium\webdrivers\chrome-driver\chromedriver.exe"))
    
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver,10)
    driver.maximize_window()
    request.cls.driver = driver 
    request.cls.wait = wait

    yield
    
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")

def pytest_html_report_title(report):
    report.title = "My very own title!"

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("https://tickets.kz/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure


#             # now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             filename = report.nodeid.replace("::","_") + ".png"
#             destination_file = os.path.join(report_directory,filename)
#             # driver.save_screenshot(f".\\Screenshots\\fail_{now}.png")
#             # **feature_request = item.funcargs["request"]
#             # **driver = feature_request.getfixturevalue("setup")

#             driver.save_screenshot(destination_file)
#             if filename:
#                 html = f'<div><img src="{filename}" alt ="screenshot" style = "width:300px;height:300px" onclick="window.open(this.src)"  align="right/></div>"'
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra