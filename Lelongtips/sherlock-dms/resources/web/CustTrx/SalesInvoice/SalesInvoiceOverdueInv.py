from PageObjectLibrary import PageObject
from resources.web.CustTrx.SalesInvoice import SalesInvoiceAddPage, SalesInvoiceListPage
from resources.web.CustTrx.SalesOrder import CreditLimit
from resources.web.Common import AlertCheck, MenuNav
from resources.web import PAGINATION, TAB, BUTTON, RADIOBTN
from robot.api.deco import keyword


class SalesInvoiceOverdueInv(PageObject):
    PAGE_TITLE = "Customer Transaction / Sales Invoice"
    PAGE_URL = "customer-transactions-ui/invoice/NEW"

    _locators = {
        "ConfirmDialog" : "//*[contains(text(),'This customer has over due invoice. Do you want to proceed?')]"
    }

    @keyword('user validates created distributor is in the table and select to ${cond}')
    def user_validate_dist_in_listing(self, cond):
        col_list = ["DIST_CD", "DIST_NAME"]
        d_code = "DistEgg"
        d_name = "Eggy Global Company"
        data_list = [d_code, d_name]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "distributor", cond, col_list,
                                                                   data_list)

    @keyword('Verified warning prompt appear when select cust ${cx} and route ${route}')
    def verify_warning_from_overdue_inv(self, route, cx):
        SalesInvoiceListPage.SalesInvoiceListPage().click_add_invoice_button()
        self.select_cust_and_route(route, cx)
        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec",
                                                 "page_should_contain_element",
                                                 self.locator.ConfirmDialog)

    def select_cust_and_route(self, cust, route):
        SalesInvoiceAddPage.SalesInvoiceAddPage().select_route_for_invoice(route)
        SalesInvoiceAddPage.SalesInvoiceAddPage().select_customer_for_invoice(cust)

    @keyword('Verified blocking prompt appear when select cust ${cx} and route ${route}')
    def verify_blocking_from_overdue_inv(self, route, cust):
        SalesInvoiceListPage.SalesInvoiceListPage().click_add_invoice_button()
        self.select_cust_and_route(route, cust)
        AlertCheck.AlertCheck().successfully_with_message("blocked", "This customer has over due invoice. Not allowed to perform Order.")

    @keyword('turned ${onoff} invoice overdue and set to ${BlockOrWarning} condition')
    def switch_dist_invoice_overdue_setup(self, onoff, cond):
        TAB.user_navigates_to_tab("Option")
        RADIOBTN.select_from_radio_button("Overdue Invoice Checking", cond)
        BUTTON.click_button("Save")
        self.switch_cust_invoice_overdue_setup(onoff)
        self.selib.reload_page()

    def switch_cust_invoice_overdue_setup(self, onoff):
        self.selib.reload_page()
        MenuNav.MenuNav().user_navigates_to_menu("Master Data Management | Customer")
        CreditLimit.CreditLimit().user_validate_data_in_cx_listing("edit")
        TAB.user_navigates_to_tab("Customer Option")
        if onoff == 'on':
            onoff = 'Yes'
        else:
            onoff = 'No'
        RADIOBTN.select_from_radio_button("Over Due Checking", onoff)





