import datetime
import json
import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


END_POINT_URL = PROTOCOL + "salesorder" + APP_URL


class SalesOrderGet(object):
    """ Functions to retrieve sales order transaction """

    def user_retrieves_all_sales_order_transaction(self):
        """ Function to retrieve all sales order transaction """
        distributor_id = self.get_dist()
        url = "{0}distributors/{1}/salesorder-header".format(END_POINT_URL, distributor_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.choice(range(0, len(body_result)))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${rand_so_selection}", body_result[rand_so]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_sales_order_transaction_by_id(self):
        """ Function to retrieve sales order transaction by using id.
            Currently get all Sales Order and randomize pick 1 id to use.
            Will update again when Sales Order POST is ready """
        distributor_id = self.get_dist()
        res_bd_salesorder_id = BuiltIn().get_variable_value("${res_bd_sales_order_id}")
        if res_bd_salesorder_id is None:
            self.user_retrieves_all_sales_order_transaction()
            res_bd_salesorder_id = BuiltIn().get_variable_value("${rand_so_selection}")
        url = "{0}salesorder/{1}/".format(END_POINT_URL, res_bd_salesorder_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable("${res_bd_sales_order_header}", response.json())
            body_result = response.json()
            res_bd_id = body_result['ID']
            prime_status = body_result['PRIME_FLAG']
            assert prime_status == 'PRIME' or prime_status == 'NON_PRIME', "Prime flag not showing correctly in respond"
            assert res_bd_id == res_bd_salesorder_id, "ID retrieved not matched"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_sales_order_details_by_id(self):
        """ Function to retrieve sales order details """
        distributor_id = self.get_dist()
        so_id = BuiltIn().get_variable_value("${res_bd_sales_order_id}")
        url = "{0}distributors/{1}/salesorder-header/{2}/salesorder-detail".format(END_POINT_URL, distributor_id, so_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            BuiltIn().set_test_variable("${res_bd_sales_order_details}", response.json())
            body_result = response.json()
            return body_result
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)



    def user_retrieves_sales_order_transaction_in_last_30_days(self):
        distributor_id = self.get_dist()
        lastmonth = (datetime.datetime.now() - datetime.timedelta(30)).strftime("%Y-%m-%d")
        filter_dt = [{"TXN_DT":{"$gte":lastmonth}}]
        filter_dt = json.dumps(filter_dt)
        url = "{0}distributors/{1}/salesorder-header?filter={2}".format(END_POINT_URL, distributor_id, filter_dt)
        print("URL IS {0}".format(url))
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print(body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword("user retrieves multiple ${data_type} sales order transaction")
    def user_retrieves_multiple_sales_order_transaction(self, data_type):
        """ Function to retrieve multiple sales order transactions"""
        url = "{0}salesorder-copy".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        details = BuiltIn().get_variable_value("${SO_details}")
        so_id = BuiltIn().get_variable_value("${res_bd_sales_order_id}")
        payload = []
        if so_id is not None:
            if isinstance(so_id, list):
                for i in so_id:
                    payload.append({"ID": i})
            else:
                payload.append({"ID": so_id})
        else:
            for i in details:
                payload.append({"ID": i})
        payload = json.dumps(payload)
        print("PAyload:", payload)
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
            return body_result

    def user_retrieves_salesorder_by_code(self, so_no):
        filter_txn = [{"TXN_NO": {"$eq": so_no}}]
        filter_txn = json.dumps(filter_txn)
        distributor_id = self.get_dist()
        str(filter_txn).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors/{1}/salesorder-header?filter={2}".format(END_POINT_URL, distributor_id, filter_txn)
        print("BY CODE URL {0}".format(url))
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve sales order by code"
        body_result = response.json()
        if response.status_code == 200:
            BuiltIn().set_test_variable("${res_bd_so_id}", body_result[0]['ID'])
        return body_result[0]

    def get_dist(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        return dist_id

    @keyword("validate the group discount is retrieved correctly")
    def user_retrieves_customer_group_discount(self):
        body_result = BuiltIn().get_variable_value("${res_bd_sales_order_header}")
        print('body results: ', body_result)
        grpdisc_amt = body_result['GRPDISC_AMT']
        print('Group discount amount: ', grpdisc_amt)
        assert grpdisc_amt > '0.000000', "Group discount should not be 0"
        return body_result


    def validate_no_customer_group_discount_in_sales_order_details(self):
        body_result = BuiltIn().get_variable_value("${res_bd_sales_order_details}")
        print('body results: ', body_result)
        grpdisc_amt = body_result[0]['GRPDISC_AMT']
        print('Group discount amount: ', grpdisc_amt)
        assert grpdisc_amt == '0.000000', "No customer group discount should be applied"
        return body_result

    @keyword("validate customer group discount details from sales order is retrieved correctly")
    def user_retrieves_customer_group_discount_details(self):
        body_result = BuiltIn().get_variable_value("${res_bd_sales_order_details}")
        print('body results: ', body_result)
        group_discount_details = BuiltIn().get_variable_value("${payload_groupdisc}")
        print('group discount details: ', group_discount_details)
        grp_disc_type = group_discount_details['DISC_TYPE']
        grp_apply_on = group_discount_details['APPLY_ON']
        grp_discount = group_discount_details['DISCOUNT']
        grp_grpdisc_amt = group_discount_details['GRPDISC_AMT']
        disc_type = body_result[0]['DISC_TYPE']
        apply_on = body_result[0]['APPLY_ON']
        discount = body_result[0]['DISCOUNT']
        grpdisc_amt = body_result[0]['GRPDISC_AMT']
        grpdisc_amt = round(float(grpdisc_amt), 2)
        grp_grpdisc_amt = float(grp_grpdisc_amt)
        assert disc_type == grp_disc_type, "Discount type is incorrect"
        assert apply_on == grp_apply_on, "Product applied on is incorrect"
        assert discount == grp_discount, "Group discount percentage is incorrect"
        assert grpdisc_amt == grp_grpdisc_amt, "Group discount amount is incorrect"
        return body_result

    def validate_no_customer_group_discount_in_sales_order_header(self):
        body_result = BuiltIn().get_variable_value("${res_bd_sales_order_header}")
        print('body results: ', body_result)
        grpdisc_amt = body_result['GRPDISC_AMT']
        print('Group discount amount: ', grpdisc_amt)
        assert grpdisc_amt == '0.000000', "No customer group discount should be applied"
        return body_result