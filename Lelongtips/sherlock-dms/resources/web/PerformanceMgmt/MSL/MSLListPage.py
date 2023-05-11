""" Python file related to vs score card UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON, TEXTFIELD

class MSLListPage(PageObject):
    """ Functions related to vs score card list page """
    PAGE_TITLE = "Performance Management / Must Sell List"
    PAGE_URL = "/performance/msl"
    MSL_DETAILS = "${msl_details}"
    _locators = {
        "first_row_hyperlink": "//tr[1]//td[2]//core-cell-render//div//a"
    }

    def user_retrieved_all_msl(self):
        """ Functions to ensure there is at least one record shown in listing page """
        self.user_verify_record_shown()
        is_record_shown = BuiltIn().get_variable_value("${is_record_shown}")
        assert is_record_shown is True, "No record shown in listing page"

    def user_verify_record_shown(self):
        """ Functions to verify if record shown in the listing page """
        try:
            self.selib.wait_until_element_is_enabled(self.locator.first_row_hyperlink)
            is_record_shown = True
        except Exception as e:
            print(e.__class__, "occured")
            is_record_shown = False

        BuiltIn().set_test_variable("${is_record_shown}", is_record_shown)

    @keyword('user validate created MSL is listed in the table and select to ${action}')
    def user_perform_on_MSL(self, action):
        details = BuiltIn().get_variable_value(self.MSL_DETAILS)
        if details:
            desc = details['desc']
        else:
            desc = BuiltIn().get_variable_value("${msl_desc}")
        col_list = ["MSL_DESC"]
        data_list = [desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
        ("present", "MSL", action, col_list, data_list)

    @keyword('user searches created MSL in listing page')
    def user_search_created_msl(self):
        details = BuiltIn().get_variable_value(self.MSL_DETAILS)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Description", details['desc'])


    @keyword('user filters created MSL in listing page')
    def user_filters_created_msl(self):
        details = BuiltIn().get_variable_value(self.MSL_DETAILS)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Description", details['desc'])
        BUTTON.click_button("Apply")

    @keyword('user validates all managing buttons present and visible')
    def user_validates_all_managing_buttons_present(self):
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("delete")

    @keyword('user validates all managing buttons absent and hidden')
    def user_validates_all_managing_buttons_absent(self):
        BUTTON.validate_button_is_hidden("Add")
        BUTTON.validate_icon_is_hidden("delete")
