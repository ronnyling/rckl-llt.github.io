from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD,PAGINATION
from robot.libraries.BuiltIn import BuiltIn

class KPITypeListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / KPI Type"
    PAGE_URL = "/objects/vs-kpi-type"
    KPI_DETAILS = "${kpi_details}"
    KPI_CODE = "${kpi_code}"
    KPI_DESC = "${kpi_desc}"
    _locators = {
    }

    @keyword('user selects KPI type to ${action}')
    def user_selects_kpi_type_to(self, action):
        details = self.builtin.get_variable_value(self.KPI_DETAILS)
        if details is None:
            type_code = BuiltIn().get_variable_value(self.KPI_CODE)
            type_desc = BuiltIn().get_variable_value(self.KPI_DESC)
        else:
            type_code = details['kpi_code']
            type_desc = details['kpi_desc']
        col_list = ["KPI_TYPE_CODE", "KPI_TYPE_DESC"]
        data_list = [type_code, type_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "KPI Type", action, col_list, data_list)

    @keyword('user searches created KPI type')
    def user_searches_kpi_type(self):
        type_code = BuiltIn().get_variable_value(self.KPI_CODE)
        type_desc = BuiltIn().get_variable_value(self.KPI_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("KPI Type Code", type_code)
        TEXTFIELD.insert_into_search_field("KPI Type Description", type_desc)

    @keyword('user filters created KPI type')
    def user_filters_kpi_type(self):
        type_code = BuiltIn().get_variable_value(self.KPI_CODE)
        type_desc = BuiltIn().get_variable_value(self.KPI_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("KPI Type Code", type_code)
        TEXTFIELD.insert_into_filter_field("KPI Type Description", type_desc)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching KPI type in listing"
