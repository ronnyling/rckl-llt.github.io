from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD,PAGINATION
from robot.libraries.BuiltIn import BuiltIn

class ClaimTypeListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Claim Type"
    PAGE_URL = "objects/claim-type"
    CLAIM_DETAILS = "${claim_details}"
    CLAIM_CODE = "${claim_code}"
    CLAIM_DESC = "${claim_desc}"
    _locators = {
    }

    @keyword('created claim type is verified successfully and selects to ${action}')
    def user_selects_claim_type_to(self, action):
        details = self.builtin.get_variable_value(self.CLAIM_DETAILS)
        if details is None:
            claim_code = BuiltIn().get_variable_value(self.CLAIM_CODE)
            claim_desc = BuiltIn().get_variable_value(self.CLAIM_DESC)
        else:
            claim_code = details['claim_code']
            claim_desc = details['claim_desc']
        col_list = ["CLAIM_TYPE_CD", "CLAIM_TYPE_DESC"]
        data_list = [claim_code, claim_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Claim Type", action, col_list, data_list)

    @keyword('user searches created claim type')
    def user_searches_claim_type(self):
        claim_code = BuiltIn().get_variable_value(self.CLAIM_CODE)
        claim_desc = BuiltIn().get_variable_value(self.CLAIM_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Claim Type Code", claim_code)
        TEXTFIELD.insert_into_search_field("Claim Type Description", claim_desc)

    @keyword('user filters created claim type')
    def user_filters_claim_type(self):
        claim_code = BuiltIn().get_variable_value(self.CLAIM_CODE)
        claim_desc = BuiltIn().get_variable_value(self.CLAIM_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Claim Type Code", claim_code)
        TEXTFIELD.insert_into_filter_field("Claim Type Description", claim_desc)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching claim type in listing"
