""" Python file related to debit note product UI """
import datetime
import secrets
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.web import BUTTON, DRPSINGLE, CALENDAR, TEXTFIELD, RADIOBTN, PAGINATION, COMMON_KEY
from resources.web.Common import POMLibrary
from resources.web.CustTrx.DebitNoteProduct import DebitNoteProductListPage
from setup.hanaDB import HanaDB

today = datetime.datetime.now()


class DebitNoteProductAddPage(PageObject):
    """ Functions in debit note product add page """
    PAGE_TITLE = "Customer Transaction / Debit Note (Product)"
    PAGE_URL = "customer-transactions-ui/debit-note"
    DN_DETAILS = "${DNDetails}"
    DN = "debit note"

    _locators = {
        "DNList": "//*[contains(text(),'Debit Note (Product) Listing')]",
        "CustDrp": "//label[text()='Customer']//following::input[1]",
        "CustSel": "(//*[contains(text(),'Customer')]/following::div[contains(@class, 'ant-table-scroll')])[2]//following::tr",
        "InvList": "//*[contains(text(),'Invoice No.')]/following::i[contains(@class, 'anticon-ellipsis')]",
        "cust_label": "//*[contains(text(),'Customer')]",
        "product": "//input[@placeholder='Enter Code / Description']",
        "load_img": "//div[@class='loading-text']//img"
    }

    @keyword("user creates ${dn_type} debit note product using ${data_type} data")
    def user_creates_debit_note_product_using_data(self, dn_type, data_type):
        """ Function to create debit note product using random/fixed data """
        self.user_creates_new_debit_note_product()
        calculation = self.user_fills_up_header_section(dn_type, data_type)
        calculation_list_is_empty = True
        if calculation is not None:
            for result in calculation:
                if result != "":
                    calculation_list_is_empty = False
                    break
            if calculation_list_is_empty is True:
                dic = {
                    "route": "REgg02",
                    "customer": "Salted Egg",
                    "product": "ProdAde1",
                    "productUom": "PCK:2,PC:4"
                }
                self.builtin.set_test_variable(self.DN_DETAILS, dic)
                self.user_fills_up_header_section("Prime", "fixed")
        BUTTON.click_button("Save")
        HanaDB.HanaDB().connect_database_to_environment()
        print("today", today)
        HanaDB.HanaDB().check_if_exists_in_database_by_query("SELECT * FROM TXN_DBN WHERE TXN_DT = '{0}'".format(today))
        HanaDB.HanaDB().disconnect_from_database()

    @keyword("user confirms ${dn_type} debit note product using ${data_type} data after creates")
    def user_confirms_debit_note_product_using_data_after_creates(self, dn_type, data_type):
        self.user_creates_new_debit_note_product()
        calculation = self.user_fills_up_header_section(dn_type, data_type)
        calculation_list_is_empty = True
        print("calculation", calculation)
        if calculation is not None:
            for result in calculation:
                if result != "":
                    calculation_list_is_empty = False
                    break
            if calculation_list_is_empty is True:
                dic = {
                    "route": "REgg02",
                    "customer": "Salted Egg",
                    "product": "ProdAde1",
                    "productUom": "PCK:2,PC:4"
                }
                self.builtin.set_test_variable(self.DN_DETAILS, dic)
                self.user_fills_up_header_section("Prime", "fixed")
        BUTTON.click_button("Save & Confirm")

    def user_creates_new_debit_note_product(self):
        """ Function to create new debit note product by clicking add button """
        self.selib.wait_until_element_is_visible(self.locator.DNList)
        POMLibrary.POMLibrary().check_page_title("DebitNoteProductListPage")
        DebitNoteProductListPage.DebitNoteProductListPage().click_add_debit_note_button()

    @keyword("user fills up header section with ${dn_type} selection using ${data_type} data")
    def user_fills_up_header_section(self, dn_type, data_type):
        """ Function to fill up header section with Prime/Non Prime using random/fixed data """
        if dn_type != "None":
            self.select_principal_radio_button(dn_type)
        DRPSINGLE.select_from_single_selection_dropdown("Reason", "random")
        CALENDAR.select_date_from_calendar("Due Date", "random")
        details = self.builtin.get_variable_value(self.DN_DETAILS)
        if data_type == 'fixed' and details is not None:
            dn_cust = DRPSINGLE.user_selects_customer_route_for(self.locator.DN, details['customer'])
            self._wait_for_page_refresh()
            dn_route = DRPSINGLE.select_from_single_selection_dropdown("Route", details['route'])
            if isinstance(details['product'], list):
                for i in details['product']:
                    prd_detail = TEXTFIELD.inserts_into_trx_field(i['product'], i['productUom'])
            else:
                prd_detail = TEXTFIELD.inserts_into_trx_field(details['product'], details['productUom'])
        else:
            dn_cust = DRPSINGLE.user_selects_customer_route_for(self.locator.DN, "random")
            self._wait_for_page_refresh()
            dn_route = DRPSINGLE.select_from_single_selection_dropdown("Route", "random")
            prd_detail = TEXTFIELD.inserts_into_trx_field("random", "random")
        self.validates_principal_visibility_in_debit_note("disabled")
        print("dn_cust", dn_cust)
        dn_cust_name = self.split_customer_name(dn_cust)
        print("transaction start:")
        calculation = TransactionFormula.TransactionFormula().tran_calculation(dn_type, prd_detail[0], dn_cust_name,
                                                                               prd_detail[1], 0, "value")
        print("Calculation result: ", calculation)
        self.builtin.set_test_variable("${dn_route}", dn_route)
        self.builtin.set_test_variable("${dn_cust}", dn_cust)
        self.builtin.set_test_variable("${dn_cust_name}", dn_cust_name)
        self.builtin.set_test_variable("${prd_detail}", prd_detail)
        dn_route = dn_route.split(' - ')
        dn_route_name = dn_route[1].split(' (')
        self.builtin.set_test_variable("${dn_cust_cd}", dn_cust[0])
        self.builtin.set_test_variable("${dn_route_cd}", dn_route[0])
        self.builtin.set_test_variable("${dn_route_name}", dn_route_name[0])
        return calculation

    def select_principal_radio_button(self, dn_type):
        RADIOBTN.select_from_radio_button("Principal", dn_type)
        dn_type = dn_type.lower()

    @keyword("user fills up fields in header section with ${dn_type} selection using ${data_type} data")
    def user_fills_up_fields_in_header_section(self, dn_type, data_type):
        """ Function to fill up header section with Prime/Non Prime/None using random/fixed data """
        if dn_type != "None":
            self.select_principal_radio_button(dn_type)
        DRPSINGLE.select_from_single_selection_dropdown("Reason", "random")
        CALENDAR.select_date_from_calendar("Due Date", "random")
        details = self.builtin.get_variable_value(self.DN_DETAILS)
        if data_type == 'fixed' and details is not None:
            DRPSINGLE.user_selects_customer_route_for(self.locator.DN, details['customer'])
            self._wait_for_page_refresh()
            DRPSINGLE.select_from_single_selection_dropdown("Route", details['route'])
        else:
            DRPSINGLE.user_selects_customer_route_for(self.locator.DN, "random")
            self._wait_for_page_refresh()
            DRPSINGLE.select_from_single_selection_dropdown("Route", "random")

    def selected_product_hidden_successfully_from_product_selection(self):
        details = self.builtin.get_variable_value(self.DN_DETAILS)
        if details is not None:
            if isinstance(details['product'], list):
                for i in details['product']:
                    self.selib.wait_until_page_does_not_contain_element(self.locator.load_img)
                    COMMON_KEY.wait_keyword_success("click_element", self.locator.product)
                    self.builtin.run_keyword_and_continue_on_failure("input_text", self.locator.product, i['product'])
                    COMMON_KEY.wait_keyword_success("press_keys", None, "TAB")
            else:
                self.selib.wait_until_page_does_not_contain_element(self.locator.load_img)
                COMMON_KEY.wait_keyword_success("click_element", self.locator.product)
                self.builtin.run_keyword_and_continue_on_failure("input_text", self.locator.product, details['product'])
                COMMON_KEY.wait_keyword_success("press_keys", None, "TAB")

    def split_customer_name(self, dn_cust):
        if ' - ' or ' ' or '\n' in dn_cust:
            try:
                dn_cust = dn_cust.split(' - ')
                dn_cust_name = dn_cust[1].split(',')
                dn_cust_name = dn_cust_name[0]
            except Exception as e:
                print(e.__class__, "occured")
                dn_cust_name = dn_cust[0].split('\n')
                if len(dn_cust_name) > 1:
                    dn_cust_name = dn_cust_name[1]
        else:
            dn_cust_name = dn_cust

        return dn_cust_name

    def validate_multi_principal_field(self, dn_type):
        """ Function to validate multi principal field """
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            RADIOBTN.principal_field_in("displaying")
            prin_sel = RADIOBTN.select_from_radio_button("Principal", dn_type)
        else:
            RADIOBTN.principal_field_in("not displaying")
            prin_sel = "random"
        return prin_sel

    def select_principal_radio_button_for_debit_note(self, dn_type):
        """ Function to select value for principal field """
        prin_sel = RADIOBTN.select_from_radio_button("Principal", dn_type)
        return prin_sel

    @keyword("principal in debit note product showing ${status}")
    def validates_principal_visibility_in_debit_note(self, status):
        """ Function to validate principal visibility in debit note """
        self._wait_for_page_refresh()
        if status == 'enabled':
            status = "false"
        elif status == 'disabled':
            status = 'true'
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            rb_status = RADIOBTN.return_visibility_of_radio_buttons("Principal")
            print("rb_status", rb_status)
            print("status", status)
            self.builtin.should_be_equal(rb_status, status)

    def user_deletes_product_from_grid(self):
        """ Function to delete product from grid """
        self.user_creates_new_debit_note_product()
        DRPSINGLE.select_from_single_selection_dropdown("Reason", "random")
        details = self.builtin.get_variable_value(self.DN_DETAILS)
        DRPSINGLE.user_selects_customer_route_for(details['customer'])
        DRPSINGLE.select_from_single_selection_dropdown("Route", details['route'])
        TEXTFIELD.inserts_into_trx_field(details['product'], "random")
        self.validates_principal_visibility_in_debit_note("true")
        BUTTON.click_inline_delete_icon("1")
        BUTTON.click_button("Yes")

    @keyword("user validates ${principal} invoice listed correctly")
    def user_validates_invoice_listed_correctly(self, principal):
        """ Function to validate invoice listed correctly """
        RADIOBTN.select_from_radio_button("Principal", principal)
        DRPSINGLE.select_from_single_selection_dropdown("Reference Document Type", "Invoice No.")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.InvList)

    @keyword("invoice listed with all ${principal} invoice")
    def invoice_listed_with_all_invoice(self, principal):
        """ Function to compare invoice listed """
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        inv_list = self.builtin.get_variable_value("${inv_list}")
        if inv_list:
            for i in range(0, int(num_row - 1)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='INV_NO']".format(i))
                self.builtin.should_be_equal(get_principal, inv_list[i])
        BUTTON.click_pop_up_screen_button("Cancel")

    def prerequisite_for_debit_note(self):
        """ Function to set pre-requisite for debit note """
        rand = secrets.choice(['"Return - Bad Stock", "Return - Good Stock"'])
        ReasonTypeGet.ReasonTypeGet().user_retrieves_reason_type(rand)

    def user_clicks_on_save_and_confirm_button(self):
        BUTTON.click_button("Save & Confirm")
        self._wait_for_page_refresh()

    @keyword("${description} product is shown successfully on the product listing")
    def product_is_shown_successfully_on_the_product_listing(self, description):
        product_code = self.builtin.get_variable_value("${product_code}")
        self._wait_for_page_refresh()
        self.selib.wait_until_page_does_not_contain_element(self.locator.load_img)
        self.selib.page_should_contain_element('//core-cell-render[@col-id="PRD_CD"][@ng-reflect-cell-value="{0}"]'.format(product_code))

    @keyword("user ${selection} to add new ${description} product successfully")
    def user_to_add_new_product_successfully(self, selection, description):
        product_code = self.builtin.get_variable_value("${product_code}")
        if selection == "able":
            self._wait_for_page_refresh()
            self.selib.wait_until_page_does_not_contain_element(self.locator.load_img)
            TEXTFIELD.inserts_into_trx_field(product_code, "random")
        else:
            try:
                status = self.selib.get_element_attribute(self.locator.product, "ng-reflect-is-disabled")
                self.builtin.should_be_true(bool(status))
            except Exception as e:
                print(e.__class__, "occured")
                self.builtin.run_keyword_and_continue_on_failure("input_text", self.locator.product, product_code)
