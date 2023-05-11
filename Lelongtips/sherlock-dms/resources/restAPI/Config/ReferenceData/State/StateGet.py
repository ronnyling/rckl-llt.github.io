from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "metadata" + APP_URL
END_POINT_URL_NEW = PROTOCOL + "setting" + APP_URL


class StateGet(object):
    """ Functions to retrieve state record """

    def user_gets_all_states_data(self):
        """ Functions to retrieve all states record """
        url = "{0}module-data/address-state".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${state_br}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_state_by_using_id(self):
        """ Functions to retrieve state record by using id given """
        res_bd_state_id = BuiltIn().get_variable_value("${res_bd_state_id}")
        url = "{0}module-data/address-state/{1}".format(END_POINT_URL, res_bd_state_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result['ID']
            assert res_bd_id == res_bd_state_id, "ID retrieved not matched"
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_gets_all_states_data_new(self):
        """ Functions to retrieve all states record """
        url = "{0}address-state".format(END_POINT_URL_NEW)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = None
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${state_br}", body_result)
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return body_result
