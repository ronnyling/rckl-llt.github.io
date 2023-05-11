from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Promo import PromoBuyTypeGet
import json
import secrets

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class ClaimTypeGet(object):

    @keyword("user retrieves all promotion claim type")
    def get_claim_type(self):
        url = "{0}claim-type".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        BuiltIn().set_test_variable("${claim_bd_rs}", body_result)
        return response.status_code

    @keyword("user retrieves promotion claim type by ID")
    def get_claim_type_by_id(self, claim_type_id=None):
        details = BuiltIn().get_variable_value("&{claim_type_details}")
        if details is not None:
            claim_type_id = details.get('CLAIM_TYPE_ID')
        url = "{0}claim-type/{1}".format(END_POINT_URL, claim_type_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        try:
            claim_cd = response.json()['CLAIM_TYPE_CD']
            claim_type = response.json()['TYPE']
            return response.status_code, claim_cd, claim_type
        except NameError:
            return response.status_code, 0, 0

    def get_claim_type_by_promo(self, data_type):
        promo_deal_type = PromoBuyTypeGet.PromoBuyTypeGet().user_retrieves_promo_type(data_type, 'refParam')[0]['ID']
        claim_filter = {"TYPE": {"$eq": promo_deal_type}}
        claim_filter = json.dumps(claim_filter)
        str(claim_filter).encode(encoding='UTF-8', errors='strict')
        url = "{0}claim-type?filter={1}".format(END_POINT_URL, claim_filter)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${rand_claim_type_id}", response.json()[0]['ID'])

    def get_claim_type_id_by_code(self, claim_type_code):
        claim_filter = {"CLAIM_TYPE_CD": {"$eq": claim_type_code}}
        claim_filter = json.dumps(claim_filter)
        str(claim_filter).encode(encoding='UTF-8', errors='strict')
        url = "{0}claim-type?filter={1}".format(END_POINT_URL, claim_filter)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        if response.status_code == 200:
            bd_res = response.json()
            claim_type_id = bd_res[0]['ID']
            BuiltIn().set_test_variable("${claim_type_id}", claim_type_id)
            print("claim type id = ", claim_type_id)
            return claim_type_id

    def get_rand_claim_type_id(self):
        self.get_claim_type()
        claim_br = BuiltIn().get_variable_value("${claim_bd_rs}")
        if len(claim_br) > 1:
            rand_no = secrets.randbelow(len(claim_br))
        else:
            rand_no = 0
        rand_ct_id = claim_br[rand_no]['ID']
        return rand_ct_id
