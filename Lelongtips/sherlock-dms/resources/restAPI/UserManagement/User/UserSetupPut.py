import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
fake = Faker()

END_POINT_URL = PROTOCOL + "user-info" + APP_URL


class UserSetupPut(object):

    @keyword("user updates user setup using ${data_type} data")
    def user_updates_user_setup_using_data(self, data_type):
        user_id = BuiltIn().get_variable_value("${user_id}")
        if user_id is None :
            user_id = BuiltIn().get_variable_value("${res_bd_salesperson_id}")
        url = "{0}user/{1}".format(END_POINT_URL, user_id)
        print(url)
        common = APIMethod.APIMethod()
        payload = self.payload_user_setup()
        response = common.trigger_api_request("PUT", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def payload_user_setup(self):
        details = BuiltIn().get_variable_value("${res_bd_user}")

        payload = {
            "ACT_APPROVAL_STATUS": None,
            "ACT_REQUEST_STATUS": None,
            "CONTACT_NO": ''.join(secrets.choice('0123456789') for _ in range(8)),
            "CREATED_BY": details['CREATED_BY'],
            "CREATED_DATE": details['CREATED_DATE'],
            "DIST_CD": None,
            "DIST_ID": None,
            "DIST_NAME": None,
            "EMAIL":  f'qa_{fake.word()}_{fake.word()}@accenture.com',
            "ID": details['ID'],
            "IS_DELETED": False,
            "IS_ENABLED": secrets.choice([True, False]),
            "IS_LICENSED": True,
            "LOGIN_ID": details['LOGIN_ID'],
            "MODIFIED_BY": details['MODIFIED_BY'],
            "MODIFIED_DATE": details['MODIFIED_DATE'],
            "NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
            "ROLE": {
                "ID": details['ROLE']['ID'],
                "NAME": details['ROLE']['NAME'],
                "ROLE_CD": details['ROLE']['ROLE_CD']
            },
            "SAML_USER_ID": None,
            "VERSION": 1
        }

        details = BuiltIn().get_variable_value("${setup_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print(payload)
        return payload