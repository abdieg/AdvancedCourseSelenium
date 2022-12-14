import random
import string
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from Common.Constant import Constant

def sleepy(_seconds):
     time.sleep(_seconds)

def wait_for_alert(_driver):
    timeout = Constant.timeout
    ignored_exceptions = (StaleElementReferenceException,)
    try:
        alert_present = EC.alert_is_present()
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(alert_present)
    except TimeoutException:
        print('Timed out waiting for alert to display')

def wait_for_element(_driver, _element):
    _by = By.XPATH
    timeout = Constant.timeout
    ignored_exceptions = (StaleElementReferenceException,)
    try:
        element_present = EC.presence_of_element_located((_by, _element))
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(element_present)
        element_visible = EC.visibility_of_element_located((_by, _element))
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(element_visible)
        element_clickable = EC.element_to_be_clickable((_by, _element))
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(element_clickable)
        print('Element found: ' + str(_element))
    except TimeoutException:
        print('Timed out waiting for element to load: ' + _element)

def does_element_exist(_driver, _xpath):
    try:
        _driver.find_element_by_xpath(_xpath)
    except NoSuchElementException:
        return False
    return True

def click_on_element(_driver, _element):
    _by = By.XPATH
    timeout = Constant.timeout
    ignored_exceptions = (StaleElementReferenceException,)
    try:
        element_present = EC.presence_of_element_located((_by, _element))
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(element_present)
        element_visible = EC.visibility_of_element_located((_by, _element))
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(element_visible)
        element_clickable = EC.element_to_be_clickable((_by, _element))
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(element_clickable).click()
        print('Element found to be clicked: ' + str(_element))
    except TimeoutException:
        print('Timed out waiting for element to load: ' + _element)

def write_on_element(_driver, _element, _text):
    _by = By.XPATH
    timeout = Constant.timeout
    ignored_exceptions = (StaleElementReferenceException,)
    try:
        element_present = EC.presence_of_element_located((_by, _element))
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(element_present)
        element_visible = EC.visibility_of_element_located((_by, _element))
        WebDriverWait(_driver, timeout, ignored_exceptions=ignored_exceptions).until(element_visible).send_keys(_text)
        print('Element found to write on it: ' + str(_element))
    except TimeoutException:
        print('Timed out waiting for element to load: ' + _element)

def generate_random_lower_string(_length):
    result = ''.join(random.choice(string.ascii_lowercase) for x in range(_length))
    return result

def generate_random_upper_string(_length):
    result = ''.join(random.choice(string.ascii_uppercase) for x in range(_length))
    return result

def assertTrue(_input):
    if _input is True:
        print('Successful assert: True')
    else:
        raise AssertionError()

def assertFalse(_input):
    if _input is False:
        print('Successful assert: False')
    else:
        raise AssertionError()

def assertText(_base, _comparison):
    if str(_base) == str(_comparison):
        print('Assert successful: ' + str(_comparison))
    else:
        print('Assert fail. Actual value is: ' + str(_comparison))
        raise AssertionError()