from PageObjectLibrary import PageObject
from resources.web.CompTrx.CompDebitNoteNonProduct.CompDebitNoteNonProductListPage import CompDebitNoteNonProductListPage
from resources.web.CompTrx.CompanyInvoice.CompInvoiceAddPage import CompInvoiceAddPage
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import TokenAccess
from resources.web import DRPSINGLE, BUTTON, CALENDAR, TEXTFIELD
from robot.api.deco import keyword
from resources.Common import Common
from resources.TransactionFormula import TransactionFormula
from resources.restAPI.MasterDataMgmt.Supplier.SupplierGet import SupplierGet


class CompDebitNoteNonProductAddPage(PageObject):
    """ Functions for Company debit note non product Add Page actions """
    SVCS = []
    _locators = {
        "ref_no" : "",
        "load_image": "//div[@class='loading-text']//img",
        "service": "//input[@placeholder='Enter Service Code / Name']"
    }

    @keyword("user creates company debit note non product")
    def create_dnnp(self):
        dnnp_details = BuiltIn().get_variable_value("${DNNPDetails}")
        CompDebitNoteNonProductListPage().click_add_comp_cnnp_button()
        CompInvoiceAddPage().select_supplier_for_company_invoice(dnnp_details)
        self.select_dnnp_date(dnnp_details)
        self.user_inserts_dnnp_no(dnnp_details)
        self.select_reason_for_dnnp(dnnp_details)


    def user_inserts_dnnp_no(self, cnnp_details):
        """ Function to insert dnnp no code with random/fixed data """
        dnnp_details_given = self.builtin.get_variable_value("&{DNNPDetails['DnnpNo']}")
        if dnnp_details_given is not None:
            dnnp_no = TEXTFIELD.insert_into_field("Debit Note No.", cnnp_details['DnnpNo'])
        else:
            dnnp_no = TEXTFIELD.insert_into_field_with_length("Debit Note No", "random", 15)
        return dnnp_no

    def select_dnnp_date(self, details):
        """ Function to select dnnp date in company debit note screen """
        dnnp_date_given = self.builtin.get_variable_value("${fixedData['DnnpDate']}")
        if dnnp_date_given is not None:
            dnnp_date = CALENDAR.select_date_from_calendar("Due Date", details['DnnpDate'])
        else:
            dnnp_date = CALENDAR.select_date_from_calendar("Due Date", "today")
        return dnnp_date

    def select_reason_for_dnnp(self, details):
        """ Function to select reason in company debit note non product screen """
        if details is None:
            reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", "random")
        else:
            if details.get("Reason") is not None:
                reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", details['Reason'])
            else:
                reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", "random")
        return reason

    def create_svc_payload(self, svc_cd, amt):
        svc_info = {
            "SVC_CD": svc_cd,
            "AMT": amt
        }
        self.SVCS.append(svc_info)
        BuiltIn().set_test_variable("${service_info}", self.SVCS)

    def click_save_comp_dnnp_button(self):
        """ Function to save debit note non product """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()

    def click_close_button(self):
        """ Function to create new claim """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_icon("close")
        self._wait_for_page_refresh()
