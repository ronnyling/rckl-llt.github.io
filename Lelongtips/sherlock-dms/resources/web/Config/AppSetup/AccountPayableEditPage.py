""" Python file related to Account Payable UI """
import random
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import TOGGLE, BUTTON
from robot.libraries.BuiltIn import BuiltIn


class AccountPayableEditPage(PageObject):
    """ Functions related to Account Payable page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "setting-ui/application-setup?template=p"

    _locators = {
        "AccountPayable": "//label[contains(text(),'Make Reference Number Mandatory')]"
    }

    @keyword("user updates account payable using ${data_type} data")
    def user_updates_account_payable_using_data(self, data_type):
        """ Functions to create account payable using random/given data """
        self.selib.wait_until_element_is_visible(self.locator.AccountPayable)
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${AccountPayableDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                TOGGLE.switch_toggle(key, given_data[label])
        else:
            TOGGLE.switch_toggle("Make Reference Number Mandatory", random)

        BUTTON.click_button("Save")






