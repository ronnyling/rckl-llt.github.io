import secrets
from resources.web.CustTrx import UICustTrxCommon
from PageObjectLibrary import PageObject
from resources.web import PAGINATION, TEXTFIELD, DRPSINGLE, RADIOBTN, BUTTON, COMMON_KEY
from resources.web.CustTrx.CreditNoteProduct import CreditNoteProductListPage
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from setup.hanaDB import HanaDB
import datetime


class CreditNoteProductAddPage(PageObject):
    """ Functions in Credit Note Product add page """
    PAGE_TITLE = "Customer Transaction / Credit Note (Product)"
    PAGE_URL = "customer-transactions-ui/creditnote-product"
    CN_DETAILS = "${CNDetails}"
    ROUTE = "Route"

    _locators = {
        "CNList": "//*[contains(text(),'Credit Note (Product) Listing')]",
        "InvList": "//*[contains(text(),'Invoice No')]/following::i[@class='anticon anticon-dash']",
        "InvNo": "//*[@row-index='{0}']//*[@col-id='INV_NO']"
    }

    @keyword("user creates ${cn_type} credit note with ${data_type} data")
    def user_creates_credit_note_with_data(self, cn_type, data_type):
        """ Function to create credit note with random/fixed data """
        self.user_creates_new_credit_note()
        prin_sel = self.validate_multi_principal_field(cn_type)
        details = self.builtin.get_variable_value(self.CN_DETAILS)
        if data_type == 'fixed':
            cn_cust = TEXTFIELD.select_from_textfield_selection("Customer", "CUST_NAME", details['customer'])
            cn_route = DRPSINGLE.select_from_single_selection_dropdown(self.ROUTE, details['route'])
        else:
            cn_cust = TEXTFIELD.select_from_textfield_selection("Customer", "CUST_NAME")
            cn_route = DRPSINGLE.select_from_single_selection_dropdown(self.ROUTE, "random")
        self.select_reason_in_credit_note(prin_sel)
        if details is not None:
            if isinstance(details['product'], list):
                for i in details['product']:
                    TEXTFIELD.inserts_into_trx_field(i['product'], i['productUom'])
            else:
                TEXTFIELD.inserts_into_trx_field(details['product'], details['productUom'])
        else:
            TEXTFIELD.inserts_into_trx_field("random", "random")
        self.validates_principal_visibility_in_credit_note("true")
        cn_route = cn_route.split(' - ')
        cn_route_name = cn_route[1].split(' (')
        self.builtin.set_test_variable("${cn_cust_name}", cn_cust)
        self.builtin.set_test_variable("${cn_route_cd}", cn_route[0])
        self.builtin.set_test_variable("${cn_route_name}", cn_route_name[0])
        UICustTrxCommon.UICustTrxCommon().validation_on_ui_transaction_calculation(details)
        BUTTON.click_button("Save")

    def user_creates_new_credit_note(self):
        self.selib.wait_until_element_is_visible(self.locator.CNList)
        POMLibrary.POMLibrary().check_page_title("CreditNoteProductListPage")
        CreditNoteProductListPage.CreditNoteProductListPage().click_add_credit_note_button()
        POMLibrary.POMLibrary().check_page_title("CreditNoteProductAddPage")

    def validate_multi_principal_field(self, cn_type):
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            self.principal_field_in_credit_note("displaying")
            prin_sel = self.select_principal_radio_button_for_credit_note(cn_type)
        else:
            self.principal_field_in_credit_note("not displaying")
            prin_sel = "random"
        return prin_sel

    def user_selects_customer_for_credit_note(self, item):
        cust = TEXTFIELD.select_from_textfield_selection("Customer", "CUST_NAME", item)
        return cust

    def select_principal_radio_button_for_credit_note(self, cn_type):
        prin_sel = RADIOBTN.select_from_radio_button("Principal", cn_type)
        return prin_sel

    def select_reason_in_credit_note(self, prin_sel):
        if prin_sel == 'Prime':
            selection = "Expired"
        elif prin_sel == 'Non-Prime':
            selection = "Damaged"
        else:
            selection = prin_sel
        DRPSINGLE.select_from_single_selection_dropdown("Reason ", selection)

    @keyword('principal field ${action} in credit note')
    def principal_field_in_credit_note(self, action):
        if action == 'displaying':
            principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
            assert principal == 'Prime', "Principal not default to Prime"
        elif action == 'not displaying':
            RADIOBTN.validates_radio_button("Principal", action)

    @keyword("principal in credit note showing ${status}")
    def validates_principal_visibility_in_credit_note(self, status):
        if status == 'enabled':
            status = "false"
        elif status == 'disabled':
            status = 'true'
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            rb_status = RADIOBTN.return_visibility_of_radio_buttons("Principal")
            self.builtin.should_be_equal(rb_status, status)

    def user_deletes_product_from_grid(self):
        """ Function to create credit note with random/fixed data """
        self.user_creates_new_credit_note()
        prin_sel = self.validate_multi_principal_field("Prime")
        self.select_reason_in_credit_note(prin_sel)
        details = self.builtin.get_variable_value(self.CN_DETAILS)
        DRPSINGLE.select_from_single_selection_dropdown(self.ROUTE, details['route'])
        self.user_selects_customer_for_credit_note(details['customer'])
        TEXTFIELD.inserts_into_trx_field(details['product'], "random")
        self.validates_principal_visibility_in_credit_note("true")
        BUTTON.click_inline_delete_icon("1")
        BUTTON.click_button("Yes")

    def user_selects_reason_without_warehouse_assigned(self):
        self.user_creates_new_credit_note()
        details = self.builtin.get_variable_value(self.CN_DETAILS)
        self.validate_multi_principal_field(details['principal'])
        self.select_reason_in_credit_note(details['reason'])

    @keyword("user validates ${principal} invoice listed correctly")
    def user_validates_invoice_listed_correctly(self, principal):
        details = self.builtin.get_variable_value("&{FilterDetails}")
        self.user_selects_customer_for_credit_note(details['customer_code'])
        DRPSINGLE.select_from_single_selection_dropdown(self.ROUTE, details['route_code'])
        self.select_principal_radio_button_for_credit_note(principal)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.InvList)

    @keyword("invoice listed with all ${principal} invoice")
    def invoice_listed_with_all_invoice(self, principal):
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        inv_list = self.builtin.get_variable_value("${inv_list}")
        if inv_list:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text(self.locator.InvNo.format(i))
                self.builtin.should_be_equal(get_principal, inv_list[i])
        BUTTON.click_pop_up_screen_button("Cancel")

    def user_selects_invoice_created(self):
        details = self.builtin.get_variable_value(self.CN_DETAILS)
        prin_sel = self.validate_multi_principal_field(details['principal'])
        self.select_reason_in_credit_note(prin_sel)
        DRPSINGLE.select_from_single_selection_dropdown(self.ROUTE, details['route'])
        self.user_selects_customer_for_credit_note(details['customer'])
        COMMON_KEY.wait_keyword_success("click_element", self.locator.InvList)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        rand = secrets.choice(range(0, num_row -1))
        inv_no = self.selib.get_text(self.locator.InvNo.format(rand))
        inv_dt = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='INV_DT']".format(rand))
        inv_dt = datetime.datetime.strptime(inv_dt, '%b %d, %Y').strftime("%Y-%m-%d")
        query = "SELECT CAST(PRD_ID as varchar) FROM TXN_INVDTL where TXN_ID = " \
                "(SELECT ID FROM TXN_INVOICE where INV_NO = '{0}' AND INV_DT = '{1}')".format(inv_no, inv_dt)
        HanaDB.HanaDB().connect_database_to_environment()
        HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.InvNo.format(rand))
        COMMON_KEY.wait_keyword_success("click_element", TEXTFIELD.locator.product)
        self.selib.get_text("{0}[0]//*[@col-id='PRD_CD']".format(TEXTFIELD.locator.productList))

    def prerequisite_for_credit_note(self):
        rand = secrets.choice(['"Return - Bad Stock", "Return - Good Stock"'])
        ReasonTypeGet.ReasonTypeGet().user_retrieves_reason_type(rand)
