import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker
from resources import Common, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.UserManagement.UserGroup import UserGroupPost

END_POINT_URL = PROTOCOL + "user-info" + APP_URL


class UserGroupPut(object):

    @keyword("user updates user group using ${data_type} data")
    def user_updates_user_group_using_data(self, data_type):
        user_group_id = BuiltIn().get_variable_value("${user_group_id}")
        url = "{0}user-group/{1}".format(END_POINT_URL, user_group_id)
        common = APIMethod.APIMethod()
        payload = self.payload_user_group()
        response = common.trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            body_result = response.json()
            print("Response Body ", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_user_group(self):
        group_details = BuiltIn().get_variable_value("${res_bd_user_group}")
        print("GROUP DETAILS", group_details)
        role_id = group_details['ROLE']['ID']
        role_cd = group_details['ROLE']['ROLE_CD']
        role_name = group_details['ROLE']['NAME']
        group_cd = group_details['GROUP_CD']
        user_id = group_details['ID']
        tenant_id = COMMON_KEY.convert_string_to_id(BuiltIn().get_variable_value("${tenant_id}"))

        payload = {
            "IS_ENABLED": secrets.choice([True, False]),
            "GROUP_CD": group_cd,
            "NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "DESCRIPTION": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
            "VERSION": 1,
            "ID": user_id,
            "IS_DELETED": False,
            "ROLE": {
                "ID": role_id,
                "TENANT_ID": tenant_id,
                "ROLE_CD": role_cd,
                "NAME": role_name,
                "IS_ENABLED": True,
                "IS_DELETED": False,
                "CREATED_DATE": None,
                "CREATED_BY": None,
                "MODIFIED_DATE": None,
                "MODIFIED_BY": None,
                "VERSION": 1
            }

        }
        details = BuiltIn().get_variable_value("${user_group_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print(payload)
        return payload
