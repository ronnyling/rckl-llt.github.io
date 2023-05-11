""" Python file related to Claim Management UI """
import random
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import TOGGLE, DRPSINGLE, TEXTFIELD, BUTTON
from robot.libraries.BuiltIn import BuiltIn


class ClaimMgmtEditPage(PageObject):
    """ Functions related to Inventory page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "setting-ui/application-setup?template=p"

    _locators = {
        "ClaimMgmt": "//label[contains(text(),'Enable Stock Out for Damage Claim')]"
    }

    @keyword("user updates claim management using ${data_type} data")
    def user_updates_claim_management_using_data(self, data_type):
        """ Functions to create Inventory using random/given data """
        self.selib.wait_until_element_is_visible(self.locator.ClaimMgmt)
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${ClaimMgmtDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Enable Stock Out for Damage Claim", "Check Profile Match", "Enable Claim Acknowledgement"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                    self._wait_for_page_refresh(timeout=15)
                elif key in ["Auto Promotion Claim Type", "Auto Claim Status"]:
                    DRPSINGLE.selects_from_single_selection_dropdown(key, given_data[label])
                    self._wait_for_page_refresh(timeout=15)
                else:
                    TEXTFIELD.insert_into_field(key, given_data[label])
        else:
            TOGGLE.switch_toggle("Enable Stock Out for Damage Claim", random)
            TOGGLE.switch_toggle("Enable Claim Acknowledgement", random)
            TOGGLE.switch_toggle("Restrict Claim Confirmation before Closure", random)
            TEXTFIELD.insert_into_field_with_length("Promotion Day of Claim Generation (Days)", "number", 1)
            DRPSINGLE.selects_from_single_selection_dropdown("Auto Promotion Claim Type", "random")
            TEXTFIELD.insert_into_field_with_length("Damage Day of Claim Generation (Days)", "number", 1)
            TEXTFIELD.insert_into_field_with_length("Others Day of Claim Generation (Days)", "number", 1)
            DRPSINGLE.selects_from_single_selection_dropdown("Auto Claim Status", "random")

        BUTTON.click_button("Save")






