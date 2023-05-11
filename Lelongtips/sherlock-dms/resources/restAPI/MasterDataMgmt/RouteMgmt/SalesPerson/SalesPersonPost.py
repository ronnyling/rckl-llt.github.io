import secrets
from resources.restAPI import PROTOCOL, APP_URL
import json
from resources.restAPI.Common import APIMethod, APIAssertion, TokenAccess
from resources.restAPI.Config.ReferenceData.Country import CountryPost
from resources.restAPI.Config.ReferenceData.Locality import LocalityPost
from resources.restAPI.Config.ReferenceData.State import StatePost
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class SalesPersonPost(object):

    @keyword("user creates ${user_type} salesperson with ${data_type} data")
    def user_create_route_salesperson_with(self, user_type, data_type):
        """ Function to create route salesperson with fixed/random data"""
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/route-salesperson".format(END_POINT_URL, dist_id)
        payload = self.payload_route_salesperson_info(user_type)
        payload = json.dumps(payload)
        print('User Payload is : ', payload)
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        print("POST Status code for route sales person is " + str(response.status_code))
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code != 201:
            return str(response.status_code), ""
        else:
            body_result = response.json()
            res_bd_salesperson_id = body_result['ID']
            BuiltIn().set_test_variable("${salesperson_name}",body_result['SALESPERSON_NAME'])
            BuiltIn().set_test_variable("${salesperson_cd}", body_result['SALESPERSON_CODE'])
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            BuiltIn().set_test_variable("${res_bd_salesperson_id}", res_bd_salesperson_id)

    def payload_route_salesperson_info(self, user_type):
        """Function to create salesperson payload"""
        name = "".join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(50))
        details = BuiltIn().get_variable_value("${salesperson_details}")
        if user_type == 'telesales':
            telesales_flag = True
            hht_flag = False
            ROUTE_ASSIGNMENT_PAYLOAD = []
        else:
            telesales_flag = False
            hht_flag = secrets.choice([True, False])
            ROUTE_ASSIGNMENT_PAYLOAD = []

        payload = {
            "SALESPERSON_CODE": "".join(secrets.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
            "SALESPERSON_NAME": name,
            "SALESPERSON_STATUS": "Active",
            "LANGUAGE": "[en-US]",
            "ADDRESS_CD":
                {
                    "ADD1": "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
                    "ADD2": "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
                    "ADD3": "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)),
                    "LOCALITY": BuiltIn().get_variable_value("${res_bd_locality_payload}"),
                    "STATE": BuiltIn().get_variable_value("${res_bd_state_payload}"),
                    "COUNTRY": BuiltIn().get_variable_value("${res_bd_country_payload}"),
                    "POST_CD": "".join(secrets.choice('1234567890') for _ in range(5)),
                },
            "SALESPERSON_EMAIL": "".join((name, secrets.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"]))),
            "SALESPERSON_ID_NUM": "".join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "SALESPERSON_FOLLOW_DIST_WORKING": True,
            "SALESPERSON_FOLLOW_DIST_HOLIDAYS": True,
            "SALESPERSON_WORKING_DAYS": [],
            "ROUTE_ASSIGNMENT_PAYLOAD": ROUTE_ASSIGNMENT_PAYLOAD,
            "DELETE_ROUTES": [],
            "HHT_ENABLED": hht_flag,
            "IS_TELESALES": telesales_flag,

        }
        if details:
            payload.update((k, v) for k, v in details.items())
        return payload

    def set_prerequisites_for_salesperson(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code('DistEgg')
        CountryPost.CountryPost().user_creates_country_as_prerequisite()
        StatePost.StatePost().user_creates_state_as_prerequisite()
        LocalityPost.LocalityPost().user_creates_locality_as_prerequisite()

    def user_creates_salesperson_as_prerequisite(self):
        self.set_prerequisites_for_salesperson()
        TokenAccess.TokenAccess().get_token_by_role("distadm")
        self.user_create_route_salesperson_with('route', 'random')
        APIAssertion.APIAssertion().expected_return_status_code("201")

    def user_creates_telesales_salesperson_as_prerequisite(self):
        self.set_prerequisites_for_salesperson()
        TokenAccess.TokenAccess().get_token_by_role("distadm")
        self.user_create_route_salesperson_with('telesales', 'random')
        APIAssertion.APIAssertion().expected_return_status_code("201")