from PageObjectLibrary import PageObject
from resources.web.CompTrx.CompCreditNoteProduct.CompCreditNoteProductListPage import CompCreditNoteProductListPage
from resources.web.CompTrx.CompDebitNoteProduct.CompDebitNoteProductAddPage import CompDebitNoteProductAddPage
from resources.web.CompTrx.CompanyInvoice.CompInvoiceAddPage import CompInvoiceAddPage
from robot.libraries.BuiltIn import BuiltIn
from resources.web import DRPSINGLE, BUTTON, CALENDAR, TEXTFIELD, COMMON_KEY, CHECKBOX
from robot.api.deco import keyword


class CompCreditNoteProductAddPage(PageObject):
    """ Functions for Company credit note product Add Page actions """
    PRDS = []
    PROD = "${prod}"
    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "product": "//input[@placeholder='Enter Code/Name']"
    }

    @keyword("user creates company credit note product")
    def create_cn(self):
        cn_details = BuiltIn().get_variable_value("${CNDetails}")
        CompCreditNoteProductListPage().click_add_comp_cn_button()
        CompInvoiceAddPage().select_supplier_for_company_invoice(cn_details)
        self.select_cn_date(cn_details)
        self.user_inserts_cn_no(cn_details)
        CompDebitNoteProductAddPage().select_reason_for_dn(cn_details)

    @keyword("user removes existing record")
    def remove_existing_record(self):
        CHECKBOX.select_checkbox("Product Details", "vertical", "all", "True")
        BUTTON.click_icon("delete")
        BuiltIn().sleep("2s")
        BUTTON.click_button("Yes")

    def user_inserts_cn_no(self, cn_details):
        """ Function to insert cn no code with random/fixed data """
        cn_details_given = self.builtin.get_variable_value("&{CNDetails['CnNo']}")
        if cn_details_given is not None:
            cn_no = TEXTFIELD.insert_into_field("Credit Note No.", cn_details['CnNo'])
        else:
            cn_no = TEXTFIELD.insert_into_field_with_length("Credit Note No.", "random", 15)
        BuiltIn().set_test_variable("${cn_no}", cn_no)
        return cn_no

    def select_cn_date(self, details):
        """ Function to select cn date in company credit note screen """
        cn_date_given = self.builtin.get_variable_value("${fixedData['CnDate']}")
        if cn_date_given is not None:
            cn_date = CALENDAR.select_date_from_calendar("Credit Note Date", details['CnDate'])
        else:
            cn_date = CALENDAR.select_date_from_calendar("Credit Note Date", "today")
        return cn_date

    def select_reason_for_cn(self, details):
        """ Function to select reason in company credit note product screen """
        if details is None:
            reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", "random")
        else:
            if details.get("Reason") is not None:
                reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", details['Reason'])
            else:
                reason = DRPSINGLE.selects_from_single_selection_dropdown("Reason", "random")
        return reason

    def click_save_comp_cn_button(self):
        """ Function to save company credit note product """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        COMMON_KEY.wait_keyword_success("click_element",
                                        '(//core-button//child::*[contains(text(),"{0}")]//ancestor::core-button[1])[1]'
                                        .format("Save"))

        #BUTTON.click_button("Save")
        self._wait_for_page_refresh()



