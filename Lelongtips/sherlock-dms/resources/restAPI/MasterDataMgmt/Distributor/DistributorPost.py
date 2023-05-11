from random import random
import datetime
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import random
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from faker import Faker
from setup.hanaDB import HanaDB
from resources.restAPI.Config.DynamicHierarchy.GeoHierarchy import AssignDistributorPost

FAKE = Faker()

END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorPost(object):
    @keyword('user creates distributor with given data')
    def user_creates_route_with(self):
        url = "{0}distributors".format(END_POINT_URL)
        payload = self.payload_distributor()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            distributor_id = body_result['ID']
            BuiltIn().set_test_variable("${distributor_id}", distributor_id)
            # distributor_id = distributor_id.replace(":", "")
            # distributor_id = distributor_id.replace("-", "")
            # query = "SELECT F.FIELD, R.FIELD_VALUE FROM MODULE_DATA_FIELDS R INNER JOIN METADATA_FIELD F\
            #        ON R.FIELD_ID = F.ID WHERE R.ROW_ID IN (SELECT ROW_ID FROM MODULE_DATA_FIELDS R\
            #        INNER JOIN METADATA_FIELD F ON R.FIELD_ID = F.ID INNER JOIN MODULE_DATA_ROWS D\
            #        ON D.MODULE_ID = F.MODULE_ID WHERE F.MODULE_ID= (SELECT ID FROM METADATA_MODULE WHERE LOGICAL_ID='distributors' AND IS_DELETED=false)\
            #        AND R.ROW_ID LIKE '%{0}%' AND D.IS_DELETED=false GROUP BY ROW_ID)".format(distributor_id)
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().row_count_is_greater_than_x(query, 1)
            # HanaDB.HanaDB().disconnect_from_database()
            """ If error occurs during virtual warehouse creation/IAS user creation, above query will fail"""
            BuiltIn().set_test_variable("${dist_cd}", body_result['DIST_CD'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_distributor(self):
        LOCALITY = BuiltIn().get_variable_value("&{LOCALITY}")
        STATE = BuiltIn().get_variable_value("&{STATE}")
        COUNTRY = BuiltIn().get_variable_value("&{COUNTRY}")
        PRICE_GRP = BuiltIn().get_variable_value("&{PRICE_GRP}")
        OTH_PRICE_GRP = BuiltIn().get_variable_value("&{OTH_PRICE_GRP}")
        TIMEZONE = BuiltIn().get_variable_value("&{TIME_ZONE}")
        TIMEZONE = TIMEZONE["TIMEZONE"]
        REPLENISHMENT_METHOD = BuiltIn().get_variable_value("&{REPLENISHMENT_METHOD}")
        REPLENISHMENT_METHOD = REPLENISHMENT_METHOD["REPLENISHMENT_METHOD"]
        TODAYSDATE = self.current_account_date()
        payload = {
            "DIST_ADMIN_LOGIN_ID": ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20)),
            "DIST_ADMIN_NAME": ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20)),
            "DIST_ADMIN_EMAIL": f'{FAKE.word()}{FAKE.email()}',
            "DIST_CD": ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(10)),
            "DIST_NAME": ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20)),
            "ADDRESS_CD": {
                "ADD1": ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20)),
                "ADD2": ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20)),
                "ADD3": ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZDRGSERGREGERG') for _ in range(20)),
                "POST_CD": ''.join(random.choice('0123456789') for _ in range(7)),
                "LOCALITY": LOCALITY,
                "STATE": STATE,
                "COUNTRY": COUNTRY,
            },
            "MAIN_DIST_IND": False,
            "SUB_DIST_IND": False,
            "DIST_STATUS": True,
            "BRANCH_IND": False,
            "PRICE_GRP": PRICE_GRP,
            "OTH_PRICE_GRP": OTH_PRICE_GRP,
            "DIST_OPEN_DT": TODAYSDATE,
            "TIMEZONE": TIMEZONE,
            "REPLENISHMENT_METHOD": REPLENISHMENT_METHOD,
        }
        payload = json.dumps(payload)
        print("Distributor Payload: ", payload)
        return payload

    def current_account_date(self):
        today = datetime.datetime.now()
        choose_date = today.strftime("%Y-%m-%d")
        return choose_date

    def user_assign_distributor_to_geotree_with_started_date(self):
        """ Function to assign route to geo tree and patch start date """
        # AssignDistributorPost.AssignDistributorPost().user_add_dist_to_geotree()
        AssignDistributorPost.AssignDistributorPost().user_assign_dist_user_to_geotree()
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        dist_id = dist_id.replace(":", "")
        dist_id = dist_id.replace("-", "")
        today_date = datetime.datetime.today().strftime("%Y-%m-%d")
        query = "UPDATE HIER_GEO_USER_ASSIGN SET START_DATE='{0}' WHERE USER_ID='{1}'".format(today_date, dist_id)
        # HanaDB.HanaDB().connect_database_to_environment()
        # HanaDB.HanaDB().execute_sql_string(query)
        # HanaDB.HanaDB().disconnect_from_database()
