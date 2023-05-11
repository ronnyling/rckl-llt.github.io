from robot.api.deco import keyword
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
import datetime
from setup.sqllite.SQLLite import SQLLite


class ActionForYou(POMLibrary):
    _locators = {
        "delivery_button": "//android.widget.Button[@resource-id='DLG_CustROOT.GRID_CustList_Delivery.{0}.BBTN_Visit']",
        "collapse_action": "//android.widget.Button[@resource-id='DLG_Cust_TimeIn.BBTN_CollapseActions']",
        "cust_code": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_CustCode']",
        "delivery_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_DeliveryValue']",
        "delivery_open_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_OpenValue']",
        "delivery_delivered_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_DeliveredValue']",
        "delivery_rejected_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_RejectedValue']",
        "return_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_ReturnValue']",
        "return_open_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Return_OpenValue']",
        "return_collected_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Return_CollectedValue']",
        "return_cancelled_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Return_CancelledValue']",
        "col_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_CollectionValue']",
        "col_outstanding": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Col_OutstandingAmtValue']",
        "provisional_inv": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Col_ProvisionalInvValue']",
        "provisional_ret": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Col_ProvisionalReturnValue']",
        "total_value": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Collection_TotalValue']",
        "paid_amt": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Collection_PaidAmtValue']",
        "balance": "//android.view.View[@resource-id='DLG_Cust_TimeIn.LBL_Delivery_Collection_BalanceValue']"
    }


    @keyword('user navigates to action for you for customer no:${cust_no}')
    def navigates_to_action_for_you(self, cust_no):
        cust_no = int(cust_no) - 1
        self.applib().wait_until_page_contains_element(self.locator.delivery_button.format(cust_no))
        self.applib().click_element(self.locator.delivery_button.format(cust_no))

        self.applib().wait_until_page_contains_element(self.locator.collapse_action)
        self.applib().click_element(self.locator.collapse_action)

    @keyword('validate data shown correctly')
    def check_data(self):
        cust_code = self.applib().get_text(self.locator.cust_code)
        cust_code = cust_code.replace('(', '')
        cust_code = cust_code.replace(')', '')
        cust_code = cust_code.replace(' ', '')
        app_data_list = self.get_data()
        db_data_list = self.get_data_from_db(cust_code)
        print("app list = ", app_data_list)
        print("db_list = ", db_data_list)
        print("len is = ", len(app_data_list))
        for x in range(len(app_data_list)):
            print("app = ", app_data_list[x])
            print("db = ", db_data_list[x])
            if app_data_list[x] != db_data_list[x]:
                raise ValueError("Data not same")


    def get_data(self):
        self.builtin.run_keyword_and_return_status("Wait Until Page Contains Element", self.locator.delivery_value)
        delivery_value = self.applib().get_text(self.locator.delivery_value)
        delivery_open_value = self.applib().get_text(self.locator.delivery_open_value)
        delivery_delivered_value = self.applib().get_text(self.locator.delivery_delivered_value)
        delivery_rejected_value = self.applib().get_text(self.locator.delivery_rejected_value)
        return_value = self.applib().get_text(self.locator.return_value)
        return_open_value = self.applib().get_text(self.locator.return_open_value)
        return_collected_value = self.applib().get_text(self.locator.return_collected_value)
        return_cancelled_value = self.applib().get_text(self.locator.return_cancelled_value)
        col_value = self.remove_comma_from_string(self.applib().get_text(self.locator.col_value))
        col_outstanding = self.remove_comma_from_string(self.applib().get_text(self.locator.col_outstanding))
        provisional_inv = self.remove_comma_from_string(self.applib().get_text(self.locator.provisional_inv))
        provisional_ret = self.remove_comma_from_string(self.applib().get_text(self.locator.provisional_ret))
        total_value = self.remove_comma_from_string(self.applib().get_text(self.locator.total_value))
        paid_amt = self.remove_comma_from_string(self.applib().get_text(self.locator.paid_amt))
        balance = self.remove_comma_from_string(self.applib().get_text(self.locator.balance))

        print("delivery value is = ", delivery_value)
        print("delivery_open_value is = ", delivery_open_value)
        print("delivery_delivered_value is = ", delivery_delivered_value)
        print("delivery_rejected_value is = ", delivery_rejected_value)
        print("return_value is = ", return_value)
        print("return_open_value is = ", return_open_value)
        print("return_collected_value is = ", return_collected_value)
        print("return_cancelled_value is = ", return_cancelled_value)
        print("col_value is = ", col_value)
        print("col_outstanding is = ", col_outstanding)
        print("provisional_inv is = ", provisional_inv)
        print("provisional_ret is = ", provisional_ret)
        print("total_value is = ", total_value)
        print("paid_amt is = ", paid_amt)
        print("balance is = ", balance)
        data_list = [
            delivery_value, delivery_open_value, delivery_delivered_value, delivery_rejected_value,
            return_value, return_open_value, return_collected_value, return_cancelled_value,
            col_value, col_outstanding, provisional_inv, provisional_ret, total_value, paid_amt, balance
        ]
        print("data list in app = ", data_list)
        return data_list

    def remove_comma_from_string(self, string):
        string = string.replace(',', '')
        return string


    def get_data_from_db(self, cust_code):
        cust_id = SQLLite().fetch_one_record("select ID from M_CUST where CUST_CD = '{0}'".format(cust_code))
        print("cust_id = ", cust_id)
        ttl_inv = self.fetch_record_count_from_db("select COUNT(M_INVOICE.ID) from W_PICKLIST, M_PICKLIST_CUSTINV, "
                                                  "M_INVOICE where W_PICKLIST.ID = M_PICKLIST_CUSTINV.PICKLIST_ID AND "
                                                  "M_PICKLIST_CUSTINV.INV_ID = M_INVOICE.ID AND "
                                                  "W_PICKLIST.DELIVERY_STATUS = 'D' AND M_PICKLIST_CUSTINV.CUST_ID = "
                                                  "'{0}'".format(cust_id))
        delivery_query = "select COUNT(TXN_DELIVERY_INV.ID) from TXN_DELIVERY_INV, W_PICKLIST, M_PICKLIST_CUSTINV where " \
                         "TXN_DELIVERY_INV.INV_ID = M_PICKLIST_CUSTINV.INV_ID AND TXN_DELIVERY_INV.PICKLIST_ID = " \
                         "W_PICKLIST.ID AND TXN_DELIVERY_INV.DELIVERY_STATUS = '{0}' AND W_PICKLIST.DELIVERY_STATUS = " \
                         "'D' AND M_PICKLIST_CUSTINV.CUST_ID = '{1}'"
        del_inv = self.fetch_record_count_from_db(delivery_query.format('S', cust_id))
        rejected_inv = self.fetch_record_count_from_db(delivery_query.format('R', cust_id))
        processed_inv = del_inv + rejected_inv
        open_inv = ttl_inv - processed_inv
        inv_record = "{0}/{1}".format(processed_inv, ttl_inv)
        print("inv record is = ", inv_record)
        print("open = ", open_inv)
        print("del = ", del_inv)
        print("ref = ", rejected_inv)

        return_query = "select COUNT(ID) from M_NOTEHDR where STATUS = '{0}' AND CUST_ID = '{1}'"
        open_ret = self.fetch_record_count_from_db(return_query.format('D', cust_id))
        collected_ret = self.fetch_record_count_from_db(return_query.format('S', cust_id))
        cancelled_ret = self.fetch_record_count_from_db(return_query.format('C', cust_id))
        ttl_ret = open_ret + collected_ret + cancelled_ret
        processed_ret = collected_ret + cancelled_ret
        ret_record = "{0}/{1}".format(processed_ret, ttl_ret)
        print("ret record is = ", ret_record)
        print("open = ", open_ret)
        print("col = ", collected_ret)
        print("can = ", cancelled_ret)

        currency = SQLLite().fetch_one_record("select FIELD_VALUE from M_SETUP_APP where FIELD = 'CURRENCY_SETTING'")
        cust_out_amt = SQLLite().fetch_one_record("select OUT_AMT from M_DEL_CUSTOUTSTAND_AMT where CUST_ID = '{0}' "
                                                  "AND PRIME_FLAG = '{1}'".format(cust_id, "PRIME"))

        cust_out_amt = float("{:.2f}".format(cust_out_amt))
        print("cust out amt = ", cust_out_amt)
        pro_inv = SQLLite().fetch_one_record("select SUM(TXN_DELIVERY_INVOICE.NET_TTL_TAX + TXN_DELIVERY_INVOICE.ADJ_AMT) "
                                             "from TXN_DELIVERY_INV, W_PICKLIST, M_PICKLIST_CUSTINV, TXN_DELIVERY_INVOICE "
                                             "where TXN_DELIVERY_INV.INV_ID = M_PICKLIST_CUSTINV.INV_ID AND "
                                             "TXN_DELIVERY_INV.PICKLIST_ID = W_PICKLIST.ID AND TXN_DELIVERY_INVOICE.ID "
                                             "= TXN_DELIVERY_INV.INV_ID AND TXN_DELIVERY_INV.DELIVERY_STATUS = 'S' "
                                             "AND W_PICKLIST.DELIVERY_STATUS = 'D' AND M_PICKLIST_CUSTINV.CUST_ID = "
                                             "'{0}'".format(cust_id))
        if pro_inv is None:
            pro_inv = 0.00
        else:
            pro_inv = '%.2f' % pro_inv
        print("pro inv = ", pro_inv)
        pro_ret = SQLLite().fetch_one_record("select SUM(NET_TTL_TAX+ ADJ_AMT) from M_NOTEHDR where STATUS = 'S' AND "
                                             "CUST_ID = '{0}'".format(cust_id))
        if pro_ret is None:
            pro_ret = 0.00
        else:
            pro_ret = '%.2f' % pro_ret
        print("pro ret = ", pro_ret)
        paid_amt = SQLLite().fetch_one_record("select TTL_SETTLEAMT from TXN_DELIVERY_COLHDR WHERE COMMS_STATUS = 'H' "
                                              "AND CUST_ID = '{0}'".format(cust_id))

        print("paid = ", paid_amt)
        total = (cust_out_amt + pro_inv) - pro_ret
        total = float("{:.2f}".format(total))
        balance = total - paid_amt
        balance = float("{:.2f}".format(balance))
        fc_record = "{0}{1}".format(currency, balance)
        print("fc record is = ", fc_record)
        print("out = ", cust_out_amt)
        print("pro inv = ", pro_inv)
        print("pro ret = ", pro_ret)
        print("total = ", total)
        print("paid = ", paid_amt)
        print("balance = ", balance)

        data_list = [
            inv_record, str(open_inv), str(del_inv), str(rejected_inv),
            ret_record, str(open_ret), str(collected_ret), str(cancelled_ret),
            fc_record, str(cust_out_amt), str(pro_inv), str(pro_ret), str(total), str(paid_amt), str(balance)
        ]
        print("data list in db = ", data_list)
        return data_list

    def to_string(self, data):
        data = str(data)
        return data

    def fetch_record_count_from_db(self, query):
        rec_count = SQLLite().fetch_one_record(query)
        return rec_count
