import secrets

from PageObjectLibrary import PageObject

from resources import Common
from resources.restAPI.Common import TokenAccess
from resources.restAPI.Config.TaxMgmt.TaxSetting import TaxSettingGet
from resources.restAPI.CustTrx.SalesOrder import SalesOrderGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.MasterDataMgmt.PriceGroup import ProductPriceGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet, ProductUomGet
from resources.web.CustTrx.SalesOrder import SalesOrderListPage
from resources.web.CustTrx.SalesInvoice import SalesInvoiceOverdueInv
from resources.web.CustTrx import UICustTrxCommon
from robot.libraries.BuiltIn import BuiltIn
from resources.web import RADIOBTN, DRPSINGLE, CALENDAR, TEXTFIELD, BUTTON, COMMON_KEY, PAGINATION, POPUPMSG
from robot.api.deco import keyword
import datetime
import re


class SalesOrderAddPage(PageObject):
    """ Functions for Sales Order Add Page actions """
    PAGE_TITLE = "Customer Transaction / Sales Order"
    PAGE_URL = "/customer-transactions-ui/salesorder/NEW"
    SO_DETAIL = "${fixedData}"
    TXN_TYPE = "${txnDetails}"
    DISC_DETAILS = "${discountDetails}"

    _locators = {
        "SOList": "//div[text()='Sales Order Listing']",
        "confirmOverdue": "//core-button[@ng-reflect-label='Yes']",
        "YesBtn": "//span[contains(text(),'Yes')]/ancestor::button[1]",
        "SaveBtn": "//core-button//child::*[contains(text(),'Save')]//ancestor::core-button[1]",
        "CopyBtn": "//button//child::*[contains(text(),'Copy')]//ancestor::button[1]",
        "OrderDT": "//core-cell-render[@ng-reflect-cell-value='Order Date']",
        "load_image": "//div[@class='loading-text']//img",
        "tax_summary": "//div//a[contains(text(),'Tax Summary')]",
        "closeBtn": "//button//child::*[@ng-reflect-nz-type='close']//ancestor::button[1]",
        "PopupCopyBtn": "(//button//child::*[contains(text(),'Copy')]//ancestor::button[1])[2]",
        "gross_amt":"//tr[@row-index='0']//core-cell-render[@col-id='TOTAL_GROSS_DISP']",
        "net_amt":"//tr[@row-index='0']//core-cell-render[@col-id='TOTAL_NET_DISP']",
        "CustDrp": "//label[text()='Customer']//following::input[1]",
        "CustSel": "(//*[contains(text(),'Customer')]/following::div[contains(@class, 'ant-table-scroll')])[2]//following::tr",
        "other_discount": "//div[contains(text(),'Other Discount')]/following::core-cell-render[@class='ng-star-inserted']//label",
        "customer_group_discount": "//div[contains(text(),'Cust Group Discount')]/following::div[contains(text(),'value_cgd')]"
    }

    def select_principal_radio_button_for_sales_order(self, details):
        """ Function to select route in sales order screen """
        if details is None:
            principal = RADIOBTN.select_from_radio_button("Principal", "random")
        else:
            if details.get("principal") is not None:
                principal = details['principal']
                principal = RADIOBTN.select_from_radio_button("Principal", details.get("principal"))
            else:
                principal = RADIOBTN.select_from_radio_button("Principal", "random")
        return principal

    def select_route_for_sales_order(self, details):
        """ Function to select route in sales order screen """
        if details is None:
            route = DRPSINGLE.selects_from_single_selection_dropdown("Route", "random")
        else:
            if details.get("route") is not None:
                route = DRPSINGLE.selects_from_single_selection_dropdown("Route", details['route'])
            else:
                route = DRPSINGLE.selects_from_single_selection_dropdown("Route", "random")
        return route

    def select_delivery_date_for_sales_order(self, details):
        """ Function to select delivery date in sales order screen """
        delivery_date_given = self.builtin.get_variable_value("${fixedData['deliveryDate']}")
        if delivery_date_given is not None:
            del_date = CALENDAR.select_date_from_calendar("Delivery Date", details['deliveryDate'])
        else:
            del_date = CALENDAR.select_date_from_calendar("Delivery Date", "random")
        return del_date

    def select_ship_to_address_for_sales_order(self, details):
        """ Function to select ship to address in sales order screen """
        ship_to_given = self.builtin.get_variable_value("${fixedData['shipTo']}")
        if ship_to_given is not None:
            DRPSINGLE.selects_from_single_selection_dropdown("Ship to Address", details['shipTo'])
        else:
            DRPSINGLE.selects_from_single_selection_dropdown("Ship to Address", "random")

    def select_warehouse_for_sales_order(self, details):
        """ Function to select warehouse in sales order screen """
        if details.get("warehouse") is not None:
            DRPSINGLE.selects_from_single_selection_dropdown("Warehouse", details['warehouse'])
        else:
            DRPSINGLE.selects_from_single_selection_dropdown("Warehouse", "random")

    @keyword("user inserts ${details} customer info")
    def select_customer_for_sales_order(self, details):
        """ Function to select customer in sales order screen """
        if details.get('customer'):
            cust = TEXTFIELD.select_from_textfield_selection("Customer", "CUST_NAME", details.get('customer'))
        else:
            cust = TEXTFIELD.select_from_textfield_selection("Customer", "CUST_NAME")
        self.builtin.run_keyword_and_ignore_error("click_element", self.locator.confirmOverdue)
        return cust

    def validate_dollar_sign_is_removed_from_details(self):
        details = self.builtin.get_variable_value(self.SO_DETAIL)
        UICustTrxCommon.UICustTrxCommon().validates_currency_in_product_details(details)

    def validate_selling_price(self, product_code, selling_price):
        """ Function to validate selling price value in sales order screen """
        get_selling_price = self.selib.get_text("//tr//*[text()='{0}']//following::*[@col-id='PRD_COST_DISP']"
                                                .format(product_code))
        self.builtin.should_be_equal(selling_price, get_selling_price)

    def validate_gross(self, product_code, gross):
        """ Function to validate gross value in sales order screen """
        get_gross = self.selib.get_text("//tr//*[text()='{0}']//following::*[@col-id='TOTAL_GROSS_DISP']"
                                        .format(product_code))
        self.builtin.should_be_equal(gross, get_gross)

    def validates_credit_limit(self, multi_status):
        if multi_status is False:
            credit_limit = TEXTFIELD.retrieves_text_field_text("Credit Limit")
            self.builtin.should_be_equal(credit_limit, 0)

    @keyword("user creates sales order with ${data_type} data")
    def user_creates_sales_order_with_data(self, data_type):
        """ Function to create sales order without applying promotion """
        details = self.user_inserts_sales_order_data(data_type)
        if data_type != 'sampling':
            self.user_applies_promotion()
            details = UICustTrxCommon.UICustTrxCommon().validation_on_ui_transaction_calculation(details)
            self.builtin.set_test_variable(self.SO_DETAIL, details)
        if self.DISC_DETAILS is None:
            self.user_click_save()

    def user_click_save(self):
        BUTTON.click_button("Save")

    @keyword("user inserts sales order with ${data_type} data")
    def user_inserts_sales_order_data(self, data_type):
        self.selib.wait_until_element_is_visible(self.locator.SOList)
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        details = self.builtin.get_variable_value(self.SO_DETAIL)
        SalesOrderListPage.SalesOrderListPage().click_add_sales_order_button()
        cust = self.select_customer_for_sales_order(details)
        del_date = self.select_delivery_date_for_sales_order(details)
        route = self.select_route_for_sales_order(details)
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            self.principal_field_in_sales_order("displaying")
            principal = self.select_principal_radio_button_for_sales_order(details)
            self.builtin.set_test_variable("${principal}", principal)
            print("PRINCIPAL TRUE? ", principal)
        elif multi_status is False:
            self.principal_field_in_sales_order("not displaying")

        self.select_warehouse_for_sales_order(details)
        status = BuiltIn().run_keyword_and_ignore_error \
            ("page_should_contain_element", SalesInvoiceOverdueInv.SalesInvoiceOverdueInv().locator.ConfirmDialog)
        if status == 'True ':
            COMMON_KEY.wait_keyword_success("click_element", self.locator.YesBtn)
        self.select_ship_to_address_for_sales_order(details)
        #if data_type == 'Sampling' or data_type =='non selling' :
        #    self.select_product_type("Sampling")
        self.inserts_order_product_details(details)
        route = route.split(" - ")
        self.builtin.set_test_variable('${so_cust}', cust)
        self.builtin.set_test_variable('${so_route}', route[0])
        self.builtin.set_test_variable('${del_date}', del_date)
        return details


    def inserts_order_product_details(self, details):
        txn_details = BuiltIn().get_variable_value(self.TXN_TYPE)
        if txn_details is None:
            details['productType'] = "Selling"
        if details.get('product', None) is not None:
            print("PRODUCT HERE:{0}".format(details.get('product')))
            products = details.get('product').split(",")
            productUom = details.get('productUom').split(",")
            productType = details.get('productType').split(",")
            print ("PRODUCTS1 :: ", products)
            if isinstance(products, list):
                for i, j, k in zip(products, productUom, productType):
                    if k == "Sampling":
                        BUTTON.click_button("Sampling")
                    else :
                        BUTTON.click_button("Selling")
                    TEXTFIELD.inserts_into_trx_field(i, j)
            else:
                TEXTFIELD.inserts_into_trx_field(details['product'], details['productUom'])
        if details.get('PROD_ASS_DETAILS', None) is not None:
            print("PRODUCT DETAILS HERE:{0}".format(details.get('PROD_ASS_DETAILS')))
            products = details.get('PROD_ASS_DETAILS').split(",")
            if isinstance(details['PROD_ASS_DETAILS'], list):
                for i in details['PROD_ASS_DETAILS']:
                    TEXTFIELD.inserts_into_trx_field(i['PRD_CODE'], i['PRD_UOM_DETAILS'])
            else:
                TEXTFIELD.inserts_into_trx_field(details['PRD_CODE'], details['PRD_UOM_DETAILS'])

    @keyword("principal field ${action} in sales order")
    def principal_field_in_sales_order(self, action):
        try:
            self.selib.wait_until_element_is_visible(self.locator.SOList)
            SalesOrderListPage.SalesOrderListPage().click_add_sales_order_button()
        except Exception as e:
            print(e.__class__, "occured")
            self.selib.page_should_not_contain_element(self.locator.SOList)
        self.check_principal_field(action)

    def check_principal_field(self, action):
        if action == 'displaying':
            principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
            assert principal == 'Prime', "Principal not default to Prime"
        elif action == 'not displaying':
            RADIOBTN.validates_radio_button("Principal", action)

    @keyword("save button showing ${status}")
    def save_button_showing(self, status):
        btn_disabled = BUTTON.check_button_is_disabled("Save")
        print("BTN_DISABLED: {0}".format(btn_disabled))
        if status == "enabled":
            assert btn_disabled == "false", "Save button disabled"
        elif status == "disabled":
            assert btn_disabled == "true", "Save button enabled"

    def copy_order_button(self, status):
        if status == "enabled":
            self.selib.page_should_contain_element(self.locator.CopyBtn)
        elif status == "disabled":
            self.selib.page_should_not_contain_element(self.locator.CopyBtn)

    @keyword("user copies ${data_type} sales order")
    def user_copies_sales_order(self, data_type):
        self.copy_order_button("disabled")
        self.user_inserts_sales_order_data("fixed")
        self.copy_order_button("enabled")
        PAGINATION.return_number_of_rows_in_a_page()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.CopyBtn)
        COMMON_KEY.wait_keyword_success("click_element",
                                                 "(//core-button[@ng-reflect-icon='search'])[2]")
        if data_type == "random":
            so_no = BuiltIn().get_variable_value("${res_bd_so_no}")
            for x in range(0, len(so_no)):
                TEXTFIELD.insert_into_filter_field("Order No.", so_no[x])
                self.select_sales_order()
        elif data_type == "created":
            Common().wait_keyword_success("click_element", "//tr[1]//td[2]//core-cell-render//div//a")
        else:
            so_no = BuiltIn().get_variable_value("${SOIDs}")
            print("length is {0}".format(len(so_no)))
            for x in range(0, len(so_no)):
                print("{0} time".format(x))
                data_list = [so_no[x]]
                print("Data list is {0}".format(data_list))
                TEXTFIELD.insert_into_filter_field("Order No.", so_no[x])
                self.select_sales_order()
        BuiltIn().set_test_variable("${copied_so_nos}",so_no)
        self.click_popup_copy()

    def select_sales_order(self):
        COMMON_KEY.wait_keyword_success("click_element", "//*[@role='row' and @row-index='0']//"
                                                         "child::*[contains(@class,'ant-checkbox-wrapper')]")

    def click_popup_copy(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.PopupCopyBtn)

    def user_verify_only_last_30_days_shown(self):
        self.user_inserts_sales_order_data("fixed")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.CopyBtn)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.OrderDT)
        oldest_date = self.selib.get_text("(//tr[@row-index='0']//core-cell-render[@col-id='TXN_DT']//div)[1]")
        oldest_date = datetime.datetime.strptime(oldest_date, '%d/%m/%Y')
        current_date = datetime.datetime.today()
        time_between_dates = current_date - oldest_date
        assert time_between_dates.days <= 31, "Listing contains sales order from more than 30 days ago"
        self.select_sales_order()
        self.click_popup_copy()

    def user_verify_product_price(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        rows = PAGINATION.return_number_of_rows_in_a_page()
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        for i in range(0, int(rows)):
            prd_name = self.selib.get_text("(//tr[@row-index='{0}']//core-cell-render[@col-id='PRD_CD']//div)[1]".format(i))
            prd_price = self.selib.get_text("(//tr[@row-index='{0}']//core-cell-render[@col-id='PRD_COST_DISP']//div)[1]".format(i))
            results = ProductPriceGet.ProductPriceGet().get_prd_price("CAC822D9:FCC178C1-9E97-4AC9-8649-AB8F2E409C44", prd_name)
            assert prd_price == results['SELLING_PRC'], "Price of Product {0} is incorrect".format(prd_name)

    def user_verify_product_tax(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.tax_summary)
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        results = TaxSettingGet.TaxSettingGet().get_tax_sett("B1846865:3B6F7FCA-E095-4538-91A9-959D545243A1")
        tax_rate = self.builtin.run_keyword_and_ignore_error("get_text","//*[contains(text(),'Tax Rate')]//following::td[2]")
        print("tax_rate is {0}".format(tax_rate))
        if tax_rate[0] == 'PASS':
            tax_rate = re.sub("[^0-9]", "", tax_rate[1])
            print("Current tax: {0}".format(tax_rate))
            print("API Tax is {0}".format(results[0]['TAX_RATE']))
            assert tax_rate == results[0]['TAX_RATE'], "Tax Rate is not using latest values"
        COMMON_KEY.wait_keyword_success("click_element", self.locator.closeBtn)

    def user_verify_product_quantity_merged(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code('DistEgg')
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        so_nos = BuiltIn().get_variable_value("${copied_so_nos}")
        so_ids = []
        for so in so_nos:
            result = SalesOrderGet.SalesOrderGet().user_retrieves_salesorder_by_code(so)
            so_ids.append(result['ID'])
            print("SO_ID IS {0}".format(so_ids))
        BuiltIn().set_test_variable("${res_bd_sales_order_id}", so_ids)
        products = SalesOrderGet.SalesOrderGet().user_retrieves_multiple_sales_order_transaction("fixed")
        self.verify_product_quantity(products)

    def verify_product_quantity(self,products):
        for x in products:
            prd = ProductGet.ProductGet().user_retrieves_prd_cd_by_prd_id(x["PRD_ID"])
            prd_name = prd["PRD_CD"]
            product_uom = ProductUomGet.ProductUomGet().user_retrieves_prd_uom(x["PRD_ID"])
            for y in range (0, len(product_uom)):
                print("y is {0}".format(product_uom[y]["ID"]))
                print("X is {0}".format(x["UOM_ID"]))
                if product_uom[y]["ID"] == x["UOM_ID"]:
                    print("Once")
                    uom_choice = y
                    qty = self.selib.get_text("//tr//*[text()='{0}']//following::input[contains(""@class,'ant-input-number')\
                                and (""@max='Infinity')][{1}]".format(prd_name, uom_choice))
                    print("API QTY IS {0}".format(x["PRD_QTY"]))
                    print("UI QTY IS {0}".format(qty))
                    assert x["PRD_QTY"] == qty

    def user_applies_promotion(self):
        BUTTON.click_button("Apply Promotion")
        try:
            POPUPMSG.validate_pop_up_message("Order is not entitled for promotions")
        except Exception as e:
            print(e.__class__, "occured")
            rows = PAGINATION.return_number_of_rows_in_a_page()
            assert rows > 0, "No promos shown"
            promo_cd = self.builtin.get_variable_value("${fixedData['promo']}")
            if promo_cd:
                col_list = ["PROMO_CD"]
                data_list = [promo_cd]
                PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Promotion", "check",
                                                                                            col_list, data_list)
                promo_amt = self.builtin.get_variable_value("${fixedData['promoAmt']}")
                self.builtin.set_test_variable("${promo_disc}", promo_amt)
            BUTTON.click_button("Apply")

    def user_creates_sales_order_and_apply_promo(self):
        self.user_inserts_sales_order_data("random")
        self.builtin.get_variable_value(self.SO_DETAIL)
        self.user_applies_promotion()

    def validate_unable_to_save_the_transaction(self):
        BUTTON.check_button_is_disabled("Apply Promotion")
        BUTTON.check_button_is_disabled("Save")

    def validate_unable_to_select_different_product_type(self):
        txn_details = BuiltIn().get_variable_value(self.TXN_TYPE)
        if txn_details['txnType'] == 'P':
            BUTTON.check_button_is_disabled("Selling")
        else:
            BUTTON.check_button_is_disabled("Sampling")

    def user_validates_the_amount_of_product_being_copied_over(self):
        gross = self.selib.get_text(self.locator.gross_amt)
        net = self.selib.get_text(self.locator.net_amt)
        details = BuiltIn().get_variable_value("${amountData}")
        assert gross == details['gross'], "Gross amt is incorrect"
        assert net == details['net'], "Net amt is incorrect"

    @keyword("user verify cust group discount on ${level} level")
    def verify_customer_group_discount_shown_on_other_discount(self, level):
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
        self.user_click_save()

    @keyword("user verify customer group discount not applied")
    def verify_customer_group_discount_not_applied(self):
        discount_amount = self.selib.get_text(self.locator.other_discount)
        assert float(discount_amount) == 0.00, "CUSTOMER GROUP DISC IS APPLIED"
