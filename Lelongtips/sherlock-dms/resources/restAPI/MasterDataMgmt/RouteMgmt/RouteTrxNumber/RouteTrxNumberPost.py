from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from setup.hanaDB import HanaDB
import json
import secrets
import pandas as pd
import datetime
NOW = datetime.datetime.now()
END_POINT_URL = PROTOCOL + "profile-route" + APP_URL


class RouteTrxNumberPost(object):
    """ Functions for creating route transaction number """
    ROUTE_TRX_DETAILS = "${route_trx_no_details}"
    DT_FORMAT = "%Y-%m-%d"
    TRIAL = 0

    @keyword('user creates route transaction number with ${data_type} data')
    def user_creates_route_trans_num_with_data(self, data_type):
        """ Functions to create route transaction number with random/fixed data """
        route_id = BuiltIn().get_variable_value("${route_id}")
        url = "{0}route/{1}/transactionnumber-route".format(END_POINT_URL, route_id)
        payload = self.payload_route_trans("create random")
        payload_dump = json.dumps(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload_dump)
        print(response.text)
        if response.status_code == 404:
            while self.TRIAL < 4:
                self.TRIAL = self.TRIAL + 1
                start_dt = pd.to_datetime(payload['START_DT'], format=self.DT_FORMAT)
                start_dt = ((start_dt + datetime.timedelta(days=365)).strftime(self.DT_FORMAT))
                end_dt = pd.to_datetime(payload['END_DT'], format=self.DT_FORMAT)
                end_dt = ((end_dt + datetime.timedelta(days=500)).strftime(self.DT_FORMAT))
                update_dates = {
                    "START_DT": start_dt,
                    "END_DT": end_dt
                }
                details = BuiltIn().get_variable_value(self.ROUTE_TRX_DETAILS)
                if details is None:
                    details = update_dates
                else:
                    details.update(update_dates)
                BuiltIn().set_test_variable(self.ROUTE_TRX_DETAILS, details)
                payload = self.payload_route_trans("create random")
                payload_dump = json.dumps(payload)
                common = APIMethod.APIMethod()
                response = common.trigger_api_request("POST", url, payload_dump)
                if response.status_code == 200:
                    break
        print("Route Trx Num Payload: ", payload_dump)
        if response.status_code == 200:
            body_result = response.json()
            print("Route Trx Num Response: ", body_result)
            res_bd_route_trxno_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_route_trxno_id}", res_bd_route_trxno_id)
            BuiltIn().set_test_variable("${res_bd_route_trxno}", body_result)
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("transactionnumber-route", body_result)
            # HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_route_trans(self, type):
        """ distributor route transaction number payload content """
        end_num = str(secrets.choice(range(100000, 10000000)))
        payload = {
            "PRIME_FLAG": secrets.choice(["PRIME", "NON_PRIME"]),
            "ROUTE_ID": str(BuiltIn().get_variable_value("${route_id}")),
            "TXN_TYPE": secrets.choice(["RETURN", "SALES_ORDER", "SAMPLING_SALES_ORDER", "VAN_SALES", "SAMPLING_VAN_SALES"]),
            "PREFIX": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVXYZ') for _ in range(5)),
            'START_NUM': int(secrets.choice(range(1, 99999))),
            'END_NUM': int(end_num),
            'TXN_NUMBERLEN': len(end_num),
            'SUFFIX': ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVXYZ') for _ in range(5)),
            'START_DT': ((NOW + datetime.timedelta(days=365)).strftime(self.DT_FORMAT)),
            'END_DT': ((NOW + datetime.timedelta(days=500)).strftime(self.DT_FORMAT))
        }
        res_bd_route_trxno = BuiltIn().get_variable_value("${res_bd_route_trxno}")
        if type == 'update random':
            payload['PRIME_FLAG'] = res_bd_route_trxno['PRIME_FLAG']
        details = BuiltIn().get_variable_value(self.ROUTE_TRX_DETAILS)
        if details:
            payload.update((k, v) for k, v in details.items())
        return payload
