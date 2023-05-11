""" Python file related to Inventory UI """
import random
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TOGGLE, BUTTON


class InventoryEditPage(PageObject):
    """ Functions related to Inventory page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates Inventory using ${data_type} data")
    def user_updates_Inventory_using_data(self, data_type):
        """ Functions to create Inventory using random/given data """
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${InventoryDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                TOGGLE.switch_toggle(key, given_data[label])
        else:
            TOGGLE.switch_toggle("Stock Adjustment Approval", random)
            TOGGLE.switch_toggle("Stock Out Approval", random)
            TOGGLE.switch_toggle("Stock Audit Approval", random)

        BUTTON.click_button("Save")
