from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON, TEXTFIELD

class UserGroupListPage(PageObject):
    PAGE_TITLE = "User Management / User Group"
    PAGE_URL = "/setting-ui/user-group?template=p"
    GROUP_DETAILS = "${group_details}"

    _locators = {

    }
    @keyword('user performs ${action} on user group')
    def user_performs_on_user_group(self, action):
        setup = BuiltIn().get_variable_value(self.GROUP_DETAILS)
        if setup is not None :
            setup_code = setup['code']
        else:
            setup_code = BuiltIn().get_variable_value("${group_code}")
        col_list = ["GROUP_CD"]
        data_list = [setup_code]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
        ("present", "User Group", action, col_list, data_list)

    @keyword('user searches created user group in listing page by ${type}')
    def user_search_created_user_group(self,type):
        setup = BuiltIn().get_variable_value(self.GROUP_DETAILS)
        BUTTON.click_icon("search")
        if type == "code":
            TEXTFIELD.insert_into_search_field("User Group Code",setup['code'])
        elif type=="name":
            TEXTFIELD.insert_into_search_field("User Group Name", setup['name'])

    @keyword('user filters created user group in listing page by ${type}')
    def user_filters_created_user_group(self,type):
        setup = BuiltIn().get_variable_value(self.GROUP_DETAILS)
        BUTTON.click_icon("filter")
        if type=="code":
            TEXTFIELD.insert_into_filter_field("User Group Code", setup['code'])
        elif type=="description":
            TEXTFIELD.insert_into_filter_field("User Group Name", setup['name'])
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No user group in listing"

    def validate_delete_button_is_not_visible(self):
        BUTTON.validate_icon_is_hidden("delete")
