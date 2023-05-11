import datetime
import json
import secrets

from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.Merchandising.TradeProgramSetup.TradeProgram.TradeProgramGet import TradeProgramGet

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL

class TradeProgramPost(object):

    @keyword('user post to trade program')
    def user_post_to_trade_program(self):
        url = "{0}trade-program".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.gen_tp_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${tp_br}", body_result)
            BuiltIn().set_test_variable("${tp_id}", body_result['HEADER']['ID'])
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_tp_payload(self):
        visit_type = secrets.choice(["NL", "FP"])
        fixed_period = []
        if visit_type == "FP":
            fixed_period = [
                    {
                        "TP_ID": 0,
                        "ID": 0,
                        "PERIOD_NAME": "1",
                        "PAYOUT_DATE": (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%Y-%m-%d %H:%M:%S'),
                        "START_DT": (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
                        "END_DT": (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
                        "NO_OF_TIMES": 1,
                        "REDEEM_DEADLINE": (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')
                    }
                ]
        payload = {
            "HEADER": {
                "APPROVAL_TYPE": secrets.choice(["A", "M"]),
                "COMPL_VISIT": visit_type,
                "AGREEMENT_CTRL_IND": False,
                "STATUS": "O",
                "VALID_START_DT": (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
                "COMPL_START_DT": (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
                "TP_CD": "TP" + ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
                "TP_DESC": "test",
                "VALID_END_DT": (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
                "COMPL_END_DT": (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
                "AGREEMENT_NUM": "",
                "PAYOUT_CUTOFF_DAYS": 1,
                "PAYOUT_DT": (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%Y-%m-%d %H:%M:%S'),
                "REIMBURSE_DEADLINE_DT": None,
                "fixed_period": fixed_period
            }
        }
        return payload

    @keyword('user post to trade program for criteria')
    def user_post_to_trade_program_criteria(self):
        tp_id = BuiltIn().get_variable_value("${tp_id}")
        url = "{0}trade-program/{1}/criteria".format(END_POINT_URL, tp_id)
        common = APIMethod.APIMethod()
        payload = self.gen_criteria_tp_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${criteria_tp_details}", body_result)
            BuiltIn().set_test_variable("${criteria_id}", body_result[0]['ID'])
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_criteria_tp_payload(self):
        TradeProgramGet().user_retrieves_all_criterias()
        criteria_ls = BuiltIn().get_variable_value("${criteria_ls}")
        rand = secrets.choice(criteria_ls)
        criteria_details = rand
        payload = [
            {
                "CRITERIA_CODE": criteria_details['CRITERIA_CODE'],
                "CRITERIA_DESCRIPTION": criteria_details['CRITERIA_DESCRIPTION'],
                "CRITERIA_STATUS": criteria_details['CRITERIA_STATUS'],
                "IS_DELETED": False,
                "VERSION": 1,
                "CORE_FLAGS": criteria_details['CORE_FLAGS'],
                "CRITERIA_ID": criteria_details['ID']
            }
        ]
        return payload

    @keyword('user post to trade program for criteria objective')
    def user_post_to_trade_program_criteria_objective(self):
        tp_id = BuiltIn().get_variable_value("${tp_id}")
        criteria_id = BuiltIn().get_variable_value("${criteria_id}")
        url = "{0}trade-program/{1}/criteria/{2}/objective".format(END_POINT_URL, tp_id, criteria_id)
        common = APIMethod.APIMethod()
        payload = self.gen_objective_criteria_tp_payload()
        payload = json.dumps(payload)
        response = common.trigger_api_request("POST", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${objective_id}", body_result[0]['ID'])
            print("Total number of records retrieved are ", len(body_result))
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_objective_criteria_tp_payload(self):
        TradeProgramGet().user_retrieves_all_objectives()
        objective_ls = BuiltIn().get_variable_value("${objective_ls}")
        rand = secrets.choice(objective_ls)
        objective_details = rand
        payload = [
                {
                    "OBJECTIVE_CODE": objective_details['OBJECTIVE_CODE'],
                    "OBJECTIVE_DESCRIPTION": objective_details['OBJECTIVE_DESCRIPTION'],
                    "WITH_POINT_IND": "true",
                    "MAX_POINT": 5,
                    "CALCULATION_TYPE": "M",
                    "MANDATORY_IND": True,
                    "MAX_POINT_EDIT_IND": True,
                    "OBJECTIVE_ID": objective_details['ID'],
                    "FORMULA_NUM": None,
                    "FORMULA_FACTOR": None,
                    "OBJECTIVE_TYPE": "Y"
                }
            ]
        return payload
