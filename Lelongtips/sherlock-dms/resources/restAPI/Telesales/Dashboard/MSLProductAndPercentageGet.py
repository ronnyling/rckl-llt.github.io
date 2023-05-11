from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Customer.CustomerGet import CustomerGet
END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class MSLProductAndPercentageGet(object):
    @keyword('user retrieves all MSL Products and MSL Percentage')
    def user_retrieves_all_MSL_products_and_percentage(self):
        details = BuiltIn().get_variable_value("${MSL_details}")
        CustomerGet().user_gets_cust_by_using_code(details['CUST_CD'])
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        url = "{0}telesales/msl-kpi/{1}".format(END_POINT_URL, cust_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve MSL Products and MSL Percentage"
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body_result = response.json()
        print("MSL Products & MSL Percentage: ", body_result)
