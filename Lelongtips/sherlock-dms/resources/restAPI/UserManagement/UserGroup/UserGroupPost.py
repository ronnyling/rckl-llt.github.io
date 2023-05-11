import json
import secrets
import random
import re
import string
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker

from resources import Common, COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from setup.hanaDB import HanaDB
from setup.sqllite.SQLLite import SQLLite

fake = Faker()

END_POINT_URL = PROTOCOL + "user-info" + APP_URL
err_msg = "Data not purged"

class UserGroupPost(object):

    @keyword("user creates user group using ${data_type} data")
    def user_creates_user_group_using_data(self, data_type):
        url = "{0}user-group".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        payload = self.payload_user_group()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Response Body ", body_result)
            BuiltIn().set_test_variable("${res_bd_user_group}", body_result)
            BuiltIn().set_test_variable("${user_group_id}", body_result['ID'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_user_group(self):
        self.retrieve_user_role()
        # role_id = COMMON_KEY.convert_string_to_id(BuiltIn().get_variable_value("${role_id}"))
        role_cd = COMMON_KEY.convert_string_to_id(BuiltIn().get_variable_value("${role_cd}"))
        role_name = COMMON_KEY.convert_string_to_id(BuiltIn().get_variable_value("${role_name}"))
        # tenant_id = COMMON_KEY.convert_string_to_id(BuiltIn().get_variable_value("${tenant_id}"))
        tenant_id = BuiltIn().get_variable_value("${tenant_id}")
        role_id = BuiltIn().get_variable_value("${role_id}")
        payload = {
            "IS_ENABLED": True,
            "GROUP_CD": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5)),
            "NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "DESCRIPTION":''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15)),
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

    def retrieve_user_role(self):
        """Comment out hana db script, change it to retrieve by API"""
        # query = "SELECT CAST(ID as VARCHAR),CAST(ROLE_CD as VARCHAR),CAST(NAME as VARCHAR),CAST(TENANT_ID as VARCHAR) from IDT_ROLE ORDER BY RAND ( ) LIMIT 1"
        # HanaDB.HanaDB().connect_database_to_environment()
        # result = HanaDB.HanaDB().fetch_all_record(query)
        # HanaDB.HanaDB().disconnect_from_database()
        # body_result = result[0]
        # BuiltIn().set_test_variable("${role_id}", body_result[0])
        # BuiltIn().set_test_variable("${role_cd}", body_result[1])
        # BuiltIn().set_test_variable("${role_name}", body_result[2])
        # BuiltIn().set_test_variable("${tenant_id}", body_result[3])

        """Changed to retrieve random user role by API"""
        url = "{0}user-role".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        if response.status_code == 200:
            body_result = response.json()
            print("Total number of records retrieved are ", len(body_result))
            if len(body_result) > 1:
                rand_user_role = secrets.choice(range(0, len(body_result)))
            else:
                rand_user_role = 0
            print("Rand User Role", rand_user_role)
            # tenant_id = body_result[rand_user_role]["TENANT_ID"]
            BuiltIn().set_test_variable("${role_id}", body_result[rand_user_role]["ID"])
            BuiltIn().set_test_variable("${role_cd}", body_result[rand_user_role]["ROLE_CD"])
            BuiltIn().set_test_variable("${role_name}", body_result[rand_user_role]["NAME"])
            # BuiltIn().set_test_variable("${tenant_id}", tenant_id.replace(":", "").replace("-", ""))
            BuiltIn().set_test_variable("${tenant_id}", body_result[rand_user_role]["TENANT_ID"])
