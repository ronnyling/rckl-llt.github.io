from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION


class PosmRequestListPage(PageObject):

    PAGE_TITLE = "Merchandising / POSM Management / POSM Request"
    PAGE_URL = "/merchandising/posm-request"
    PR_DETAILS = "${pr_details}"

    @keyword('user validates buttons on posm request listing page')
    def user_validates_buttons_on_listing_page(self):
        BUTTON.validate_button_is_shown("Add New Request")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects posm request to ${action}')
    def user_selects_posm_request_to(self, action):
        request_no = BuiltIn().get_variable_value("${request_no}")
        print("Request No = ", request_no)
        col_list = ["TXN_NO"]
        data_list = [request_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "POSM Request", action, col_list, data_list)







