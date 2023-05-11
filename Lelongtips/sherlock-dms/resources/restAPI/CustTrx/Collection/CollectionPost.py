import json
import secrets
import datetime
import logging

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.Bank.BankGet import BankGet
from resources.Common import Common
from setup.hanaDB import HanaDB
from random import randint

current_date = datetime.datetime.today().strftime('%Y-%m-%d')
END_POINT_URL = PROTOCOL + "collection" + APP_URL
DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


class CollectionPost(object):
    """ Functions to create collection """

    @keyword('user creates collection with ${type} data')
    def user_creates_collection(self, type):
        """ Function to create collection with random/fixed data"""
        res_bd_inv = BuiltIn().get_variable_value("${res_bd_invoice_body_result}")
        dist_id = res_bd_inv['TXN_HEADER']['DIST_ID']
        cust_id = res_bd_inv['TXN_HEADER']['CUST_ID']
        route_id = res_bd_inv['TXN_HEADER']['ROUTE_ID']
        prime_flag = res_bd_inv['TXN_HEADER']['PRIME_FLAG']
        is_future = False
        if type == "future":
            is_future = True

        url = "{0}distributors/{1}/collection-data".format(END_POINT_URL, dist_id)
        payload = self.get_collection_payload(cust_id, route_id, prime_flag, is_future)
        common = APIMethod.APIMethod()
        headers = {
            'np-session': "27ea0ccb:688a61a9-80e1-4c6f-bae6-d2a6d28ceee6"
        }
        print("payload = ", payload)
        print("endpoint = ", url)
        print("json payload", json.dumps(payload))
        logging.warning(f'Payload#{json.dumps(payload)}')
        logging.warning(f'Endpoint#{url}')
        time_one = Common().get_local_time()
        logging.warning(f'Time before POST#{time_one}')
        print("time before post = ", time_one)
        response = common.trigger_api_request("POST", url, json.dumps(payload), **headers)
        time_post = Common().get_local_time()
        logging.warning(f'Time after POST#{time_post}')
        print("time after post = ", time_post)
        if response.status_code == 202:
            current_time = Common().get_local_time()
            logging.warning(f'Time#{current_time}')
            print("current time = ", current_time)
            current_time = datetime.datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%S.000Z').strftime(DATE_FORMAT)
            current_time = datetime.datetime.strptime(current_time, DATE_FORMAT)
            logging.warning(f'Time2#{current_time}')
            print("current time 2 = ", current_time)
            ten_min_before = current_time - datetime.timedelta(minutes=30)
            ten_min_after = current_time + datetime.timedelta(minutes=30)

            query = "select CAST(ID as VARCHAR) from TXN_COLHDR where DIST_ID = '{0}' AND " \
                    "ROUTE_ID = '{1}' AND CUST_ID = '{2}' " \
                    "AND TXN_DT = '{3}' AND TTL_CASH = '{4}' "\
                    "AND TXN_CREATED_DT BETWEEN '{5}' AND '{6}'"\
                .format(Common().convert_id_to_string(dist_id), Common().convert_id_to_string(payload[0]['ROUTE_ID']),
                        Common().convert_id_to_string(payload[0]['CUST_ID']), current_date, payload[0]['CASH_AMT'],
                        ten_min_before, ten_min_after)
            query = "select CAST(ID as VARCHAR) from TXN_COLHDR where DIST_ID = '{0}' AND " \
                    "ROUTE_ID = '{1}' AND CUST_ID = '{2}' " \
                    "AND TXN_DT = '{3}' AND TTL_CASH = '{4}' "\
                .format(Common().convert_id_to_string(dist_id), Common().convert_id_to_string(payload[0]['ROUTE_ID']),
                        Common().convert_id_to_string(payload[0]['CUST_ID']), current_date, payload[0]['CASH_AMT'])
            BuiltIn().set_test_variable("${col_query}", query)
            print("db query = ", query)
            logging.warning(f'Query#{query}')
            HanaDB.HanaDB().connect_database_to_environment()
            HanaDB.HanaDB().check_if_exists_in_database_by_query(query)
            col_id = None
            try_count = 1
            while try_count < 300:
                try:
                    logging.warning(f'Attempt#{try_count}')
                    try_count += 1
                    col_id = HanaDB.HanaDB().fetch_one_record(query)
                    break
                except Exception as e:
                    print(e.__class__, "occured")
            assert col_id, "Collection ID is not retrieved"
            BuiltIn().set_test_variable("${collection_id}", col_id)
            created_col = {
                "COL_ID": col_id,
                "CUST_ID": cust_id,
                "ROUTE_ID": route_id,
                "PRIME_FLAG": prime_flag
            }
            BuiltIn().set_test_variable("${created_col}", created_col)
            HanaDB.HanaDB().disconnect_from_database()
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def get_collection_payload(self, cust_id, route_id, prime_flag, is_future):
        """ Function for collection payload"""
        payload = {
                "ROUTE_ID": route_id,
                "CUST_ID": cust_id,
                "CASH_AMT": secrets.randbelow(1000),
                "OTHER_PYMTS": [self.get_payment_payload("", "",is_future)],
                "ADJUSTMENT": secrets.choice([True, False]),
                "PRIME_FLAG": prime_flag
            }
        collection_details = BuiltIn().get_variable_value("${collection_details}")
        if collection_details:
            payload.update((k, v) for k, v in collection_details.items())
        if payload["OTHER_PYMTS"] == "[]":
            payload["OTHER_PYMTS"] = []

        other_payment = BuiltIn().get_variable_value("${other_payment}")
        if other_payment:
            payload["OTHER_PYMTS"] = []
            payment_list = other_payment.split(",")
            for payment in payment_list:
                payment = payment.split("=")
                payload['OTHER_PYMTS'].append(self.get_payment_payload(payment[0], int(payment[1]), is_future))

        payload = [payload]
        print("Collection Payload: ", payload)
        return payload

    def get_payment_payload(self, payment_type, payment_amount, is_future):
        if payment_type == "":
            payment_type = secrets.choice(["Q", "B", "W"])
        if payment_amount == "":
            payment_amount = secrets.randbelow(100)

        BankGet().user_retrieves_all_bank()
        rand_bank = BuiltIn().get_variable_value("${rand_bank_selection}")
        payment_payload = {
            "OTHER_PYMT_METHOD": payment_type,
            "CHEQUE_AMT": payment_amount,
            "CHEQUE_DATE": current_date,
            "DRAWEE_BANK_ID": rand_bank,
            "CHEQUE_NO": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
        }
        payment_details = BuiltIn().get_variable_value("${payment_details}")
        if is_future:
            payment_details['CHEQUE_DATE'] = '2030-01-01'
        if payment_details:
            payment_payload.update((k, v) for k, v in payment_details.items())

        if payment_type == "W":
            payment_payload["PAY_REF_ING"] = {
                "FILE_NAME": "test.jpg",
                "FILE_SIZE": 115.71,
                "FILE_TYPE": "image/jpeg",
                "URL": "/objectstore-svc/api/v1.0/storage/collection-ewallet/PAY_REF_IMG/test-1610440694075.jpg",
                "DESCRIPTION": ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
            }
        return payment_payload

