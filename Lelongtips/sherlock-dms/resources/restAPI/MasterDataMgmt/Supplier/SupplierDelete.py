from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.ReferenceData.Country import CountryDelete
from resources.restAPI.Config.ReferenceData.Locality import LocalityDelete
from resources.restAPI.Config.ReferenceData.State import StateDelete
from robot.libraries.BuiltIn import BuiltIn

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class SupplierDelete:

    def user_deletes_supplier(self):
        sup_id = BuiltIn().get_variable_value("${supplier_id}")
        url = "{0}supplier/{1}".format(END_POINT_URL, sup_id)
        response = APIMethod.APIMethod().trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        assert response.status_code == 200, "Supplier not deleted"

    def user_deletes_supplier_prerequisite(self):
        LocalityDelete.LocalityDelete().user_deletes_created_locality_as_teardown()
        StateDelete.StateDelete().user_deletes_created_state_as_teardown()
        CountryDelete.CountryDelete().user_deletes_created_country_as_teardown()