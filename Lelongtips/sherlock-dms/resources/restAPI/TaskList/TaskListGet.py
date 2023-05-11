import secrets

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()


END_POINT_URL = PROTOCOL + "workflow" + APP_URL


class TaskListGet(object):

    @keyword("user retrieves ${data_type} task")
    def user_retrieves_task(self, data_type):
        url = "{0}task".format(END_POINT_URL)
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
            BuiltIn().set_test_variable("${task_id}", body_result[rand_so]["ID"])
            BuiltIn().set_test_variable("${task_id}", body_result[rand_so]["DESCRIPTION"])
        return str(response.status_code), response.json()



