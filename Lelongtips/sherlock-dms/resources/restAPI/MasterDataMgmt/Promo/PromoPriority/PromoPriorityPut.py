import json
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.MasterDataMgmt.Promo.PromoPriority import PromoPriorityPost
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword


END_POINT_URL = PROTOCOL + "setting" + APP_URL


class PromoPriorityPut(object):
    @keyword('user updates promotion sequence with ${type} data')
    def update_promo_sequence(self, type):
        sequence_id = BuiltIn().get_variable_value("${sequence_id}")
        url = "{0}promotion-sequence/{1}".format(END_POINT_URL, sequence_id)
        payload = PromoPriorityPost.PromoPriorityPost().payload_details(type)
        payload['ID'] = sequence_id
        payload = json.dumps(payload)
        print(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
