""" Python file related to round off UI """
import secrets

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.web import BUTTON, TEXTFIELD, DRPSINGLE
from resources.web.Common import POMLibrary


class RoundOffEditPage(PageObject):
    """ Functions related to round off page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"
    CURRENCY_NAME = "Currency Name"

    _locators = {
    }

    @keyword("user updates round off using ${data_type} data")
    def user_updates_round_off_using_data(self, data_type):
        """ Functions to create round off using random/given data """
        POMLibrary.POMLibrary().check_page_title("RoundOffEditPage")
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${RoundOffDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                if key in ["Currency Setting", self.CURRENCY_NAME, "Payment Adjustment"]:
                    TEXTFIELD.insert_into_field(key, given_data[label])
                else:
                    DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
        else:
            item = TEXTFIELD.insert_into_field("Currency Setting", secrets.choice(["$", "US$"]))
            if item == "$":
                TEXTFIELD.insert_into_field(self.CURRENCY_NAME, "Dollar")
            else:
                TEXTFIELD.insert_into_field(self.CURRENCY_NAME, "US Dollar")
            DRPSINGLE.selects_from_single_selection_dropdown("Round Off Decimal (Data Storage)", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("Round Off Decimal (Display)", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("Round Off Value", "random")
            DRPSINGLE.selects_from_single_selection_dropdown("Round Off to the", "random")
            TEXTFIELD.insert_into_field_with_length("Payment Adjustment", "number", 1)
            DRPSINGLE.selects_from_single_selection_dropdown("Invoice Adjustment Method", "random")

        BUTTON.click_button("Save")
