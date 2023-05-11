from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.PerformanceMgmt.MustSellList.MustSellListPost import MustSellListPost

END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class SamplingProductAssignment(object):

    @keyword('When user retrieves sampling product assignment')
    def user_retrieves_sampling_product_assignment(self):
        sampling_id = BuiltIn().get_variable_value("${sampling_id}")
        url = "{0}sample/{1}/prdAssignment".format(END_POINT_URL, sampling_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('When user adds product assignment to sampling')
    def user_adds_product_assignment_to_sampling(self):
        sampling_id = BuiltIn().get_variable_value("${sampling_id}")
        url = "{0}sample/{1}/prdAssignment/N".format(END_POINT_URL, sampling_id)
        payload = MustSellListPost().payload_prod()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        #if response.status_code == 201:
        #    body_result = response.json()
        #    print("Body Result: ", body_result)
        #BuiltIn().set_test_variable("${assignment_id}", body_result[0]['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)
