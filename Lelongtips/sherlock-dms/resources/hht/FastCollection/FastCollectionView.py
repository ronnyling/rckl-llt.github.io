import re
import decimal

from robot.api.deco import keyword
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from datetime import datetime
current_date = datetime.today().strftime('%d/%m/%Y')


class FastCollectionView(POMLibrary):
    _locators = {
        "delivery_button": "//android.widget.Button[@resource-id='DLG_CustROOT.GRID_CustList_Delivery.{0}.BBTN_Visit']",
        "fast_collection": "//android.widget.Button[@resource-id='DLG_SOC_Phone.GRID_SOC.{0}.BBTN_Txn']",
        "completion_status": "//android.view.View[@resource-id='DLG_SOC_Phone.GRID_SOC.{0}.LBL_Completion_Status'",
        "total_pay_amount": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_TotalPayAmt']",
        "outstanding_amount_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_OutstandingAmt_T']",
        "outstanding_amount": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_OutstandingAmt']",
        "adjustment_amount_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_AdjAmt_T']",
        "adjustment_amount": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_AdjAmt']",
        "receipt_no_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_RecepitNo_T']",
        "receipt_no": "//android.widget.EditText[@resource-id='DLG_Delivery_Collection.EDIT_ReceiptNo']",
        "cash_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_Cash_T']",
        "full_cash_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.BBTN_FullCash']",
        "cash": "//android.widget.EditText[@resource-id='DLG_Delivery_Collection.EDIT_Cash']",
        "cheque_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_Cheque_T']",
        "cheque_add_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.BBTN_AddCheque']",
        "cheque_record": "//android.view.View[@resource-id='DLG_Delivery_Collection.GRID_Cheque']",
        "bank_transfer_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_BankTransfer_T']",
        "bank_transfer_add_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.BBTN_AddBank']",
        "bank_transfer_record": "//android.view.View[@resource-id='DLG_Delivery_Collection.GRID_BankTransfer']",
        "ewallet_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_EWallet_T']",
        "ewallet_add_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.BBTN_AddEWallet']",
        "ewallet_label_record": "//android.view.View[@resource-id='DLG_Delivery_Collection.GRID_EWallet']",
        "total_paid_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_TtlPaid_T']",
        "total_paid": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_TtlPaid']",
        "balance_to_pay_label": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_BalToPay_T']",
        "balance_to_pay": "//android.view.View[@resource-id='DLG_Delivery_Collection.LBL_BalToPay']",
        "save_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.BBTN_Save']",
        "customer_list": "//android.view.View[@resource-id='DLG_CustROOT.GRID_CustList_Delivery']",
        "customer_name": "//android.view.View[@resource-id='DLG_CustROOT.GRID_CustList_Delivery.{0}.LBL_CustName']",
        "yes_button": "//android.widget.Button[@text='Yes']",
        "time_in_popup": "//android.view.View[contains(@text,'Visit again')]"
    }

    @keyword('user navigates to fast collection page for customer no:${cust_no}')
    def navigate_to_fast_collection(self, cust_no):
        cust_no = int(cust_no)-1
        self.applib().wait_until_page_contains_element(self.locator.delivery_button.format(cust_no))
        self.applib().click_element(self.locator.delivery_button.format(cust_no))
        time_in_popup = self.builtin.run_keyword_and_return_status(
            "Wait Until Page Contains Element", self.locator.time_in_msg)
        if time_in_popup:
            print("got inside pop")
            self.applib().click_element(self.locator.yes_button)
        else:
            print("no inside pop")
            self.applib().click_element(self.locator.yes_button)

        self.applib().wait_until_page_contains_element(self.locator.fast_collection.format("2"))
        self.applib().click_element(self.locator.fast_collection.format("2"))

    def select_customer_to_visit(self, customer_name):
        self.applib().wait_until_page_contains_element(self.locator.customer_list)
        cust_list_num = (self.applib().get_matching_xpath_count(self.locator.customer_list))
        cust_list_num = int(cust_list_num)

        for x in range(0, cust_list_num):
            c_locator = self.locator.customer_name.format(x)
            cust_name = self.applib().get_text(c_locator)
            if cust_name == customer_name:
                selected_cust = x
                break
        self.applib().wait_until_page_contains_element(self.locator.delivery_button.format(selected_cust))
        self.applib().click_element(self.locator.delivery_button.format(selected_cust))

    def validate_element_in_fast_collection_page(self):
        self.applib().wait_until_page_contains_element(self.locator.total_pay_amount)
        self.applib().wait_until_page_contains_element(self.locator.outstanding_amount_label)
        self.applib().wait_until_page_contains_element(self.locator.outstanding_amount)
        self.applib().wait_until_page_contains_element(self.locator.adjustment_amount_label)
        self.applib().wait_until_page_contains_element(self.locator.adjustment_amount)
        self.applib().wait_until_page_contains_element(self.locator.receipt_no_label)
        self.applib().wait_until_page_contains_element(self.locator.receipt_no)
        self.applib().wait_until_page_contains_element(self.locator.cash_label)
        self.applib().wait_until_page_contains_element(self.locator.full_cash_button)
        self.applib().wait_until_page_contains_element(self.locator.cash)
        self.applib().wait_until_page_contains_element(self.locator.cheque_label)
        self.applib().wait_until_page_contains_element(self.locator.cheque_button)
        self.applib().wait_until_page_contains_element(self.locator.cheque_record)
        self.applib().wait_until_page_contains_element(self.locator.bank_transfer_label)
        self.applib().wait_until_page_contains_element(self.locator.bank_transfer_button)
        self.applib().wait_until_page_contains_element(self.locator.bank_transfer_record)
        self.applib().wait_until_page_contains_element(self.locator.ewallet_label)
        self.applib().wait_until_page_contains_element(self.locator.ewallet_add_button)
        self.applib().wait_until_page_contains_element(self.locator.ewallet_label_record)
        self.applib().wait_until_page_contains_element(self.locator.total_paid_label)
        self.applib().wait_until_page_contains_element(self.locator.total_paid)
        self.applib().wait_until_page_contains_element(self.locator.balance_to_pay_label)
        self.applib().wait_until_page_contains_element(self.locator.balance_to_pay)
        self.applib().wait_until_page_contains_element(self.locator.save_button)

    def validate_collectable_amount(self):
        self.applib().wait_until_page_contains_element(self.locator.total_pay_amount)
        ttl_pay_amt = self.applib().get_text(self.locator.total_pay_amount)
        ttl_pay_amt = self.convert_string_amount_to_decimal(ttl_pay_amt)
        out_amt = self.applib().get_text(self.locator.outstanding_amount)
        out_amt = self.convert_string_amount_to_decimal(out_amt)
        adj_amt = self.applib().get_text(self.locator.adjustment_amount)
        adj_amt = self.convert_string_amount_to_decimal(adj_amt)
        if ttl_pay_amt != out_amt - adj_amt:
            raise ValueError("Total Collectable Amount should be outstanding amount deduct adjustment amount")

    def convert_string_amount_to_decimal(self, amount):
        amount = re.sub("[^\d\.]", "", amount)
        return decimal.Decimal(amount)
