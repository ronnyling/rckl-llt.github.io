import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxGroupPost(object):

    @keyword('user creates tax group using ${data} data')
    def user_creates_tax_group(self, data):

        url = "{0}tax-group/".format(END_POINT_URL)
        payload = self.tax_group_payload(data)
        print("payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${tax_group_id}", body['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def tax_group_payload(self, data):
        user = BuiltIn().get_variable_value("${user_role}")
        if user == 'distadm':
            flag = "NON_PRIME"
            tax_type = secrets.choice(['S', 'P'])
        else:
            flag = "PRIME"
            tax_type = secrets.choice(['R', 'S', 'P'])
        payload = {
            'TAX_GRP_CD': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(20)),
            'TAX_GRP_DESC': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(50)),
            'TYPE': tax_type,
            'TAX_TYPE': secrets.choice(['INTER', 'INTRA']),
            'PRIME_FLAG': flag
        }
        details = BuiltIn().get_variable_value("&{tax_group_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        dump_payload = json.dumps(payload)
        return dump_payload



