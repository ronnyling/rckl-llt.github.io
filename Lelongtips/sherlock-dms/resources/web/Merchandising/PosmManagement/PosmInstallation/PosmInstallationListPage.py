from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION


class PosmInstallationListPage(PageObject):

    PAGE_TITLE = "Merchandising / POSM Management / POSM Installation"
    PAGE_URL = "/merchandising/posm-direct-installation"

    @keyword('user validates buttons on posm installation listing page for ${login}')
    def user_validates_buttons_on_listing_page(self, login):
        if login == "distributor":
            BUTTON.validate_button_is_shown("Direct Installation")
            BUTTON.validate_button_is_shown("Process Installation")
            BUTTON.validate_button_is_shown("Reject")
        elif login == "hq admin":
            BUTTON.validate_button_is_hidden("Direct Installation")
            BUTTON.validate_button_is_hidden("Process Installation")
            BUTTON.validate_button_is_hidden("Reject")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects posm installation to ${action}')
    def user_selects_posm_installation_to(self, action):
        installation_no = BuiltIn().get_variable_value("${installation_no}")
        col_list = ["TXN_NO"]
        data_list = [installation_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "POSM Installation", action, col_list, data_list)

    def user_selects_posm_installation_by_request_no(self, req_no):
        col_list = ["REQ_NO"]
        data_list = [req_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "POSM Installation", "check", col_list,
                                                                   data_list)





