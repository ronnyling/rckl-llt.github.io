import secrets

from robot.api.deco import keyword
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime
from resources.hht.FastCollection.FastCollectionView import FastCollectionView
from resources.Common import Common
from setup.sqllite.SQLLite import SQLLite


current_date = datetime.today().strftime('%d/%m/%Y')


class FastCollectionCreate(POMLibrary):
    _locators = {
        "cheque_no": "//android.widget.EditText[@resource-id='DLG_Delivery_AddPayment.EDIT_ChequeNo']",
        "payment_transfer_amount": "//android.widget.EditText[@resource-id='DLG_Delivery_AddPayment.EDIT_TrfAmt']",
        "payment_transfer_date": "//android.view.View[@resource-id='DLG_Delivery_AddPayment.DATE_TrfDate']",
        "bank": "//android.view.View[@resource-id='DLG_Delivery_AddPayment.CBOX_Bank']",
        "payment_save_button": "//android.widget.Button[@resource-id='DLG_Delivery_AddPayment.BBTN_Save']",
        "transfer_no": "//android.widget.EditText[@resource-id='DLG_Delivery_AddPayment.EDIT_TrfNo']",
        "ewallet_next_button": "//android.widget.Button[@resource-id='DLG_Delivery_EWallet_QR.BBTN_Next']",
        "ewallet_save_button": "//android.widget.Button[@resource-id='DLG_Delivery_AddPayment.CBOX_Bank']",
        "ewallet": "//android.view.View[@resource-id='DLG_Delivery_AddEWallet.CBOX_EWallet']",
        "ewallet_transfer_amount": "//android.widget.EditText[@resource-id='DLG_Delivery_AddEWallet.EDIT_TrfAmt']",
        "ewallet_transfer_date": "//android.view.View[@resource-id='DLG_Delivery_AddEWallet.DATE_TrfDate']",
        "ewallet_reference_no": "//android.widget.EditText[@resource-id='DLG_Delivery_AddEWallet.EDIT_RefNo']",
        "ewallet_take_image_button": "//android.widget.Button[@resource-id='DLG_Delivery_AddEWallet.BTN_TakeEWalletImage']",
        "android_take_image_button": "//android.widget.ImageView[@resource-id='com.android.camera2:id/shutter_button']",
        "android_done_button": "//android.widget.ImageView[@resource-id='com.android.camera2:id/done_button']",
        "collection_save_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.BBTN_Save']",
        "cheque_delete_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.GRID_Cheque.{0}.BBTN_Delete']",
        "bank_transfer_delete_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.GRID_BankTransfer.{0}.BBTN_Delete']",
        "ewallet_delete_button": "//android.widget.Button[@resource-id='DLG_Delivery_Collection.GRID_EWallet.{0}.BBTN_Delete']",
        "end_visit_button": "//android.widget.Button[@resource-id='DLG_SOC_Phone.BBTN_EndVisit']",
        "cust_code": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_CustCode']",
        "signature": "//android.view.View[@resource-id='DLG_Signature.SIGN']",
        "signature_done": "//android.widget.Button[@resource-id='DLG_Signature.BTN_Done']"
    }

    @keyword('user ${action} fast collection')
    def create_fast_collection(self, action):
        self.applib().wait_until_page_contains_element(FastCollectionView().locator.total_pay_amount)
        ttl_pay_amt = self.applib().get_text(FastCollectionView().locator.total_pay_amount)
        ttl_pay_amt = FastCollectionView().convert_string_amount_to_decimal(ttl_pay_amt)
        paid_amt = secrets.randbelow(100)
        if paid_amt == 0:
            paid_amt = 1
        print("Amount paid = ", paid_amt)
        rand_receipt_no = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        Common().wait_keyword_success("input_text", FastCollectionView().locator.receipt_no, rand_receipt_no)
        Common().wait_keyword_success("input_text", FastCollectionView().locator.cash, paid_amt)
        self.applib().click_element(FastCollectionView().locator.save_button)
        self.create_signature()

    def fast_collection_saved(self):
        self.applib().wait_until_page_contains_element(FastCollectionView().locator.fast_collection.format('2'))
        print("Fast Collection saved")

    def validates_fast_collect(self):
        cust_code = self.applib().get_text(self.locator.cust_code)
        cust_code = cust_code.replace('(', '')
        cust_code = cust_code.replace(')', '')
        cust_code = cust_code.replace(' ', '')
        cust_id = SQLLite().fetch_one_record("select ID from M_CUST where CUST_CD = '{0}'".format(cust_code))
        col_id = SQLLite().fetch_one_record("select ID from TXN_DELIVERY_COLHDR WHERE CUST_ID = '{0}' AND "
                                            "COMMS_STATUS = 'H'".format(cust_id))
        BuiltIn().set_test_variable("${col_id}", col_id)
        fast_collect = SQLLite().fetch_one_record("select FAST_COLLECT from TXN_DELIVERY_COLHDR WHERE CUST_ID = '{0}' AND "
                                                  "COMMS_STATUS = 'H'".format(cust_id))
        if fast_collect is False:
            raise ValueError("FAST_COLLECT should be TRUE")

    @keyword('user adds ${type} payment')
    def add_payment(self, type):
        if type == "cheque":
            add_button_locator = FastCollectionView().locator.cheque_add_button
        elif type == "bank transfer":
            add_button_locator = FastCollectionView().locator.bank_transfer_add_button
        elif type == "ewallet":
            add_button_locator = FastCollectionView().locator.ewallet_add_button
        else:
            raise ValueError("Invalid payment type")
        self.applib().wait_until_page_contains_element(add_button_locator)
        self.applib().click_element(add_button_locator)

        rand_no = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        rand_amount = secrets.randbelow(100)
        Common().wait_keyword_success("input_text", self.locator.cheque_no, rand_no)
        Common().wait_keyword_success("input_text", self.locator.payment_transfer_amount, rand_amount)

        self.applib().click_element(self.locator.payment_save_button)

    def remove_payment(self, type, no):
        if type == "cheque":
            delete_button_locator = self.locator.cheque_delete_button.format(no)
        elif type == "bank transfer":
            delete_button_locator = self.locator.bank_transfer_delete_button.format(no)
        elif type == "ewallet":
            delete_button_locator = self.locator.ewallet_delete_button.format(no)
        else:
            raise ValueError("Invalid payment type")
        self.applib().wait_until_page_contains_element(delete_button_locator)
        self.applib().click_element(delete_button_locator)

    def validates_fast_collection_completion_status(self):
        self.applib().wait_until_page_contains_element(FastCollectionView().locator.completion_status.format(2))
        print("Fast Collection completion status shown")

    @keyword('user ends visit')
    def end_visit(self):
        self.applib().wait_until_page_contains_element(self.locator.end_visit_button)
        self.applib().click_element(self.locator.end_visit_button)

    def create_signature(self):
        self.applib().click_element(self.locator.signature)
        self.applib().click_element(self.locator.signature_done)
