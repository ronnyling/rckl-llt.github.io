from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, PAGINATION
from robot.libraries.BuiltIn import BuiltIn

class TaxDefinitionListPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Tax Definition"
    PAGE_URL = "/tax-group"
    TAX_DETAILS = "${tax_details}"
    TAX_CODE = "${tax_code}"
    TAX_DESC = "${tax_desc}"
    _locators = {
    }

    @keyword('user selects tax definition to ${action}')
    def user_selects_tax_definition_to(self, action):
        details = self.builtin.get_variable_value(self.TAX_DETAILS)
        if details is None:
            tax_code = BuiltIn().get_variable_value(self.TAX_CODE)
            tax_desc = BuiltIn().get_variable_value(self.TAX_DESC)
        else:
            tax_code = details['tax_code']
            tax_desc = details['tax_desc']
        col_list = ["TAX_CD", "TAX_COM_DESC"]
        data_list = [tax_code, tax_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Tax Definition", action, col_list, data_list)


    @keyword('user searches created tax definition')
    def user_searches_tax_definition(self):
        tax_code = BuiltIn().get_variable_value(self.TAX_CODE)
        tax_desc = BuiltIn().get_variable_value(self.TAX_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Tax Code", tax_code)
        TEXTFIELD.insert_into_search_field("Tax Component Description", tax_desc)

    @keyword('user filters created tax definition')
    def user_filters_tax_definition(self):
        tax_code = BuiltIn().get_variable_value(self.TAX_CODE)
        tax_desc = BuiltIn().get_variable_value(self.TAX_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Tax Code", tax_code)
        TEXTFIELD.insert_into_filter_field("Tax Component Description", tax_desc)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching tax definition in listing"