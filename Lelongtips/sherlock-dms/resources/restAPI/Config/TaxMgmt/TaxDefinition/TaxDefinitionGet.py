from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import secrets, json

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxDefinitionGet(object):

    @keyword('user retrieves ${cond} tax definition')
    def user_retrieves_tax_definition(self, cond):
        if cond == 'all':
            url = "{0}tax-definition/".format(END_POINT_URL)
        else:
            if cond == 'invalid':
                tax_def_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
            else:
                tax_def_id = BuiltIn().get_variable_value("${tax_def_id}")
            url = "{0}tax-definition/{1}".format(END_POINT_URL, tax_def_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_get_tax_definition_by_code(self, tax_cd):
        filter_ts = {"TAX_CD": {"$eq": tax_cd}}
        filter_ts = json.dumps(filter_ts)
        url = "{0}tax-definition?filter={1}".format(END_POINT_URL, filter_ts)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 200, "Unable to retrieve tax definition"
        body_result = response.json()[0]
        return body_result