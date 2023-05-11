from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD,PAGINATION
from robot.libraries.BuiltIn import BuiltIn

class TaxStructureListPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Tax Structure"
    PAGE_URL = "/taxstructure"
    TAX_DETAILS = "${tax_details}"
    TAX_CODE = "${tax_code}"
    TAX_DESC = "${tax_desc}"
    _locators = {
    }

    @keyword('user selects tax structure to ${action}')
    def user_selects_tax_definition_to(self, action):
        details = self.builtin.get_variable_value(self.TAX_DETAILS)
        if details is None:
            tax_code = BuiltIn().get_variable_value(self.TAX_CODE)
        else:
            tax_code = details['tax_code']
        col_list = ["TAX_STRUCTURE_CD"]
        data_list = [tax_code]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Tax Structure", action, col_list, data_list)


    @keyword('user searches created tax structure')
    def user_searches_tax_structure(self):
        tax_code = BuiltIn().get_variable_value(self.TAX_CODE)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_filter_field("Tax Structure Code", tax_code)

    @keyword('user filters created tax structure')
    def user_filters_tax_structure(self):
        tax_code = BuiltIn().get_variable_value(self.TAX_CODE)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Tax Structure Code", tax_code)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching tax structure in listing"