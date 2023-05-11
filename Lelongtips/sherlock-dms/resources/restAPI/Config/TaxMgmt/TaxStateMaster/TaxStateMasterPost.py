from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json, secrets
END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxStateMasterPost(object):

    @keyword('user creates tax state master with ${code} data')
    def user_create_tax_state_master(self, cond):
        url = "{0}tax-state".format(END_POINT_URL)
        payload = self.tax_state_master_payload(cond)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def tax_state_master_payload(self, cond):
        payload = {
                    "TAX_STATE_CD": ''.join(secrets.choice('0123456789') for _ in range(3)),
                    "TAX_STATE_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                    "TAX_STATE_TYPE": secrets.choice(['INTER', 'INTRA', 'INTRAUT'])
        }
        if cond == "fixed":
            details = BuiltIn().get_variable_value("&{tax_state_master_details}")
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        return payload
