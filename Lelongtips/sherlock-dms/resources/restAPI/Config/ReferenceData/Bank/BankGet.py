import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class BankGet(object):
    """ Functions to retrieve bank """

    @keyword('user retrieves all bank')
    def user_retrieves_all_bank(self):
        """ Function to retrieve all bank """
        url = "{0}bank".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${rand_bank_selection}", body_result[rand_so]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves bank by ${type} id')
    def user_retrieves_bank_by_id(self, type):
        """ Function to retrieve bank by using id """
        self.user_retrieves_all_bank()
        if type == 'created':
            res_bd_bank_id = BuiltIn().get_variable_value("${bank_id}")
        else:
            res_bd_bank_id = Common().generate_random_id("0")
        url = "{0}bank/{1}".format(END_POINT_URL, res_bd_bank_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
