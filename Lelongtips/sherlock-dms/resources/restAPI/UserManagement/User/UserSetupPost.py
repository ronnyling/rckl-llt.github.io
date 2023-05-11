import json
import secrets
import random
import re
import string
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker

from resources import COMMON_KEY
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL
from setup.hanaDB import HanaDB

fake = Faker()

END_POINT_URL = PROTOCOL + "user-info" + APP_URL


class UserSetupPost(object):

    @keyword("user creates user setup using ${data_type} data")
    def user_creates_user_setup_using_data(self, data_type):
        url = "{0}user".format(END_POINT_URL)
        print(url)
        common = APIMethod.APIMethod()
        payload = self.payload_user_setup()
        response = common.trigger_api_request("POST", url, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        try:
            data = response.json()
            print("Newly created user data: " + str(data))
            print("ID:", data['ID'], "ROLE:", data['ROLE']['NAME'])
            BuiltIn().set_test_variable("${user_id}", data['ID'])
            BuiltIn().set_test_variable("${res_bd_user}", data)
            return data['ID'], str(response.status_code),  data['ROLE']['NAME']
        except Exception as e:
            print(e.__class__, "occured")
            return " ", str(response.status_code), print(response.text)


    def payload_user_setup(self):
        role_details = BuiltIn().get_variable_value("${role_details}")
        if role_details is None :
            user = BuiltIn().get_variable_value("${user_role}")
            if user == "distadm":
                role = secrets.choice(['DIST_SLSMAN', 'DIST_OPERATOR'])
            elif user == "hqadm":
                role = secrets.choice(['HQ_ADMIN', 'HQ_USER'])
            else:
                role = secrets.choice(['SYS_IMPLEMENTER', 'HQ_ADMIN', 'HQ_USER'])
        else :
            role = role_details['ROLE']
        self.retrieve_role_details(role)
        # role_id = COMMON_KEY.convert_string_to_id(BuiltIn().get_variable_value("${role_id}"))
        role_name = COMMON_KEY.convert_string_to_id(BuiltIn().get_variable_value("${role_name}"))
        # tenant_id = COMMON_KEY.convert_string_to_id(BuiltIn().get_variable_value("${tenant_id}"))
        role_id = BuiltIn().get_variable_value("${role_id}")
        tenant_id = BuiltIn().get_variable_value("${tenant_id}")
        payload = {
              "IS_LICENSED": True,
              "IS_ENABLED": secrets.choice([True, False]),
              "LOGIN_ID": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
              "NAME": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(15)),
              "CONTACT_NO":  ''.join(secrets.choice('0123456789') for _ in range(10)),
              "ROLE": {
                "ID": role_id,
                "TENANT_ID": tenant_id,
                "ROLE_CD": role,
                "NAME": role_name,
                "IS_ENABLED": True,
                "IS_DELETED": False,
                "CREATED_DATE": None,
                "CREATED_BY": None,
                "MODIFIED_DATE": None,
                "MODIFIED_BY": None,
                "VERSION": 1
              },
              "EMAIL": f'qa_{fake.word()}_{fake.word()}@accenture.com'
            }
        details = BuiltIn().get_variable_value("${setup_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print(payload)
        return payload

    def retrieve_role_details(self, role):
        """Comment out hana db script, change it to retrieve by API"""
        # query = "SELECT CAST(ID as VARCHAR),CAST(NAME as VARCHAR),CAST(TENANT_ID as VARCHAR) from IDT_ROLE WHERE ROLE_CD ='{0}' ".format(role)
        # print('QUERY',query)
        # HanaDB.HanaDB().connect_database_to_environment()
        # result = HanaDB.HanaDB().fetch_all_record(query)
        # HanaDB.HanaDB().disconnect_from_database()
        # body_result = result[0]
        # BuiltIn().set_test_variable("${role_id}", body_result[0])
        # BuiltIn().set_test_variable("${role_name}", body_result[1])
        # BuiltIn().set_test_variable("${tenant_id}", body_result[2])

        """Changed to retrieve user role based on role code by API"""
        url = "{0}user-role".format(END_POINT_URL)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()

        role_listing = json.dumps(body_result)
        role_listing_converted = json.loads(role_listing)

        role_details = [x for x in role_listing_converted if x['ROLE_CD'] == role]

        BuiltIn().set_test_variable("${role_id}", body_result[role_details]["ID"])
        BuiltIn().set_test_variable("${role_name}", body_result[role_details]["NAME"])
        BuiltIn().set_test_variable("${tenant_id}", body_result[role_details]["TENANT_ID"])
