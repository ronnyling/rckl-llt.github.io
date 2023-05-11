import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "product" + APP_URL


class UomPost(object):
    """ Functions to create uom """

    @keyword('user creates uom with ${data_type}')
    def user_creates_uom_with(self, data_type):
        """ Function to create uom with random/fixed data """
        url = "{0}uom-setting".format(END_POINT_URL)
        payload = self.payload_uom('create')
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_uom_payload}", body_result)
            res_bd_uom_id = body_result['ID']
            uom_cd = body_result['UOM_CD']
            BuiltIn().set_test_variable("${res_bd_uom_id}", res_bd_uom_id)
            BuiltIn().set_test_variable("${uom_cd}", uom_cd)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_uom(self, status):
        """ Function for uom payload content """
        user_role = BuiltIn().get_variable_value("${user_role}")
        if user_role == 'distadm':
            principal = 'NON_PRIME'
        else:
            principal = 'PRIME'
        if status == 'create':
            uom_cd = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3))
        else:
            uom_cd = BuiltIn().get_variable_value("${uom_cd}")
        payload = {
            "PRIME_FLAG": principal,
            "UOM_CD": uom_cd,
            "UOM_DESCRIPTION": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        }
        details = BuiltIn().get_variable_value("${uom_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("UOM Payload: ", payload)
        return payload

