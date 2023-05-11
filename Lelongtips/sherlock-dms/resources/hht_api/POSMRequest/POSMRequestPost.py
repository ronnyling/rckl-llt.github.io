import json
import random
import secrets
from resources.restAPI.Common import APIMethod, APIAssertion
from datetime import datetime, timedelta
from resources.restAPI.Common import TokenAccess
from robot.libraries.BuiltIn import BuiltIn
from setup.yaml.YamlDataManipulator import YamlDataManipulator
from resources.Common import Common

URL = 'https://mobile-comm-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.0/transaction'
TXN_NAME = 'TXN_MERC_POSM_MAT_REQ'

class POSMRequestPost(object):

    def get_request_type(self, request_type):
        if request_type == 'installation':
            return 'POSM_INS'
        elif request_type == 'removal':
            return 'POSM_REM'
        else:
            return 'POSM_MAI'

    def user_creates_posm_request_with(self):
        details = BuiltIn().get_variable_value("${RequestDetails}")

        # Hardcoded due to Get Function not available
        BuiltIn().set_test_variable("${route_id}", "02C42079:B8134E0D-7086-4931-9A0D-C4667507218E")
        BuiltIn().set_test_variable("${customer_id}", "81398E09:AA0D3769-B52E-4E0C-9C82-7953737B8BED")
        BuiltIn().set_test_variable("${user_id}", "BEB19326:CA5345F4-035A-479E-A6F5-B6A429D810B7")
        BuiltIn().set_test_variable("${rp_id}", "F30DE957:98B0B7B9-8177-402C-97C5-D080BB085675")
        BuiltIn().set_test_variable("${req_reason_id}", "7AB3B033:30B8124A-192F-4600-B3AA-873BB187A583")
        BuiltIn().set_test_variable("${prd_id}", "D34A04AD:06ED78DE-15F0-4AF9-BE2D-88A57297390A")
        BuiltIn().set_test_variable("${prd_uom_id}", "5D04252C:38AFBBC6-28A9-4F19-81E2-D463D3989689")
        ######
        TokenAccess.TokenAccess().user_retrieves_token_access_as("salesperson")
        Common().get_tenant_id()
        payload = self.posm_material_request_payload(details)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", URL, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        APIAssertion.APIAssertion().expected_return_status_code("200")
        body_result = {'ID': BuiltIn().get_variable_value('${requestID}')}
        BuiltIn().set_test_variable('${body_result}', body_result)
        print('payload2: ', payload)

    def posm_material_request_payload(self, detail):
        request_hdr = YamlDataManipulator().user_retrieves_data_from_yaml('2-POSMRequestPayload.yaml', 'TXN_MERC_POSM_MAT_REQHDR')
        request_dtl = YamlDataManipulator().user_retrieves_data_from_yaml('2-POSMRequestPayload.yaml', 'TXN_MERC_POSM_MAT_REQDTL')
        posm_req_id = Common().generate_random_id(request_hdr['ID'][0])
        BuiltIn().set_test_variable("${requestID}", posm_req_id)

        payload = {
            "Comm": {
                "MsgID": str(secrets.choice(range(1, 9999))),
                "RequestDT": datetime.today().strftime('%Y-%m-%d'),
                "TenantID": BuiltIn().get_variable_value("${tenant_id}"),
                "AppID": "SFA",
                "HardwareID": "NP1234567891",
                "EngVersion": "8.7.64.0",
                "AppVersion": "1.1.0",
                "Type": "TRANSACTION",
                "Name": TXN_NAME
            },
            "Payload": {
                "Schema": {
                    "Header": {
                        "Name": "TXN_MERC_POSM_MAT_REQHDR",
                        "Columns": [keys for keys in request_hdr]
                    },
                    "Detail": [
                        {
                            "Name": "TXN_MERC_POSM_MAT_REQDTL",
                            "Columns": [keys for keys in request_dtl]
                        }
                    ]
                },
                "Data": [
                    {
                        "Header": {
                            "Name": "TXN_MERC_POSM_MAT_REQHDR",
                            "Record": [
                                posm_req_id,
                                BuiltIn().get_variable_value("${tenant_id}"),
                                BuiltIn().get_variable_value("${distributor_id}"),
                                BuiltIn().get_variable_value("${route_id}"),
                                BuiltIn().get_variable_value("${rp_id}"),
                                BuiltIn().get_variable_value("${customer_id}"),
                                BuiltIn().get_variable_value("${user_id}"),
                                'AutomationRequest_' + str(secrets.choice(range(1, 9999))),
                                self.get_request_type(detail['request_type']),
                                secrets.choice(['T', 'P']),
                                BuiltIn().get_variable_value("${req_reason_id}"),
                                "",
                                (datetime.today()).strftime('%H:%M:%S.000'),
                                (datetime.today() + timedelta(hours=1)).strftime('%H:%M:%S.000'),
                                "",
                                detail['txn_status'],
                                datetime.today().strftime('%Y-%m-%d'),
                                datetime.today().strftime('%Y-%m-%d %H:%M:%S.000'),
                                secrets.choice(range(1, 20)),
                                "5C64EC92:76AF9E9F-DF6F-495D-ADF8-5B0441678824",    #Unsure logic - hardcoded
                                ''.join(secrets.choice('0123456789ABCDEF') for _ in range(40))
                            ]
                        },
                        "Detail": [
                            {
                                "Name": "TXN_MERC_POSM_MAT_REQDTL",
                                "Record": [
                                    [
                                        Common().generate_random_id(request_dtl['ID'][0]),
                                        posm_req_id,
                                        BuiltIn().get_variable_value('${prd_id}'),
                                        None,
                                        BuiltIn().get_variable_value('${prd_uom_id}'),
                                        secrets.choice(range(1, 20)),
                                        secrets.choice(range(1, 20)),
                                        secrets.choice(range(1, 20)),
                                        secrets.choice(range(1, 20)),
                                        secrets.choice(["0", "1"])
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            }
        }
        payload = json.dumps(payload)
        return payload


