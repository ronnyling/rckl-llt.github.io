from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, APIAssertion
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class CountryDelete(object):
    """ Functions for Country deletion """

    def user_deletes_country_with_created_data(self):
        """ Function to delete country with valid data """
        res_bd_country_id = BuiltIn().get_variable_value("${res_bd_country_id}")
        url = "{0}module-data/address-country/{1}".format(END_POINT_URL, res_bd_country_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_deletes_created_country_as_teardown(self):
        self.user_deletes_country_with_created_data()
        APIAssertion.APIAssertion().expected_return_status_code("200")