""" Python file related to Mobile Comm UI """
import random
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TOGGLE, TEXTFIELD
from robot.libraries.BuiltIn import BuiltIn


class MobileCompEditPage(PageObject):
    """ Functions related to Inventory page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "setting-ui/application-setup?template=p"

    _locators = {
        "MobileComms": "//label[contains(text(),'Check Profile Match')]"
    }

    @keyword("user updates mobile comm using ${data_type} data")
    def user_updates_mobile_comm_using_data(self, data_type):
        """ Functions to create Inventory using random/given data """
        self.selib.wait_until_element_is_visible(self.locator.MobileComms)
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${MobileCommDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["HHT Validate Device Hardware ID", "Check Profile Match", "Check SafetyNet Error"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                    self._wait_for_page_refresh(timeout=15)
                else:
                    TEXTFIELD.insert_into_field(key, given_data[label])
        else:
            TOGGLE.switch_toggle("HHT Validate Device Hardware ID", random)
            TOGGLE.switch_toggle("Check Profile Match", "random")
            TOGGLE.switch_toggle("Check SafetyNet Error", "random")
            TEXTFIELD.insert_into_field_with_length("API Key", "random", 10)
            TEXTFIELD.insert_into_field_with_length("Validation Timeout (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("JWS Timeout (Hours)", "number", 2)

        BUTTON.click_button("Save")






