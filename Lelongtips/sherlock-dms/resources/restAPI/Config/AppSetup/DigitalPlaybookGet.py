""" Python file related to application setup API """
from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import APIMethod

END_POINT_URL_AUTO_PROMO_TYPE = PROTOCOL + "metadata" + APP_URL + "module-data/opt-val-playbk-max-content-size"


class DigitalPlaybookGet:
    """ Functions related to digital playbook max content size GET Request """

    def user_retrieves_option_values_playbook_max_content_size(self, given_data):
        """ Functions to retrieve option values for playbook max content size """
        url = END_POINT_URL_AUTO_PROMO_TYPE
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        selected_max_size_id = None
        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                if dic["REF_DESC"] == given_data:
                    selected_max_size_id = dic["ID"]
                    break
            BuiltIn().set_test_variable("${selected_max_size_id}", selected_max_size_id)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
