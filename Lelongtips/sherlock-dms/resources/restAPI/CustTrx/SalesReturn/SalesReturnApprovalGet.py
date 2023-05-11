import secrets, json
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod, TokenAccess
from resources.restAPI.MasterDataMgmt.Product.ProductGet import ProductGet
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL + "return" + APP_URL


class SalesReturnApprovalGet(object):
    """ Functions to retrieve return transaction """
    random_rtn = "${rand_rtn_selection}"

    def user_retrieves_all_return(self):
        """ Function to retrieve all return """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/return-header".format(END_POINT_URL, distributor_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_rtn = secrets.choice(range(0, len(body_result)))
            else:
                rand_rtn = 0
            BuiltIn().set_test_variable(self.random_rtn, body_result[rand_rtn]["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    # https: // acme - intg - dms - approuter - dev.cfapps.jp10.hana.ondemand.com / setting - svc / api / v1
    # .0 / workflow - configuration / 38292011 % 3
    # AFA4952DA - EE17 - 4884 - 9657 - 23
    # D7306E5068
    # Request
    # Method: PUT
    # Status
    # Code: 200

    def user_retrieves_return_by_id(self):
        """ Function to retrieve return by using id.
            Currently get all return and randomize pick 1 id to use.
            Will update again when return POST is ready """
        distributor_id = BuiltIn().get_variable_value(COMMON_KEY.DISTRIBUTOR_ID)
        res_bd_return_id = BuiltIn().get_variable_value("${res_bd_return_id}")
        if res_bd_return_id is None:
            self.user_retrieves_all_return()
            res_bd_return_id = BuiltIn().get_variable_value(self.random_rtn)
        url = "{0}distributors/{1}/return-header/{2}".format(END_POINT_URL, distributor_id, res_bd_return_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_return}", body_result)
            res_bd_id = body_result[0]['ID']
            prime_status = body_result[0]['PRIME_FLAG']
            assert prime_status == 'PRIME' or prime_status == 'NON_PRIME', "Prime flag not showing correctly in respond"
            assert res_bd_id == res_bd_return_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword("user retrieves return product by id ${with_or_without} id validation")
    def user_retrieves_return_product_by_id(self, with_or_without_check_id):
        """ Function to retrieve return product details by using id"""
        distributor_id = BuiltIn().get_variable_value(COMMON_KEY.DISTRIBUTOR_ID)
        res_bd_return_id = BuiltIn().get_variable_value("${res_bd_return_id}")
        url = "{0}distributors/{1}/return-header/{2}/return-detail"\
                    .format(END_POINT_URL, distributor_id, res_bd_return_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result[0]['TXN_ID']
            if with_or_without_check_id == "with":
                assert res_bd_id == res_bd_return_id, "ID retrieved not matched"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_return_based_on_status(self, return_status):
        filter_inv = [{"STATUS": {"$eq": return_status}}]
        filter_inv = json.dumps(filter_inv)
        url = "{0}distributors/1/return-header?filter={1}".format(END_POINT_URL, filter_inv)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve return"
        body_result = response.json()
        body_result = secrets.choice(body_result)
        return_id = body_result['ID']
        rtn_header_details = {"PRIME_FLAG": "PRIME", "CUST": body_result['CUST_NAME']}
        BuiltIn().set_test_variable("${rtn_header_details}", rtn_header_details)
        BuiltIn().set_test_variable(self.random_rtn, return_id)
        BuiltIn().set_test_variable("${res_bd_return_id}", return_id)
        BuiltIn().set_test_variable("${return_info}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieve_return_to_update(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        self.user_retrieves_return_based_on_status("C")
        self.user_retrieves_return_product_by_id("without")
        prd_rs_bd = ProductGet().user_retrieves_product_by_id()
        BuiltIn().set_test_variable("${prd_cd}", prd_rs_bd['PRD_CD'])

    @keyword("validate the customer group discount is retrieved correctly")
    def user_retrieves_customer_group_discount(self):
        body_result = BuiltIn().get_variable_value("${res_bd_return}")
        ttl_groupdisc = float(BuiltIn().get_variable_value("${ttl_groupdisc}"))
        grpdisc_amt = float(body_result[0]['GRPDISC_AMT'])
        assert grpdisc_amt == ttl_groupdisc, "Group discount not retrieved correctly"

    @keyword("user retrieves all return invoice ")
    def get_return_invoice(self):
        """ Function to retrieve all return invoice"""
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        url = "{0}customer-return-invoice/{1}".format(END_POINT_URL, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

