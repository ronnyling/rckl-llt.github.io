from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.CustTrx.PickList import PickListPost

END_POINT_URL = PROTOCOL + "picklist" + APP_URL


class PickListConfirm(object):

    def user_confirms_picklist(self):
        """Function to confirm picklist"""
        res_bd_picklist_id = BuiltIn().get_variable_value("${res_bd_picklist_id}")
        url = "{0}picklist-details".format(END_POINT_URL)
        payload = PickListPost.PickListPost().payload_picklist("confirm")
        print('Returned Picklist Payload is : ', payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        print("POST Status code for picklist is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code != 201:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            print("Body Result:", body_result)
            print("Picklist ID:", res_bd_picklist_id)
            BuiltIn().set_test_variable("${res_bd_picklist_id}", res_bd_picklist_id)
            BuiltIn().set_test_variable("${status_code}", response.status_code)
