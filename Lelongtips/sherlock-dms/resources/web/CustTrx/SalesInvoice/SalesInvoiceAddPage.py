from PageObjectLibrary import PageObject

from resources import Common
from resources.web.CustTrx.SalesInvoice import SalesInvoiceListPage
from resources.web.MasterDataMgmt.PromotionMgmt.Promotion import PromotionAddPage
from resources.web.CustTrx.SalesOrder import SalesOrderAddPage
import json, secrets, time
from resources.restAPI.Common import TokenAccess
from setup.hanaDB import HanaDB
from resources.restAPI.MasterDataMgmt.Warehouse import WarehouseGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet
from resources.web import COMMON_KEY, DRPSINGLE, CALENDAR, RADIOBTN, TEXTFIELD, BUTTON, POPUPMSG, PAGINATION
from selenium.common.exceptions import NoSuchElementException
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.AppSetup import TaxationGet, AppSetupPut, AppSetupGet
from resources.web.CustTrx import UICustTrxCommon
from resources.TransactionFormula import TransactionFormula

Wait_Time = "0.5 min"
retry_time = "3 sec"


class SalesInvoiceAddPage(PageObject):
    """ Functions for Sales Invoice Add Page actions """
    PAGE_TITLE = "Customer Transaction / Sales Invoice"
    PAGE_URL = "customer-transactions-ui/invoice/NEW"
    INV_DETAILS = "${InvDetails}"
    INV_LVL = "${inv_level}"
    PRD_ID = "${prd_id}"
    DISC_DETAILS = "${discountDetails}"

    _locators = {
        "PrdRow": "//*[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']/following::tr//td[2]",
        "InvList": "//div[text()='Sales Invoice Listing']",
        "InvRoute": "//*[text()='Route']/following::nz-select[1]",
        "SORouteList": "//label[contains(text(),'Route')]/following::li",
        "YesBtn": "//span[contains(text(),'Yes')]/ancestor::button[1]",
        "customer": "//*[contains(text(),'Customer')]/following::*[1]//input",
        "customerList": "//label[text()='Customer']//following::tr[@role='row']",
        "shipToAddress": "//*[text()='Ship to Address']//following::nz-select",
        "product": "//input[@placeholder='Enter Code / Description']",
        "productList": "//input[@placeholder='Enter Code / Description']//following::tr[@role='row']",
        "confirmOverdue": "//core-button[@ng-reflect-label='Yes']",
        "principal_btn": "//*[text()='Principal']/following::*[2]//nz-radio-group",
        "CreditLimit": "//*[contains(text(),'Credit Limit')]/following::*[4]//input",
        "AvailableBalance": "//*[contains(text(),'Available Bal.')]/following::*[4]//input",
        "LoadingImg": "//div[@class='loading-text']//img",
        "containText": "//*[text()='%s']",
        "SearchInput": "//*[@ng-reflect-name='PROMO_CD']//input[@type='text']",
        "customer_group_discount": "//div[contains(text(),'Cust Group Discount')]/following::div[contains(text(),'value_cgd')]"
    }

    divcontains = "//div[contains(text(),'%s')]"

    def select_route_for_invoice(self, route_name):
        """ Function to select route in invoice screen """
        COMMON_KEY.wait_keyword_success("click_element", "//label[text()='{0}']//following::nz-select[1]".format("Route"))
        self.selib.input_text("//label[text()='Route']/following::nz-select[1]//input", route_name)
        COMMON_KEY.wait_keyword_success("click_element", "{0}[contains(text(),'{1}')]".
                                      format(DRPSINGLE.locator.dropdown, route_name))
        return route_name

    def select_delivery_date_for_invoice(self, details):
        """ Function to select delivery date in invoice screen """
        CALENDAR.select_date_from_calendar("Delivery Date", "today")

    def select_invoice_date_for_invoice(self):
        """ Function to select invoice date in invoice screen """
        inv_date = CALENDAR.select_date_from_calendar('Invoice Date', 'today')
        return inv_date

    def select_warehouse_for_invoice(self, details):
        """ Function to select warehouse in invoice screen """
        if details.get("warehouse") is not None:
            DRPSINGLE.selects_from_single_selection_dropdown("Warehouse", details['warehouse'])

    def select_customer_for_invoice(self, cust_name):
        """ Function to select customer in invoice screen """
        COMMON_KEY.wait_keyword_success("click_element", self.locator.customer)
        if cust_name == 'random':
            number_of_cust = self.selib.get_element_count(self.locator.customerList)
            cust_count = secrets.choice(range(1, int(number_of_cust)))
            cust_name = self.selib.get_text("{0}[{1}]//*[@col-id='CUST_NAME']"
                                            .format(self.locator.customerList, cust_count))
        self.selib.input_text(self.locator.customer, cust_name)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.containText % cust_name)
        self.builtin.run_keyword_and_ignore_error("click_element", self.locator.confirmOverdue)
        return cust_name

    def select_principal_radio_button_for_invoice(self, details):
        """ Function to select route in sales order screen """
        if details.get("principal") is not None:
            principal = RADIOBTN.select_from_radio_button("Principal", details['principal'])
        else:
            principal = RADIOBTN.select_from_radio_button("Principal", 'random')
        return principal

    def validate_selling_price(self, product_code, selling_price):
        """ Function to validate selling price value in invoice screen """
        get_selling_price = self.selib.get_text("//tr//*[text()='{0}']//following::*[@col-id='PRD_COST_DISP']"
                                                .format(product_code))
        self.builtin.should_be_equal(selling_price, get_selling_price)

    def validate_gross(self, product_code, gross):
        """ Function to validate gross value in invoice screen """
        get_gross = self.selib.get_text("//tr//*[text()='{0}']//following::*[@col-id='TOTAL_GROSS_DISP']"
                                        .format(product_code))
        self.builtin.should_be_equal(gross, get_gross)
        return get_gross

    def get_current_inventory(self, wh_id, prod_id):
        wh_id = COMMON_KEY.convert_id_to_string(wh_id)
        prod_id = COMMON_KEY.convert_id_to_string(prod_id)
        query = "select CAST(ON_HAND_QTY as VARCHAR),CAST(AVAILABLE_QTY as VARCHAR)," \
                "CAST(ALLOCATE_QTY as VARCHAR)  from INVT_MASTER WHERE " \
                "WHS_ID='{0}' AND PRD_ID='{1}'".format(wh_id, prod_id)
        HanaDB.HanaDB().connect_database_to_environment()
        result = HanaDB.HanaDB().fetch_all_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        self.builtin.set_test_variable(self.INV_LVL, result)
        self.builtin.set_test_variable("${wh_id}", wh_id)
        self.builtin.set_test_variable(self.PRD_ID, prod_id)

    @keyword("validated inventory movement deducted correctly")
    def validate_stock_movement_is_deducted(self):
        TransactionFormula().validate_stock_movement_after_create_invoice()

    @keyword("user inserts invoice with ${cond} data")
    def user_inserts_invoice_details(self, cond):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        details = self.builtin.get_variable_value(self.INV_DETAILS)
        wh_id = WarehouseGet.WarehouseGet().user_gets_warehouse_by_using_data("WHS_CD:{0}".format(details['warehouse']))
        wh_id = wh_id[0]

        self.insert_invoice_header(details)
        if details.get('product', None) is not None:
            if isinstance(details['product'], list):
                for i in details['product']:
                    product_code = TEXTFIELD.inserts_into_trx_field(i['product'], i['productUom'])
                    self.validate_selling_price(product_code[0], i['sellingPrice'])
                    self.validate_gross(product_code[0], i['gross'])
            else:
                prod_id = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(details['product'])
                prod_id = prod_id['ID']
                self.get_current_inventory(wh_id, prod_id)
                self.builtin.set_test_variable(self.PRD_ID, prod_id)
                TEXTFIELD.inserts_into_trx_field(details['product'], details['productUom'])
        if details.get('PROD_ASS_DETAILS', None) is not None:
            print("PRODUCT DETAILS HERE:{0}".format(details.get('PROD_ASS_DETAILS')))
            if isinstance(details['PROD_ASS_DETAILS'], list):
                for i in details['PROD_ASS_DETAILS']:
                    TEXTFIELD.inserts_into_trx_field(i['PRD_CODE'], i['PRD_UOM_DETAILS'])
            else:
                TEXTFIELD.inserts_into_trx_field(details['PRD_CODE'], details['PRD_UOM_DETAILS'])


    @keyword("user creates invoice with ${data_type} data")
    def user_creates_invoice_without_promotion(self, cond):
        self.user_inserts_invoice_details(cond)
        details = self.builtin.get_variable_value(self.INV_DETAILS)
        self.user_apply_promotion(details)
        UICustTrxCommon.UICustTrxCommon().validation_on_ui_transaction_calculation(details)
        if self.DISC_DETAILS is None:
            self.user_click_save_invoice()

    def user_click_save_invoice(self):
        BUTTON.click_button("Save")

    @keyword('principal field ${action} in invoice')
    def principal_field_in_invoice(self, action):
        try:
            self.selib.wait_until_element_is_visible(self.locator.InvList)
            SalesInvoiceListPage.SalesInvoiceListPage().click_add_invoice_button()
        except Exception as e:
            print(e.__class__, "occured")
            self.selib.page_should_not_contain_element(self.locator.InvList)
        if action == 'displaying':
            principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
            assert principal == 'Prime', "Principal not default to Prime"
        elif action == 'not displaying':
            RADIOBTN.validates_radio_button("Principal", action)

    @keyword("user creates new invoice with")
    def user_creates_new_invoice_with(self, data, promotion_id_from_setup=None, randomize=None):
        time.sleep(3)
        SalesInvoiceListPage.SalesInvoiceListPage().click_add_invoice_button()  # this method is from SalesInvoice List Page
        print("creates new invoice ", promotion_id_from_setup)
        print(json.dumps(PromotionAddPage.PromotionAddPage().PromotionDict))
        self.user_provides_invoice_details(data, randomize)
        self.product_selection(data)
        self.apply_promotion(data, promotion_id_from_setup)

    @keyword("user creates new invoice from data file, verifies then saves it")
    def user_create_invoice_from_data_list(self, promotion_id_from_setup=None, randomize=None):
        data = BuiltIn().get_variable_value("&{file_data}")
        for key_invoices in data:
            print("Test scenario: ", key_invoices)
            self.user_creates_new_invoice_with(data[key_invoices], promotion_id_from_setup, randomize)

    @keyword("User provides invoice details")
    def user_provides_invoice_details(self, data, randomize=None):
        print(randomize)
        if randomize != 'random':
            DRPSINGLE.selects_from_single_selection_dropdown('Route', data.get('InvoiceDetails_Route'))
            self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
            COMMON_KEY.wait_keyword_success("click_element", "//input[@placeholder='Enter Code / Name']")
            self.selib.input_text("//input[@placeholder='Enter Code / Name']", data.get('InvoiceDetails_Customer'))
            COMMON_KEY.wait_keyword_success("click_element","//div[contains(text(),'%s')]" % data.get(
                                         'InvoiceDetails_Customer'))
            self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
            principal = data.get('InvoiceDetails_Principal')
            if principal == 'Non-Prime':
                RADIOBTN.select_from_radio_button('Principal', 'Non-Prime')

        else:
            # self.select_invoice_date_for_invoice()
            DRPSINGLE.selects_from_single_selection_dropdown('Route', 'random')
            # CALENDAR.select_date_from_calendar('Delivery Date', 'random')
            DRPSINGLE.selects_from_single_selection_dropdown('Customer', 'random')
            DRPSINGLE.selects_from_single_selection_dropdown('Route Plan', 'random')
            DRPSINGLE.selects_from_single_selection_dropdown('Ship to Address', 'random')

    def product_selection(self, data):
        # set first product and quantity in UOM
        COMMON_KEY.wait_keyword_success("click_element", self.locator.ProductSearch)
        self.selib.input_text(self.locator.ProductSearch, data.get('PrdDetails_Product 1'))
        COMMON_KEY.wait_keyword_success("click_element",
                                                 self.divcontains % data.get('PrdDetails_Product 1'))
        self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
        self.selib.input_text(self.locator.InputBoxes + "[1]", data.get('PrdDetails_Prd1 UOM1'))
        self.selib.input_text(self.locator.InputBoxes + "[2]", data.get('PrdDetails_Prd1 UOM2'))
        self.selib.input_text(self.locator.InputBoxes + "[3]", data.get('PrdDetails_Prd1 UOM3'))
        val1 = self.selib.get_element_attribute(self.locator.SellingPriceColumn + "[2]", "ng-reflect-cell-value")
        self.builtin.should_contain(val1, str(data.get('PrdDetails_Selling Price 1')))  # convert the int (price) to string for compare
        print("Product 1 selling price matches.")

        # set second product and quantity in UOM
        prd_details_product_2 = data.get('PrdDetails_Product 2')
        if prd_details_product_2 != "":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.ProductSearch)
            self.selib.input_text(self.locator.ProductSearch, prd_details_product_2)
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.divcontains % prd_details_product_2)
            self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
            self.selib.input_text(self.locator.InputBoxes + "[4]", data.get('PrdDetails_Prd2 UOM1'))
            self.selib.input_text(self.locator.InputBoxes + "[5]", data.get('PrdDetails_Prd2 UOM2'))
            self.selib.input_text(self.locator.InputBoxes + "[6]", data.get('PrdDetails_Prd2 UOM3'))
            val1 = self.selib.get_element_attribute(self.locator.SellingPriceColumn + "[3]", "ng-reflect-cell-value")
            self.builtin.should_contain(val1, str(data.get('PrdDetails_Selling Price 2')))
            print("Product 2 selling price matches.")

        # set third product and quantity in UOM
        prd_details_product_3 = data.get('PrdDetails_Product 3')
        if prd_details_product_3 != "":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.ProductSearch)
            self.selib.input_text(self.locator.ProductSearch, prd_details_product_3)
            COMMON_KEY.wait_keyword_success("click_element", self.divcontains % prd_details_product_3)
            self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
            self.selib.input_text(self.locator.InputBoxes + "[7]", data.get('PrdDetails_Prd3 UOM1'))
            self.selib.input_text(self.locator.InputBoxes + "[8]", data.get('PrdDetails_Prd3 UOM2'))
            self.selib.input_text(self.locator.InputBoxes + "[9]", data.get('PrdDetails_Prd3 UOM3'))
            val1 = self.selib.get_element_attribute(self.locator.SellingPriceColumn + "[4]", "ng-reflect-cell-value")
            self.builtin.should_contain(val1, str(data.get('PrdDetails_Selling Price 3')))
            print("Product 3 selling price matches.")

    def user_apply_promotion(self, details):
        BUTTON.click_button("Apply Promotion")
        try:
            POPUPMSG.validate_pop_up_message("Invoice is not entitled for promotions")
        except Exception as e:
            print(e.__class__, "occured")
            self.apply_promotion(details)
            rows = PAGINATION.return_number_of_rows_in_a_page()
            assert rows > 0, "No promos shown"

    def apply_promotion(self, data, promotion_id_from_setup=None):
        promo_cd = self.builtin.get_variable_value("${InvDetails['promo']}")
        if promo_cd:
            col_list = ["PROMO_CD"]
            data_list = [promo_cd]
            PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Promotion", "check",
                                                                       col_list, data_list)
            promo_amt = self.builtin.get_variable_value("${InvDetails['promoAmt']}")
            self.builtin.set_test_variable("${promo_disc}", promo_amt)
        BUTTON.click_button("Apply")

    def FOC_promo(self, data):
        self.selib.click_element(self.locator.FOC)
        self.selib.input_text(self.locator.FOCqty, data.get('PrdDetails_FOC Quantity'))
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Save)

    def user_verifies_promotion_discount(self, data):
        val1 = self.driver.find_element_by_xpath(self.locator.InvoiceGrossAmount).text
        self.builtin.should_contain(val1, data.get(
            'Summary_GrossAmount'))  # summary section that comes in "0.00" quoted decimals will be string value
        print("Summary Gross Amount matches.")
        val2 = self.driver.find_element_by_xpath(self.locator.DiscountAmount).text
        self.builtin.should_contain(val2, data.get('Summary_DiscountAmount'))
        print("Summary Discount Amount matches.")
        val3 = self.driver.find_element_by_xpath(self.locator.TaxAmount).text
        self.builtin.should_contain(val3, data.get('Summary_TaxAmount'))
        print("Summary Tax Amount matches.")
        val4 = self.driver.find_element_by_xpath(self.locator.InvoiceNetAmount).text
        self.builtin.should_contain(val4, data.get('Summary_NetAmount'))
        print("Summary Net Amount matches.")
        val5 = self.driver.find_element_by_xpath(self.locator.InvoiceNetReceivableAmount).text
        self.builtin.should_contain(val5, data.get('Summary_NetReceivableAmount'))
        print("Summary Net Receivable Amount matches.")

        try:
            if data.get('Summary_FOC') != "":
                valfoc = self.selib.get_element_attribute(self.locator.InvoiceFOC, "ng-reflect-model")
                self.builtin.should_contain(valfoc, data.get(
                    'Summary_FOC'))  # FOC counts might be read as int type, need convert
                print("FOC amount matches.")
        except NoSuchElementException:
            pass

    def user_saves_the_invoice(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Save)
        self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
        self.selib.page_should_not_contain_element(self.locator.principal_btn)

    @keyword("user provides invoice header with ${details}")
    def insert_invoice_header(self, details):
        SalesInvoiceListPage.SalesInvoiceListPage().click_add_invoice_button()
        cust_name = self.select_customer_for_invoice(details['customer'])
        route_cd = self.select_route_for_invoice(details['route'])
        principal = self.select_principal_radio_button_for_invoice(details)
        self.select_warehouse_for_invoice(details)
        self.select_delivery_date_for_invoice(details)
        inv_date = self.select_invoice_date_for_invoice()
        self.builtin.set_test_variable("${principal}", principal)
        self.builtin.set_test_variable("${inv_date}", inv_date)
        self.builtin.set_test_variable("${cust_name}", cust_name)
        self.builtin.set_test_variable("${route_cd}", route_cd)

    @keyword('user verifies ${flag} product is listed in product selection when invoice is ${cond} transaction')
    def retrieve_product_list_from_product_selection(self, prd_prin_flag, cond):

        details = self.builtin.get_variable_value(self.INV_DETAILS)
        self.insert_invoice_header(details)
        self.builtin.wait_until_keyword_succeeds("0.2 min", retry_time, "click_element",
                                                 SalesOrderAddPage.SalesOrderAddPage().locator.product)

    @keyword('verified only ${flag} product are listed')
    def compare_listing_product_with_api_product_data(self, prin_flag):
        prd_list = self.selib.get_webelements(self.locator.PrdRow)
        for item in prd_list:
            text = self.selib.get_text(item)
            if prin_flag == 'prime':
                TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
            else:
                TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
            ProductGet.ProductGet().user_retrieves_prd_by_prd_code(text)

    @keyword("verified only ${flag} warehouse will appear when ${trans_flag} invoice is selected")
    def verify_warehouse_drop_down_principal(self, principal_flag, trans_flag):
        SalesInvoiceListPage.SalesInvoiceListPage().click_add_invoice_button()
        details = self.builtin.get_variable_value(self.INV_DETAILS)
        self.select_principal_radio_button_for_invoice(details)
        wh_list = DRPSINGLE.return_item_in_singledropdown("Warehouse")
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        res_body = WarehouseGet.WarehouseGet().user_gets_warehouse_by_using_type(principal_flag)
        for wh in wh_list:
            warehouse = self.selib.get_text(wh)
            warehouse = warehouse.split(" ")
            warehouse = warehouse[0]
            print("Warehouse choon", warehouse)
            for item in res_body[1]:
                print("Warehouse samuel", item['WHS_CD'])
                if item['WHS_CD'] == warehouse:
                    flag = True
            assert flag, "Warehouse Not found"

    @keyword("verified credit limit and available balance is ${cond}")
    def credit_limit_display(self, cond):
        details = self.builtin.get_variable_value(self.INV_DETAILS)
        self.insert_invoice_header(details)
        a_balance = self.selib.get_element_attribute(self.locator.AvailableBalance, 'ng-reflect-model')
        CL = self.selib.get_element_attribute(self.locator.CreditLimit, 'ng-reflect-model')
        flag = False
        if a_balance == "0.00" and CL == "0.00":
            flag = True
        if cond == 'not displaying':
            assert flag, "Credit Limit and Avaiable Balance are displaying"
        else:
            assert not flag, "Credit Limit and Avaiable Balance are not displaying"

    @keyword("user turn ${on} discount impact with ${off}")
    def turn_discount_impact_on_off(self, on_off, disc_tobe_include):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("sysimp")
        if disc_tobe_include != 'no disc':
            disc_include = disc_tobe_include.split(",")
        disc_include_list = []
        for item in disc_include:
            data = TaxationGet.TaxationGet().user_retrieves_option_values_discount_included(item)
            disc_include_list.append(data)
        on = ""
        if on_off == 'on':
            on = True
        else:
            on = False
        payload = {
            "DISCOUNT_IMPACT_FOR_TAX_COMPUTATION": on,
            "DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION": disc_include_list
        }
        self.builtin.set_test_variable("${AppSetupDetails}", payload)
        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        AppSetupPut.AppSetupPut().user_updates_app_setup_details_using_data()

    @keyword("save button is ${status}")
    def save_button_is(self, status):
        btn_disabled = BUTTON.check_button_is_disabled("Save")
        print("BTN_DISABLED: {0}".format(btn_disabled))
        if status == "enabled":
            assert btn_disabled == "false", "Save button disabled"
        elif status == "disabled":
            assert btn_disabled == "true", "Save button enabled"

    def user_removes_random_product(self):
        total_rows = PAGINATION.return_number_of_rows_in_a_page()
        product_row = secrets.choice(range(0, total_rows))
        BUTTON.click_product_delete_icon(product_row)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.YesBtn)

    def user_adds_random_product(self):
        TEXTFIELD.inserts_into_trx_field("random", "random")

    def user_changes_random_product_quantity(self):
        self.builtin.run_keyword_and_ignore_error("wait_until_element_is_not_visible", self.locator.load_image)
        total_rows = PAGINATION.return_number_of_rows_in_a_page()
        print("TOTAL ROWS:{0}".format(total_rows))
        product_row = secrets.choice(range(0, int(total_rows)))
        prd_name = self.selib.get_text(
            "(//tr[@row-index='{0}']//core-cell-render[@col-id='PRD_CD']//div)[1]".format(product_row))
        number_of_uom = COMMON_KEY.wait_keyword_success("get element count", "//tr//*[text()='{0}']//following::"
                                                    "input[contains(""@class,'ant-input-number')"
                                                    "and (@max='Infinity')]".format(prd_name))
        print("num uom:{0}".format(number_of_uom))
        uom_choice = secrets.choice(range(1, int(number_of_uom)))
        uom_random = secrets.choice(range(1, 10))
        print("prd_name: {0}, uom_choice:{1}, uom_random:{2}".format(prd_name,uom_choice,uom_random))
        COMMON_KEY.wait_keyword_success("input_text", "//tr//*[text()='{0}']//following::input[contains("
                                                 "@class,'ant-input-number')and (@max='Infinity')][{1}]"
                                                 .format(prd_name, uom_choice), uom_random)
        self.builtin.wait_until_keyword_succeeds(Wait_Time, "3sec" ,"click_element", "//li[contains(@class,'ant-pagination-next')]")

    def user_creates_invoice_and_apply_promo(self):
        self.user_inserts_invoice_details("random")
        details = self.builtin.get_variable_value(self.INV_DETAILS)
        self.user_apply_promotion(details)

    def product_not_populated_in_dropdown(self):
        details = self.builtin.get_variable_value(self.INV_DETAILS)
        self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.product)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.product, details['product'])
        self.selib.page_should_not_contain_element(self.locator.containText % details['product'])
        COMMON_KEY.wait_keyword_success("press_keys", None, "TAB")

    def product_populated_in_details_correctly(self):
        details = self.builtin.get_variable_value(self.INV_DETAILS)
        self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
        COMMON_KEY.wait_keyword_success("page_should_contain_element", self.locator.containText % details['product'])

    def validate_currency_sign_is_removed_from_details(self):
        details = self.builtin.get_variable_value(self.INV_DETAILS)
        UICustTrxCommon.UICustTrxCommon().validates_currency_in_product_details(details)

    @keyword("user verify customer group discount on sales invoice ${level} level")
    def verify_customer_group_discount_applied_on_leve(self, level):
        custGrpDisc = BuiltIn().get_variable_value("${customer_group_disc}")
        grp_disc_amt_locator = self.locator.customer_group_discount
        grp_disc_amt_locator = grp_disc_amt_locator.replace("value_cgd", custGrpDisc)
        if level == 'product':
            Common().wait_keyword_success("click_element", "//tr[@row-index='0']//div//a")
        elif level == 'footer':
            Common().wait_keyword_success("click_element", "//div[@class='col-sm-2']//core-popover//a")
        grpDiscAmt = self.selib.get_text(grp_disc_amt_locator)
        Common().wait_keyword_success("press_keys", None, "ESC")
        assert float(grpDiscAmt) == float(custGrpDisc), "GRP DISC NOT MATCH"
        self.user_click_save_invoice()

    @keyword('user opens created sales invoice')
    def open_created_sales_invoice(self):
        Common().wait_keyword_success("click_element", "//tr[1]//td[2]//core-cell-render//div//a")

    def verify_unable_to_edit_product_details(self):
        Common().wait_keyword_success("click_element", "//div[@class='col-sm-2']//core-popover//a")
        Common().wait_keyword_success("press_keys", None, "ESC")
        details = self.builtin.get_variable_value(self.DISC_DETAILS)
        uom_field = self.selib.get_element_attribute \
            ("(//*[text()='{0}']/following::input)[1]".format(details['PROD_CD']), "ng-reflect-is-disabled")
        assert uom_field == 'true', "PRODUCT UOM FIELD NOT DISABLE"

