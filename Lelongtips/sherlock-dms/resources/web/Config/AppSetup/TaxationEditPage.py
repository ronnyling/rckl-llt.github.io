""" Python file related to taxation UI """

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, DRPSINGLE, DRPMULTIPLE, TOGGLE
from resources.web.Common import POMLibrary


class TaxationEditPage(PageObject):
    """ Functions related to taxation page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates taxation using ${data_type} data")
    def user_updates_taxation_using_data(self, data_type):
        """ Functions to create taxation using random/given data """
        POMLibrary.POMLibrary().check_page_title("TaxationEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${TaxationDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Tax Model", "Product - Tax Group Mapping Level", "Default Customer Tax Group",
                           "Default Supplier Tax Group"]:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
                elif key in ["Discounts to Be Considered"]:
                    DRPMULTIPLE.select_from_multi_selection_dropdown(key, given_data[label])
                else:
                    TOGGLE.switch_toggle(key, given_data[label])
        else:
            DRPSINGLE.select_from_single_selection_dropdown("Tax Model", "random")
            item = self.builtin.get_variable_value("${selectedItem}")
            if not item == "India GST":
                TOGGLE.switch_toggle("Accumulative Tax Enable", "random")
                TOGGLE.switch_toggle("Tax Setting Apply On - Multi Select", "random")
            TOGGLE.switch_toggle("Discount Impact", "random")
            toggle_selection = self.builtin.get_variable_value("${toggle_selection}")
            if toggle_selection:
                DRPMULTIPLE.select_from_multi_selection_dropdown("Discounts to Be Considered", "random")
            TOGGLE.switch_toggle("Enable Service Tax - Space Buy", "random")

        BUTTON.click_button("Save")
