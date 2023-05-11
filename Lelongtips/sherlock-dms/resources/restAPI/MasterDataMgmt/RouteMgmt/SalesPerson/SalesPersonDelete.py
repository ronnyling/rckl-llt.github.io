from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.ReferenceData.Country import CountryDelete
from resources.restAPI.Config.ReferenceData.Locality import LocalityDelete
from resources.restAPI.Config.ReferenceData.State import StateDelete
from robot.libraries.BuiltIn import BuiltIn
END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class SalesPersonDelete(object):

    def user_deletes_created_salesperson(self):
        salesperson_id = BuiltIn().get_variable_value("${res_bd_salesperson_id}")
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/route-salesperson/{2}".format(END_POINT_URL, dist_id, salesperson_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        print(response.status_code)
        print(response.text)
        return response.status_code

    def set_teardown_for_salesperson(self):
        LocalityDelete.LocalityDelete().user_deletes_created_locality_as_teardown()
        StateDelete.StateDelete().user_deletes_created_state_as_teardown()
        CountryDelete.CountryDelete().user_deletes_created_country_as_teardown()

    def user_deletes_created_salesperson_as_teardown(self):
        self.set_teardown_for_salesperson()
        self.user_deletes_created_salesperson()
