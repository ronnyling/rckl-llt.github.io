from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

from resources import Common
from resources.web import PAGINATION, BUTTON, TEXTFIELD

class UserListPage(PageObject):
    PAGE_TITLE = "User Management / User"
    PAGE_URL = "/setting-ui/user?template=p"
    USER_DETAILS = "${user_details}"

    _locators = {
        "login_search":"(//input[@placeholder='Enter'])[1]",
        "name_search":"(//input[@placeholder='Enter'])[2]"
    }
    @keyword('user performs ${action} on user')
    def user_performs_on_user_group(self, action):
        setup = BuiltIn().get_variable_value(self.USER_DETAILS)
        if setup is not None :
            setup_id = setup['login']
        else:
            setup_id = BuiltIn().get_variable_value("${user_login}")
        col_list = ["LOGIN_ID"]
        data_list = [setup_id]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
        ("present", "User", action, col_list, data_list)

    @keyword('user searches created user in listing page')
    def user_search_created_user(self):
        setup = BuiltIn().get_variable_value(self.USER_DETAILS)
        BUTTON.click_icon("search")
        Common().wait_keyword_success("input_text", self.locator.login_search, setup['login'])
        Common().wait_keyword_success("input_text", self.locator.name_search, setup['name'])
        #TEXTFIELD.insert_into_search_field("Login ID",setup['login'])
        #TEXTFIELD.insert_into_search_field("Name", setup['name'])

    @keyword('user filters created user in listing page')
    def user_filters_created_user(self):
        setup = BuiltIn().get_variable_value(self.USER_DETAILS)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Login ID", setup['login'])
        TEXTFIELD.insert_into_filter_field("Name", setup['name'])
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No user in listing"

