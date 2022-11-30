from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u':launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install())



@when(u':open orange HRpage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # context.driver.implicitWait(5)




@then(u':verify the logo presence')
def logoPresene(context):
    status=context.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
    assert status is True





@then(u':close browser')
def closeBrowser(context):
    context.driver.close()


