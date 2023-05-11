from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "taxation" + APP_URL

class TaxGroupDelete(object):

    @keyword('user deletes created tax group')
    def user_deletes_tax_group(self):
        tax_group_id = BuiltIn().get_variable_value("${tax_group_id}")
        url = "{0}tax-group/{1}".format(END_POINT_URL, tax_group_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)