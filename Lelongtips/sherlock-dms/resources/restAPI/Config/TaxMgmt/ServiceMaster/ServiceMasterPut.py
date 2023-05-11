import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json, datetime

NOW = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class ServiceMasterPut(object):
    DT_FORMAT = "%Y-%m-%d"
    @keyword('user updates service master using ${data} data')
    def user_updates_tax_definition(self, data):
        sac_id = BuiltIn().get_variable_value("${sac_id}")
        url = "{0}sac-master/{1}".format(END_POINT_URL, sac_id)
        payload = self.sac_payload(data)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        try:
            BuiltIn().set_test_variable("${res_body}", response.json())
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def sac_payload(self, data):
        sac_details = BuiltIn().get_variable_value("${res_body}")
        st_date = str((NOW + datetime.timedelta(days=5)).strftime(self.DT_FORMAT))
        end_date = str((NOW + datetime.timedelta(days=100)).strftime(self.DT_FORMAT))
        tg_id = BuiltIn().get_variable_value("${tax_group_id}")
        payload = {
                   "PRINCIPAL": sac_details['PRINCIPAL'],
                   "TAX_GROUP":[
                       {
                           "START_DT": st_date,
                            "END_DT": end_date,
                            "TAX_GROUP_CD": tg_id,
                            "TAX_GROUP": tg_id
                        }
                    ],
                   "SVC_CD": sac_details["SVC_CD"],
                   "SAC_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8)),
                   "SAC_CD": sac_details["SAC_CD"]
        }
        details = BuiltIn().get_variable_value("&{tax_definition_details}")
        if details :
            payload.update((k, v) for k, v in details.items())
        BuiltIn().set_test_variable("${payload}", payload)
        payload = json.dumps(payload)
        return payload

