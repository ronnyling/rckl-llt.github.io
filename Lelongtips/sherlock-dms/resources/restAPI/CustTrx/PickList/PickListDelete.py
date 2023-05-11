from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "picklist" + APP_URL


class PickListDelete(object):

    def user_deletes_picklist(self):
        """Function to delete picklist"""
        res_bd_picklist_id = BuiltIn().get_variable_value("${res_bd_picklist_id}")
        url = "{0}picklist/{1}".format(END_POINT_URL, res_bd_picklist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        print("DELETE Status code for picklist is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code != 201:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            print("Body Result:", body_result)
            print("Picklist ID:", res_bd_picklist_id)
            BuiltIn().set_test_variable("${res_bd_picklist_id}", res_bd_picklist_id)
            BuiltIn().set_test_variable("${status_code}", response.status_code)
