from datetime import datetime
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import secrets
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import datetime
NOW = datetime.datetime.now()

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class StepsOfCallPost(object):
    @keyword('user creates an soc as created the transaction control with ${status} data')
    def user_creates_an_soc_as_created_the_transaction_control_with_data(self, status):
        activity_name = BuiltIn().get_variable_value("${txn_id}")
        apply_to = BuiltIn().get_variable_value("${opt_type}")
        url = "{0}steps-of-call".format(END_POINT_URL)
        print("url_soc: ", url)
        payload = self.payload_soc(activity_name, apply_to, status)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(str(response.status_code))
        print("SOC Response: ", response.text)
        BuiltIn().set_test_variable("${status_code}", str(response.status_code))
        if response.status_code == 201:
            body_result = response.json()
            soc_id = body_result['ID']
            soc_cd = body_result['STEP_OF_CALL_CD']
            BuiltIn().set_test_variable("${soc_id}", soc_id)
            BuiltIn().set_test_variable("${soc_cd}", soc_cd)

    def payload_soc(self, activity_name, apply_to, status):
        op_type = BuiltIn().get_variable_value("${type}")
        print("op_type: ", op_type)
        start_date = None
        end_date = None
        details = BuiltIn().get_variable_value("${SOCDateDetails}")
        if status == "fixed":
            start_date = details['StartDate']
            end_date = details['EndDate']
        elif status == 'random':
            start_date= str((NOW + datetime.timedelta(days=1000)).strftime("%Y-%m-%d"))
            end_date= str((NOW + datetime.timedelta(days=1001)).strftime("%Y-%m-%d"))
        steps = BuiltIn().get_variable_value("${stepsNo}")
        steps_no = steps["STEPS_NO"]
        payload = {
                "STEPS_OF_CALL_DESC": 'SOC' + str(secrets.choice(range(1, 999))),
                "APPLY_TO": apply_to,
                "START_DATE": start_date,
                "END_DATE": end_date,
                "STATUS": True,
                "ASSIGNMENTS":[
                                {
                                    "ACTIVITY_NAME":activity_name,
                                    "STEPS_NO":steps_no,
                                    "IS_AUTOSCREEN":secrets.choice([True, False]),
                                    "IS_MANDATORY":secrets.choice([True, False]),
                                    "IS_PREREQUISITE":secrets.choice([True, False])
                                }
                            ]
                }
        payload = json.dumps(payload)
        print("SOC Payload: ", payload)
        return payload
