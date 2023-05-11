from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, COMMON_KEY, CALENDAR
import secrets


class ChecklistAddPage(PageObject):

    PAGE_TITLE = "Merchandising / Activity Setup / Checklist"
    PAGE_URL = "/merchandising/checklist"
    CL_DETAILS = "${checklist_details}"

    _locators = {
        "activity_cd_field": "(//*[contains(text(),'Activity Code')]/following::input)[2]",
        "activity_desc_field": "(//*[contains(text(),'Activity Code')]/following::input)[3]"
    }

    @keyword('user creates merchandising checklist using ${data_type} data')
    def user_creates_merchandising_checklist(self, data_type):
        details = self.builtin.get_variable_value(self.CL_DETAILS)
        random_str = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        BUTTON.click_button("Add")
        if data_type == "fixed":
            checklist_desc = details['CHECKLIST_DESC']
            start_dt = details['START_DATE']
            end_dt = details['END_DATE']
            activity_cd = details['ACTIVITY_CODE']
            activity_desc = details['ACTIVITY_DESC']
            status = details['STATUS']
        else:
            checklist_desc = random_str
            start_dt = "next day"
            end_dt = "next day"
            activity_cd = random_str
            activity_desc = random_str
            status = secrets.choice(["Active", "Inactive"])

        TEXTFIELD.insert_into_field("Checklist Description", checklist_desc)
        CALENDAR.selects_date_from_calendar("Start Date", start_dt)
        CALENDAR.selects_date_from_calendar("End Date", end_dt)
        BUTTON.click_button("Add Row")
        COMMON_KEY.wait_keyword_success("input_text", self.locator.activity_cd_field, activity_cd)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.activity_desc_field, activity_desc)
        DRPSINGLE.select_from_single_selection_dropdown("Status", status)
        BuiltIn().set_test_variable("${checklist_desc}", checklist_desc)
        BUTTON.click_button("Save")
        BUTTON.click_button("Cancel")
