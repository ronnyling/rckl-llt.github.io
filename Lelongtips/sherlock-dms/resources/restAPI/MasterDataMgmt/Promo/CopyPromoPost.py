from robot.api.deco import keyword
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.MasterDataMgmt.Promo import PromoGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from setup.hanaDB import HanaDB
import json, secrets, datetime

PROMO_END_POINT_URL = PROTOCOL + "promotion" + APP_URL


class CopyPromoPost(object):

    DATE_FORMAT = "%Y-%m-%dT00:00:00.000Z"

    @keyword('user copy promotion with ${type} data')
    def user_copy_promotion_with_data(self, type):
        payload = self.payload_details(type)
        get_status = BuiltIn().get_variable_value("${status_code}")
        print ('get status' , get_status)
        if get_status !=404:
            payload = json.dumps(payload)
            print("Copied Promotion Payload: ", payload)
            url = "{0}copy-promotion".format(PROMO_END_POINT_URL)
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("POST", url, payload)
            if response.status_code == 201:
                body_result = response.json()
                print("Success print result: ", body_result)
                BuiltIn().set_test_variable("${copied_result}", body_result)
                BuiltIn().set_test_variable("${promo_id}", body_result['ID'])
                HanaDB.HanaDB().connect_database_to_environment()
                HanaDB.HanaDB().row_count_is_greater_than_x("SELECT * FROM PROMO where ID = '{0}'".format(body_result['ID']), 1)
                HanaDB.HanaDB().disconnect_from_database()
                result = BuiltIn().get_variable_value("${result}")
                if result:
                    result.append(body_result['ID'])
                else:
                    result = [body_result['ID']]
                BuiltIn().set_test_variable("${result}", result)
            BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)
        else:
            BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, get_status)

    def payload_details(self, type):
        promo_id = BuiltIn().get_variable_value("${promo_id}")
        code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
        if type == 'existing':
            code = BuiltIn().get_variable_value("${promotion_cd}")
        desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code('DistEgg')
        start_time = COMMON_KEY.get_local_time()
        current_time = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.000Z')
        start_time = (current_time + datetime.timedelta(days=1)).strftime(self.DATE_FORMAT)
        end_time = (current_time + datetime.timedelta(days=365)).strftime(self.DATE_FORMAT)
        claim_dt = None
        spacebuy_dt = None
        status = PromoGet.PromoGet().get_promotion()
        BuiltIn().set_test_variable("${status_code}", status)
        if status != 404:
            promo_response = BuiltIn().get_variable_value("${promo_response}")
            if promo_response['CLAIMABLE_IND'] is True:
                claim_dt = (current_time + datetime.timedelta(days=369)).strftime(self.DATE_FORMAT)
            if promo_response['SPACEBUY_END_DT'] is not None:
                spacebuy_dt = (current_time + datetime.timedelta(days=369)).strftime(self.DATE_FORMAT)
            payload = {
                "PROMO_ID": promo_id,
                "PROMO_CD": code,
                "PROMO_DESC": desc,
                "START_DT": start_time,
                "END_DT": end_time,
                "SPACEBUY_END_DT": spacebuy_dt,
                "CLAIM_ENDDT": claim_dt
            }
            copy_record = BuiltIn().get_variable_value("${copy_record}")
            if copy_record:
                payload.update((k, v) for k, v in copy_record.items())
            return payload
