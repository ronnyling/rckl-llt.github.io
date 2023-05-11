import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxDefinitionPut(object):

    @keyword('user updates tax definition using ${data} data')
    def user_updates_tax_definition(self, data):
        tax_def_id = BuiltIn().get_variable_value("${tax_def_id}")
        url = "{0}tax-definition/{1}".format(END_POINT_URL, tax_def_id)
        payload = self.tax_def_payload(data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        try:
            BuiltIn().set_test_variable("${res_body}", response.json())
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def tax_def_payload(self, data):
        details = BuiltIn().get_variable_value("${res_body}")
        payload = {
            'TAX_CD': details["TAX_CD"],
            'TAX_COM_DESC': ''.join(secrets.choice(
                '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in
                                    range(30)),
            'TAX_LEVEL': details["TAX_LEVEL"],
        }
        up_details = BuiltIn().get_variable_value("&{tax_definition_details}")
        if up_details:
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        payload = json.dumps(payload)
        return payload





