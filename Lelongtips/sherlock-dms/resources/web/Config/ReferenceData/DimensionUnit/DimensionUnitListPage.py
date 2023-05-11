from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, PAGINATION
from robot.libraries.BuiltIn import BuiltIn
du = "Dimension Unit"

class DimensionUnitListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Dimension Unit"
    PAGE_URL = "objects/dimension-unit"
    DIMENSION_DETAILS = "${dimension_details}"
    DIMENSION_UNIT = "${dimension_unit}"
    DIMENSION_DESC = "${dimension_desc}"
    CONVERSION_FACTOR = "${conversion_factor}"
    _locators = {
    }

    @keyword('created Dimension Unit is verified successfully and selects to ${action}')
    def user_selects_dimension_unit_to(self, action):
        details = self.builtin.get_variable_value(self.DIMENSION_DETAILS)
        if details is None:
            dimension_unit = BuiltIn().get_variable_value(self.DIMENSION_UNIT)
            dimension_desc = BuiltIn().get_variable_value(self.DIMENSION_DESC)
        else:
            dimension_unit = details['dimension_unit']
            dimension_desc = details['dimension_desc']
        col_list = ["DIMENSION_CD", "DIMENSION_DESC"]
        data_list = [dimension_unit, dimension_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", du, action, col_list,
                                                                   data_list)

    @keyword('user searches created Dimension Unit')
    def user_searches_dimension_unit(self):
        dimension_unit = BuiltIn().get_variable_value(self.DIMENSION_UNIT)
        dimension_desc = BuiltIn().get_variable_value(self.DIMENSION_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field(du, dimension_unit)
        TEXTFIELD.insert_into_search_field("Dimension Description", dimension_desc)


    @keyword('user filters created Dimension Unit')
    def user_filters_dimension_unit(self):
        dimension_unit = BuiltIn().get_variable_value(self.DIMENSION_UNIT)
        dimension_desc = BuiltIn().get_variable_value(self.DIMENSION_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field(du, dimension_unit)
        TEXTFIELD.insert_into_filter_field("Dimension Description", dimension_desc)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching Dimension Unit in listing"
