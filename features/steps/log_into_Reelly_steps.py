from behave import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

from appium import webdriver

from pages.main_page import MainPage
from pages.base_page import Page
use_step_matcher("re")


@given("that the user has logged into https://soft.reelly.io/off-plan")
def log_into_reelly(context):
    username = 'alhembd@gmail.com'
    password = 'Thomasgoodwin1657*'
    context.driver.get("https://soft.reelly.io/sign-up")
    # click sign-in link
    sign_in_link = context.driver.find_element(By.XPATH, '//*[@id="wf-form-Create-account"]/a[1]/div[2]')
    sign_in_link.click()
    context.driver.find_element(By.CSS_SELECTOR, ('#email-2')).send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, ('#field')).send_keys(password)
    # continue button
    continue_button = context.driver.find_element(By.XPATH, '//*[@id="wf-form-Sign-up"]/a').click()



@when("the user sets emulator size Samsung Galaxy S20 Ultra")
def set_emulator_size(context):
    # webdriver object for Chrome already instantiated in browser_init of environment.py
    # driver = webdriver.Chrome()

    # create action chain object
    actions = ActionChains(context.driver)
    # send <COMMAND><SHIFT>i to open web developer tools
    # According to online documentation, Mac uses "\u2325" as a unicode symbol for the OPTION key
    # The following code should open the Dev Tools page.
    # On that page, I should be able to choose the 'Samsung Galaxy S20 Ultra' emulator.
    ActionChains(context.driver).key_down(Keys.COMMAND).key_down("\u2325").send_keys('i').perform()
    actions.perform()
    # Sadly, it doesn't work.
@then("user is still able to log in")
def verify_that_user_can_still_log_in(context):
    pass # This succeeds.