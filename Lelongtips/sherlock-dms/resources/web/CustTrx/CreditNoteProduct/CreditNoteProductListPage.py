from PageObjectLibrary import PageObject
from resources.restAPI.Config.DistConfig import DistConfigPost
from resources.web import PAGINATION, BUTTON, DRPSINGLE
from robot.api.deco import keyword
from resources.web.Common import Logout, LoginPage, MenuNav
from robot.libraries.BuiltIn import BuiltIn


class CreditNoteProductListPage(PageObject):
    """ Functions in Credit Note Product listing page """
    PAGE_TITLE = "Customer Transaction / Credit Note (Product)"
    PAGE_URL = "customer-transactions-ui/creditnote-product-listing"
    principal = "${principal}"
    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "ADD": "//core-button[@ng-reflect-label='Add']",
        "PrincipalCol": "//th//child::*[text()='Principal']"
    }

    def click_add_credit_note_button(self):
        """ Function to add new credit note """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects credit note to ${action}')
    def user_selects_credit_note_to(self, action):
        """ Function to select warehouse to edit/delete """
        self.builtin.get_variable_value("${cn_cust_cd}")
        cn_cust_name = self.builtin.get_variable_value("${cn_cust_name}")
        cn_route_cd = self.builtin.get_variable_value("${cn_route_cd}")
        cn_route_name = self.builtin.get_variable_value("${cn_route_name}")
        col_list = ["CUST_NAME", "ROUTE_CD", "ROUTE_NAME"]
        data_list = [cn_cust_name, cn_route_cd, cn_route_name]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Credit Note", action, col_list, data_list)

    @keyword("user filters credit note with ${data_type} data")
    def click_filters_credit_note_with_data(self, data_type):
        """ Function to filter credit note product with fixed/random data """
        details = BuiltIn().get_variable_value("${FilterDetails}")
        BUTTON.click_icon("filter")
        self.select_principal_from_filter(details)
        element = self.driver.find_element_by_xpath("//core-button//child::*[contains(text(),'Apply')]//ancestor::core-button[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        BUTTON.click_button("Apply")

    def select_principal_from_filter(self, details):
        multi_status = BuiltIn().get_variable_value("${multi_status}")
        if multi_status is True:
            if details.get('principal') is not None:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", details['principal'])
            else:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", "random")
            self.builtin.set_test_variable(self.principal, principal)

    @keyword('principal listed successfully with ${action} data')
    def principal_listed_successfully_with_data(self, action):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        principal = self.builtin.get_variable_value(self.principal)
        if principal:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='PRIME_FLAG']".format(i))
                self.builtin.should_be_equal(get_principal, principal)

    @keyword('user searches credit note with ${action} data')
    def user_searches_credit_note(self, action):
        """ Function to search credit note with inline search """
        BUTTON.click_icon("search")
        if "Prime" in action:
            principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", action)
        else:
            principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", "random")
        self.builtin.set_test_variable(self.principal, principal)
        BUTTON.click_icon("search")

    @keyword('principal column ${action} in credit note listing')
    def principal_column_in_credit_note_listing(self, action):
        """ Function to check if principal column is showing in credit note listing"""
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if action == 'not visible':
            """If 'Not Visible' is passed in & Principal Column is showing,
                verify if non-prime credit notes are in listing"""
            try:
                self.selib.page_should_not_contain_element(self.locator.PrincipalCol)
                column_shown = False
            except Exception as e:
                e.args = ("Column shown is true", *e.args)
                column_shown = True
            if column_shown:
                try:
                    self.user_searches_credit_note("Non-Prime")
                    rows = PAGINATION.return_number_of_rows_in_a_page()
                    print(rows)
                    assert rows != 0, "Non-prime listings are not available"
                except Exception as e:
                    e.args = ("Non prime not found", *e.args)
                    assert False

        else:
            self.selib.page_should_contain_element(self.locator.PrincipalCol)

    def user_verify_credit_note_defaults_to_prime(self):
        """Verifies first that principal column is hidden when multi principal off,
            then turning on MultiPrincipal to check if credit note default to Prime"""
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        try:
            self.selib.page_should_not_contain_element(self.locator.PrincipalCol)
            column_shown = False
        except Exception as e:
            e.args = ("Column shown is false", *e.args)
            column_shown = True
        if not column_shown:
            user_role = self.builtin.get_variable_value("$user_role")
            self.builtin.set_test_variable(self.principal, "Prime")
            DistConfigPost.DistConfigPost().user_switches_multi_principal("On")
            Logout.Logout().user_logouts_and_closes_browser()
            LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)
            MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | Credit Note")
            self.principal_listed_successfully_with_data("Prime")