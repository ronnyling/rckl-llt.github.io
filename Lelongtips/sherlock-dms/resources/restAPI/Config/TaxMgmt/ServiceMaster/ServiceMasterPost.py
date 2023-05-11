import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json, datetime

NOW = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class ServiceMasterPost(object):
    DT_FORMAT = "%Y-%m-%d"
    @keyword('user creates service master using ${data} data')
    def user_creates_tax_definition(self, data):
        url = "{0}sac-master".format(END_POINT_URL)
        payload = self.sac_payload(data)
        print("payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${sac_id}", body['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def sac_payload(self, data):
        user = BuiltIn().get_variable_value("${user_role}")
        tg_id = BuiltIn().get_variable_value("${tax_group_id}")
        st_date = str((NOW + datetime.timedelta(days=2)).strftime(self.DT_FORMAT))
        end_date = str((NOW + datetime.timedelta(days=1000)).strftime(self.DT_FORMAT))
        if user == 'distadm':
            principal = "Non-Prime"
        else:
            principal = "Prime"
        payload = {
                   "PRINCIPAL": principal,
                   "TAX_GROUP":[
                       {
                           "START_DT": st_date,
                            "END_DT": end_date,
                            "TAX_GROUP_CD": tg_id,
                            "TAX_GROUP": tg_id
                        }
                    ],
                   "SVC_CD": ''.join(secrets.choice('0123456789') for _ in range(3)),
                   "SAC_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8)),
                   "SAC_CD": ''.join(secrets.choice('0123456789') for _ in range(3))}
        if data == 'fixed':
            details = BuiltIn().get_variable_value("&{tax_definition_details}")
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        dump_payload = json.dumps(payload)
        return dump_payload

