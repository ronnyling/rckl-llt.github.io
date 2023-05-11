import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import json
from datetime import datetime

CREATED_DATE=""
MODIFIED_DATE=""

END_POINT_URL = PROTOCOL + "perf-mgt" + APP_URL


class SFADashboardSetupPost(object):

    DEL_REP = "3ED405B3:EF51FA2A-5C57-4E26-8467-B30C80A1C423"
    @keyword('user creates dashboard with ${data_type} data')
    def user_creates_dashboard_with(self, data_type):
        url = "{0}advance-kpi".format(END_POINT_URL)
        payload = self.payload_dashboard("create")
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            body_result = response.json()
            BuiltIn().set_test_variable("${res_bd_dashboard_payload}", body_result)
            BuiltIn().set_test_variable("${res_bd_dashboard_id}", body_result["ID"])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_dashboard(self, action):
        details = BuiltIn().get_variable_value("${dashboard_details}")
        new_details = BuiltIn().get_variable_value("${new_dashboard_details}")
        new_sequence = BuiltIn().get_variable_value("${new_sequence_details}")
        new_type = BuiltIn().get_variable_value("${new_dashboard_type}")
        invoices = False
        collection = False
        SEQ = None
        if details is not None:
            PROFILE_CODE = details['PROFILE_CODE']
            PROFILE_DESC = details['PROFILE_DESC']
            DASHBOARD_CODE = details['DASHBOARD_CODE']
            DASHBOARD_NAME = details['DASHBOARD_NAME']
            DASHBOARD_DESC = details['DASHBOARD_DESC']
            CARD = details['CARD']
            GRAPH = details['GRAPH']

        else :
            PROFILE_CODE = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
            PROFILE_DESC = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))
            DASHBOARD_CODE = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
            DASHBOARD_NAME = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            DASHBOARD_DESC = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))
            CARD = 0
            GRAPH = 0

        if action == "edit" :
            if new_details is not None:
                CARD = new_details['CARD']
                GRAPH = new_details['GRAPH']

            if new_sequence is not None:
                SEQ = new_sequence['SEQ']

            if new_type is not None:
                DASHBOARD_CODE = new_type['DASHBOARD_CODE']
                DASHBOARD_NAME = new_type['DASHBOARD_NAME']
                DASHBOARD_DESC = new_type['DASHBOARD_DESC']
        if CARD == "1":
            invoices = True
        elif CARD == "2":
            collection = True
            invoices = True


        self.CREATED_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S.000')
        self.MODIFIED_DATE= datetime.now().strftime('%Y-%m-%d %H:%M:%S.000')

        payload = {
            "PROFILE": {
                "ID": self.DEL_REP,
                "PROFILE_CODE": PROFILE_CODE,
                "PROFILE_DESC": PROFILE_DESC,
                "OP_TYPE": "L",
                "IS_DELETED": False,
                "MODIFIED_DATE": self.MODIFIED_DATE,
                "MODIFIED_BY": "54AAA1DF29687E32ACA648C2A32351841624CA0A",
                "CREATED_DATE": self.CREATED_DATE,
                "CREATED_BY": "system_core",
                "VERSION": 1,
                "CORE_FLAGS": "C"
            },
            "DASHBOARD": {
                "ID": "B9C56BEF:34C8962A-FF87-4D02-BA9F-14D10A942551",
                "DASHBOARD_CODE": DASHBOARD_CODE,
                "DASHBOARD_NAME": DASHBOARD_NAME,
                "PROFILE": self.DEL_REP,
                "CARD": 4,
                "CHART": 0,
                "DASHBOARD_DESC": DASHBOARD_DESC,
                "GRID": 0,
                "IS_DELETED": False,
                "MODIFIED_DATE": self.MODIFIED_DATE,
                "MODIFIED_BY": "54AAA1DF86DE7E6CD4F746E1869A52019117070C",
                "CREATED_DATE": self.CREATED_DATE,
                "CREATED_BY": "system_core",
                "VERSION": 5,
                "CORE_FLAGS": "C"
            },
            "CARD": CARD,
            "GRAPH": GRAPH,
            "GRID": "0",
            "ADVANCE_KPI": [
                {
                    "ID": "C72BB59D:5A306E17-03DC-4CA2-AB29-1FE9EBAE1A16",
                    "KPI_ID": "KP18",
                    "KPI_CODE": "INVOICES",
                    "KPI_DESC": "Invoices for Delivery",
                    "CARD": invoices,
                    "GRAPH": False,
                    "PROFILE": [
                        self.DEL_REP
                    ],
                    "GRID": False,
                    "IS_DELETED": False,
                    "MODIFIED_DATE": self.MODIFIED_DATE,
                    "MODIFIED_BY": "54AAA1DF86DE7E6CD4F746E1869A52019117070C",
                    "CREATED_DATE": self.CREATED_DATE,
                    "CREATED_BY": "system_core",
                    "VERSION": 3,
                    "CORE_FLAGS": "C",
                    "SEQ": SEQ
                },
                {
                    "ID": "C72BB59D:A338B752-F13F-4993-A9E5-9669C45F6613",
                    "KPI_ID": "KP19",
                    "KPI_CODE": "RETURN_COLLECTION",
                    "KPI_DESC": "Collection of Arranged Return",
                    "CARD": collection,
                    "GRAPH": False,
                    "PROFILE": [
                        self.DEL_REP
                    ],
                    "GRID": False,
                    "IS_DELETED": False,
                    "MODIFIED_DATE": self.MODIFIED_DATE,
                    "MODIFIED_BY": "54AAA1DF86DE7E6CD4F746E1869A52019117070C",
                    "CREATED_DATE": self.CREATED_DATE,
                    "CREATED_BY": "system_core",
                    "VERSION": 3,
                    "CORE_FLAGS": "C",
                    "SEQ": None
                },
                {
                    "ID": "C72BB59D:84B829EB-8DBA-4026-A138-88746D281155",
                    "KPI_ID": "KP21",
                    "KPI_CODE": "STORES",
                    "KPI_DESC": "No. of Stores",
                    "CARD": False,
                    "GRAPH": False,
                    "PROFILE": [
                        self.DEL_REP
                    ],
                    "GRID": False,
                    "IS_DELETED": False,
                    "MODIFIED_DATE": self.MODIFIED_DATE,
                    "MODIFIED_BY": "54AAA1DF86DE7E6CD4F746E1869A52019117070C",
                    "CREATED_DATE": self.CREATED_DATE,
                    "CREATED_BY": "system_core",
                    "VERSION": 3,
                    "CORE_FLAGS": "C",
                    "SEQ": None
                }
            ]
        }

        payload = json.dumps(payload)
        print("Dashboard Payload: ", payload)
        return payload






