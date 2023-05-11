""" Python file related to debit note non product UI """
import datetime
import secrets

from PageObjectLibrary import PageObject

from resources.restAPI.Config.ReferenceData.ReasonType import ReasonTypeGet
from resources.web import DRPSINGLE, TEXTFIELD, CALENDAR, TOGGLE, BUTTON, RADIOBTN
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web.CustTrx.DebitNoteNonProduct import DebitNoteNonProductListPage
from setup.hanaDB import HanaDB
from resources.Common import Common


class DebitNoteNonProductAddPage(PageObject):
    """ Functions in debit note non product add page """
    PAGE_TITLE = "Customer Transaction / Debit Note (Non Product)"
    PAGE_URL = "customer-transactions-ui/debitnote-nonprd"
    DN_CUST_NAME = "${dn_cust_name}"

    _locators = {
        "DNList": "//*[contains(text(),'Debit Note (Non-Product) Listing')]",
        "CustDrp": "//label[text()='Customer']//following::input[1]",
        "CustSel": "(//*[contains(text(),'Customer')]/following::div[contains(@class, 'ant-table-scroll')])[2]//following::tr",
        "InvList": "//*[contains(text(),'Invoice No.')]/following::i[contains(@class, 'anticon-ellipsis')]",
        "cust_label": "//*[contains(text(),'Customer')]"
    }

    @keyword("user creates ${dn_type} debit note non product using ${data_type} data")
    def user_creates_debit_note_non_product_using_data(self, dn_type, data_type):
        """ Function to create debit note non product using random/fixed data """
        self.user_creates_new_debit_note_non_product()
        self.user_fills_up_header_section(dn_type, data_type)
        dn_route = self.builtin.get_variable_value("${dn_route}")
        dn_cust = self.builtin.get_variable_value("${dn_cust}")
        dn_cust_name = self.builtin.get_variable_value(self.DN_CUST_NAME)
        dn_route = dn_route.split(' - ')
        dn_route_name = dn_route[1].split(' (')
        self.builtin.set_test_variable("${dn_cust_cd}", dn_cust[0])
        self.builtin.set_test_variable(self.DN_CUST_NAME, dn_cust_name)
        self.builtin.set_test_variable("${dn_route_cd}", dn_route[0])
        self.builtin.set_test_variable("${dn_route_name}", dn_route_name[0])
        save_btn = BUTTON.return_locator_for_button("Save")
        Common.wait_keyword_success("click_element", "({0})[2]".format(save_btn))

    def user_creates_new_debit_note_non_product(self):
        """ Function to create new debit note non product by clicking add button """
        self.selib.wait_until_element_is_visible(self.locator.DNList)
        POMLibrary.POMLibrary().check_page_title("DebitNoteNonProductListPage")
        DebitNoteNonProductListPage.DebitNoteNonProductListPage().click_add_debit_note_button()

    @keyword("user fills up header section with ${dn_type} selection using ${data_type} data")
    def user_fills_up_header_section(self, dn_type, data_type):
        """ Function to fill up header section with Prime/Non Prime using random/fixed data """
        self.select_principal_radio_button_for_debit_note(dn_type)
        dn_type = dn_type.lower()
        self.select_reason_in_debit_note("random")
        CALENDAR.select_date_from_calendar("Due Date", "random")
        details = self.builtin.get_variable_value("${DNDetails}")
        if data_type == 'fixed':
            dn_cust = self.user_selects_customer_for_debit_note(details['customer'])
            self._wait_for_page_refresh()
            dn_route = DRPSINGLE.select_from_single_selection_dropdown("Route", details['route'])
        else:
            dn_cust = self.user_selects_customer_for_debit_note("random")
            self._wait_for_page_refresh()
            dn_route = DRPSINGLE.select_from_single_selection_dropdown("Route", "random")
        RADIOBTN.select_from_radio_button("Tax", "Non-Taxable")
        TEXTFIELD.inserts_into_transaction_service_field()
        self.validates_principal_visibility_in_debit_note("disabled")
        print("dn_cust", dn_cust)
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

        self.builtin.set_test_variable("${dn_route}", dn_route)
        self.builtin.set_test_variable("${dn_cust}", dn_cust)
        self.builtin.set_test_variable(self.DN_CUST_NAME, dn_cust_name)

    def validate_multi_principal_field(self, dn_type):
        """ Function to validate multi principal field """
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            self.principal_field_in_debit_note_product("displaying")
            prin_sel = self.select_principal_radio_button_for_debit_note(dn_type)
        else:
            self.principal_field_in_debit_note_product("not displaying")
            prin_sel = "random"
        return prin_sel

    def user_selects_customer_for_debit_note(self, item):
        """ Function to select customer for debit note """
        Common.wait_keyword_success("click_element", self.locator.CustDrp)
        total = self.selib.get_element_count(self.locator.CustSel)
        print("total customers:", total)
        if total <= 1:
            Common.wait_keyword_success("click_element", self.locator.CustDrp)
            DRPSINGLE.select_from_single_selection_dropdown("Route", "random")
            Common.wait_keyword_success("click_element", self.locator.CustDrp)
        if item == "random":
            cust = DRPSINGLE.randomize_dropdown_selection_in_dropdown()
            DRPSINGLE.select_from_single_selection_dropdown("Route", "random")
        else:
            Common.wait_keyword_success("click_element", "//*[@class='cdk-overlay-pane']//core-cell-render[@ng-reflect-cell-value='{0}']//preceding::a[1]".format(
                                                         item))
            cust = item
        print("cust", cust)
        return cust

    def select_principal_radio_button_for_debit_note(self, dn_type):
        """ Function to select value for principal field """
        prin_sel = RADIOBTN.select_from_radio_button("Principal", dn_type)
        return prin_sel

    def select_reason_in_debit_note(self, prin_sel):
        """ Function to select reason in debit note """
        DRPSINGLE.select_from_single_selection_dropdown("Reason", prin_sel)

    @keyword('principal field ${action} in debit note non product')
    def principal_field_in_debit_note_product(self, action):
        """ Function to check principal field if is displayed/not displayed """
        if action == 'displaying':
            principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
            assert principal == 'Prime', "Principal not default to Prime"
        elif action == 'not displaying':
            RADIOBTN.validates_radio_button("Principal", action)

    @keyword("principal in debit note non product showing ${status}")
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

    def user_deletes_service_from_grid(self):
        """ Function to delete service from grid """
        self.user_creates_new_debit_note_non_product()
        self.select_reason_in_debit_note("random")
        details = self.builtin.get_variable_value("${DNDetails}")
        self.user_selects_customer_for_debit_note(details['customer'])
        DRPSINGLE.select_from_single_selection_dropdown("Route", details['route'])
        TEXTFIELD.inserts_into_transaction_service_field()
        self.validates_principal_visibility_in_debit_note("true")
        BUTTON.click_inline_delete_icon("1")
        BUTTON.click_button("Yes")

    @keyword("user validates ${principal} invoice listed correctly")
    def user_validates_invoice_listed_correctly(self, principal):
        """ Function to validate invoice listed correctly """
        self.select_principal_radio_button_for_debit_note(principal)
        DRPSINGLE.select_from_single_selection_dropdown("Reference Document Type", "Invoice No.")
        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element", self.locator.InvList)

    @keyword("invoice listed with all ${principal} invoice")
    def invoice_listed_with_all_invoice(self, principal):
        """ Function to compare invoice listed """
        inv_list = self.builtin.get_variable_value("${inv_list}")
        if inv_list:
            for i in range(0, 4):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='INV_NO']".format(i))
                self.builtin.should_be_equal(get_principal, inv_list[i])
        BUTTON.click_pop_up_screen_button("Cancel")

    def prerequisite_for_debit_note(self):
        """ Function to set pre-requisite for debit note """
        rand = secrets.choice(['"Return - Bad Stock", "Return - Good Stock"'])
        ReasonTypeGet.ReasonTypeGet().user_retrieves_reason_type(rand)
