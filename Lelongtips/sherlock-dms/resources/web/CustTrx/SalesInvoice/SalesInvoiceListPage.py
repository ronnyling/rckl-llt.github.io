from PageObjectLibrary import PageObject
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.Config.DistConfig import DistConfigPost
from resources.web import PAGINATION, BUTTON, DRPSINGLE, COMMON_KEY, POPUPMSG, TEXTFIELD
from robot.api.deco import keyword

from resources.web.Common import Logout, LoginPage, MenuNav


class SalesInvoiceListPage(PageObject):
    """ Functions in Sales Invoice listing page """
    PAGE_TITLE = "Customer Transaction / Sales Invoice"
    PAGE_URL = "customer-transactions-ui/invoice"
    INV_NAME = "Sales Invoice"
    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "ADD": "//core-button[@ng-reflect-label='ADD']",
        "PrincipalCol": "//th//child::*[text()='Principal']",

        ## listing page: list section
        "Title": "//div[@class='ant-card-head-title ng-star-inserted']",
        "Add": "//span[contains(text(),'Add')]/parent::button[1]",
        "Search": "(//button[@class='ant-btn ng-star-inserted ant-btn-icon-only'])[2]",
        "InvoiceNoSearchBox": "(//*[text()='SalesInvoice Listing']/following::*//core-textfield[@ng-reflect-name='INV_NO']//input[@type='text'])",
        "DeallocateInvoice": "//span[contains(text(),'Deallocate Invoice')]/parent::button[1]",
        "LoadingImg": "//div[@class='loading-text']//img",
        "ConfirmInvoice": "//span[contains(text(),'Confirm Invoice')]/parent::button[1]"
    }

    timeout = "0.2 min"
    wait = "3 sec"

    def click_add_invoice_button(self):
        """ Function to add new invoice """

        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element", self.locator.ADD)
        self._wait_for_page_refresh()

    @keyword('user selects invoice to ${action}')
    def user_selects_invoice_to(self, action):
        """ Function to select invoice to edit/delete """
        principal = self.builtin.get_variable_value("${principal}")
        res_bd_so_no = self.builtin.get_variable_value("${res_bd_so_no}")
        if isinstance(principal, list):
            principal = principal[0]
        principal = principal.capitalize()
        if res_bd_so_no is None:
            res_bd_so_no = ""
        cust_name = self.builtin.get_variable_value("${cust_name}")
        route_cd = self.builtin.get_variable_value("${route_cd}")
        if cust_name is None:
            cust_id = self.builtin.get_variable_value("${cust_id}")
            CustomerGet.CustomerGet().user_gets_cust_by_using_code(cust_id)
            cust_name = self.builtin.get_variable_value("${cust_name}")
        col_list = ["PRIME_FLAG", "SO_NO", "CUST_NAME", "ROUTE_CD"]
        if isinstance(res_bd_so_no, list):
            for i in res_bd_so_no:
                data_list = [principal, i, cust_name, route_cd]
                PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", self.INV_NAME, action, col_list, data_list)
        else:
            data_list = [principal, res_bd_so_no, cust_name, route_cd]
            PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", self.INV_NAME, action, col_list,
                                                                       data_list)

    @keyword("user filters invoice with ${data_type} data")
    def click_filters_invoice_with_data(self, data_type):
        """ Function to filter invoice with given/random data """
        details = self.builtin.get_variable_value("&{FilterDetails}")
        BUTTON.click_icon("filter")
        if data_type == 'Sampling' or data_type == 'Selling':
            DRPSINGLE.selects_from_single_selection_dropdown("Type", data_type)
        else :
            self.select_principal_from_filter(details)
            if details.get('status'):
                DRPSINGLE.selects_from_single_selection_dropdown("Status", details['status'])
            if details.get('customer_code'):
                DRPSINGLE.selects_from_single_selection_dropdown("Customer Code", details['customer_code'])
            if details.get('route_code'):
                DRPSINGLE.selects_from_single_selection_dropdown("Route Code", details['route_code'])
        BUTTON.click_button("Apply")

    @keyword('invoice principal listed successfully with ${action} data')
    def principal_listed_successfully_with_data(self, action):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        principal = self.builtin.get_variable_value(COMMON_KEY.PRINCIPAL)
        if principal:
            inv_list = []
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='PRIME_FLAG']".format(i))
                self.builtin.should_be_equal(get_principal, principal)
                get_inv = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='INV_NO']".format(i))
                inv_list.append(get_inv)
                self.builtin.set_test_variable("${inv_list}", inv_list)

    def select_principal_from_filter(self, details):
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            if details.get('principal') is not None:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", details['principal'])
            else:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", "random")
            self.builtin.set_test_variable(COMMON_KEY.PRINCIPAL, principal)

    @keyword('user searches invoice with ${action} data')
    def user_searches_invoice(self, action):
        """ Function to search invoice with inline search """
        BUTTON.click_icon("search")
        if "Sampling" or "Selling" in action:
            DRPSINGLE.selects_from_search_dropdown_selection("INVOICE_TXNTYPE", action)
        else :
            if "Prime" in action:
                principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", action)
            else:
                principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", "random")
                self.builtin.set_test_variable(COMMON_KEY.PRINCIPAL, principal)
        BUTTON.click_icon("search")

    @keyword('principal column ${action} in invoice listing')
    def principal_column_in_invoice_listing(self, action):
        """ Function to check if principal column is showing in invoice listing"""
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if action == 'not visible':
            """If 'Not Visible' is passed in & Principal Column is showing,
                    verify if non-prime credit notes are in listing"""
            try:
                self.selib.page_should_not_contain_element(self.locator.PrincipalCol)
                column_shown = False
            except Exception as e:
                print(e.__class__, "occured")
                column_shown = True
            if column_shown:
                try:
                    self.user_searches_invoice("Non-Prime")
                    rows = PAGINATION.return_number_of_rows_in_a_page()
                    print(rows)
                    assert rows != 0, "Non-prime listings are available"
                except Exception as e:
                    print(e.__class__, "occured")
                    assert False, "Issue in searching non-prime listings"
        else:
            self.selib.page_should_contain_element(self.locator.PrincipalCol)

    def user_verify_invoice_defaults_to_prime(self):
        """Verifies first that principal column is hidden when multi principal off,
            then turning on MultiPrincipal to check if invoice default to Prime"""
        try:
            self.selib.page_should_not_contain_element(self.locator.PrincipalCol)
            column_shown = False
        except Exception as e:
            print(e.__class__, "occured")
            column_shown = True
        if not column_shown:
            user_role = self.builtin.get_variable_value("$user_role")
            self.builtin.set_test_variable(COMMON_KEY.PRINCIPAL, "Prime")
            DistConfigPost.DistConfigPost().user_switches_multi_principal("On")
            Logout.Logout().user_logouts_and_closes_browser()
            LoginPage.LoginPage().user_open_browser_and_logins_using_user_role(user_role)
            MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | SalesInvoice")
            self.principal_listed_successfully_with_data("Prime")

    def user_search_with_invoice_number(self, inv_no):
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "input_text",
                                                 self.locator.InvoiceNoSearchBox, inv_no)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 "//a[contains(text(),'" + inv_no + "')]")
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")

    def user_confirm_selected_invoice(self):
        BUTTON.click_button('Confirm Invoice')
        POPUPMSG.validate_pop_up_msg("Are you sure to confirm the invoice?")
        BUTTON.click_button("Yes")

    def user_deallocate_selected_invoice(self):
        BUTTON.click_button('Deallocate Invoice')
        POPUPMSG.validate_pop_up_msg("Are you sure to deallocate the invoice?")
        BUTTON.click_button("Yes")

    def user_validates_status_updated_to_Invoiced(self):
        res_bd_so_no = self.builtin.get_variable_value("${res_bd_so_no}")
        trial = 0
        while trial < 300:
                trial = trial + 1
                if isinstance(res_bd_so_no, list):
                    for i in res_bd_so_no:
                        status = self.validate_invoice_status_at_listing(i, trial)
                        if status is True:
                            break
                else:
                    status = self.validate_invoice_status_at_listing(res_bd_so_no, trial)
                    if status is True:
                        break

    def validate_invoice_status_at_listing(self, data, trial):
        col_list = ["SO_NO", "INV_STATUS"]
        data_list = [data, "Invoiced"]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", self.INV_NAME, 'verify',
                                                                   col_list, data_list)
        actual_data = self.builtin.get_variable_value('${actual_data}')
        if actual_data[1] == "Invoiced":
            return True
        if trial == 299:
            assert actual_data[1] == "Invoiced", "Invoice not updated to Invoiced status"
        return False

    @keyword('validate type column is ${condition}')
    def validate_type_column_is_condition(self,condition):
        PAGINATION.validates_table_column_visibility("Type",condition)

    @keyword('validate ${inv_type} invoice listed successfully')
    def validate_matching_invoice_listed_successfully(self, inv_type):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        assert num_row >= 1, "Matching invoice not displayed"

    @keyword('user filter listing page with customer name')
    def user_filter_invoice_listing_with_cust_name(self):
        details = self.builtin.get_variable_value("&{discountDetails}")
        self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("CUST_NAME", details['CUST_NAME'])
