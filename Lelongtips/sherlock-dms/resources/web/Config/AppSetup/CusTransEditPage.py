from PageObjectLibrary import PageObject
from resources.web import TOGGLE, BUTTON
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import random


class CusTransEditPage(PageObject):
    """ Functions related to Customer Transfer page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
        "CusTrans": "//label[contains(text(),'Customer with Assigned Trade Asset')]"
    }

    @keyword("user updates customer transfer using ${data_type} data")
    def user_updates_customer_transfer_using_data(self, data_type):
        """ Functions to create customer transfer using random/given data """
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${Cus_Trans_Details}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                TOGGLE.switch_toggle(key, given_data[label])

        else:
            TOGGLE.switch_toggle("Customer with Outstanding Collection", random)
            TOGGLE.switch_toggle("Customer with Open Order", random)
            TOGGLE.switch_toggle("Customer with Unconfirmed Invoice", random)
            TOGGLE.switch_toggle("Customer with Unconfirmed Return", random)
            TOGGLE.switch_toggle("Customer with Unconfirmed Exchange", random)
            TOGGLE.switch_toggle("Customer with Unconfirmed CN / DN", random)
            TOGGLE.switch_toggle("Customer with Assigned Trade Asset", random)

        BUTTON.click_button("Save")

