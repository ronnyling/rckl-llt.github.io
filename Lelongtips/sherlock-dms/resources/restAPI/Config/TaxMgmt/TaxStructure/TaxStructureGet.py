from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
import secrets

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxStructureGet(object):
    @keyword('user retrieve ${cond} tax structure')
    def user_retrieve_tax_structure(self, cond):
        if cond == 'all':
            url = "{0}tax-structure/".format(END_POINT_URL)
        else:
            if cond == 'invalid':
                tax_def_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
            else:
                tax_def_id = BuiltIn().get_variable_value("${tax_struct_id}")
            url = "{0}tax-structure/{1}".format(END_POINT_URL, tax_def_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def get_tax_structure_by_cust_and_prd_tax_group(self, cx_tg_id, prd_tg_id):
        filter_ts = {"TAX_GRP_CD": {"$eq": cx_tg_id}, "PRD_TAX_GRP": {"$eq": prd_tg_id}}
        filter_ts = json.dumps(filter_ts)
        str(filter_ts).encode(encoding='UTF-8', errors='strict')
        url = "{0}tax-structure?filter={1}".format(END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        body_result = 0
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()[0]
        return body_result
