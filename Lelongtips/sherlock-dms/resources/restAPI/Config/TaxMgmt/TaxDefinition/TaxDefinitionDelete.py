from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxDefinitionDelete(object):

    @keyword('user deletes created tax definition')
    def user_deletes_tax_definition(self):
        tax_def_id = BuiltIn().get_variable_value("${tax_def_id}")
        url = "{0}tax-definition/{1}".format(END_POINT_URL, tax_def_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)