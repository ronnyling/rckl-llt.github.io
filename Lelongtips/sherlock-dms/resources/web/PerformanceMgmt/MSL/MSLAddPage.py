from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

from resources import Common
from resources.web import TEXTFIELD, DRPSINGLE, BUTTON, TOGGLE, POPUPMSG, CALENDAR, TAB

class MSLAddPage(PageObject):
    PAGE_TITLE = "Performance Management / Must Sell List"
    PAGE_URL = "/performance/msl/NEW"
    MSL_DETAILS="${msl_details}"
    MSL_DESC = "Description"
    _locators = {
    "ProductAdd" : "(//core-button//child::*[contains(text(),'Add')]//ancestor::core-button[1])[1]",
    "DistAdd": "(//core-button//child::*[contains(text(),'Add')]//ancestor::core-button[1])[2]",
    "RouteAdd": "(//core-button//child::*[contains(text(),'Add')]//ancestor::core-button[1])[3]",
    "CustomerAdd": "(//core-button//child::*[contains(text(),'Add')]//ancestor::core-button[1])[4]",
    "AttributeAdd": "(//core-button//child::*[contains(text(),'Add')]//ancestor::core-button[1])[5]",
    "FirstCheckBox": "(//*[@nz-checkbox=''])[7]",
    }

    @keyword('user creates MSL using ${data_type} data')
    def user_creates_msl_with_data(self, data_type):
        if data_type != "update":
            BUTTON.click_button("Add")
        details = BuiltIn().get_variable_value("${msl_details}")
        if details is None:
            msl_desc = TEXTFIELD.insert_into_field_with_length("Description", "random", 15)
            DRPSINGLE.selects_from_single_selection_dropdown("Type", "MSL")
            CALENDAR.selects_date_from_calendar("Start Date", "greater day")
            CALENDAR.selects_date_from_calendar("End Date", "greater day")
            self.builtin.set_test_variable("${msl_desc}", msl_desc)
        else:
            TEXTFIELD.insert_into_field("Description", details['desc'])
            DRPSINGLE.selects_from_single_selection_dropdown("Type", "MSL")
            CALENDAR.selects_date_from_calendar("Start Date", details['start_dt'])
            CALENDAR.selects_date_from_calendar("End Date", details['end_dt'])
            if details['status'] != "Active":
                TOGGLE.switch_toggle("Status", False)
        BUTTON.click_button("Save")


    @keyword('user validates the missing mandatory error message')
    def validate_missing_mandatory_error_message(self):
        TEXTFIELD.validate_validation_msg("Description", "Please enter a value")
        DRPSINGLE.validate_validation_msg_for_dropdown("Type")

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()
        BUTTON.click_button("Cancel")


    @keyword("user assigns ${type} to MSL")
    def user_assigns_to_MSL(self, type):
        if type=="product":
            Common().wait_keyword_success("click_element", self.locator.ProductAdd)
        elif type=="distributor":
            Common().wait_keyword_success("click_element", self.locator.DistAdd)
        elif type == "route":
            Common().wait_keyword_success("click_element", self.locator.RouteAdd)
        elif type == "customer":
            Common().wait_keyword_success("click_element", self.locator.CustomerAdd)
        else :
            Common().wait_keyword_success("click_element", self.locator.AttributeAdd)

        if type!="attribute":
            DRPSINGLE.selects_from_single_selection_dropdown("Level","random")
        else:
            DRPSINGLE.selects_from_single_selection_dropdown("Attribute", "random")
        Common().wait_keyword_success("click_element", self.locator.FirstCheckBox)
        BUTTON.click_pop_up_screen_button("Assign")
