from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import TEXTFIELD, BUTTON
import secrets
from robot.libraries.BuiltIn import BuiltIn


class ChecklistAddPage(PageObject):
    PAGE_TITLE = "Master Data Management / Supervisor / Checklist"
    PAGE_URL = "/supervisor-checklist"
    CHECKLIST_DETAILS="${checklist_details}"
    _locators = {
        'add_checklist' : "//core-dynamic-actions[@class='ng-star-inserted']//core-button[@class='ng-star-inserted']//span//button[@type='submit']",
        'add_workplan' : "//span[@ng-reflect-ng-switch='primary']//button[@type='submit']",
        'item_cd' : "//td[2]/core-dynamic-field[1]/div[1]/core-textfield[1]/nz-form-item[1]/nz-form-control[1]/div[1]/span[1]/nz-input-group[1]/input[1]",
        'item_desc' : "//td[3]/core-dynamic-field[1]/div[1]/core-textfield[1]/nz-form-item[1]/nz-form-control[1]/div[1]/span[1]/nz-input-group[1]/input[1]",
        'workplan_confirm' : "//div[@class='ant-modal-footer ng-star-inserted']//button[@class='ant-btn ng-star-inserted ant-btn-primary']"
    }

    @keyword('user creates checklist with ${data_type} data')
    def user_creates_checklist_with_data(self, data_type):
        BUTTON.click_button("Add")
        checklist_code = TEXTFIELD.insert_into_field_with_length("Checklist Code","random",10)
        checklist_desc = TEXTFIELD.insert_into_field_with_length("Checklist Description", "random", 15)
        RADIOBTN.select_from_radio_button("Checklist Type","Route")
        CALENDAR.selects_date_from_calendar("Start Date","next day")
        CALENDAR.selects_date_from_calendar("End Date", "greater day")
        if data_type == "no checklist":
            self.user_adds_workplan_item()
        elif data_type == "no workplan":
            self.user_adds_checklist_item()
        else :
            self.user_adds_workplan_item()
            self.user_adds_checklist_item()
        BuiltIn().set_test_variable("${checklist_code}", checklist_code)
        BuiltIn().set_test_variable("${checklist_desc}", checklist_desc)
        BUTTON.click_button("Save")

    @keyword('user adds checklist item')
    def user_adds_checklist_item(self):
        item_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        item_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(25))
        self.selib.click_element(self.locator.add_checklist)
        self.selib.input_text(self.locator.item_cd, item_code)
        self.selib.input_text(self.locator.item_desc, item_desc)

    @keyword('user adds workplan item')
    def user_adds_workplan_item(self):
        self.selib.click_element(self.locator.add_workplan)
        BUTTON.click_hyperlink_in_popup("0")
        self.selib.click_element(self.locator.workplan_confirm)

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()
