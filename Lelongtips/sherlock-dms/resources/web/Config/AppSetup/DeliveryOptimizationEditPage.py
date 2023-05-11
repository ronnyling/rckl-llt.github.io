""" Python file related to Delivery Optimization UI """
import random

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TOGGLE, TEXTFIELD, BUTTON, RADIOBTN, DRPMULTIPLE


class DeliveryOptimizationEditPage(PageObject):
    """ Functions related to Delivery Optimization page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates Delivery Optimization using ${data_type} data")
    def user_updates_delivery_optimization_using_data(self, data_type):
        """ Functions to create Delivery Optimization using random/given data """
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${DeliveryOptimizationDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Enable Delivery Optimisation"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                elif key in ["Address Fields for Delivery Optimisation"]:
                    DRPMULTIPLE.select_from_multi_selection_dropdown(key, given_data[label])
                elif key in ["Delivery Optimisation by"]:
                    RADIOBTN.select_from_radio_button(key, given_data[label])
                else:
                    TEXTFIELD.insert_into_field(key, given_data[label])
        else:

            TOGGLE.switch_toggle("Enable Delivery Optimisation", random)
            DRPMULTIPLE.select_from_multi_selection_dropdown("Address Fields for Delivery Optimisation", "all")
            RADIOBTN.select_from_radio_button("Delivery Optimisation by", "random")
            TEXTFIELD.verifies_text_field_is_disabled("Open Route Service Key")

        BUTTON.click_button("Save")
