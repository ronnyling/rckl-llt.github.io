""" Python file related to Account Receivable UI """
import random
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import TOGGLE, BUTTON
from robot.libraries.BuiltIn import BuiltIn


class AccountReceivableEditPage(PageObject):
    """ Functions related to Account Receivable page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "setting-ui/application-setup?template=p"

    _locators = {
        "AccountReceivable": "//label[contains(text(),'Restrict Billing in Case of Outlet Type Changes')]"
    }

    @keyword("user updates account receivable using ${data_type} data")
    def user_updates_account_receivable_using_data(self, data_type):
        """ Functions to create account receivable using random/given data """
        self.selib.wait_until_element_is_visible(self.locator.AccountReceivable)
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${AccountReceivableDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                TOGGLE.switch_toggle(key, given_data[label])
        else:
            TOGGLE.switch_toggle("Restrict Billing in Case of Outlet Type Changes", random)
            TOGGLE.switch_toggle("Allow to Toggle Cash/Credit", random)
            TOGGLE.switch_toggle("Ref No. Mandatory", random)
            TOGGLE.switch_toggle("Allow Return/CN from Single Invoice Only", random)
            TOGGLE.switch_toggle("Allow Editing Price in Return (SFA)", random)

        BUTTON.click_button("Save")
