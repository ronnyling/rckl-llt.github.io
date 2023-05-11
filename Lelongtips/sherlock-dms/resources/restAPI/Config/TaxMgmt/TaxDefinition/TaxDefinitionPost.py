import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxDefinitionPost(object):

    @keyword('user creates tax definition using ${data} data')
    def user_creates_tax_definition(self, data):
        url = "{0}tax-definition/".format(END_POINT_URL)
        payload = self.tax_def_payload(data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${tax_def_id}", body['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def tax_def_payload(self, data):
        payload = {
            'TAX_CD': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
            'TAX_COM_DESC': ''.join(secrets.choice(
                '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in
                                    range(30)),
            'TAX_LEVEL': ''.join(secrets.choice('12345') for _ in range(1)),
        }
        if data == 'fix':
            details = BuiltIn().get_variable_value("&{tax_definition_details}")
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        dump_payload = json.dumps(payload)
        return dump_payload

    @keyword('verified created data is matching with the response body')
    def data_compare(self):
        flag = True
        response = BuiltIn().get_variable_value("${res_body}")
        payload = BuiltIn().get_variable_value("${payload}")
        for key in list(payload.keys()):
            if key in list(response.keys()):
                if payload[key] != response[key]:
                    flag = False
                    break
            else:
                flag = False
                break
        assert flag is True, "Data Mismatch"



