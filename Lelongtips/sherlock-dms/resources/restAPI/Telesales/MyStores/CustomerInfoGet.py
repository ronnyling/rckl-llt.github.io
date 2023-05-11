from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet

METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL
CUST_END_POINT_URL = PROTOCOL + "profile-cust" + APP_URL
ATTRIBUTE_END_POINT_URL = PROTOCOL + "dynamic-attribute" + APP_URL


class CustomerInfoGet(object):
    DISTRIBUTOR_ID = "${distributor_id}"

    @keyword('user retrieves all telesales info')
    def user_retrieves_all_telesales_info(self):
        url = "{0}modules/telesales-outlet-note".format(METADATA_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve telesales info"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Telesales info: ", body_result)

    @keyword('user retrieves cust info and address for ${custname}')
    def user_retrieves_customer_info(self, cust_name):
        cust_id = CustomerGet().user_retrieves_cust_name(cust_name)['ID']
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        url = "{0}distributors/{1}/customer/{2}".format(CUST_END_POINT_URL, dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve customer info"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Customer Code: ", body_result['CUST_CD'])
        print("Customer Name: ", body_result['CUST_NAME'])
        print("Customer Address: ", body_result['ADDRESS_SUMMARY'])


    @keyword('user retrieves cust hierarchy for ${custname}')
    def user_retrieves_customer_hierarchy(self, cust_name):
        dist_id = BuiltIn().get_variable_value(self.DISTRIBUTOR_ID)
        cust_id = CustomerGet().user_retrieves_cust_name(cust_name)['ID']
        url = "{0}distributors/{1}/customer/{2}/status/details".format(CUST_END_POINT_URL, dist_id, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve telesales info"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Customer Hierarchy: ", body_result)

    @keyword('user retrieves cust attribute')
    def user_retrieves_customer_attribute(self):
        url = "{0}attribute-assignment/CUST/FILT_ASSIGN/CUST_ASSIGN".format(ATTRIBUTE_END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve telesales info"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("Customer Attribute: ", body_result)



