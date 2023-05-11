from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, PAGINATION
from robot.libraries.BuiltIn import BuiltIn
wu = "Weight Code"

class WeightUnitListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / Weight Unit"
    PAGE_URL = "objects/weight-unit"
    WEIGHT_DETAILS = "${weight_details}"
    WEIGHT_CD = "${weight_cd}"
    WEIGHT_DESC = "${weight_desc}"
    CONV_FACTOR_KG = "${conv_factor_kg}"
    _locators = {
    }

    @keyword('created Weight Unit is verified successfully and selects to ${action}')
    def user_selects_weight_unit_to(self, action):
        details = self.builtin.get_variable_value(self.WEIGHT_DETAILS)
        if details is None:
            weight_cd = BuiltIn().get_variable_value(self.WEIGHT_CD)
            weight_desc = BuiltIn().get_variable_value(self.WEIGHT_DESC)
        else:
            weight_cd = details['weight_cd']
            weight_desc = details['weight_desc']
        col_list = ["WEIGHT_CD", "WEIGHT_DESC"]
        data_list = [weight_cd, weight_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", wu, action, col_list,
                                                                   data_list)

    @keyword('user searches created Weight Unit')
    def user_searches_weight_unit(self):
        weight_cd = BuiltIn().get_variable_value(self.WEIGHT_CD)
        weight_desc = BuiltIn().get_variable_value(self.WEIGHT_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field(wu, weight_cd)
        TEXTFIELD.insert_into_search_field("Weight Description", weight_desc)


    @keyword('user filters created Weight Unit')
    def user_filters_weight_unit(self):
        weight_cd = BuiltIn().get_variable_value(self.WEIGHT_CD)
        weight_desc = BuiltIn().get_variable_value(self.WEIGHT_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field(wu, weight_cd)
        TEXTFIELD.insert_into_filter_field("Weight Description", weight_desc)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching Weight Unit in listing"
