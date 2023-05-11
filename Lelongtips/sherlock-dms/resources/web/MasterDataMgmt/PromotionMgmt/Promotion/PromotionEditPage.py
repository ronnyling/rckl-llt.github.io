import secrets
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources import Common
from resources.web import TEXTFIELD, CALENDAR, RADIOBTN, BUTTON, TAB, PAGINATION
import datetime

NOW = datetime.datetime.now()


class PromotionEditPage(PageObject):
    PAGE_TITLE = "Master Data Management / Promotion Management / Promotion"
    Page_URL = "/promotion/listing"

    _locators = {
        "budget_field": "(//input[@type='text'])[1]"
    }

    def user_updates_the_selected_promotion(self):
        CALENDAR.select_date_from_calendar("Promotion Start Date","next month")
        CALENDAR.select_date_from_calendar("Promotion End Date","next month")
        TEXTFIELD.insert_into_field_with_length("Remarks","letter",15)
        status = RADIOBTN.return_selected_item_of_radio_button("Status")
        if status == "Active":
            RADIOBTN.select_from_radio_button("Status","Inactive")
        else:
            RADIOBTN.select_from_radio_button("Status", "Active")
        BUTTON.click_button("Save")

    @keyword('user validates unable to edit the promotion')
    def user_validates_unable_to_edit(self):
        BUTTON.validate_button_is_hidden("Save")

    def user_updates_the_overall_budget(self):
        rand_amount = secrets.randbelow(1000)
        TEXTFIELD.insert_into_field("Promotion Budget", rand_amount)
        BUTTON.click_button("Save")

    def user_updates_the_route_budget_allocation(self):
        details = BuiltIn().get_variable_value("${PromoDetails}")
        if details:
            amount = details['route_budget']
        else:
            amount = secrets.randbelow(100)
        Common().wait_keyword_success("input_text", self.locator.budget_field, amount)
        BUTTON.click_button("Save")

    @keyword("user validates ${field_name} field is disabled")
    def user_validates_field_is_disabled(self,field_name):
        TEXTFIELD.verifies_text_field_is_disabled(field_name)

    @keyword("user validates budget tab is ${condition}")
    def user_validates_budget_tab_is(self,condition):
        if condition == "enabled":
            TAB.validate_tab_is_visible("Budget Allocation")
        else :
            TAB.validate_tab_is_hidden("Budget Allocation")

    def user_approves_promotion(self):
        BUTTON.click_button("Approve")

