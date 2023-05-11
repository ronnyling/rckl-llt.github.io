from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from setup.hanaDB import HanaDB
import json
import secrets
import pandas as pd
import datetime
NOW = datetime.datetime.now() + datetime.timedelta(days=1)
TOMORROW = NOW + datetime.timedelta(days=1)
END_POINT_URL = PROTOCOL + "profile-dist" + APP_URL


class DistributorTrxNumPost(object):
    """ Functions for creating distributor transaction number """
    DIST_TRX_DETAILS = "${dist_trx_no_details}"
    DT_FORMAT = "%Y-%m-%d"
    TRIAL = 0
    @keyword('user creates distributor transaction number with ${data_type} data')
    def user_creates_distributor_trans_num_with_data(self, data_type):
        """ Functions to create distributor transaction number with random/fixed data """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/transactionnumber".format(END_POINT_URL, distributor_id)
        payload = self.payload_dist_trans("create random")
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
                details = BuiltIn().get_variable_value(self.DIST_TRX_DETAILS)
                if details is None:
                    details = update_dates
                else:
                    details.update(update_dates)
                BuiltIn().set_test_variable(self.DIST_TRX_DETAILS, details)
                payload = self.payload_dist_trans("create random")
                payload_dump = json.dumps(payload)
                common = APIMethod.APIMethod()
                response = common.trigger_api_request("POST", url, payload_dump)
                if response.status_code == 201:
                    break
        print("Distributor Payload: ", payload_dump)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_dist_trxno_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_dist_trxno_id}", res_bd_dist_trxno_id)
            BuiltIn().set_test_variable("${res_bd_dist_trxno}", body_result)
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().user_validates_database_data("transactionnumber", body_result)
            # HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_dist_trans(self, type):
        """ distributor transaction number payload content """
        end_num = int(secrets.choice(range(100000, 10000000)))
        payload = {
            "PRIME_FLAG": secrets.choice(["PRIME", "NON_PRIME"]),
            "TXN_TYPE": secrets.choice(["SALES_ORDER", "CASH_BILL", "CREDIT_NOTE", "DEBIT_NOTE", "INVOICE", "RETURN", "SAMPLING_SALES_ORDER"]),
            "PREFIX": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVXYZ') for _ in range(5)),
            'START_NUM': int(secrets.choice(range(1, 99999))),
            'END_NUM': end_num,
            'TXN_NUMBERLEN': len(str(end_num)),
            'SUFFIX': ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVXYZ') for _ in range(5)),
            'START_DT': ((TOMORROW + datetime.timedelta(days=365)).strftime(self.DT_FORMAT)),
            'END_DT': ((NOW + datetime.timedelta(days=500)).strftime(self.DT_FORMAT))
        }
        res_bd_dist_trxno = BuiltIn().get_variable_value("${res_bd_dist_trxno}")
        if type == 'update random':
            payload['PRIME_FLAG'] = res_bd_dist_trxno['PRIME_FLAG']
        details = BuiltIn().get_variable_value(self.DIST_TRX_DETAILS)
        if details:
            payload.update((k, v) for k, v in details.items())
        return payload

    def user_creates_random_distributor_trxno(self):
        """ Functions to create distributor transaction number """
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        url = "{0}distributors/{1}/transactionnumber".format(END_POINT_URL, distributor_id)
        payload = self.payload_dist_trans("create random")
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
                details = BuiltIn().get_variable_value(self.DIST_TRX_DETAILS)
                if details is None:
                    details = update_dates
                else:
                    details.update(update_dates)
                BuiltIn().set_test_variable(self.DIST_TRX_DETAILS, details)
                payload = self.payload_dist_trans("create random")
                payload_dump = json.dumps(payload)
                common = APIMethod.APIMethod()
                response = common.trigger_api_request("POST", url, payload_dump)
                if response.status_code == 201:
                    break
        print("Distributor Payload: ", payload_dump)
        if response.status_code == 201:
            body_result = response.json()
            res_bd_dist_trxno_id = body_result['ID']
            BuiltIn().set_test_variable("${res_bd_dist_trxno_id}", res_bd_dist_trxno_id)
            BuiltIn().set_test_variable("${res_bd_dist_trxno}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
