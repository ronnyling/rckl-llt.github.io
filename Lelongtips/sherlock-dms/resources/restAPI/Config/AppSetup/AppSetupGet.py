""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
import numpy as np
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "setting" + APP_URL + "module-data/application-setup"


class AppSetupGet:
    """ Functions related to application setup GET request """

    def user_retrieves_application_setup_id(self):
        """ Functions to retrieve application setup id """
        url = END_POINT_URL
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${app_setup_id}", body_result[0]["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_retrieves_details_of_application_setup(self):
        """ Functions to retrieve all details of application setup """
        self.user_retrieves_application_setup_id()
        app_setup_id = BuiltIn().get_variable_value("${app_setup_id}")
        url = "{0}/{1}".format(END_POINT_URL, app_setup_id)
        print("url", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            result_body = response.json()
            print("Total number of records retrieved are ", len(result_body))
            print("Get payload = ", result_body)
            BuiltIn().set_test_variable("${body_result}", result_body)
            np.save('appsetup.npy', result_body)
            BuiltIn().set_test_variable("${prev_sett}", result_body)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
