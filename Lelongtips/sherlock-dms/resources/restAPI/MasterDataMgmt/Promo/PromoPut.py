from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Promo import PromoPost
from setup.hanaDB import HanaDB
import json

PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class PromoPut(object):

    @keyword('user updates promotion with fixed data')
    def update_promotion(self):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        promo = BuiltIn().get_variable_value("${promo_payload}")
        promo_update = BuiltIn().get_variable_value("${promo_update}")
        update_payload = {
            "ID": promo_id,
            "PROMO_SLABS": [],
            "VERSION": 1,
            "action": "update"
        }
        if promo_update:
            promo_update.update(update_payload)
        else:
            promo_update = update_payload
        BuiltIn().set_test_variable("${promo_update}", promo_update)
        promo_payload = PromoPost.PromoPost().update_promo_payload(promo)
        promo_payload = json.dumps(promo_payload)
        print("ADE Payl: ", promo_payload)
        url = "{0}promotion/{1}".format(PROMO_END_POINT_URL, promo_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, promo_payload)
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${promo}", body_result)
            HanaDB.HanaDB().connect_database_to_environment()
            HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM PROMO where ID = '{0}'".format(promo_id), 1)
            HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        return response.status_code
