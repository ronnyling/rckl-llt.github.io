import json, secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod,TokenAccess
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL

class SupplierGet:

    def user_retrieves_all_supplier(self):
        url = "{0}supplier".format(END_POINT_URL)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        respond_len = len(response.json())
        if response.status_code == 200:
            for i in range(respond_len):
                if response.json()[i]['DEFAULT_SUPP'] is True:
                    default_sup = True
                    default_id = response.json()[i]['ID']
                    break
                else:
                    default_sup = False
                    default_id = ''
            BuiltIn().set_test_variable("${default_sup}", default_sup)
            BuiltIn().set_test_variable("${default_sup_id}", default_id)
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            BuiltIn().set_test_variable("${supplier_ls}", response.json())
            return response.status_code
        else:
            return response.status_code, '', ''

    def user_retrieves_supplier_by_id(self):
        sup_id = BuiltIn().get_variable_value("${supplier_id}")
        if sup_id is None:
            supp_ls = BuiltIn().get_variable_value("${supplier_ls}")
            self.user_retrieves_all_supplier()
            sup_id = secrets.choice(supp_ls)['ID']

        url = "{0}supplier/{1}".format(END_POINT_URL, sup_id)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        if response.status_code == 200:
            assert response.json()['ID'] == sup_id, "Retrieved ID not match"
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            BuiltIn().set_test_variable("${update_supplier_details}", response.json())
        return response.status_code, response.json()

    def user_retrieves_supplier(self, cond):
        if cond == "random":
            url = "{0}module-data/supplier".format(METADATA_END_POINT_URL)
        else:
            sup_filter = {"SUPP_NAME": {"$eq": cond}}
            sup_filter = json.dumps(sup_filter)
            url = "{0}module-data/supplier?filter={1}".format(METADATA_END_POINT_URL, sup_filter)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve supplier"
        body_result = response.json()
        return secrets.choice(body_result)

    def user_retrieves_supplier_by_code(self, code):
        sup_filter = {"SUPP_CD": {"$eq": code}}
        sup_filter = json.dumps(sup_filter)
        url = "{0}module-data/supplier?filter={1}".format(METADATA_END_POINT_URL, sup_filter)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve supplier"
        body_result = response.json()
        return body_result[0]['ID']

    @keyword('user validates is there any default supplier')
    def user_validate_default_supplier(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        self.user_retrieves_all_supplier()
        status = BuiltIn().get_variable_value("${default_sup}")
        assert status == False

    def user_retrieves_rand_supplier_for_dist(self):
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        sup_filter = {"DIST_ID": {"$eq": distributor_id}}
        sup_filter = json.dumps(sup_filter)
        url = "{0}supplier?filter={1}".format(END_POINT_URL, sup_filter)
        response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
        body_result = response.json()
        rand_supp = secrets.choice(body_result)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${rand_supp_id}", rand_supp['ID'])

    # def user_retrieves_rand_supplier_for_dist(self):
    #     distributor_id = BuiltIn().get_variable_value("${distributor_id}")
    #     sup_filter = {"DIST_ID": {"$eq": distributor_id}}
    #     sup_filter = json.dumps(sup_filter)
    #     url = "{0}module-data/supplier?filter={1}".format(METADATA_END_POINT_URL, sup_filter)
    #     response = APIMethod.APIMethod().trigger_api_request("GET", url, "")
    #     body_result = response.json()
    #     rand_supp = secrets.choice(body_result)
    #     if response.status_code == 200:
    #         BuiltIn().set_test_variable("${rand_supp_id}", rand_supp['ID'])
