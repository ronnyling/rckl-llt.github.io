from PageObjectLibrary import PageObject
from resources.web.CompTrx.CompCreditNoteNonProduct.CompCreditNoteNonProductListPage import CompCreditNoteNonProductListPage
from resources.web.CompTrx.CompanyInvoice.CompInvoiceAddPage import CompInvoiceAddPage
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import TokenAccess
from resources.web import DRPSINGLE, BUTTON, CALENDAR, TEXTFIELD
from robot.api.deco import keyword
from resources.Common import Common
from resources.TransactionFormula import TransactionFormula
from resources.restAPI.MasterDataMgmt.Supplier.SupplierGet import SupplierGet


class CompCreditNoteNonProductAddPage(PageObject):
    """ Functions for Company credit note non product Add Page actions """
    SVCS = []
    _locators = {
        "ref_no" : "",
        "load_image": "//div[@class='loading-text']//img",
        "service": "//input[@placeholder='Enter Service Code / Name']"
    }
    SVC_INFO = "${service_info}"

    @keyword("user creates company credit note non product")
    def create_cnnp(self):
        cnnp_details = BuiltIn().get_variable_value("${CNNPDetails}")
        CompCreditNoteNonProductListPage().click_add_comp_cnnp_button()
        CompInvoiceAddPage().select_supplier_for_company_invoice(cnnp_details)
        self.select_cnnp_date(cnnp_details)
        self.user_inserts_cnnp_no(cnnp_details)
        self.select_reason_for_cnnp(cnnp_details)

    def user_inserts_cnnp_no(self, cnnp_details):
        """ Function to insert cnnp no code with random/fixed data """
        cnnp_details_given = self.builtin.get_variable_value("&{CNNPDetails['CnnpNo']}")
        if cnnp_details_given is not None:
            cnnp_no = TEXTFIELD.insert_into_field("Credit Note No.", cnnp_details['CnnpNo'])
        else:
            cnnp_no = TEXTFIELD.insert_into_field_with_length("Credit Note No.", "random", 15)
        return cnnp_no

    def select_cnnp_date(self, details):
        """ Function to select cnnp date in company credit note screen """
        cnnp_date_given = self.builtin.get_variable_value("${fixedData['CnnpDate']}")
        if cnnp_date_given is not None:
            cnnp_date = CALENDAR.select_date_from_calendar("Credit Note Date", details['CnnpDate'])
        else:
            cnnp_date = CALENDAR.select_date_from_calendar("Credit Note Date", "today")
        return cnnp_date

    def select_reason_for_cnnp(self, details):
        """ Function to select reason in company credit note non product screen """
        if details is None:
            reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", "random")
        else:
            if details.get("Reason") is not None:
                reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", details['Reason'])
            else:
                reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", "random")
        return reason

    @keyword("user intends to select service '${service}' and enter amount '${amount}'")
    def user_intend_to_select_service_and_enter_amount_details(self, service, amount):
        Common().wait_keyword_success("input_text", self.locator.service, service)
        Common().wait_keyword_success("click_element", "(//*[text()='%s'])[1]" % service)
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0}']/preceding::input[1]".format(service), "1")
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0}']/following::input[2]".format(service),
                                      amount)
        Common().wait_keyword_success("click_element", "(//*[text()='%s'])[1]" % service)
        self.create_svc_payload(service, amount)
        TransactionFormula().company_tax_calculation_for_non_product_service()

    def create_svc_payload(self, svc_cd, amt):
        svc_info = {
            "SVC_CD": svc_cd,
            "AMT": amt
        }
        self.SVCS.append(svc_info)
        BuiltIn().set_test_variable(self.SVC_INFO, self.SVCS)

    def click_save_comp_cnnp_button(self):
        """ Function to save credit note non product """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()

    def click_close_button(self):
        """ Function to create new claim """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_icon("close")
        self._wait_for_page_refresh()

    @keyword("user validate tax is calculated correctly")
    def validate_tax_amount(self):
        service_info = BuiltIn().get_variable_value(self.SVC_INFO)
        display_rounding = BuiltIn().get_variable_value("${display_rounding}")
        for service in service_info:
            Common().wait_keyword_success("click_element", "//tr//label[text()='{0}']/following::a[1]".format(service['SVC_CD']))
            total_tax = self.selib.get_text("//tr//label[text()='{0}']/following::a[1]".format(service['SVC_CD']))
            total_tax = total_tax.split(" ")
            count = 1
            for tax_amt in service['ALL_LEVEL_TAX']:
                tax = self.selib.get_text("//div[contains(text(),'Tax Summary')]/following::*//tr[{0}]//td[5]".format(count))
                tax_component = self.selib.get_text(
                    "//div[contains(text(),'Tax Summary')]/following::*//tr[{0}]//td[2]".format(count))
                assert tax_component == tax_amt['TAX_CD'], "Tax Component Incorrect"
                print(round(float(tax_amt['TAX_AMT']), display_rounding))
                print(float(tax))
                assert round(float(tax_amt['TAX_AMT']), display_rounding) == float(tax), "Tax Incorrect"
                count = count + 1
            tax_summ_total_tax = self.selib.get_text(
                "//div[contains(text(),'Grand Total')]/following::div[1]")
            tax_summ_total_tax = tax_summ_total_tax.split(" ")
        assert float(tax_summ_total_tax[1]) == round(float(service['TAX_AMT']), display_rounding), "total tax not tally"
        assert float(total_tax[1]) == round(float(service['TAX_AMT']), display_rounding), "total tax not tally"
        self.click_close_button()
        self.click_save_comp_cnnp_button()
        self.SVCS = []
        BuiltIn().set_test_variable(self.SVC_INFO, self.SVCS)



