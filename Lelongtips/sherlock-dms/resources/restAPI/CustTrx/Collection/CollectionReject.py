import json

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.Common import Common
from robot.api.deco import keyword

from resources.restAPI.Config.ReferenceData.ReasonType.ReasonGet import ReasonGet

END_POINT_URL = PROTOCOL + "collection" + APP_URL


class CollectionReject(object):
    """ Functions to process Collection"""

    @keyword('user rejects created collection by id')
    def user_rejects_collection_by_id(self):
        """ Function to process collection """
        created_col = BuiltIn().get_variable_value("${created_col}")
        col_id = created_col['COL_ID']
        col_id = Common().convert_string_to_id(col_id)
        headers = {
            'np-session': "27ea0ccb:688a61a9-80e1-4c6f-bae6-d2a6d28ceee6"
        }
        BuiltIn().set_test_variable("${res_bd_reason_type_id}", "D4269B2F:234EC35E-802B-4946-A7FB-05936964D322")
        ReasonGet().user_retrieves_all_reasons()
        reject_reason = BuiltIn().get_variable_value("${rand_reason}")

        url = "{0}reject-customer-collection".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = [{"COLLECTION_ID": col_id, "REASON_ID": reject_reason}]
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload, **headers)

        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)


