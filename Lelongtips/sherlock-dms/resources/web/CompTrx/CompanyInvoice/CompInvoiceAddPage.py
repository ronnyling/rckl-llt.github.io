from PageObjectLibrary import PageObject
from resources.web.CompTrx.CompanyInvoice.CompInvoiceListPage import CompInvoiceListPage
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import TokenAccess
from resources.web import DRPSINGLE, BUTTON, CALENDAR, TEXTFIELD, COMMON_KEY
from robot.api.deco import keyword
from resources.Common import Common
from resources.TransactionFormula import TransactionFormula
from resources.restAPI.MasterDataMgmt.Supplier.SupplierGet import SupplierGet
from resources.restAPI.MasterDataMgmt.Warehouse.WarehouseGet import WarehouseGet
from resources.restAPI.MasterDataMgmt.Product import ProductGet, ProductUomGet


class CompInvoiceAddPage(PageObject):
    """ Functions for Company Invoice Add Page actions """
    PROD = "${prod}"
    PRDS = []
    _locators = {
        "price_loading" : "//img[@src='assets/images/glow_logo.gif']",
        "load_image": "//div[@class='loading-text']//img",
        "product": "//input[@placeholder='Enter Code/Name']"
    }

    def check_current_warehouse_inventory(self):
        wh_cd = BuiltIn().get_variable_value("${wh_cd}")
        wh_cd = wh_cd.split(" - ")
        wh_cd = wh_cd[0]
        wh_id = WarehouseGet().user_retrieves_warehouse_by_using_code(wh_cd)
        BuiltIn().set_test_variable("${wh_id}", wh_id)
        for prd in self.PRDS:
            print("PRD1 = ", prd)
            prd_details = ProductGet.ProductGet().user_retrieves_prd_by_prd_code(prd['PRD_CODE'])
            prd['PRD_ID'] = prd_details['ID']
            prd_uoms = prd['PRD_UOM']
            qty_in_smallest = 0
            for uom in prd_uoms:
                uom_details = ProductUomGet.ProductUomGet().user_retrieves_prd_uom_by_code(prd['PRD_ID'], uom['UOM'])
                base_qty = int(uom['QTY']) * int(uom_details['CONV_FACTOR_SML'])
                qty_in_smallest = qty_in_smallest + base_qty
            invt_master_result = TransactionFormula().get_current_inventory(wh_id, prd['PRD_ID'])
            print("WH ID = ", wh_id)
            print("PRD_ID = ", prd['PRD_ID'])
            master_his_result = TransactionFormula().get_current_inventory_master_history(wh_id, prd['PRD_ID'])
            print("invt_master_result = ", invt_master_result)
            #print("master_his_result = ", master_his_result)
            prd['CURRENT_QTY_ON_HAND'] = float(invt_master_result[0][0])
            prd['CURRENT_AVAILABLE_QTY'] = float(invt_master_result[0][1])
            prd['CURRENT_MASTER_HIST_STKRCP_QTY'] = float(master_his_result[0][0])
            prd['CURRENT_MASTER_HIST_STOCKBAL'] = float(master_his_result[0][1])
            prd['TOTAL_BUY_QTY_IN_SMALLEST'] = float(qty_in_smallest)
            print("PRD2 = ", prd)

    @keyword("validated inventory movement from INVT_MASTER, INVT_MASTER_HIS, INVT_TEMP is correct")
    def compare_master_invt_after_save_comp_invoice(self):
        wh_id = BuiltIn().get_variable_value("${wh_id}")
        for prd in self.PRDS:
            invt_master_result = TransactionFormula().get_current_inventory(wh_id, prd['PRD_ID'])
            master_his_result = TransactionFormula().get_current_inventory_master_history(wh_id, prd['PRD_ID'])
            invt_temp_result = TransactionFormula().get_current_inventory_temp(wh_id, prd['PRD_ID'])
            print("invt_master_result = ", invt_master_result)
            print("invt_temp_result = ", invt_temp_result)
            prd['CURRENT_INVT_TEMP_QTY'] = float(invt_temp_result[0][0])
            master_his_result = master_his_result[0]
            print("invt_master_his_result = ", master_his_result)
            assert float(invt_master_result[0][0]) == (prd['CURRENT_QTY_ON_HAND'] + prd['TOTAL_BUY_QTY_IN_SMALLEST']), "Current Qty On Hand Not Match"
            assert float(invt_master_result[0][1]) == (
                        prd['CURRENT_AVAILABLE_QTY'] + prd['TOTAL_BUY_QTY_IN_SMALLEST']), "Current Available Qty Not Match"
            assert prd['CURRENT_INVT_TEMP_QTY'] == prd['TOTAL_BUY_QTY_IN_SMALLEST'], "QTY in INVT temp is not correct"
            assert (prd['CURRENT_MASTER_HIST_STKRCP_QTY'] + prd['TOTAL_BUY_QTY_IN_SMALLEST']) == float(master_his_result[0]), "CURRENT_MASTER_HIST_STKRCP_QTY incorrect"
            assert (prd['CURRENT_MASTER_HIST_STOCKBAL'] + prd['TOTAL_BUY_QTY_IN_SMALLEST']) == float(master_his_result[1]), "CURRENT_MASTER_HIST_STOCKBAL incorrect"

    def create_prd_payload(self, prod_uom, r_qty, prod):
        uom_array = []
        uom_qty = {
            'UOM': prod_uom,
            'QTY': r_qty
        }
        uom_array.append(uom_qty)
        prd_info = {
            "PRD_CODE": prod,
            "PRD_UOM": uom_array,
            "ALL_PRD_QTY": r_qty
        }
        self.PRDS.append(prd_info)

    @keyword("user creates company invoice")
    def create_company_invoice(self):
        ci_details = BuiltIn().get_variable_value("${CIDetails}")
        CompInvoiceListPage().click_add_comp_invoice_button()
        self.user_inserts_invoice_no(ci_details)
        self.select_invoice_date_for_company_invoice(ci_details)
        self.select_invoice_due_date_for_company_invoice(ci_details)
        self.select_supplier_for_company_invoice(ci_details)
        wh_cd = self.select_warehouse_for_company_invoice(ci_details)
        BuiltIn().set_test_variable("${wh_cd}", wh_cd)

    def user_inserts_invoice_no(self, ci_details):
        """ Function to insert warehouse code with random/fixed data """
        ci_details_given = self.builtin.get_variable_value("&{CIDetails['InvNo']}")
        if ci_details_given is not None:
        #if 'InvNo' in ci_details:
            inv_no = TEXTFIELD.insert_into_field("Invoice No.", ci_details['InvNo'])
        else:
            inv_no = TEXTFIELD.insert_into_field_with_length("Invoice No.", "random", 15)
        return inv_no

    def select_delivery_date_for_sales_order(self, details):
        """ Function to select delivery date in sales order screen """
        delivery_date_given = self.builtin.get_variable_value("${fixedData['deliveryDate']}")
        if delivery_date_given is not None:
            del_date = CALENDAR.select_date_from_calendar("Delivery Date", details['deliveryDate'])
        else:
            del_date = CALENDAR.select_date_from_calendar("Delivery Date", "random")
        return del_date

    def select_supplier_for_company_invoice(self, details):
        """ Function to select supplier in company invoice screen """
        if details is None:
            supplier = DRPSINGLE.selects_from_single_selection_dropdown("Supplier", "random")
        else:
            if details.get("Supplier") is not None:
                supplier = DRPSINGLE.selects_from_single_selection_dropdown("Supplier", details['Supplier'])
            else:
                supplier = DRPSINGLE.selects_from_single_selection_dropdown("Supplier", "random")
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        if " - " in supplier:
            supplier = supplier.split(" - ")
            supplier = supplier[0]
        supp = SupplierGet().user_retrieves_supplier(supplier)
        BuiltIn().set_test_variable("${supplierinfo}", supp)
        return supplier

    def select_warehouse_for_company_invoice(self, details):
        """ Function to select warehouse in company invoice screen """
        if details is None:
            wh = DRPSINGLE.selects_from_single_selection_dropdown("Warehouse", "random")
        else:
            if details.get("Warehouse") is not None:
                wh = DRPSINGLE.selects_from_single_selection_dropdown("Warehouse", details['Warehouse'])
            else:
                wh = DRPSINGLE.selects_from_single_selection_dropdown("Warehouse", "random")
        return wh

    def select_invoice_date_for_company_invoice(self, details):
        """ Function to select invoice date in company invoice screen """
        inv_date_given = self.builtin.get_variable_value("${fixedData['InvDate']}")
        print("inv date given = ", inv_date_given)
        if inv_date_given is not None:
            invoice_date = CALENDAR.select_date_from_calendar("Invoice Date", details['InvDate'])
        else:
            invoice_date = CALENDAR.select_date_from_calendar("Invoice Date", "today")
        return invoice_date

    def select_invoice_due_date_for_company_invoice(self, details):
        """ Function to select invoice due date in company invoice screen """
        inv_due_date_given = self.builtin.get_variable_value("${fixedData['InvDueDate']}")
        if inv_due_date_given is not None:
            inv_due_date = CALENDAR.select_date_from_calendar("Invoice Due Date", details['InvDueDate'])
        else:
            inv_due_date = CALENDAR.select_date_from_calendar("Invoice Due Date", "next day")
        return inv_due_date

    @keyword("user intends to insert product '${prod}' with uom '${prod_uom}', Invoice Qty. '${i_qty}', Received Qty. '${r_qty}'")
    def user_intend_to_insert_product_details(self, prod, prod_uom, i_qty, r_qty):
        Common().wait_keyword_success("input_text", self.locator.product, prod)
        Common().wait_keyword_success("click_element", "//*[text()='%s']" % prod)
        Common().wait_keyword_success("click_element", "//tr//label[text()='{0} ']/following::*/nz-select[1]".format(prod))
        Common().wait_keyword_success("click_element",
                                      "//*[@class='cdk-overlay-pane']//following-sibling::li[contains(text(),'{0}')]".format(prod_uom))
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0} ']/following::input[2]".format(prod), i_qty)
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0} ']/following::input[3]".format(prod),
                                      r_qty)
        BuiltIn().set_test_variable(self.PROD, prod)
        self.create_prd_payload(prod_uom, r_qty, prod)
        self.check_current_warehouse_inventory()

    def click_save_comp_invoice_button(self, action):
        """ Function to save company invoice """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if action == "confirm":
            BUTTON.click_button("Save")
        else:
            COMMON_KEY.wait_keyword_success\
                ("click_element", '(//core-button//child::*[contains(text(),"{0}")]//ancestor::core-button[1])[1]'.
                 format("Save"))
        self._wait_for_page_refresh()

    def click_close_button(self):
        """ Function to click close button """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_icon("close")
        self._wait_for_page_refresh()

    @keyword("insert price '${price}' and discount '${disc}' then ${action} company invoice")
    def user_intend_to_insert_price_and_disc(self, price, disc, action):
        prod = BuiltIn().get_variable_value(self.PROD)
        for item in self.PRDS:
            if item['PRD_CODE'] == prod:
                item['GROSS_AMT'] = float(item['ALL_PRD_QTY']) * float(price)
                item['CUST_DISC'] = float(disc)
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0} ']/following::input[4]".format(prod), price)
        BuiltIn().sleep("2s")
        Common().wait_keyword_success("input_text", "//tr//label[text()='{0} ']/following::input[5]".format(prod), disc)
        BuiltIn().sleep("2s")
        Common().wait_keyword_success("click_element", "//*[contains(text(),'Discount Amt. ($)')]")
        BuiltIn().set_test_variable("${prd_info}", self.PRDS)
        TransactionFormula().company_tax_calculation_for_multi_product()
        prd_info = BuiltIn().get_variable_value("${prd_info}")
        self.validate_tax_amount(prd_info)
        #self.click_close_button()
        self.click_save_comp_invoice_button(action)

    def validate_tax_amount(self, prd_info):
        display_rounding = BuiltIn().get_variable_value("${display_rounding}")
        for prd in prd_info:
            total = 0
            Common().wait_keyword_success("click_element", "//tr//label[text()='{0} ']/following::a[1]".format(prd['PRD_CODE']))
            total_tax = self.selib.get_text("//tr//label[text()='{0} ']/following::a[1]".format(prd['PRD_CODE']))
            total_tax = total_tax.split(" ")
            count = 1
            for tax_amt in prd['ALL_LEVEL_TAX']:
                tax = self.selib.get_text("//div[contains(text(),'Tax Summary')]/following::*//tr[{0}]//td[5]".format(count))
                tax_component = self.selib.get_text(
                    "//div[contains(text(),'Tax Summary')]/following::*//tr[{0}]//td[2]".format(count))

                assert tax_component == prd['ALL_TAX_DESC'][count-1], "Tax Component Incorrect"
                assert round(float(tax_amt), display_rounding) == float(tax), "Tax Incorrect"
                total += tax_amt
                count = count + 1
            tax_summ_total_tax = self.selib.get_text(
                "//div[contains(text(),'Grand Total')]/following::div[1]")
            tax_summ_total_tax = tax_summ_total_tax.split(" ")
            assert float(tax_summ_total_tax[1]) ==  round(float(total), display_rounding), "Total tax not tally"
            assert float(total_tax[1]) == round(float(total), display_rounding), "Total tax not tally"
            BUTTON.click_icon("close")
