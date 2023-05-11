from PageObjectLibrary import PageObject
from resources.web.CompTrx.Claims.ClaimListPage import ClaimListPage
from robot.libraries.BuiltIn import BuiltIn
from resources.web import DRPSINGLE, BUTTON, COMMON_KEY, CALENDAR
from robot.api.deco import keyword


class ClaimAddPage(PageObject):
    """ Functions for Claim Add Page actions """

    _locators = {
        "promotion": "//*[contains(text(),'Promotion')]//following::core-button[@ng-reflect-icon='ellipsis'][1]"
    }

    @keyword("user creates ${type} claim")
    def create_claim(self, type):
        details = BuiltIn().get_variable_value("${ClaimDetails}")
        from_date = details['fromDate']
        to_date = details['toDate']

        if type == "spacebuy":
            claim_type = "Space Buy - Off-Invoice Promotion"

        ClaimListPage().click_create_claim_button()
        DRPSINGLE.select_from_single_selection_dropdown("Claim Type", claim_type)
        CALENDAR.select_date_from_calendar("From Date", from_date)
        CALENDAR.select_date_from_calendar("To Date", to_date)

        COMMON_KEY.wait_keyword_success("click_element", self.locator.promotion)
        BUTTON.click_hyperlink_in_popup("0")
        BUTTON.click_button("Apply")
        BUTTON.click_button("Save As Draft")
