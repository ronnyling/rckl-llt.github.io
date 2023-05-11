""" Python file related to pricing UI """

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, TOGGLE, TEXTFIELD, DRPSINGLE
from resources.web.Common import POMLibrary


class PricingEditPage(PageObject):
    """ Functions related to pricing page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates pricing using ${data_type} data")
    def user_updates_pricing_using_data(self, data_type):
        """ Functions to create pricing using random/given data """
        POMLibrary.POMLibrary().check_page_title("PricingEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${PricingDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["No. of Margin Input"]:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
                elif key in ["MRP Managed", "Batch Managed", "Allow Batch Creation"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                else:
                    TEXTFIELD.insert_into_field(key, given_data[label])
        else:
            TOGGLE.switch_toggle("MRP Managed", "random")
            TOGGLE.switch_toggle("Batch Managed", "random")
            TOGGLE.switch_toggle("Allow Batch Creation", "random")
            DRPSINGLE.select_from_single_selection_dropdown("No. of Margin Input", "random")
            selected_item = self.builtin.get_variable_value("${selectedItem}")
            random_text = "test margin convention"
            for i in range(1, int(selected_item)):
                field_name = "Margin Naming Convention {0}".format(i)
                TEXTFIELD.insert_into_field(field_name, random_text)
        BUTTON.click_button("Save")
