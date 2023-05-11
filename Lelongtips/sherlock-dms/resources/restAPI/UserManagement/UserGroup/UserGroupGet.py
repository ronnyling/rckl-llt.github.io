import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()


END_POINT_URL = PROTOCOL + "user-info" + APP_URL


class UserGroupGet(object):

    @keyword("user retrieves all user group")
    def user_retrieves_user_setup(self):
        url = "{0}user-group".format(END_POINT_URL)
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
            BuiltIn().set_test_variable("${user_group_id}", body_result[rand_so]["ID"])
        return str(response.status_code), response.json()

    @keyword('user retrieves user group by ${cond} id')
    def user_retrieves_user_group_by_id(self, cond):
        if cond == 'invalid':
            grp_id = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(45))
        else:
            grp_id = BuiltIn().get_variable_value("${user_group_id}")
        url = "{0}user-group/{1}".format(END_POINT_URL, grp_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)



