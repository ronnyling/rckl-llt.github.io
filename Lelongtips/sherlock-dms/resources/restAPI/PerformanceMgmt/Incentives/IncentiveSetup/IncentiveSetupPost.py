import datetime
import json
import secrets
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI.PerformanceMgmt.Incentives.IncentiveSetup.IncentiveSetupGet import IncentiveSetupGet

END_POINT_URL = PROTOCOL + "performance" + APP_URL


class IncentiveSetupPost(object):
    @keyword('user posts for incentive setup')
    def user_posts_for_incentive_setup(self):
        url = "{0}incentives".format(END_POINT_URL)
        payload = self.gen_inc_setup_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, json.dumps(payload))
        print("payload = ", str(json.dumps(payload)))
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_setup_br}', body_result)
            BuiltIn().set_test_variable('${inc_setup_id}', body_result['ID'])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_inc_setup_payload(self):
        IncentiveSetupGet().user_retrieves_kpi_config()
        inc_kpi_ls = BuiltIn().get_variable_value('${inc_kpi_ls}')
        kpi_type = BuiltIn().get_variable_value("${kpi_type}")
        if kpi_type is None:
            kpi_type = secrets.choice(["S", "PC", "MSL", "VR", "AH"])
        kpi_e_category = ["PC", "MSL", "VR"]
        kpi_cat = "E" if kpi_type in kpi_e_category else kpi_type
        type_type_ls = None
        kpi_type_type = None
        for kpis in inc_kpi_ls:
            if kpis['KPI_CATEGORY'] == kpi_cat:
                for kpi in kpis['KPIS']:
                    if kpi['KPI'] == kpi_type:
                        type_type_ls = kpi['TYPE']
                        break
            if type_type_ls is not None:
                break
        if len(type_type_ls) > 0:
            rand_type = secrets.choice(type_type_ls)
            kpi_type_type = rand_type

        next_month = (datetime.datetime.today() + datetime.timedelta(days=31)).strftime('%m')
        cut_off = secrets.choice(range(1, 15))
        as_soon = (datetime.datetime.today() + datetime.timedelta(days=(cut_off + 1))).strftime('%Y-%m-%d')
        payload = {
            "INC_CD": "INC" + ''.join(secrets.choice('0123456789ABCDEF') for _ in range(15)),
            "INC_DESC": ''.join(secrets.choice('0123456789ABCDEF') for _ in range(10)),
            "INC_FOR": "R",
            "KPI_CATEGORY": kpi_cat,
            "KPI": kpi_type,
            "TYPE": kpi_type_type,
            "FREQUENCY": "O",
            "INC_METHOD": 1,
            "INC_YEAR": datetime.datetime.today().strftime('%Y'),
            "INC_MTH_FROM": next_month,
            "INC_MTH_TO": next_month,
            "INC_LEVEL": "O",
            "CUTOFF_DAYS": cut_off,
            "ENABLE_CONDITION": kpi_cat == "S",
            "ENABLE_PHASING": kpi_cat == "S",
            "STATUS": "O",
            "PERIODS": [
                {
                    "MTH_FROM": next_month,
                    "MTH_TO": next_month,
                    "CALC_DT": as_soon,
                    "APPROVAL_DEADLINE": as_soon,
                    "CLAIM_DEADLINE": as_soon
                }
            ],
            "PRODUCT_ASSIGNMENT_EXCL": [],
            "PRODUCT_ASSIGNMENT": [
                {
                    "PRD_HIER_LVL_ID": None,
                    "PRD_HIER_VAL_ID": "D34A04AD:F6ED8347-7E89-4EE0-B271-B379E95AC5AF"
                }
            ],
            "CLAIMABLE": False,
            "CLAIM_TYPE": None
        }
        return payload

    @keyword('user posts to incentive setup details slabs')
    def user_posts_to_incentive_setup_details_slabs(self):
        inc_setup_id = BuiltIn().get_variable_value("${inc_setup_id}")
        url = "{0}incentives/{1}/slabs".format(END_POINT_URL, inc_setup_id)
        payload = self.gen_inc_setup_slabs(inc_setup_id)
        payload = json.dumps(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("payload = ", str(payload))
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            BuiltIn().set_test_variable('${inc_setup_slab_br}', body_result)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def gen_inc_setup_slabs(self, inc_setup_id):
        IncentiveSetupGet().user_retrieves_kpi_config()
        inc_setup_br = BuiltIn().get_variable_value('${inc_setup_br}')

        payload = {
            "INC_DTL_PERIOD_SLAB": [
                {
                    "ID": None,
                    "INC_ID": inc_setup_id,
                    "INC_PERIOD_ID": inc_setup_br['PERIODS'][0]['ID'],
                    "ACH_PERC": 20,
                    "ACH_PERC_CAP": 25,
                    "PAYOUT": 200,
                    "PAYOUT_CALC_BASIC": "P",
                    "IS_NEW": True
                }
            ],
            "INC_DTL_PHASING": []
        }
        return payload
