""" Python file related to reward setup API """
import datetime
import json
import secrets
import string

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod, TokenAccess, APIAssertion
from resources.restAPI.PerformanceMgmt.Gamification.Badges import BadgesGet
from resources.restAPI.PerformanceMgmt.Gamification.Rewards import RewardsDelete
from resources.Common import Common

END_POINT_URL_REWARD = PROTOCOL + "gamification" + APP_URL + "gamification-reward-setup"
END_POINT_URL_ACTIVE_PRODUCT = PROTOCOL + "metadata" + APP_URL + "module-data/product"
NOW = datetime.datetime.now()


class RewardsPost:
    """ Functions related to reward setup POST request """
    REWARD_SETUP_DETAILS = "${RewardSetupDetails}"
    YEAR_MONTH_DAY = "%Y-%m-%d"
    BADGE_ID = "C0F0299B:92897BE7-751B-41F6-BCC5-2F67B57946F8"

    def validate_user_scope_on_post_reward_setup(self, user_role, expected_status):
        """ Functions to validate user scope on POST request """
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)
        BuiltIn().set_test_variable(Common.USER_ROLE, user_role)
        self.user_creates_reward_setup_using_data("random")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if str(expected_status) == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    @keyword('user creates reward setup using ${data_type} data')
    def user_creates_reward_setup_using_data(self, data_type):
        """ Functions to create reward setup using random/given data """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)
        url = END_POINT_URL_REWARD
        if data_type == "given":
            given_data = BuiltIn().get_variable_value(self.REWARD_SETUP_DETAILS)
            payload = self.create_payload_reward(given_data)
        else:
            payload = self.create_payload_reward(None)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print("POST URL: ", url)
        print("POST payload: ", payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            BuiltIn().set_test_variable("${reward_setup_id}", body_result['ID'])
        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

    def create_payload_reward(self, given_data):
        """ Functions to create payload for reward setup """
        alphabet = string.digits + string.ascii_letters
        random_char = ''.join(secrets.choice(alphabet) for _ in range(5))
        kpi_code = secrets.choice(["LPC", "MSL", "PC", "PRDC", "PRDCT", "SF", "ST", "VS", "DC"])
        payload = {
            "KPI_CD": kpi_code,
            "REWARD_DESC": "test{0}".format(random_char),
            "START_DT": str((NOW + datetime.timedelta(days=1)).strftime(self.YEAR_MONTH_DAY)),
            "END_DT": str((NOW + datetime.timedelta(days=2)).strftime(self.YEAR_MONTH_DAY)),
            "GAME_REWARD_DTL": [
                {
                    "RANGE_FROM": secrets.randbelow(50),
                    "RANGE_TO": secrets.choice(range(51, 100)),
                    "POINT": secrets.choice(range(1, 100))
                }
            ],
            "GAME_REWARD_BADGE": [
                {
                    "BADGE_ID": self.return_random_badge_setup_id(),
                    "MIN_VAL": secrets.choice(range(1, 90)),
                    "CONT_MTHS": secrets.choice(range(1, 12)),
                }
            ]
        }

        if given_data:
            payload.update((k, v) for k, v in given_data.items())

        if payload["KPI_CD"] == "PRDC":
            payload["TYPE"] = secrets.choice(["A", "Q"])

        if payload["KPI_CD"] == "PRDC" or payload["KPI_CD"] == "PRDCT":
            payload["GAME_REWARD_PRD"] = [
                {
                    "PRD_HIER_ID": None,
                    "PRD_ENTITY_ID": None,
                    "PRD_ENTITY_VALUE_ID": self.return_random_product_id()
                }
            ]
            if given_data:
                payload.update((k, v) for k, v in given_data.items())

        payload = json.dumps(payload)

        return payload

    def validate_mandatory_fields_for_reward_setup(self, key, value, expected_status):
        """ Functions to validate mandatory fields for reward setup """
        dictionary = {key: value}

        BuiltIn().set_test_variable(self.REWARD_SETUP_DETAILS, dictionary)

        self.user_creates_reward_setup_using_data("given")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

    def validate_dropdown_values_for_kpi(self, kpi_values, expected_status):
        """ Functions to validate drop down values for kpi """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        self.validate_mandatory_fields_for_reward_setup("KPI_CD", kpi_values, expected_status)

        if expected_status == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    def validate_valid_length_for_reward_description(self, key, value, expected_status):
        """ Functions to validate valid length for reward description """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        self.validate_mandatory_fields_for_reward_setup(key, value, expected_status)

        if expected_status == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    def validate_valid_start_date_and_end_date(self, start_date, end_date, expected_status):
        """ Functions to validate start date and end date """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        if start_date == "today":
            start_date = str((NOW + datetime.timedelta(days=0)).strftime(self.YEAR_MONTH_DAY))
        elif start_date == "tomorrow":
            start_date = str((NOW + datetime.timedelta(days=1)).strftime(self.YEAR_MONTH_DAY))

        if end_date == "any":
            end_date = str((NOW + datetime.timedelta(days=10)).strftime(self.YEAR_MONTH_DAY))

        dictionary = {"START_DT": start_date, "END_DT": end_date}

        BuiltIn().set_test_variable(self.REWARD_SETUP_DETAILS, dictionary)

        self.user_creates_reward_setup_using_data("given")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if expected_status == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    def validate_valid_type_for_prodcat_activity(self, type_value, expected_status):
        """ Functions to validate type value for prodcat activity """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        dictionary = {"KPI_CD": "PRDC", "TYPE": type_value}

        BuiltIn().set_test_variable(self.REWARD_SETUP_DETAILS, dictionary)

        self.user_creates_reward_setup_using_data("given")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if expected_status == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    def validate_valid_badge_value(self, badge_value, expected_status):
        """ Functions to validate badge value for reward setup """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        badge_array = [{
            "BADGE_ID": self.BADGE_ID,
            "MIN_VAL": badge_value,
            "CONT_MTHS": secrets.choice(range(1, 12))
        }]

        dictionary = {"GAME_REWARD_BADGE": badge_array}

        BuiltIn().set_test_variable(self.REWARD_SETUP_DETAILS, dictionary)

        self.user_creates_reward_setup_using_data("given")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if expected_status == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    def validate_valid_continue_value(self, continue_value, expected_status):
        """ Functions to validate continue value for reward setup """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        badge_array = [{
            "BADGE_ID": self.BADGE_ID,
            "MIN_VAL": secrets.choice(range(1, 90)),
            "CONT_MTHS": continue_value
        }]

        dictionary = {"GAME_REWARD_BADGE": badge_array}

        BuiltIn().set_test_variable(self.REWARD_SETUP_DETAILS, dictionary)

        self.user_creates_reward_setup_using_data("given")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if expected_status == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    def validate_valid_tiers_value(self, continue_value, expected_status):
        """ Functions to validate continue value for reward setup """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        tiers_array = [
            {
                "RANGE_FROM": 0,
                "RANGE_TO": continue_value,
                "POINT": secrets.choice(range(1, 100))
            }
        ]

        dictionary = {"GAME_REWARD_DTL": tiers_array}

        BuiltIn().set_test_variable(self.REWARD_SETUP_DETAILS, dictionary)

        self.user_creates_reward_setup_using_data("given")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if expected_status == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    def validate_badge_information_in_reward_setup(self, badge_info, expected_status):
        """ Functions to validate badge information in reward setup """
        user_role = BuiltIn().get_variable_value(Common.USER_ROLE)
        common = TokenAccess.TokenAccess()
        common.user_retrieves_token_access_as(user_role)

        badge_array = [{
            "BADGE_ID": self.BADGE_ID,
            "MIN_VAL": secrets.choice(range(1, 90)),
            "CONT_MTHS": secrets.choice(range(1, 12)),
        }, {
            "BADGE_ID": "C0F0299B:65FD0573-35CB-4436-8C40-BE9132E64AB7",
            "MIN_VAL": secrets.choice(range(1, 90)),
            "CONT_MTHS": secrets.choice(range(1, 12)),
        }]

        if badge_info == "same":
            badge_array = [{
                "BADGE_ID": self.BADGE_ID,
                "MIN_VAL": secrets.choice(range(1, 90)),
                "CONT_MTHS": secrets.choice(range(1, 12)),
            }, {
                "BADGE_ID": self.BADGE_ID,
                "MIN_VAL": secrets.choice(range(1, 90)),
                "CONT_MTHS": secrets.choice(range(1, 12)),
            }]

        dictionary = {"GAME_REWARD_BADGE": badge_array}

        BuiltIn().set_test_variable(self.REWARD_SETUP_DETAILS, dictionary)

        self.user_creates_reward_setup_using_data("given")

        common = APIAssertion.APIAssertion()
        common.expected_return_status_code(expected_status)

        if expected_status == "201":
            common = RewardsDelete.RewardsDelete()
            common.user_deletes_created_reward_setup()

    def return_random_badge_setup_id(self):
        """ Functions to retrieve random badge setup id """
        BadgesGet.BadgesGet().user_retrieves_badge_setup("random")
        random_id = BuiltIn().get_variable_value(Common.RANDOM_ID)
        return random_id

    def return_random_product_id(self):
        """ Functions to retrieve all/random product id """
        filter_product = {"FILTER": {"STATUS": {"$eq": "Active"}, "SELLING_IND": {"$eq": "1"}}}
        filter_product = json.dumps(filter_product)
        str(filter_product).encode(encoding='UTF-8', errors='strict')
        url = "{0}?filter={1}".format(END_POINT_URL_ACTIVE_PRODUCT, filter_product)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

        try:
            body_result = response.json()
            BuiltIn().set_test_variable("${body_result}", body_result)

            random_count = secrets.choice(body_result)
            random_id = random_count['ID']
            BuiltIn().set_test_variable(Common.RANDOM_ID, random_id)

        except Exception as e:
            print(e.__class__, "occured")
            print("ResultFail: ", response.status_code)

        random_id = BuiltIn().get_variable_value(Common.RANDOM_ID)
        return random_id

    @keyword("user creates reward setup using ${data_type} data for ${data_level} product assignment")
    def user_creates_reward_setup_using_data_for_product_assignment(self, data_type, data_level):
        """ Functions to create reward setup using random data for same level product assignment """
        if data_type == "random":
            array = [
                {
                    "PRD_HIER_ID": None,
                    "PRD_ENTITY_ID": None,
                    "PRD_ENTITY_VALUE_ID": self.return_random_product_id()
                },
                {
                    "PRD_HIER_ID": None,
                    "PRD_ENTITY_ID": None,
                    "PRD_ENTITY_VALUE_ID": self.return_random_product_id()
                }
            ]

        dic = {
            "GAME_REWARD_PRD": array,
            "KPI_CD": "PRDC"
        }

        BuiltIn().set_test_variable(self.REWARD_SETUP_DETAILS, dic)
        self.user_creates_reward_setup_using_data("given")
