import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from setup.hanaDB import HanaDB

END_POINT_URL = PROTOCOL + "message" + APP_URL


class DigitalPlaybookGet(object):
    """ Functions to retrieve playbook """

    def user_retrieves_all_playbook(self):
        """ Function to retrieve all playbook """
        url = "{0}playbk-setup".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            print("br = ", body_result)
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${rand_playbook_selection}", body_result[rand_so]["ID"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    @keyword('user retrieves playbook by ${type} id')
    def user_retrieves_playbook_by_id(self, type):
        """ Function to retrieve playbook by using id """
        self.user_retrieves_all_playbook()
        if type == 'valid':
            #playbook having content assignment
            res_bd_playbook_id = '240651B8:01C71573-D723-48C5-B4BF-69B22A5D826B'
        else:
            res_bd_playbook_id = Common().generate_random_id("0")
        url = "{0}playbk-setup/{1}".format(END_POINT_URL, res_bd_playbook_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("playbk-setup", body_result['GENERAL_INFO'])
            # HanaDB.HanaDB().disconnect_from_database()
            BuiltIn().set_test_variable("${playbook_desc}", body_result['GENERAL_INFO']['PLAYBK_DESC'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

