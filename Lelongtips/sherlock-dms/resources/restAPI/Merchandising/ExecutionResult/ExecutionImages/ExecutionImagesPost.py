"""_Python file related to execution images API """

import datetime
import json
import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import TokenAccess, APIMethod, APIAssertion
from setup.hanaDB import HanaDB

END_POINT_URL = PROTOCOL + "merchandising" + APP_URL + "photo-search"
NOW = datetime.datetime.now()


class ExecutionImagesPost:
    """ Functions related to execution images POST request """
    FIXED_DATA = "${fixed_data}"

    @keyword("user retrieves ${data_type} execution images")
    def user_retrieves_execution_images(self, data_type):
        """ Functions to create module setup using random/fixed data """
        url = END_POINT_URL

        if data_type == "fixed":
            fixed_data = BuiltIn().get_variable_value(self.FIXED_DATA)
            payload = self.create_payload_execution_images(fixed_data)
            print("fixed_data Payload", payload)
        else:
            payload = self.create_payload_execution_images(fixed_data=None)

        print("POST URL", url)
        print("POST Payload", payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            print("Result: ", body_result)
            HanaDB.HanaDB().connect_database_to_environment()
            HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_MERC_POSM_RECORDDTL", 1)
            HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_MERC_POSM_RECORDHDR", 1)
            HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM TXN_MERC_POSM_RECORDIMG", 1)
            HanaDB.HanaDB().disconnect_from_database()
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def create_payload_execution_images(self, fixed_data):
        """ Functions to create payload for execution images """
        payload = {
            "START_DT": "2020-01-01",  # hardcoded
            "END_DT": str((NOW + datetime.timedelta(days=0)).strftime("%Y-%m-%d")),
            "ACTIVITY": secrets.choice(
                ["DIST_CHECK", "FACING_AUDIT", "PRICE_AUDIT", "PLANO_CHECK", "PROMO_CHECK", "POSM_NW_INS", "POSM_RECORD"]),
            "STOCK_AVAIL": secrets.choice([True, False]),
            "ON_PROMO": secrets.choice([True, False]),
            "COMPLIANCE": secrets.choice([True, False])
        }

        if fixed_data:
            payload.update((k, v) for k, v in fixed_data.items())

        payload = json.dumps(payload)

        return payload

    def validate_end_date_greater_than_or_equal_to_start_date(self, start_date, end_date, expected_status,
                                                              expected_status1):
        """ Functions to validate end date must be greater than or equal to start date """
        user_role = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().user_retrieves_token_access_as(user_role)
        fixed_data = {
            "START_DT": start_date,
            "END_DT": end_date
        }
        BuiltIn().set_test_variable(self.FIXED_DATA, fixed_data)
        self.user_retrieves_execution_images("fixed")

        APIAssertion.APIAssertion().expected_return_either_status_code_or_status_code(expected_status, expected_status1)

    def validate_fields_shown_with_each_activity_selected(self, activity, on_promo, stock_availability, compliance,
                                                          expected_status, expected_status1):
        """ Functions to validate respective fields needed with each activity selected """
        user_role = BuiltIn().get_variable_value("${user_role}")
        TokenAccess.TokenAccess().user_retrieves_token_access_as(user_role)
        fixed_data = {
            "ACTIVITY": activity,
            "STOCK_AVAIL": on_promo,
            "ON_PROMO": stock_availability,
            "COMPLIANCE": compliance
        }
        BuiltIn().set_test_variable(self.FIXED_DATA, fixed_data)
        self.user_retrieves_execution_images("fixed")
        APIAssertion.APIAssertion().expected_return_either_status_code_or_status_code(expected_status, expected_status1)
