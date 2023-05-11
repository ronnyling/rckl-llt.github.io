from PageObjectLibrary import PageObject
from resources.web import BUTTON, DRPSINGLE, RADIOBTN, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.web.CustTrx.SalesReturn.SalesReturnAddPage import SalesReturnAddPage


class SalesReturnGetLatestInvoiceDetails(PageObject):
    """ Functions in Sales Return add page """
    PAGE_TITLE = "Customer Transaction / Sales Return"
    PAGE_URL = "customer-transactions-ui/return/NEW"
    RTN_DETAILS = "${return_details}"

    _locators = {
        "RtnList": "//*[contains(text(),'Sales Return Listing')]",
        "RouteDrp": "//label[text()='Route']//following::nz-select[1]",
        "customer": "//*[contains(text(),'Customer')]/following::*[1]//input",
        "WarehouseDrp": "//label[contains(text(),'Warehouse')]//following::nz-select",
        "ReasonDrp": "//label[text()='Reason']//following::nz-select[1]",
        "product_field": "//input[@placeholder='Enter Code / Description']",
        "load_image": "//div[@class='loading-text']//img",
        "orange_colour": '//tr[contains(@class, "orange")]',
        "selection": "//tr//*[text()='{0}']//following::core-dropdown//nz-select",
        "invoice_field": "//input[@placeholder='Invoice No.']"
    }

    @keyword("user retrieves latest invoice")
    def user_retrieves_latest_invoice(self):
        """invoice number created"""
        invoice_no = BuiltIn().get_variable_value("${res_bd_invoice_no}")

        BUTTON.click_button('Add')
        """select customer"""
        details = BuiltIn().get_variable_value("${return_details}")
        SalesReturnAddPage().user_selects_customer_for_return(details['CUST_NAME'])

        """select route"""
        DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.RouteDrp, details['ROUTE'])

        """set return type"""
        RADIOBTN.select_from_radio_button("Type", details['TYPE'])

        """select product"""
        COMMON_KEY.wait_keyword_success("click_element", self.locator.product_field)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.product_field, details['PRODUCT'])
        COMMON_KEY.wait_keyword_success("click_element", "//*[text()='%s']" % details['PRODUCT'])

        """check invoice"""
        get_invoice = self.selib.get_element_attribute(self.locator.invoice_field, "ng-reflect-model")
        print("Existing invoice: ", get_invoice)
        print("Existing invoice: ", invoice_no)
        self.builtin.should_be_equal(get_invoice, invoice_no)
