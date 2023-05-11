""" Python file related to promotion UI """

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import  BUTTON, TOGGLE, DRPSINGLE
from resources.web.Common import POMLibrary


class PromotionEditPage(PageObject):
    """ Functions related to promotion page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"

    _locators = {
    }

    @keyword("user updates promotion using ${data_type} data")
    def user_updates_promotion_using_data(self, data_type):
        """ Functions to create promotion using random/given data """
        POMLibrary.POMLibrary().check_page_title("PromotionEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${PromotionDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Apply Promotion (Auto/Manual)", "Allow Multiple Promotion - SKU",
                           "Allow Promotion - Unapproved Customers"]:
                    TOGGLE.switch_toggle(key, given_data[label])
                else:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
        else:
            TOGGLE.switch_toggle("Apply Promotion (Auto/Manual)", "random")
            TOGGLE.switch_toggle("Allow Multiple Promotion - SKU", "random")
            TOGGLE.switch_toggle("Allow Promotion - Unapproved Customers", "random")
            DRPSINGLE.select_from_single_selection_dropdown("Apply Promotion based on", "random")
            DRPSINGLE.select_from_single_selection_dropdown("QPS Open Invoice Check", "random")
            DRPSINGLE.select_from_single_selection_dropdown("QPS Eligibility based on", "random")

        BUTTON.click_button("Save")
