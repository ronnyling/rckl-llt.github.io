""" Python file related to Replenishment UI """
import random

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, TOGGLE, TEXTFIELD, DRPSINGLE


class ReplenishmentEditPage(PageObject):
    """ Functions related to Replenishment page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates Replenishment using ${data_type} data")
    def user_updates_replenishment_using_data(self, data_type):
        """ Functions to create replenishment using random/given data """
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${ReplenishmentDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Allow Edit of Replenishment Method", "Validate Manual Purchase Order Qty"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                elif key in ["Replenishment AMS Months"]:
                    TEXTFIELD.insert_into_field(key, given_data[label])
                else:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
        else:

            DRPSINGLE.selects_from_single_selection_dropdown("Default Replenishment Method", "random")
            # DRPSINGLE.selects_from_single_selection_dropdown("Replenishment Product Group", "random")
            TOGGLE.switch_toggle("Allow Edit of Replenishment Method", random)
            TOGGLE.switch_toggle("Validate Manual Purchase Order Qty", random)
            TEXTFIELD.insert_into_field_with_length("Replenishment AMS Months", "number", 1)

        BUTTON.click_button("Save")
