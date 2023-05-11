from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Config.TaxMgmt.TaxGroup.TaxGroupPost import TaxGroupPost
from robot.api.deco import keyword

TgPost = TaxGroupPost()
END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxGroupPut(object):

    @keyword('user edits tax group by ${data} data')
    def user_edits_tax_group(self, data):
        tax_id = BuiltIn().get_variable_value("${tax_group_id}")
        url = "{0}tax-group/{1}".format(END_POINT_URL, tax_id)
        payload = TgPost.tax_group_payload(data)
        print("payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        body = response.json()
        try:
            print("Result: ", response.json())
            BuiltIn().set_test_variable("${res_body}", response.json())
            BuiltIn().set_test_variable("${tax_group_id}", body['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


