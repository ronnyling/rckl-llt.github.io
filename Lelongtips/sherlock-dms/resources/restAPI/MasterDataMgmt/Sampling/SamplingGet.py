from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Customer import CustomerGet
import secrets
END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class SamplingGet(object):
    """ Functions to retrieve sampling """
    SAMPLING_ID = "${sampling_id}"

    def user_retrieves_all_sampling(self):
        """ Function to retrieve all sampling """
        url = "{0}sample".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves sampling by ${type} id')
    def user_retrieves_sampling_by_id(self, type):
        """ Function to retrieve sampling by using id """
        if type == 'valid':
            sampling_id = BuiltIn().get_variable_value(self.SAMPLING_ID)
        else:
            sampling_id = Common().generate_random_id("0")
        url = "{0}sample/generalInfo/{1}".format(END_POINT_URL, sampling_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves ${type} sampling program by customer')
    def user_retrieves_sampling_program_by_customer(self, type):
        if type == "invalid":
            BuiltIn().set_test_variable(self.SAMPLING_ID, ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45)))
        else :
            details = BuiltIn().get_variable_value("${fixedData}")
            cust_name = details['INV_CUST']
            cust = CustomerGet.CustomerGet().user_retrieves_cust_name(cust_name)
            url = "{0}sample/customer-product/{1}".format(END_POINT_URL, cust['ID'])
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("GET", url, "")
            if response.status_code == 200:
                body_result = response.json()
                BuiltIn().set_test_variable(self.SAMPLING_ID, body_result[0]['SAMPLE_ID'])
                print("Sampling program retrieved : ", body_result)
            BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
