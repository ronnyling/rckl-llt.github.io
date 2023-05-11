import json
import random
import secrets
from resources.restAPI.Common import APIMethod, APIAssertion
from faker import Faker
from datetime import datetime, timedelta
from resources.restAPI.Common import TokenAccess
from robot.libraries.BuiltIn import BuiltIn
from setup.yaml.YamlDataManipulator import YamlDataManipulator
from resources.Common import Common

fake = Faker()
URL = 'https://mobile-comm-svc-qa.cfapps.jp10.hana.ondemand.com/api/v1.0/transaction'
TXN_NAME = 'TXN_MERC_POSM_NEWINSTALL'

class POSMInstallationPost(object):
    POSMINSTALL_YAML_FILE = '2-POSMInstallationPayload.yaml'
    DATE_FORMAT = '%Y-%m-%d'
    def user_creates_posm_installation_with(self):
        details = BuiltIn().get_variable_value("${InstallDetails}")

        # Hardcoded due to Get Function not available
        BuiltIn().set_test_variable("${route_id}", "02C42079:B8134E0D-7086-4931-9A0D-C4667507218E")
        BuiltIn().set_test_variable("${customer_id}", "81398E09:AA0D3769-B52E-4E0C-9C82-7953737B8BED")
        BuiltIn().set_test_variable("${user_id}", "BEB19326:CA5345F4-035A-479E-A6F5-B6A429D810B7")
        BuiltIn().set_test_variable("${rp_id}", "F30DE957:98B0B7B9-8177-402C-97C5-D080BB085675")
        BuiltIn().set_test_variable("${req_reason_id}", "7AB3B033:30B8124A-192F-4600-B3AA-873BB187A583")
        BuiltIn().set_test_variable("${warehouse_id}", "ECB38BFC:37D1A7FC-C1F3-45CF-9740-49FF3B6CBBEC")
        BuiltIn().set_test_variable("${prd_id}", "D34A04AD:06ED78DE-15F0-4AF9-BE2D-88A57297390A")
        BuiltIn().set_test_variable("${prd_uom_id}", "5D04252C:38AFBBC6-28A9-4F19-81E2-D463D3989689")
        ######
        TokenAccess.TokenAccess().user_retrieves_token_access_as("salesperson")
        Common().get_tenant_id()
        common = APIMethod.APIMethod()
        payload = self.posm_newinstall_payload(details)
        response = common.trigger_api_request("POST", URL, payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        APIAssertion.APIAssertion().expected_return_status_code("200")
        body_result = {'ID': BuiltIn().get_variable_value('${installID}')}
        BuiltIn().set_test_variable('${body_result}', body_result)
        print('payload: ', payload)

    def posm_newinstall_payload(self, details):
        install_hdr = YamlDataManipulator().user_retrieves_data_from_yaml(self.POSMINSTALL_YAML_FILE, 'TXN_MERC_POSM_NEWINSTALLHDR')
        install_dtl = YamlDataManipulator().user_retrieves_data_from_yaml(self.POSMINSTALL_YAML_FILE, 'TXN_MERC_POSM_NEWINSTALLPRD')
        install_img = YamlDataManipulator().user_retrieves_data_from_yaml(self.POSMINSTALL_YAML_FILE, 'TXN_MERC_POSM_NEWINSTALLIMG')
        with_route = secrets.choice(['WR', 'WOR'])
        new_install_id = Common().generate_random_id(install_hdr['ID'][0])
        BuiltIn().set_test_variable("${installID}", new_install_id)

        payload = {
            "Comm": {
                "MsgID": str(secrets.choice(range(1, 9999))),
                "RequestDT": datetime.today().strftime(self.DATE_FORMAT),
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
                        "Name": "TXN_MERC_POSM_NEWINSTALLHDR",
                        "Columns": [keys for keys in install_hdr]
                    },
                    "Detail": [
                        {
                            "Name": "TXN_MERC_POSM_NEWINSTALLPRD",
                            "Columns": [keys for keys in install_dtl]
                        },
                        {
                            "Name": "TXN_MERC_POSM_NEWINSTALLIMG",
                            "Columns": [keys for keys in install_img]
                        }
                    ]
                },
                "Data": [
                    {
                        "Header": {
                            "Name": "TXN_MERC_POSM_NEWINSTALLHDR",
                            "Record": [
                                new_install_id,
                                BuiltIn().get_variable_value("${tenant_id}"),
                                BuiltIn().get_variable_value("${distributor_id}"),
                                BuiltIn().get_variable_value('${route_id}') if with_route == 'WR' else None,
                                BuiltIn().get_variable_value('${customer_id}'),
                                BuiltIn().get_variable_value('${user_id}'),
                                'AutomationNewInstall_' + str(secrets.choice(range(1, 9999))),
                                with_route,
                                BuiltIn().get_variable_value('${rp_id}'),
                                details['txn_status'],
                                datetime.today().strftime(self.DATE_FORMAT),
                                datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                                BuiltIn().get_variable_value('${requestID}'),
                                secrets.choice(['D', 'T', 'P']),
                                BuiltIn().get_variable_value('${route_id}') if with_route == 'WR' else None,
                                datetime.today().strftime(self.DATE_FORMAT),
                                datetime.today().strftime(self.DATE_FORMAT),
                                (datetime.today()).strftime('%H:%M'),
                                (datetime.today() + timedelta(hours=1)).strftime('%H:%M'),
                                datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                                BuiltIn().get_variable_value('${req_reason_id}'),
                                None,
                                BuiltIn().get_variable_value('${warehouse_id}'),
                                "",
                                "",
                                secrets.choice(range(1, 20)),
                                "5C64EC92:F52FD919-BE11-4C37-A524-2CBA2A95F354",        #Unsure Logic
                                ''.join(secrets.choice('0123456789ABCDEF') for _ in range(40))
                            ]
                        },
                        "Detail": [
                            {
                                "Name": "TXN_MERC_POSM_NEWINSTALLPRD",
                                "Record": [
                                    [
                                        Common().generate_random_id(install_dtl['ID'][0]),
                                        new_install_id,
                                        BuiltIn().get_variable_value('${prd_id}'),
                                        None,
                                        BuiltIn().get_variable_value('${prd_uom_id}'),
                                        secrets.choice(range(1, 20)),
                                        secrets.choice(range(1, 20)),
                                        secrets.choice(range(1, 20)),
                                        False
                                    ]
                                ]
                            },
                            {
                                "Name": "TXN_MERC_POSM_NEWINSTALLIMG",
                                "Record": []
                            }
                        ]
                    }
                ]
            }
        }
        payload = json.dumps(payload)
        return payload


