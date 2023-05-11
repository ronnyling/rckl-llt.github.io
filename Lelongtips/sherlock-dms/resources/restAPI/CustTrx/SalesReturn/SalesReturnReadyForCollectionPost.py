import json
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL + "return" + APP_URL


class SalesReturnReadyForCollectionPost(object):


    def user_post_return_ready_for_collection(self):
        """ Function to mark return to ready for collection """
        url = "{0}ready-for-collection".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.ready_for_collection_payload()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def ready_for_collection_payload(self):
        return_id = BuiltIn().get_variable_value("${res_bd_return_id}")
        payload = [
            {
                "RETURN_ID": return_id,
                "STATUS": "R"
             }
        ]
        payload = json.dumps(payload)
        return payload