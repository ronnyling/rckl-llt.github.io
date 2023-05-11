import secrets
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources import Common, COMMON_KEY
from resources.web.MasterDataMgmt.PromotionMgmt.Promotion import PromotionEditPage
from resources.web import TEXTFIELD, CALENDAR, RADIOBTN, BUTTON, TAB, PAGINATION, DRPSINGLE, CHECKBOX, LABEL
import datetime

NOW = datetime.datetime.now()


class PromotionBudgetPage(PageObject):
    PAGE_TITLE = "Master Data Management / Promotion Management / Promotion"
    Page_URL = "/promotion/listing"

    _locators = {
        "dist_budget_field": "(//input[@type='text'])[1]",
        "route_budget_field" : "(//input[@type='text'])[2]",
        "budget_tab": "//span[contains(text(),'Budget Allocation')]",
    }

    @keyword('user selects Budget Allocation tab')
    def navigate_to_budget_tab(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.budget_tab)

    def validate_budget_allocation_tab_is_displayed(self):
        LABEL.validate_label_is_visible("Distributor Budget Allocation")
        LABEL.validate_label_is_visible("Route Budget Allocation")

    @keyword('user updates new budget for ${field}')
    def user_updates_new_budget_for_promo(self, field):
        budget_details = BuiltIn().get_variable_value("${budget_update}")
        if budget_details is None:
            budget = str(secrets.randbelow(1000))
        else :
            budget = budget_details['BUDGET']
        if field == "distributor":
            COMMON_KEY.wait_keyword_success("input_text", self.locator.dist_budget_field, budget)
        else :
            COMMON_KEY.wait_keyword_success("input_text", self.locator.route_budget_field, budget)
        BUTTON.click_button("Save")
