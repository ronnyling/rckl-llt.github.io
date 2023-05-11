""" Python file related to merchandising UI """

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, TOGGLE, RADIOBTN, DRPSINGLE
from resources.web.Common import POMLibrary


class MerchandisingEditPage(PageObject):
    """ Functions related to merchandising page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates merchandising using ${data_type} data")
    def user_updates_merchandising_using_data(self, data_type):
        """ Functions to create merchandising using random/given data """
        POMLibrary.POMLibrary().check_page_title("MerchandisingEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${MerchandisingDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Auto Populate Facing Setup", "Customer Level"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                elif key in ["POSM Inventory Trigger"]:
                    RADIOBTN.select_from_radio_button(key, given_data[label])
                else:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
        else:
            DRPSINGLE.select_from_single_selection_dropdown("Product Hierarchy Level", "random")
            TOGGLE.switch_toggle("Auto Populate Facing Setup", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Route Activities - Customer Hierarchy Level", "random")
            RADIOBTN.select_from_radio_button("POSM Inventory Trigger", "random")
            TOGGLE.switch_toggle("Customer Level", "random")
            toggle_selection = BuiltIn().get_variable_value("${toggle_selection}")
            if toggle_selection:
                DRPSINGLE.select_from_single_selection_dropdown("Customer Hierarchy Level", "random")
            else:
                DRPSINGLE.select_from_single_selection_dropdown("Customer Attribute", "random")

        BUTTON.click_button("Save")

    @keyword("user updates merchandising audit by using ${data_type} data")
    def user_updates_merchandising_audit_by_using_data(self, data_type):
        """ Functions to create merchandising audit by using random/given data """
        POMLibrary.POMLibrary().check_page_title("MerchandisingEditPage")
        if data_type == "given":
            given_data = BuiltIn().get_variable_value("${MerchandisingDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                RADIOBTN.select_from_radio_button(key, given_data[label])
        else:
            RADIOBTN.select_from_radio_button("Merchandising Audit by", "random")

        BUTTON.click_button("Save")
