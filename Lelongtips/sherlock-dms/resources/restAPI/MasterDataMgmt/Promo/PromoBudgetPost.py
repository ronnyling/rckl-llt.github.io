from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Promo import PromoBudgetGet
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from setup.hanaDB import HanaDB
from robot.api.deco import keyword
import json
import secrets

PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoBudgetPost(object):

    @keyword("user updates ${type} assignment in promotion budget")
    def user_updates_promotion_budget(self, type):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        budget_payload = self.budget_payload(type)
        url = "{0}promotion/{1}/budget-allocation".format(PROMO_END_POINT_URL, promo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, budget_payload)
        print("Response", response)
        print("Response text", response.json())
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def budget_payload(self, type):
        budget_result = PromoBudgetGet.PromoBudgetGet().user_gets_promotion_budget()
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        no_dist = len(budget_result['PROMO_DIST_BUDGET_ASSIGNMENT']['data'])
        print("ADE NO of DIST",no_dist)
        if no_dist == 1:
            rand = 0
        else:
            rand = secrets.choice(range(0, no_dist-1))
        rand_id = budget_result['PROMO_DIST_BUDGET_ASSIGNMENT']['data'][rand]['ID']
        version = budget_result['PROMO_DIST_BUDGET_ASSIGNMENT']['data'][rand]['PROMO_BUDGET_VERSION']
        rand_budget = str(secrets.choice(range(10, 99))) + str(".") + str(secrets.choice(range(10, 99)))
        bud_type = type.capitalize()
        query = "SELECT CAST(ROW_ID as varchar) FROM MODULE_DATA_FIELDS R INNER JOIN METADATA_FIELD F " \
                "ON R.FIELD_ID = F.ID WHERE R.ROW_ID IN (SELECT ROW_ID FROM MODULE_DATA_FIELDS R " \
                "INNER JOIN METADATA_FIELD F ON R.FIELD_ID = F.ID INNER JOIN MODULE_DATA_ROWS D " \
                "ON D.MODULE_ID = F.MODULE_ID WHERE F.MODULE_ID= (SELECT ID FROM METADATA_MODULE " \
                "WHERE LOGICAL_ID LIKE 'promotion-budget-ass-type-ref' AND IS_DELETED=false) " \
                "AND FIELD_VALUE = '{0}' AND D.IS_DELETED=false GROUP BY ROW_ID)".format(bud_type)
        HanaDB.HanaDB().connect_database_to_environment()
        asgn_type = HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        asgn_type = COMMON_KEY.convert_string_to_id(asgn_type)
        payload = {
            "PROMO_BUDGET_ASSIGNMENT": [
                {
                    "ID": None,
                    "PROMO_ID": promo_id,
                    "BUDGET_ASS_TYPE": asgn_type,
                    "ASS_ID": rand_id,
                    "PARENT_ID": None,
                    "BUDGET": rand_budget,
                    "BALANCE": rand_budget,
                    "SOFT_ALLOC": "0.00",
                    "HARD_ALLOC": "0.00",
                    "VERSION": version,
                    "action": "create"
                }
            ],
            "PROMO_SPACE_BUY_ASSIGNMENT": []
        }
        details = BuiltIn().get_variable_value("${budget_details}")
        if details:
            payload['PROMO_BUDGET_ASSIGNMENT'][0].update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print("Payload: ", payload)
        return payload

