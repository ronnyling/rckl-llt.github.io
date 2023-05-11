import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "picklist" + APP_URL


class PickListGet(object):
    """ Functions to retrieve picklist """

    def user_retrieves_all_picklist(self):
        """ Function to retrieve all picklist """
        url = "{0}picklist".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_pl = secrets.choice(range(0, len(body_result)))
            else:
                rand_pl = 0
            BuiltIn().set_test_variable("${rand_pl_selection}", body_result[rand_pl]["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_picklist_by_id(self):
        """ Functions to retrieve picklist by using id """
        res_bd_picklist_id = BuiltIn().get_variable_value("${res_bd_picklist_id}")
        if res_bd_picklist_id is None:
            self.user_retrieves_all_picklist()
            res_bd_picklist_id = BuiltIn().get_variable_value("${rand_pl_selection}")
        url = "{0}picklist-details/{1}".format(END_POINT_URL, res_bd_picklist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            res_bd_id = body_result[0]['ID']
            prime_status = body_result[0]['PRIME_FLAG']
            assert prime_status == 'PRIME' or prime_status == 'NON_PRIME', "Prime flag not showing correctly in respond"
            assert res_bd_id == res_bd_picklist_id, "ID retrieved not matched"
            return body_result
        BuiltIn().set_test_variable("${status_code}", response.status_code)
