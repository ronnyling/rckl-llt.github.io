""" Python file related to Data Retention UI """

from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import TEXTFIELD, BUTTON
from robot.libraries.BuiltIn import BuiltIn


class DataRetentionEditPage(PageObject):
    """ Functions related to Data Retention page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "setting-ui/application-setup?template=p"

    _locators = {
        "DataRetention": "//label[contains(text(),'Order Status (Days)')]"
    }

    @keyword("user updates data retention using ${data_type} data")
    def user_updates_data_retention_using_data(self, data_type):
        """ Functions to create data retention using random/given data """
        self.selib.wait_until_element_is_visible(self.locator.DataRetention)
        if data_type == "fixed":
            given_data = BuiltIn().get_variable_value("${DataRetentionDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                TEXTFIELD.insert_into_field(key, given_data[label])
        else:
            TEXTFIELD.insert_into_field_with_length("Order Status (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Sales History (Months)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Stock Take History (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Past Route Plan (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Future Route Plan (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Missed Call (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Missed Call Reminder (Days)", "number", 1)
            TEXTFIELD.insert_into_field_with_length("Average Visit Sales", "number", 2)
            TEXTFIELD.insert_into_field_with_length("No Distribution (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Purge Batch Code (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("MSL Compliance (Days)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Load Invoice From Past", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Ref. Doc. Period (DMS)", "number", 2)
            TEXTFIELD.insert_into_field_with_length("Ref. Doc. Period (SFA)", "number", 2)

        BUTTON.click_button("Save")






