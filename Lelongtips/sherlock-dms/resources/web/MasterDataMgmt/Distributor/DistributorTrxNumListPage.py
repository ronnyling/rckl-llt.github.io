from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON
from robot.api.deco import keyword


class DistributorTrxNumListPage(PageObject):
    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"

    _locators = {
    }

    def click_add_distributor_transaction_number_button(self):
        """ Function to add new distributor transaction number """
        BUTTON.click_tab("Distributor Transaction Number")
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user validates buttons for distributor transaction number listing page')
    def user_validates_buttons(self):
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects distributor transaction number to ${action}')
    def user_selects_distributor_transaction_number(self, action):
        """ Function to select distributor transaction number to edit/delete """
        tran_type = BuiltIn().get_variable_value("${tran_type}")
        col_list = ["TXN_TYPE"]
        data_list = [tran_type]

        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "Distributor Transaction Number", action, col_list, data_list)

