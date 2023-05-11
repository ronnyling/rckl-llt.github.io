from PageObjectLibrary import PageObject
from resources.web.CompTrx.CompDebitNoteProduct.CompDebitNoteProductListPage import CompDebitNoteProductListPage
from resources.web.CompTrx.CompanyInvoice.CompInvoiceAddPage import CompInvoiceAddPage
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import TokenAccess
from resources.web import DRPSINGLE, BUTTON, CALENDAR, TEXTFIELD
from robot.api.deco import keyword
from resources.Common import Common
from resources.restAPI.MasterDataMgmt.Supplier.SupplierGet import SupplierGet


class CompDebitNoteProductAddPage(PageObject):
    """ Functions for Company debit note product Add Page actions """
    PRDS = []
    PROD = "${prod}"
    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "product": "//input[@placeholder='Enter Code/Name']"
    }


    @keyword("user creates company debit note product")
    def create_dn(self):
        dn_details = BuiltIn().get_variable_value("${DNDetails}")
        CompDebitNoteProductListPage().click_add_comp_dn_button()
        CompInvoiceAddPage().select_supplier_for_company_invoice(dn_details)
        self.select_dn_date(dn_details)
        self.user_inserts_cn_no(dn_details)
        self.select_reason_for_dn(dn_details)


    def user_inserts_cn_no(self, cn_details):
        """ Function to insert dn no code with random/fixed data """
        dn_details_given = self.builtin.get_variable_value("&{DNDetails['DnNo']}")
        if dn_details_given is not None:
            dn_no = TEXTFIELD.insert_into_field("Debit Note No.", cn_details['DnNo'])
        else:
            dn_no = TEXTFIELD.insert_into_field_with_length("Debit Note No.", "random", 15)
        return dn_no

    def select_dn_date(self, details):
        """ Function to select dn date in company debit note screen """
        dn_date_given = self.builtin.get_variable_value("${fixedData['DnDate']}")
        if dn_date_given is not None:
            dn_date = CALENDAR.select_date_from_calendar("Debit Note Date", details['CnDate'])
        else:
            dn_date = CALENDAR.select_date_from_calendar("Debit Note Date", "today")
        return dn_date

    def select_reason_for_dn(self, details):
        """ Function to select reason in company debit note product screen """
        if details is None:
            reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", "random")
        else:
            if details.get("Reason") is not None:
                reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", details['Reason'])
            else:
                reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", "random")
        return reason

    @keyword("user intends to insert product '${prod}' with uom '${prod_uom}', Qty '${qty}'")
    def user_intend_to_insert_product_details(self, prod, prod_uom, qty):
        Common().wait_keyword_success("input_text", self.locator.product, prod)
        Common().wait_keyword_success("click_element", "//*[text()='%s']" % prod)
        Common().wait_keyword_success("click_element", "//tr//label[text()='{0} ']/following::*/nz-select[1]".format(prod))
        Common().wait_keyword_success("click_element",
                                      "//*[@class='cdk-overlay-pane']//following-sibling::li[contains(text(),'{0}')]".format(prod_uom))
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0} ']/following::input[2]".format(prod), qty)
        BuiltIn().set_test_variable(self.PROD, prod)
        CompInvoiceAddPage().create_prd_payload(prod_uom, qty, prod)

    def click_save_comp_dn_button(self):
        """ Function to save company debit note """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()



