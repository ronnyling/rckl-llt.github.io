from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
import json

END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class TelesalesOrderListingGet(object):
    DISTRIBUTOR_ID = "${distributor_id}"

    @keyword('user retrieves summary listing by order number ${order_no}')
    def user_retrieves_summary_by_order_number(self, order_no):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"TXN_NO": {"$eq": order_no}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter=[{2}]".format(END_POINT_URL, dist_id,
                                                                                    filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by order number"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with order number {0}: ".format(order_no), body_result)

    @keyword('user retrieves summary listing by from order date and to order date, ${from_date} and ${to_date}')
    def user_retrieves_summary_by_from_order_date_and_to_order_date(self, from_date, to_date):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"TXN_DT": {"$gte": from_date}}, {"TXN_DT": {"$lte": to_date}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter={2}".format(END_POINT_URL, dist_id, filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by from order date and to order date"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with from order date {0} and to order date {1}: ".format(from_date, to_date), body_result)

    @keyword('user retrieves summary listing by order type ${order_type}')
    def user_retrieves_summary_by_order_type(self, order_type):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"ORDER_TXNTYPE": {"$eq": order_type}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter=[{2}]".format(END_POINT_URL, dist_id,
                                                                                    filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by order type"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with order type {0}: ".format(order_type), body_result)

    @keyword('user retrieves summary listing by customer code ${cust_code}')
    def user_retrieves_summary_by_customer_code(self, cust_code):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"CUST_CD": {"$eq": cust_code}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter=[{2}]".format(END_POINT_URL, dist_id,
                                                                                    filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by customer code"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with customer code {0}: ".format(cust_code), body_result)

    @keyword('user retrieves summary listing by delivery date ${delivery_date}')
    def user_retrieves_summary_by_delivery_date(self, delivery_date):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"DELIVERY_DT": {"$eq": delivery_date}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter=[{2}]".format(END_POINT_URL, dist_id,
                                                                                    filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by delivery date"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with order delivery date {0}: ".format(delivery_date), body_result)

    @keyword('user retrieves summary listing by total net tax ${total_net_tax}')
    def user_retrieves_summary_by_total_net_tax(self, total_net_tax):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"NET_TTL_TAX": {"$eq": total_net_tax}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter=[{2}]".format(END_POINT_URL, dist_id,
                                                                                    filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by total net tax"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with total net tax {0}: ".format(total_net_tax), body_result)

    @keyword('user retrieves summary listing by adjustment amount ${adj_amt}')
    def user_retrieves_summary_by_adjustment_amount(self, adj_amt):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"ADJ_AMT": {"$eq": adj_amt}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter=[{2}]".format(END_POINT_URL, dist_id,
                                                                                    filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by adjustment amount"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with adjustment amount {0}: ".format(adj_amt), body_result)

    @keyword('user retrieves summary listing by order status ${order_status}')
    def user_retrieves_summary_by_order_status(self, order_status):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"STATUS": {"$eq": order_status}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter=[{2}]".format(END_POINT_URL, dist_id,
                                                                                    filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by order status"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with status {0}: ".format(order_status), body_result)

    @keyword('user retrieves summary listing by customer ID ${customer_id}')
    def user_retrieves_summary_by_customer_id(self, customer_id):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        filter_status = {"CUST_ID": {"$eq": customer_id}}
        filter_status = json.dumps(filter_status)
        url = "{0}telesales/distributors/{1}/salesorder-header?filter=[{2}]".format(END_POINT_URL, dist_id,
                                                                                    filter_status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve summary listing by customer ID"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales order with customer ID {0}: ".format(customer_id), body_result)
