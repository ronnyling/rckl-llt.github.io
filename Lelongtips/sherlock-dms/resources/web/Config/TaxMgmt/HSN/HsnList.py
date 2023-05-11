from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.web import PAGINATION, BUTTON


class HsnList(PageObject):
    PAGE_TITLE = "Configuration / Tax Management / HSN"
    PAGE_URL = "/taxation-ui/hsn-master"

    _locators = {

    }

    def user_click_hsn_add_button(self):
        BUTTON.click_button("Add")

    @keyword('user validates created hsn is in the table and select to ${cond}')
    def user_validate_data_in_hsn(self, cond):
        col_list = ["HSN_CODE", "HSN_DESCRIPTION"]
        hsn_code = BuiltIn().get_variable_value("${hsn_code}")
        hsn = BuiltIn().get_variable_value("${hsn_desc}")
        data_list = [hsn_code, hsn]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Price Group", cond, col_list, data_list)