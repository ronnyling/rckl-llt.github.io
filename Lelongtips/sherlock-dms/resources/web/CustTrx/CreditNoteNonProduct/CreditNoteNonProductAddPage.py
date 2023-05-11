from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from resources.restAPI.Common import TokenAccess
from resources.web import BUTTON, DRPSINGLE, TEXTFIELD, RADIOBTN
from resources.web.Common import POMLibrary
from resources.web.CustTrx.CreditNoteNonProduct import CreditNoteNonProductListPage


class CreditNoteNonProductAddPage(PageObject):
    """ Functions in credit note non product add page """
    PAGE_TITLE = "Customer Transaction / Credit Note (Non Product)"
    PAGE_URL = "customer-transactions-ui/creditnote-non-product-listing"
    CNNP_DETAILS = "${CNNPDetails}"
    CNNP_CUST = "${cn_np_cust}"

    @keyword("user creates ${cn_type} credit note non product using ${data_type} data")
    def user_creates_credit_note_non_product_using_data(self, cn_type, data_type):
        """ Function to create credit note non product using random/fixed data """
        self.user_creates_new_credit_note_non_product()
        self.user_fills_up_header_section(cn_type, data_type)
        cn_np_route = self.builtin.get_variable_value("${cn_np_route}")
        cn_np_cust = self.builtin.get_variable_value(self.CNNP_CUST)
        cn_np_route = cn_np_route.split(' - ')
        self.builtin.set_test_variable(self.CNNP_CUST, cn_np_cust)
        self.builtin.set_test_variable("${cn_np_route_cd}", cn_np_route[0])
        BUTTON.click_button("Save")

    def user_creates_new_credit_note_non_product(self):
        """ Function to create new credit note non product by clicking add button """
        POMLibrary.POMLibrary().check_page_title("CreditNoteNonProductListPage")
        CreditNoteNonProductListPage.CreditNoteNonProductListPage().click_add_credit_note_non_product_button()

    @keyword("user fills up header section with ${cn_type} selection using ${data_type} data")
    def user_fills_up_header_section(self, cn_type, data_type):
        """ Function to fill up header section with Prime/Non Prime using random/fixed data """
        self.select_principal_radio_button_for_credit_note(cn_type)
        self.select_reason_in_credit_note_non_product("random")
        RADIOBTN.select_from_radio_button("Tax", "Non-Taxable")
        details = self.builtin.get_variable_value(self.CNNP_DETAILS)
        if data_type == 'fixed':
            cn_np_cust = self.user_selects_customer_for_credit_note(details['customer'])
            self._wait_for_page_refresh()
            cn_np_route = DRPSINGLE.select_from_single_selection_dropdown("Route", details['route'])
        else:
            cn_np_cust = self.user_selects_customer_for_credit_note("random")
            self._wait_for_page_refresh()
            cn_np_route = DRPSINGLE.select_from_single_selection_dropdown("Route", "random")
        TEXTFIELD.inserts_into_transaction_service_field("CN_NP")
        self.builtin.set_test_variable("${cn_np_route}", cn_np_route)
        self.builtin.set_test_variable(self.CNNP_CUST, cn_np_cust)

    @keyword("user selects customer:${item} for credit note")
    def user_selects_customer_for_credit_note(self, item):
        """ Function to select customer for credit note """
        if item == 'random':
            cust = TEXTFIELD.select_from_textfield_selection("Customer ", "CUST_NAME")
        else:
            cust = TEXTFIELD.select_from_textfield_selection("Customer ", "CUST_NAME", item)
        return cust

    def select_principal_radio_button_for_credit_note(self, cn_type):
        """ Function to select value for principal field """
        principal = RADIOBTN.select_from_radio_button("Principal", cn_type)
        return principal

    def select_reason_in_credit_note_non_product(self, item):
        """ Function to select reason in credit note non product """
        DRPSINGLE.select_from_single_selection_dropdown("Reason ", item)

    @keyword("user validates ${principal} invoice listed correctly")
    def user_validates_invoice_listed_correctly(self, principal):
        """ Function to validate invoice listed correctly """
        self.select_principal_radio_button_for_credit_note(principal)
        BUTTON.click_text_field_meatballs_menu('Invoice No.')

    @keyword("invoice listed with all ${principal} invoice")
    def invoice_listed_with_all_invoice(self, principal):
        """ Function to compare invoice listed """
        inv_list = self.builtin.get_variable_value("${inv_list}")
        if inv_list:
            for i in range(0, 4):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='INV_NO']".format(i))
                self.builtin.should_be_equal(get_principal, inv_list[i])
        BUTTON.click_pop_up_screen_button("Cancel")

    def route_displayed_based_on_customer_selected(self):
        details = self.builtin.get_variable_value(self.CNNP_DETAILS)
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        CustomerGet.CustomerGet().user_retrieves_cust_name(details['customer'])
        get_route = RouteGet.RouteGet().user_gets_route_with_open_items()
        DRPSINGLE.select_from_single_selection_dropdown("Route", "random")
        route_list = self.builtin.get_variable_value('${dropdown_items}')
        assert get_route == route_list, "Route dropdown count not match with db retrieved data"
