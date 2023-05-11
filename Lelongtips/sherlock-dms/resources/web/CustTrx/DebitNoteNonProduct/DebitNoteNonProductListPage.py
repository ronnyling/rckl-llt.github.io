""" Python file related to debit note non product UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Config.DistConfig import DistConfigPost
from resources.web import BUTTON, PAGINATION, DRPSINGLE
from resources.web.Common import Logout, LoginPage, MenuNav
from resources.Common import Common


class DebitNoteNonProductListPage(PageObject):
    """ Functions in debit note non product listing page """
    PAGE_TITLE = "Customer Transaction / Debit Note (Non Product)"
    PAGE_URL = "customer-transactions-ui/debitnote-nonprd"

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "ADD": "//core-button[@ng-reflect-label='Add']",
        "PrincipalCol": "//th//child::*[text()='Principal']"
    }

    def click_add_debit_note_button(self):
        """ Function to add new debit note """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects debit note non product to ${action}')
    def user_selects_debit_note_product_to(self, action):
        """ Function to select warehouse to edit/delete """
        dn_route_cd = self.builtin.get_variable_value("${dn_route_cd}")
        col_list = ["ROUTE_ID"]
        data_list = [dn_route_cd]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Debit Note", action, col_list, data_list)

    @keyword("user filters debit note using ${data_type} data")
    def click_filters_debit_note_using_data(self, data_type):
        """ Function to filter debit note non product using fixed/random data """
        details = BuiltIn().get_variable_value("${FilterDetails}")
        BUTTON.click_icon("filter")
        self.select_principal_from_filter(details)
        element = self.driver.find_element_by_xpath(
            "//core-button//child::*[contains(text(),'Apply')]//ancestor::core-button[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        BUTTON.click_button("Apply")

    def select_principal_from_filter(self, details):
        """ Function to select principal value from filter pop up """
        multi_status = BuiltIn().get_variable_value("${multi_status}")
        if multi_status is True:
            if details.get('principal') is not None:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", details['principal'])
            else:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", "random")
            self.builtin.set_test_variable(Common.PRINCIPAL, principal)

    @keyword('principal listed successfully with ${action} data')
    def principal_listed_successfully_with_data(self, action):
        """ Function to check if principal listed successfully """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        print("num_row", num_row)
        principal = self.builtin.get_variable_value(Common.PRINCIPAL)
        print("principal", principal)
        if principal:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='PRIME_FLAG']".format(i))
                print("get_principal", get_principal)
                self.builtin.should_be_equal(get_principal, principal)

    @keyword('user searches debit note using ${action} data')
    def user_searches_debit_note_using_data(self, action):
        """ Function to search debit note with inline search """
        BUTTON.click_icon("search")
        if "Prime" in action:
            principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", action)
        else:
            principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", "random")
        self.builtin.set_test_variable(Common.PRINCIPAL, principal)
        BUTTON.click_icon("search")

    def user_verify_debit_note_product_default_to_prime(self):
        """ Verify first that principal column is hidden when multi principal off,
            then turning on MultiPrincipal to check if debit note non product default to Prime"""

        try:
            self.selib.page_should_not_contain_element(self.locator.PrincipalCol)
            column_shown = False
        except Exception as e:
            print(e.__class__, "occured")
            column_shown = True
        if not column_shown:
            user_role = self.builtin.get_variable_value("$user_role")
            self.builtin.set_test_variable(Common.PRINCIPAL, "Prime")
            DistConfigPost.DistConfigPost().user_switches_multi_principal("On")
            Logout.Logout().user_logouts_and_closes_browser()
            LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)
            MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | Debit Note Product")
            self.principal_listed_successfully_with_data("Prime")
