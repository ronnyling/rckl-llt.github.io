from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON,TEXTFIELD,PAGINATION
from robot.libraries.BuiltIn import BuiltIn

class ServiceMasterListPage(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / Service Master"
    PAGE_URL = "/sac-master"
    SVC_DETAILS = "${svc_details}"
    SVC_CODE = "${svc_code}"
    SVC_DESC = "${svc_desc}"
    _locators = {
    }

    @keyword('user selects service master to ${action}')
    def user_selects_svc_definition_to(self, action):
        details = self.builtin.get_variable_value(self.SVC_DETAILS)
        if details is None:
            svc_code = BuiltIn().get_variable_value(self.SVC_CODE)
            svc_desc = BuiltIn().get_variable_value(self.SVC_DESC)
        else:
            svc_code = details['svc_code']
            svc_desc = details['svc_desc']
        col_list = ["SVC_CD", "SAC_DESC"]
        data_list = [svc_code, svc_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Service Master", action, col_list, data_list)


    @keyword('user searches created service master')
    def user_searches_svc_group(self):
        svc_code = BuiltIn().get_variable_value(self.SVC_CODE)
        svc_desc = BuiltIn().get_variable_value(self.SVC_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Service Code", svc_code)
        TEXTFIELD.insert_into_search_field("Service Description", svc_desc)

    @keyword('user filters created service master')
    def user_filters_svc_group(self):
        svc_code = BuiltIn().get_variable_value(self.SVC_CODE)
        svc_desc = BuiltIn().get_variable_value(self.SVC_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Service Code", svc_code)
        TEXTFIELD.insert_into_filter_field("Service Description", svc_desc)
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No matching service master in listing"