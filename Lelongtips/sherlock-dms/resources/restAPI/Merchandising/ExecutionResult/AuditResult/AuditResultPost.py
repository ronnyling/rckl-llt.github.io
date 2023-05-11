import json
import datetime

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL
current_date = datetime.datetime.now()


class AuditResultPost(object):

    def user_filters_audit_result_for_planogram(self):
        url = "{0}planogram/filterData".format(END_POINT_URL)
        payload = self.payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${rand_audit_id}", body_result[rand_so]["ID"])
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable("${audit_res_bd}", body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload(self):
        start_date = str((current_date + datetime.timedelta(days=-1000)).strftime("%Y-%m-%d"))
        end_date = str(current_date.strftime("%Y-%m-%d"))
        compliance = ""
        payload = {
                   "start_date": start_date,
                   "end_date": end_date,
                   "compliance": compliance
        }
        details = BuiltIn().get_variable_value("${result_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print(payload)
        return payload
