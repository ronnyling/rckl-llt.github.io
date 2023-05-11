from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON, TEXTFIELD, DRPSINGLE

class FacingSetupListPage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising Setup / Facing Setup"
    PAGE_URL = "/merchandising/merc-prod-group?template=p"
    SETUP_DETAILS = "${setup_details}"

    _locators = {
    }

    @keyword('user validate created facing setup is listed in the table and select to ${action}')
    def user_perform_on_facing_setup(self, action):
        setup = BuiltIn().get_variable_value(self.SETUP_DETAILS)
        if setup:
            code = setup['brand_code']
            category = setup['category']
        else:
            code = BuiltIn().get_variable_value("${setup_code}")
            category = BuiltIn().get_variable_value("${setup_category}")
        col_list = ["BRAND_CD","PRDCAT_VALUE_ID"]
        data_list = [code, category]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
        ("present", "Facing Setup", action, col_list, data_list)

    @keyword('user validates all managing buttons present and visible')
    def user_validates_all_managing_buttons_present(self):
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("delete")

    @keyword('user validates all managing buttons absent and hidden')
    def user_validates_all_managing_buttons_absent(self):
        BUTTON.validate_button_is_hidden("Add")
        BUTTON.validate_icon_is_hidden("delete")

    @keyword('user filters data using filter')
    def user_filters_created_facing_setup(self):
        setup = BuiltIn().get_variable_value(self.SETUP_DETAILS)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Brand Code", setup['brand_code'])
        DRPSINGLE.selects_from_single_selection_dropdown("Category", setup['category'])
        TEXTFIELD.insert_into_filter_field("Brand Description", setup['brand_desc'])
        DRPSINGLE.selects_from_single_selection_dropdown("Type", setup['type'])
        BUTTON.click_button("Apply")



