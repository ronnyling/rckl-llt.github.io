from resources.restAPI import PROTOCOL, APP_URL
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Common import  APIMethod
from robot.api.deco import keyword
import json
import secrets
import logging

END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorGet(object):
    DIST_ID = "${distributor_id}"

    def user_retrieves_all_distributors_list(self):
        url = "{0}distributors".format(END_POINT_URL)
        # Jessie is putting a logging for verification purpose for Zhong Hua on the profile-svc issue by tracking
        # verifying if this point is the issue point
        # logging.warning(f'user_retrieves_all_distributors_list---{url}')
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            body_result = response.json()
            dist_id = body_result[0]['ID']
            BuiltIn().set_test_variable("${dist_list}", body_result)
            BuiltIn().set_test_variable("${dist_id}", dist_id)
            BuiltIn().set_test_variable(self.DIST_ID, dist_id)

    def user_retrieves_random_distributor(self):
        self.user_retrieves_all_distributors_list()
        dist_list = BuiltIn().get_variable_value("${dist_list}")
        rand_no = secrets.choice(dist_list)
        BuiltIn().set_test_variable("${dist_id}", rand_no['ID'])
        return rand_no

    def user_gets_distributor_by_using_id(self):
            distributor_id = BuiltIn().get_variable_value(self.DIST_ID)
            url = "{0}distributors/{1}".format(END_POINT_URL, distributor_id)
            # Jessie is putting a logging for verification purpose for Zhong Hua on the profile-svc issue by tracking
            # verifying if this point is the issue point
            # logging.warning(f'user_gets_distributor_by_using_id{url}')
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("GET", url, "")
            body_result = ""
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            if response.status_code == 200:
                body_result = response.json()
                BuiltIn().set_test_variable("${dist_body_result}", body_result)
            return body_result

    @keyword("user gets distributor by using code '${dist_cd}'")
    def user_gets_distributor_by_using_code(self, dist_cd):
        """ Functions to retrieve distributor id by using distributor code """
        filter_dist = {"DIST_CD": {"$eq": dist_cd}}
        filter_dist = json.dumps(filter_dist)
        str(filter_dist).encode(encoding='UTF-8', errors='strict')
        url = "{0}distributors?filter={1}".format(END_POINT_URL, filter_dist)
        # Jessie is putting a logging for verification purpose for Zhong Hua on the profile-svc issue by tracking
        # verifying if this point is the issue point
        # logging.warning(f'user_gets_distributor_by_using_code---{url}')
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Distributor"
        body_result = response.json()
        distributor_id = body_result[0]['ID']
        BuiltIn().set_test_variable(self.DIST_ID, distributor_id)
        BuiltIn().set_test_variable("${dist_cd}", dist_cd)
        BuiltIn().set_test_variable("${dist_id}", distributor_id)
        BuiltIn().set_test_variable("${dist_other_pg}", body_result[0]['OTH_PRICE_GRP'])
        BuiltIn().set_test_variable("${dist_name}", body_result[0]['DIST_NAME'])
        BuiltIn().set_test_variable("${dist_rs_bd}", body_result[0])
        return distributor_id

