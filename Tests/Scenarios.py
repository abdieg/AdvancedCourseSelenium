import inspect
from selenium.webdriver.common.by import By

import Launch
import unittest
from Common import CommonFunctions as cf
from Common.Constant import Constant
from Common.Locators import Locators

class SmokeTest(Launch.Launch):

    def test_login_credentials(self):
        tst_scenario = str(inspect.stack()[0][3].lstrip('test_'))
        print('> Executing test case: ' + tst_scenario)
        cf.wait_for_element(self.driver, Locators.main_logo)
        cf.click_on_element(self.driver, Locators.topbar_button_signin)
        cf.write_on_element(self.driver, Locators.signin_email, Constant.sign_in_user)
        cf.write_on_element(self.driver, Locators.signin_password, Constant.sign_in_pass)
        cf.click_on_element(self.driver, Locators.signin_button)

        cf.wait_for_element(self.driver, Locators.span_my_account)
        cf.assertTrue(cf.does_element_exist(self.driver, Locators.span_my_account))
        cf.wait_for_element(self.driver, Locators.account_order_history)
        cf.assertTrue(cf.does_element_exist(self.driver, Locators.account_order_history))
        cf.wait_for_element(self.driver, Locators.account_credit_slips)
        cf.assertTrue(cf.does_element_exist(self.driver, Locators.account_credit_slips))
        cf.wait_for_element(self.driver, Locators.account_addresses)
        cf.assertTrue(cf.does_element_exist(self.driver, Locators.account_addresses))
        cf.wait_for_element(self.driver, Locators.account_personal_information)
        cf.assertTrue(cf.does_element_exist(self.driver, Locators.account_personal_information))
        cf.wait_for_element(self.driver, Locators.account_wishlists)
        cf.assertTrue(cf.does_element_exist(self.driver, Locators.account_wishlists))
        cf.wait_for_element(self.driver, Locators.account_customer_account)
        cf.assertTrue(cf.does_element_exist(self.driver, Locators.account_customer_account))

        # cf.sleepy(20)
        print('> End of scenario: ' + tst_scenario)
        print('----------------------------------')

if __name__ == '__main__':
    unittest.main()