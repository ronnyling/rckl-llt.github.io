from PageObjectLibrary import PageObject
from resources import TransactionFormula
from resources.restAPI.Common import TokenAccess
from resources.restAPI.Config.AppSetup import AppSetupGet
from robot.api.deco import keyword
from setup.hanaDB import HanaDB
from resources.web import RADIOBTN, COMMON_KEY
import datetime


class UICustTrxCommon(PageObject):
    _locators = {
        "TranSummaryLabel": "//*[contains(text(),'Summary')]/following::label[contains(text(),'Gross')]//parent::div//label",
        "TranSummaryAmt": "//*[contains(text(),'Summary')]/following::label[contains(text(),'Gross')]//parent::div//following-sibling::div//label"
    }

    SUMMARY_AMT = "${summary_amount}"
    APPSETUP_DETAILS = "${body_result}"
    INV_DETAILS = "${InvDetails}"
    RTN_DETAILS = "${ReturnDetails}"
    CN_DETAILS = "${CNDetails}"
    DN_DETAILS = "${DNDetails}"
    SO_DETAILS = "${fixedData}"
    GROSS_CURRENCY = "Gross ({0})"
    TAX_CURRENCY = "Tax ({0})"
    NET_CURRENCY = "Net ({0})"

    def validates_currency_in_product_details(self, details):
        get_val_list = []
        prod_item = ["Selling Price", "Gross", "Promotion Discount", "Cash Discount", "Tax", "Net"]
        for item in prod_item:
            get_value = self.validate_product_details_value(details['product'], item)
            get_val_list.append(get_value)
        print("get_val_list, ", get_val_list)
        TokenAccess.TokenAccess().user_retrieves_token_access_as('hqadm')
        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        TokenAccess.TokenAccess().get_token_by_role('distadm')
        body_result = self.builtin.get_variable_value(self.APPSETUP_DETAILS)
        for item in get_val_list:
            assert body_result['CURRENCY_SETTING'] not in item, "Value showing currency in details"

    def validation_on_ui_transaction_calculation(self, details):
        TokenAccess.TokenAccess().user_retrieves_token_access_as('hqadm')
        AppSetupGet.AppSetupGet().user_retrieves_details_of_application_setup()
        TokenAccess.TokenAccess().user_retrieves_token_access_as('distadm')
        principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
        if details.get("PROD_ASS_DETAILS") is None:
            details["PROD_ASS_DETAILS"] = []

            if isinstance(details['product'], list):
                for i in details['product']:
                    details = self.product_and_product_uom_details(i, details)
            else:
                details = self.product_and_product_uom_details(details, details)
        rtn = self.builtin.get_variable_value(self.RTN_DETAILS)
        cn = self.builtin.get_variable_value(self.CN_DETAILS)
        dn = self.builtin.get_variable_value(self.DN_DETAILS)
        so = self.builtin.get_variable_value(self.SO_DETAILS)
        if rtn or cn or dn:
            cust_disc = 'No'
        else:
            cust_disc = 'percent'
        prd_details = TransactionFormula.TransactionFormula().tran_calculation_for_gross_and_cust_disc\
                                (principal, details['customer'], cust_disc, details['PROD_ASS_DETAILS'])
        TransactionFormula.TransactionFormula().tax_calculation_for_multi_product()
        summary_amount = {
            "TTL_GROSS": 0,
            "TTL_DISC": 0,
            "TTL_TAX": 0,
            "TTL_NET": 0
        }
        self.builtin.set_test_variable(self.SUMMARY_AMT, summary_amount)
        for item in prd_details:
            self.calculation_in_line_verification(item, item['PRD_CODE'])
        self.calculation_total_verification()
        return details

    def product_and_product_uom_details(self, item, details):
        uom_data = []
        product_uom = item['productUom'].split(",")
        for uom in product_uom:
            prod_uom_qty = uom.split(":")
            uom_details = {
                "UOM": prod_uom_qty[0],
                "QTY": prod_uom_qty[1]
            }
            uom_data.append(uom_details)
        get_prod = {
            "PRD_CODE": item['product'],
            "PRD_UOM": uom_data
        }
        details["PROD_ASS_DETAILS"].append(get_prod)
        return details

    def calculation_in_line_verification(self, calculation, prd_code):
        selling_price = self.round_decimal_to_display_in_ui(calculation['UNIT_PRICE'])
        gross = self.round_decimal_to_display_in_ui(calculation['GROSS_AMT'])
        promo_disc = self.round_decimal_to_display_in_ui(calculation['PROMO_DISC'])
        cust_disc = self.round_decimal_to_display_in_ui(calculation['CUST_DISC'])
        cust_disc_new = float(cust_disc)
        grp_discount = self.round_decimal_to_display_in_ui(calculation['GRPDISC_AMT'])
        self.builtin.set_test_variable("${customer_group_disc}", grp_discount)
        grp_discount_new = float(grp_discount)
        cust_disc = cust_disc_new + grp_discount_new
        cust_disc = "{:.2f}".format(cust_disc)
        self.builtin.set_test_variable("${other_disc}", cust_disc)
        tax_amt = self.round_decimal_to_display_in_ui(calculation['TOTAL_TAX'])
        net_amt = self.round_decimal_to_display_in_ui(calculation['NET_TTL_TAX'])
        inv = self.builtin.get_variable_value(self.INV_DETAILS)
        rtn = self.builtin.get_variable_value(self.RTN_DETAILS)
        cn = self.builtin.get_variable_value(self.CN_DETAILS)
        dn = self.builtin.get_variable_value(self.DN_DETAILS)
        so = self.builtin.get_variable_value(self.SO_DETAILS)
        body_result = self.builtin.get_variable_value(self.APPSETUP_DETAILS)
        currency = body_result['CURRENCY_SETTING']
        if dn:
            self.verify_product_column_and_value(prd_code, "Price", selling_price)
            self.verify_product_column_and_value(prd_code, "Amount ({0})".format(currency), gross)
            self.verify_product_column_and_value(prd_code, "Tax Value ({0})".format(currency), tax_amt)
            self.verify_product_column_and_value(prd_code, "Net Amount ({0})".format(currency), net_amt)
        elif cn:
            self.verify_product_column_and_value(prd_code, "Price ({0})".format(currency), selling_price)
            self.verify_product_column_and_value(prd_code, "Cust Discount ({0})".format(currency), cust_disc)
            self.verify_product_column_and_value(prd_code, self.GROSS_CURRENCY.format(currency), gross)
            self.verify_product_column_and_value(prd_code, self.TAX_CURRENCY.format(currency), tax_amt)
            self.verify_product_column_and_value(prd_code, self.NET_CURRENCY.format(currency), net_amt)
        elif rtn:
            self.verify_product_column_and_value(prd_code, "Suggested Price ({0})".format(currency), selling_price)
            self.verify_product_column_and_value(prd_code, "Promo Discount ({0})".format(currency), promo_disc)
            self.verify_product_column_and_value(prd_code, "Cust Discount ({0})".format(currency), cust_disc)
            self.verify_product_column_and_value(prd_code, self.GROSS_CURRENCY.format(currency), gross)
            self.verify_product_column_and_value(prd_code, self.TAX_CURRENCY.format(currency), tax_amt)
            self.verify_product_column_and_value(prd_code, self.NET_CURRENCY.format(currency), net_amt)
        elif inv:
            self.verify_product_column_and_value(prd_code, "Selling Price ({0})".format(currency), selling_price)
            self.verify_product_column_and_value(prd_code, "Promo Discount ({0})".format(currency), promo_disc)
            self.verify_product_column_and_value(prd_code, "Other Discount ({0})".format(currency), cust_disc)
            self.verify_product_column_and_value(prd_code, "Gross Amt. ({0})".format(currency), gross)
            self.verify_product_column_and_value(prd_code, "Tax Amt. ({0})".format(currency), tax_amt)
            self.verify_product_column_and_value(prd_code, "Net Amt. ({0})".format(currency), net_amt)
        elif so:
            self.verify_product_column_and_value(prd_code, "Selling Price ({0})".format(currency), selling_price)
            self.verify_product_column_and_value(prd_code, "Promo Discount ({0})".format(currency), promo_disc)
            self.verify_product_column_and_value(prd_code, "Other Discount ({0})".format(currency), cust_disc)
            self.verify_product_column_and_value(prd_code, "Gross Amt. ({0})".format(currency), gross)
            self.verify_product_column_and_value(prd_code, "Tax Amt. ({0})".format(currency), tax_amt)
            self.verify_product_column_and_value(prd_code, "Net Amt. ({0})".format(currency), net_amt)
        else:
            self.verify_product_column_and_value(prd_code, "Selling Price", selling_price)
            self.verify_product_column_and_value(prd_code, "Promotion Discount", promo_disc)
            self.verify_product_column_and_value(prd_code, "Cash Discount", cust_disc)
            self.verify_product_column_and_value(prd_code, "Gross", gross)
            self.verify_product_column_and_value(prd_code, "Tax", tax_amt)
            self.verify_product_column_and_value(prd_code, "Net", net_amt)
        summary_amount = self.builtin.get_variable_value(self.SUMMARY_AMT)
        summary_amount['TTL_GROSS'] = summary_amount['TTL_GROSS'] + calculation['GROSS_AMT']
        summary_amount['TTL_DISC'] = summary_amount['TTL_DISC'] + calculation['PROMO_DISC']
        summary_amount['TTL_DISC'] = summary_amount['TTL_DISC'] + calculation['CUST_DISC']
        summary_amount['TTL_TAX'] = summary_amount['TTL_TAX'] + calculation['TOTAL_TAX']
        summary_amount['TTL_NET'] = summary_amount['TTL_NET'] + calculation['NET_TTL_TAX']
        self.builtin.set_test_variable(self.SUMMARY_AMT, summary_amount)

    def calculation_total_verification(self):
        summary_amount = self.builtin.get_variable_value(self.SUMMARY_AMT)
        round_amt = TransactionFormula.TransactionFormula().rounding_based_on_setup(summary_amount['TTL_NET'])
        summary_amount["TTL_GROSS"] = self.verify_summary_amt(self.locator.TranSummaryLabel, self.locator.TranSummaryAmt, "Gross Amount", summary_amount["TTL_GROSS"])

        summary_amount["TTL_TAX"] = self.verify_summary_amt(self.locator.TranSummaryLabel, self.locator.TranSummaryAmt, "Tax Amount", summary_amount["TTL_TAX"])
        rtn = self.builtin.get_variable_value(self.RTN_DETAILS)
        cn = self.builtin.get_variable_value(self.CN_DETAILS)
        dn = self.builtin.get_variable_value(self.DN_DETAILS)
        if rtn or cn:
            summary_amount["TTL_DISC"] = self.verify_summary_amt(self.locator.TranSummaryLabel,
                                                                 self.locator.TranSummaryAmt, "Discount Amount",
                                                                 summary_amount["TTL_DISC"])
        if rtn or cn or dn:
            summary_amount["ROUND_OFF"] = self.verify_summary_amt(self.locator.TranSummaryLabel,
                                                                  self.locator.TranSummaryAmt, "Adjustment Amount",
                                                                  round_amt[1])
        else:
            summary_amount["ROUND_OFF"] = self.verify_summary_amt(self.locator.TranSummaryLabel,
                                                                  self.locator.TranSummaryAmt, "Round Off",
                                                                  round_amt[1])
        summary_amount["TTL_NET"] = self.verify_summary_amt(self.locator.TranSummaryLabel, self.locator.TranSummaryAmt,
                                                            "Net Amount", round_amt[0])
        print("AMOUNT CHECKING CORRECT!", summary_amount)

    def round_decimal_to_display_in_ui(self, num):
        body_result = self.builtin.get_variable_value(self.APPSETUP_DETAILS)
        round_decimal_display = body_result['ROUND_OFF_DECIMAL_DISPLAY']['ROUND_OFF_DECIMAL_DISPLAY']
        return format(float(num), ".{0}f".format(int(round_decimal_display)))

    @keyword("user verify Product: ${prd}, Column: ${col}, Value: ${value}")
    def verify_product_column_and_value(self, prd, column, value):
        print("Verification proc col and value")
        col_value = self.validate_product_details_value(prd, column)
        print('COL VALUE :', col_value)
        print("{0}:{1}={2}".format(column, value, col_value))
        assert value == col_value, "{0} Value not match".format(column)

    def validate_product_details_value(self, prd, column):
        count = self.selib.get_element_count("//th")
        current_count = 0
        for i in range(0, count):
            i = i + 1
            text = self.selib.get_text("//th[{0}]".format(i))
            if text == column:
                current_count = i
                break
        column_value = self.selib.get_text(
            "//*[text()='{0}']/ancestor::*[4][@role='row']//td[{1}]".format(prd, current_count))
        body_result = self.builtin.get_variable_value(self.APPSETUP_DETAILS)
        if column_value == body_result['CURRENCY_SETTING'] or column_value == "":
            column_value = self.selib.get_value(
                "//*[text()='{0}']/ancestor::*[4][@role='row']//td[{1}]//input".format(prd, current_count))
        if column_value == '0':
            column_value = '%.2f' % TransactionFormula.TransactionFormula().round_half_up(column_value, 2)
        return column_value

    def verify_summary_amt(self, label_locator, amt_locator, column, value):
        so = self.builtin.get_variable_value(self.SO_DETAILS)
        inv = self.builtin.get_variable_value(self.INV_DETAILS)
        summary = self.selib.get_webelements(label_locator)
        current_count = 0
        for item in summary:
            current_count = current_count + 1
            text = self.selib.get_text(item)
            if text.strip() == column:
                print("{0}={1}".format(column, value))
                break
        if so is not None or inv is not None:
            if column == "Tax Amount":
                current_count = 2
                column_value = self.selib.get_text("{0}[{1}]".format(amt_locator, current_count))
            elif column == "Round Off":
                current_count = 3
                column_value = self.selib.get_text("{0}[{1}]".format(amt_locator, current_count))
            elif column == "Net Amount":
                current_count = 4
                column_value = self.selib.get_text("{0}[{1}]".format(amt_locator, current_count))
            else:
                column_value = self.selib.get_text("{0}[{1}]".format(amt_locator, current_count))
        else:
            column_value = self.selib.get_text("{0}[{1}]".format(amt_locator, current_count))
        body_result = self.builtin.get_variable_value(self.APPSETUP_DETAILS)
        currency = body_result['CURRENCY_SETTING'] + " "
        column_value = column_value.replace(currency, "")
        value = self.round_decimal_to_display_in_ui(value)
        print("column value:", float(column_value))
        print("value:", float(value))
        assert float(column_value) == float(value), "Summary not match"
        return value

    @keyword("verifies product ${prd_type} saved in ${trx_type} database correctly")
    def verifies_product_saved_in_database_correctly(self, prd_type, trx_type):
        today_date = datetime.datetime.today().strftime("%Y-%m-%d")
        user = self.builtin.get_variable_value("${user_role}")
        user_data = TokenAccess.TokenAccess().user_logins_web(user)
        print("today date: ", today_date)
        HanaDB.HanaDB().connect_database_to_environment()
        if trx_type == "order":
            get_detail = "${fixedData}"
            result_id = HanaDB.HanaDB().fetch_one_record("SELECT CAST(ID AS varchar) FROM TXN_ORDHDR "
                                                        "WHERE TXN_DT = '{0}' AND CREATED_BY = '{1}' " \
                                                        "ORDER BY TXN_CREATED_DT DESC".format(today_date, user_data[0]))
            result_prd = HanaDB.HanaDB().fetch_all_record("SELECT CAST(PRD_ID as varchar),CAST(PRD_INDEX as varchar) " \
                                                        "FROM TXN_ORDPRD WHERE TXN_ID = '{0}' "
                                                        "ORDER BY PRD_INDEX ASC".format(result_id))
            tax_details = HanaDB.HanaDB().fetch_all_record("SELECT CAST(PRD_ID as VARCHAR),CAST(TAX_ID as VARCHAR), "
                                                           "CAST(TAX_AMT as VARCHAR), CAST(TAX_PERC as VARCHAR), "
                                                           "CAST(TAXABLE_AMT as VARCHAR) FROM TXN_ORDPRD_TAX "
                                                           "WHERE TXN_ID = '{0}'".format(result_id))
        elif trx_type == "invoice":
            get_detail = "${InvDetails}"
            result_id = HanaDB.HanaDB().fetch_one_record("SELECT CAST(ID AS varchar) FROM TXN_INVOICE "
                                                        "WHERE INV_DT = '{0}' "
                                                        "ORDER BY CREATED_DATE DESC".format(today_date))
            result_prd = HanaDB.HanaDB().fetch_all_record("SELECT CAST(PRD_ID as varchar),CAST(PRD_INDEX as varchar) " \
                                                        "FROM TXN_INVDTL WHERE TXN_ID = '{0}' "
                                                        "ORDER BY PRD_INDEX ASC".format(result_id))
            tax_details = HanaDB.HanaDB().fetch_all_record("SELECT CAST(PRD_ID as VARCHAR),CAST(TAX_ID as VARCHAR), "
                                                           "CAST(TAX_AMT as VARCHAR), CAST(TAX_PERC as VARCHAR), "
                                                           "CAST(TAXABLE_AMT as VARCHAR) FROM TXN_INVDTL_TAX "
                                                           "WHERE TXN_ID = '{0}'".format(result_id))
        elif trx_type == 'debit note':
            get_detail = self.DN_DETAILS
            result_id = HanaDB.HanaDB().fetch_one_record("SELECT CAST(ID AS varchar) FROM TXN_DBN "
                                                         "WHERE TXN_DT = '{0}' " \
                                                         "ORDER BY CREATED_DATE DESC".format(today_date,))
            result_prd = HanaDB.HanaDB().fetch_all_record("SELECT CAST(PRD_ID as varchar),CAST(PRD_INDEX as varchar) " \
                                                          "FROM TXN_DBNPRD WHERE TXN_ID = '{0}' "
                                                          "ORDER BY PRD_INDEX ASC".format(result_id))
            tax_details = HanaDB.HanaDB().fetch_all_record("SELECT CAST(PRD_ID as VARCHAR),CAST(TAX_ID as VARCHAR), "
                                                           "CAST(TAX_AMT as VARCHAR), CAST(TAX_PERC as VARCHAR), "
                                                           "CAST(TAXABLE_AMT as VARCHAR) FROM TXN_DBNPRD_TAX "
                                                           "WHERE TXN_ID = '{0}'".format(result_id))
        elif trx_type == 'return' or trx_type == 'credit note':
            txn_type = "CNP"
            get_detail = self.CN_DETAILS
            if trx_type == 'return':
                txn_type = "RTN"
                get_detail = self.RTN_DETAILS
            result_id = HanaDB.HanaDB().fetch_one_record("SELECT CAST(ID AS varchar) FROM TXN_NOTEHDR "
                                                             "WHERE TXN_TYPE = '{0}' "
                                                             "ORDER BY CREATED_DATE DESC".format(txn_type))
            result_prd = HanaDB.HanaDB().fetch_all_record("SELECT CAST(PRD_ID as varchar),CAST(PRD_INDEX as varchar) " \
                                                          "FROM TXN_NOTEPRD WHERE TXN_ID = '{0}' "
                                                          "ORDER BY PRD_INDEX ASC".format(result_id))
            tax_details = HanaDB.HanaDB().fetch_all_record("SELECT CAST(PRD_ID as VARCHAR),CAST(TAX_ID as VARCHAR), "
                                                           "CAST(TAX_AMT as VARCHAR), CAST(TAX_PERC as VARCHAR), "
                                                           "CAST(TAXABLE_AMT as VARCHAR) FROM TXN_NOTEPRD_TAX "
                                                           "WHERE TXN_ID = '{0}'".format(result_id))

        HanaDB.HanaDB().disconnect_from_database()
        self.tax_details_checking_in_db(get_detail, result_prd, tax_details)

    def tax_details_checking_in_db(self, get_detail, result_prd, tax_details):
        details = self.builtin.get_variable_value(get_detail)
        print("GET PROD DETAILS TO CHECK", details)
        no_prod = len(details['PROD_ASS_DETAILS'])
        prod_count = 1
        for item in details['PROD_ASS_DETAILS']:
            for j in result_prd:
                prd_id = COMMON_KEY.convert_id_to_string(item['PRD_ID'])
                if prd_id == j[0]:
                    assert j[1] == str(prod_count), "Product index stored incorrectly"
                    print("MATCHED!")
                    prod_count = prod_count + 1
                    break
        assert no_prod == len(result_prd)

        for item in details['PROD_ASS_DETAILS']:
            for j in tax_details:
                prd_id = COMMON_KEY.convert_id_to_string(item['PRD_ID'])
                if prd_id == j[0]:
                    tax_set = COMMON_KEY.convert_id_to_string(item['TAX_SETTING']['ID'])
                    assert j[1] == tax_set, "Tax Setting storing incorrectly"
                    assert j[2] == '%.6f' % float(item['TOTAL_TAX']), "Tax Amount storing incorrectly"
                    assert j[3] == '%.6f' % float(item['TAX_SETTING']['TAX_RATE']), "Tax Percentage storing incorrectly"
                    assert j[4] == '%.6f' % float(item['TAXABLE_AMT']), "Taxable amount storing incorrectly"
                    print("MATCHED!")
                    prod_count = prod_count + 1
                    break
