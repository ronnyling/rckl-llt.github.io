from PageObjectLibrary import PageObject

from resources.restAPI.Common import TokenAccess
from resources.restAPI.Config.AppSetup import AppSetupGet, AppSetupPut
from resources.web import BUTTON, PAGINATION, DRPSINGLE, TEXTFIELD
from resources.web.CustTrx.SalesOrder import SalesOrderAddPage
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class SalesOrderListPage(PageObject):
    """ Functions in sales order listing page """
    PAGE_TITLE = "Customer Transaction / Sales Order"
    PAGE_URL = "/salesorderlisting"
    PRINCIPAL = "${principal}"

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "FirstOrder": "(//td)[2]//a"
    }

    def click_add_sales_order_button(self):
        """ Function to add new sales order """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects sales order to ${action}')
    def user_selects_sales_order_to(self, action):
        """ Function to select sales order to edit/view """
        details = self.builtin.get_variable_value("&{FilterDetails}")
        if details is None :
            so_cust = self.builtin.get_variable_value("${so_cust}")
            so_route = self.builtin.get_variable_value("${so_route}")
            del_date = self.builtin.get_variable_value("${del_date}")
            col_list = ["CUST_NAME", "ROUTE_CD", "DELIVERY_DT"]
            data_list = [so_cust, so_route, del_date]
        else :
            txn_no = details['txn_no']
            col_list = ["TXN_NO"]
            data_list = [txn_no]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Sales Order", 'view', col_list,
                                                                   data_list)

    def click_process_order_button(self):
        BUTTON.click_button("PROCESS ORDER")
        self._wait_for_page_refresh()

    @keyword("user process created sales order")
    def process_order(self):
        order_no = self.selib.get_text(self.locator.FirstOrder)
        BuiltIn().set_test_variable("${TXN_NO}",order_no)
        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec",
                                                 "click_element",
                                                 self.locator.FirstRecord)
        self.click_process_order_button()
        SalesOrderAddPage.SalesOrderAddPage().locator.YesBtn

    @keyword('validated processed sales order is in ${status} status')
    def user_validate_data_in_tax_group(self, status):
        self.selib.reload_page()
        col_list = ["TXN_NO", "STATUS"]
        so_num = BuiltIn().get_variable_value("${TXN_NO}")
        data_list = [so_num, status]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Sales Order", "verify", col_list, data_list)

    @keyword("user filters sales order with ${data_type} data")
    def click_filters_sales_order_with_data(self, data_type):
        """ Function to filter sales order with given/random data """
        details = self.builtin.get_variable_value("&{FilterDetails}")
        BUTTON.click_icon("filter")
        if data_type == 'Sampling' or data_type == 'Selling' :
            DRPSINGLE.selects_from_single_selection_dropdown("Type", data_type)
        else :
            self.select_principal_from_filter(details)
        BUTTON.click_button("Apply")

    @keyword('user searches sales order with ${action} data')
    def user_searches_sales_order(self, action):
        """ Function to search warehouse with inline search """
        BUTTON.click_icon("search")
        if "Sampling" or "Selling" in action:
            DRPSINGLE.selects_from_search_dropdown_selection("ORDER_TXNTYPE", action)
        else :
            multi_status = self.builtin.get_variable_value("${multi_status}")
            if multi_status is True:
                principal = DRPSINGLE.selects_from_search_dropdown_selection("PRIME_FLAG", "random")
                self.builtin.set_test_variable(self.locator.PRINCIPAL, principal)
        BUTTON.click_icon("search")

    @keyword('principal listed successfully with ${action} data')
    def principal_listed_successfully_with_data(self, action):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        principal = self.builtin.get_variable_value(self.locator.PRINCIPAL)
        if principal:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='PRIME_FLAG']".format(i))
                self.builtin.should_be_equal(get_principal, principal)

    def select_principal_from_filter(self, details):
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            if details.get('principal') is not None:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", details['principal'])
            else:
                principal = DRPSINGLE.selects_from_single_selection_dropdown("Principal", "random")
            self.builtin.set_test_variable(self.locator.PRINCIPAL, principal)

    @keyword('validate type column is ${condition}')
    def validate_type_column_is_condition(self, condition):
        PAGINATION.validates_table_column_visibility("Type", condition)

    @keyword('validate ${ord_type} order listed successfully')
    def validate_matching_order_listed_successfully(self, ord_type):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        assert num_row >= 1, "Matching order not displayed"

