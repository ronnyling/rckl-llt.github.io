""" Python file related to General UI """
import random

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TEXTFIELD, CALENDAR, DRPMULTIPLE, DRPSINGLE, RADIOBTN, TOGGLE, BUTTON


class GeneralEditPage(PageObject):
    """ Functions related to General page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates General using ${data_type} data")
    def user_updates_general_using_data(self, data_type):
        """ Functions to create general using random/given data """
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${GeneralDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Company Name", "Business Registration Number", "Active SKU (3-12 Months)"]:
                    TEXTFIELD.insert_into_field(key, given_data[label])
                elif key in ["Effective Date"]:
                    CALENDAR.select_date_from_calendar(key, given_data[label])
                elif key in ["Product Hierarchy for Display", "Customer Hierarchy for Display", "HHT Product Hierarchy",
                             "HHT Signature Control Screens", "HHT POSM Filter by"]:
                    DRPMULTIPLE.select_from_multi_selection_dropdown(key, given_data[label])
                elif key in ["HHT Product Grouping Feature Level", "HHT Order UI Template"]:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
                elif key in ["Product Cost Price Maintenance by"]:
                    RADIOBTN.select_from_radio_button(key, given_data[label])
                else:
                    TOGGLE.switch_toggle(key, given_data[label])
        else:
            TEXTFIELD.insert_into_field_with_length("Company Name", "letter", 10)
            TEXTFIELD.insert_into_field_with_length("Business Registration Number", "number", 2)
            RADIOBTN.return_visibility_of_radio_buttons("Product Cost Price Maintenance by")
            TOGGLE.switch_toggle("Product Sector Assignment", random)
            TOGGLE.switch_toggle("Enable Distributor Transaction Number", random)
            TOGGLE.return_status_from_toggle("SKU Download to HHT based on")
            TEXTFIELD.insert_into_field_with_length("Active SKU (3-12 Months)", "number", 1)
            TOGGLE.switch_toggle("Auto CN Adjustment in Invoice", random)
            TOGGLE.switch_toggle("Enable Transaction Series Setting", random)
            DRPSINGLE.selects_from_single_selection_dropdown("HHT Product Grouping Feature Level", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("HHT Order UI Template", "random")
            TOGGLE.switch_toggle("HHT End Visit Sync", random)
            DRPSINGLE.selects_from_single_selection_dropdown("HHT Landing Page", "random")
            TOGGLE.switch_toggle("HHT Allow Show Route Plan Desc", random)
            DRPSINGLE.select_from_multi_selection_dropdown("HHT POSM Filter by", "all")
            TOGGLE.switch_toggle("HHT Signature Control", random)
            DRPMULTIPLE.select_from_multi_selection_dropdown("HHT Product Hierarchy", "all")
            DRPMULTIPLE.select_from_multi_selection_dropdown("HHT Signature Control Screens", "all")

        BUTTON.click_button("Save")
