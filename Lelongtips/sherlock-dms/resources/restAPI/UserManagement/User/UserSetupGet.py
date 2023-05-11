import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()


END_POINT_URL = PROTOCOL + "user-info" + APP_URL


class UserSetupGet(object):
    RES_BD_USER = "${res_bd_user}"

    @keyword("user retrieves ${data_type} user setup")
    def user_retrieves_user_setup(self, data_type):
        url = "{0}user".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_so = secrets.randbelow(len(body_result))
            else:
                rand_so = 0
            BuiltIn().set_test_variable("${user_id}", body_result[rand_so]["ID"])
        return str(response.status_code), response.json()

    @keyword('user retrieves user setup by ${cond} id')
    def user_retrieves_user_setup_by_id(self, cond):
        user_id = BuiltIn().get_variable_value("${res_bd_salesperson_id}")
        if user_id is None :
            user_id = BuiltIn().get_variable_value("${user_id}")
        url = "{0}user/{1}".format(END_POINT_URL, user_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable(self.RES_BD_USER, body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def validate_licensed_user_is_true(self):
        user = BuiltIn().get_variable_value(self.RES_BD_USER)
        us_license = user['IS_LICENSED']
        print('LICENSE', us_license)
        assert us_license is True, "Licensed user is false"

    def validate_user_role_is_telesales(self):
        user = BuiltIn().get_variable_value(self.RES_BD_USER)
        user_role = user['ROLE']['NAME']
        print('ROLE', user_role)
        assert user_role == "Telesales", "User role is not Telesales"