from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.Sampling.SamplingPost import SamplingPost

END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class SamplingPut(object):
    """ Functions to update sampling """

    @keyword('When ${user_role} updates sampling with ${type} data')
    def user_updates_sampling_with(self, user_type, type):
        """ Function to updates sampling with random/fixed data"""
        sampling_id = BuiltIn().get_variable_value("${sampling_id}")
        url = "{0}sample/generalInfo/{1}".format(END_POINT_URL, sampling_id)
        payload = SamplingPost().payload(user_type, type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${sampling_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

