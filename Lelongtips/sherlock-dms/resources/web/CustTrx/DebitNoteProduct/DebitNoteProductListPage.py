""" Python file related to debit note product UI """
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Config.DistConfig import DistConfigPost
from resources.web import BUTTON, PAGINATION, DRPSINGLE
from resources.web.Common import Logout, LoginPage, MenuNav


class DebitNoteProductListPage(PageObject):
    """ Functions in debit note product listing page """
    PAGE_TITLE = "Customer Transaction / Debit Note (Product)"
    PAGE_URL = "customer-transactions-ui/debit-note"

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "ADD": "//core-button[@ng-reflect-label='Add']",
        "PrincipalCol": "//th//child::*[text()='Principal']"
    }

    def click_add_debit_note_button(self):
        """ Function to add new debit note """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects debit note product to ${action}')
    def user_selects_debit_note_product_to(self, action):
        """ Function to select warehouse to edit/delete """
        dn_route_cd = self.builtin.get_variable_value("${dn_route_cd}")
        col_list = ["ROUTE_ID"]
        data_list = [dn_route_cd]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Debit Note", action, col_list, data_list)

    @keyword("user filters debit note using ${data_type} data")
    def click_filters_debit_note_using_data(self, data_type):
        """ Function to filter debit note product using fixed/random data """
        details = BuiltIn().get_variable_value("${FilterDetails}")
        BUTTON.click_icon("filter")
        DRPSINGLE.select_principal_from_filter(details)
        element = self.driver.find_element_by_xpath(
            "//core-button//child::*[contains(text(),'Apply')]//ancestor::core-button[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        BUTTON.click_button("Apply")

    @keyword('user searches debit note using ${action} data')
    def user_searches_debit_note_using_data(self, action):
        """ Function to search debit note with inline search """
        BUTTON.click_icon("search")
        if "Prime" in action:
            principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", action)
        else:
            principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", "random")
        self.builtin.set_test_variable("${principal}", principal)
        BUTTON.click_icon("search")

    @keyword('principal column ${action} in debit note ${type} listing')
    def principal_column_in_debit_note_listing(self, action, type):
        """ Function to check if principal column is showing in debit note product/non-product listing
        If 'Not Visible' is passed in & Principal Column is showing,
        verify if non-prime debit notes are in listing """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if action == 'not visible':
            try:
                self.selib.page_should_not_contain_element(self.locator.PrincipalCol)
                column_shown = False
            except Exception as e:
                print(e.__class__, "occured")
                column_shown = True
            if column_shown:
                try:
                    self.user_searches_debit_note("Non-Prime")
                    rows = PAGINATION.return_number_of_rows_in_a_page()
                    assert rows != 0, "Non-prime listings are not available"
                except Exception as e:
                    print(e.__class__, "occured")
                    assert False, "Non prime not found"
        else:
            self.selib.page_should_contain_element(self.locator.PrincipalCol)

    def user_verify_debit_note_product_default_to_prime(self):
        """ Verify first that principal column is hidden when multi principal off,
            then turning on MultiPrincipal to check if debit note product default to Prime"""

        try:
            self.selib.page_should_not_contain_element(self.locator.PrincipalCol)
            column_shown = False
        except Exception as e:
            print(e.__class__, "occured")
            column_shown = True
        if not column_shown:
            user_role = self.builtin.get_variable_value("$user_role")
            self.builtin.set_test_variable("${principal}", "Prime")
            DistConfigPost.DistConfigPost().user_switches_multi_principal("On")
            Logout.Logout().user_logouts_and_closes_browser()
            LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)
            MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | Debit Note Product")
            PAGINATION.principal_listed_successfully_with_data("Prime")
