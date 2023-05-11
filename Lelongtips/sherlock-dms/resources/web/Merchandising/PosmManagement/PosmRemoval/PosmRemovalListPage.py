from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION


class PosmRemovalListPage(PageObject):

    PAGE_TITLE = "Merchandising / POSM Management / POSM Removal"
    PAGE_URL = "/merchandising/direct-removal"

    @keyword('user validates buttons on posm removal listing page for ${login}')
    def user_validates_buttons_on_removal_listing_page(self, login):
        if login == "distributor":
            BUTTON.validate_button_is_shown("Direct Removal")
            BUTTON.validate_button_is_shown("Process Removal")
            BUTTON.validate_button_is_shown("Reject")
        elif login == "hq admin":
            BUTTON.validate_button_is_hidden("Direct Removal")
            BUTTON.validate_button_is_hidden("Process Removal")
            BUTTON.validate_button_is_hidden("Reject")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects posm removal to ${action}')
    def user_selects_posm_removal_to(self, action):
        removal_no = BuiltIn().get_variable_value("${removal_no}")
        col_list = ["TXN_NO"]
        data_list = [removal_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "POSM Removal", action, col_list, data_list)

    def user_selects_posm_removal_by_request_no(self, req_no):
        col_list = ["REQ_NO"]
        data_list = [req_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "POSM removal", "check", col_list,
                                                                   data_list)





