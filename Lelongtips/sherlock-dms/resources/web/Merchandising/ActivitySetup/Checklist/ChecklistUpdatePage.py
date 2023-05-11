from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, TEXTFIELD, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from resources.web.Merchandising.ActivitySetup.Checklist.ChecklistAddPage import ChecklistAddPage
import secrets


class ChecklistUpdatePage(PageObject):

    PAGE_TITLE = "Merchandising / Activity Setup / Checklist"
    PAGE_URL = "/merchandising/checklist"
    CL_DETAILS = "${checklist_details}"

    @keyword('user updates merchandising checklist using ${data_type} data')
    def user_updates_merchandising_checklist(self, data_type):
        details = self.builtin.get_variable_value(self.CL_DETAILS)
        random_str = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        if data_type == "fixed":
            checklist_desc = details['CHECKLIST_DESC']
            activity_cd = details['ACTIVITY_CODE']
            activity_desc = details['ACTIVITY_DESC']
        else:
            checklist_desc = random_str
            activity_cd = random_str
            activity_desc = random_str

        TEXTFIELD.insert_into_field("Checklist Description", checklist_desc)
        COMMON_KEY.wait_keyword_success("input_text", ChecklistAddPage().locator.activity_cd_field, activity_cd)
        COMMON_KEY.wait_keyword_success("input_text", ChecklistAddPage().locator.activity_desc_field, activity_desc)
        BuiltIn().set_test_variable("${checklist_desc}", checklist_desc)
        BUTTON.click_button("Save")
        BUTTON.click_button("Cancel")
