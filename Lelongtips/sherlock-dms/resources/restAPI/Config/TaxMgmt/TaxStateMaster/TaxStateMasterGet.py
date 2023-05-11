from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import json
END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxStateMasterGet(object):

    @keyword('user retrieves ${cond} tax state master')
    def user_deletes_tax_state_master(self, cond):
        tax_state_id = BuiltIn().get_variable_value("${tax_group_id}")
        if cond == 'all':
            url = "{0}tax-state".format(END_POINT_URL)
        else:
            url = "{0}tax-state/{1}".format(END_POINT_URL, tax_state_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user retrieves tax state master by code ${svc_cd}')
    def user_retrieves_tax_state_master_by_code(self, svc_cd):
        filter_ts = {"TAX_STATE_CD": {"$eq": svc_cd}}
        filter_ts = json.dumps(filter_ts)
        url = "{0}tax-state?filter={1}".format(END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 200, "Unable to retrieve service"
        body_result = response.json()[0]
        BuiltIn().set_test_variable("${tax_state_id}", body_result["ID"])
        return body_result