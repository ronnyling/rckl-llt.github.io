import json
import datetime
import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.Config.ReferenceData.ClaimType.ClaimTypeGet import ClaimTypeGet

END_POINT_URL = PROTOCOL + "promotion" + APP_URL
current_date = datetime.datetime.now()
start_date = str((current_date + datetime.timedelta(days=2)).strftime("%Y-%m-%d"))
end_date = str((current_date + datetime.timedelta(days=3)).strftime("%Y-%m-%d"))
claim_date = str((current_date + datetime.timedelta(days=5)).strftime("%Y-%m-%d"))


class SamplingPost(object):
    """ Functions to create sampling """

    @keyword('When ${user_role} creates sampling with ${type} data')
    def user_creates_sampling_with(self, user_role, type):
        """ Function to create sampling with random/fixed data"""
        url = "{0}sample/generalInfo".format(END_POINT_URL)
        payload = self.payload(user_role, type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        if response.status_code == 201:
            body_result = response.json()
            print("Body Result: ", body_result)
            BuiltIn().set_test_variable("${sampling_id}", body_result['ID'])
            BuiltIn().set_test_variable("${sample_cd}", body_result['SAMPLE_CD'])
            BuiltIn().set_test_variable("${sample_desc}", body_result['SAMPLE_DESC'])
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload(self, user_role, type):
        """ Function for sampling payload content """
        ct_id = ClaimTypeGet().get_rand_claim_type_id()
        payload = {
            "SAMPLE_DESC": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
            "CLAIMABLE_IND": secrets.choice([True, False]),
            "CLAIMABLE_ENDDT": claim_date,
            "CLAIM_TYPE_ID": ct_id,
            "START_DT": start_date,
            "END_DT": end_date,
            "SAMPLE_STATUS": False
        }
        if type == "fixed":
            sampling_details = BuiltIn().get_variable_value("${sampling_details}")
            if sampling_details:
                if 'CLAIM_TYPE_CODE' in sampling_details.keys():
                    sampling_details['CLAIM_TYPE_ID'] = ClaimTypeGet().get_claim_type_id_by_code(sampling_details['CLAIM_TYPE_CODE'])
                    sampling_details.pop('CLAIM_TYPE_CODE', None)
                payload.update((k, v) for k, v in sampling_details.items())
        if user_role == "distadm":
            payload['CLAIMABLE_IND'] = False
        if payload['CLAIMABLE_IND'] is False:
            payload.pop('CLAIMABLE_ENDDT')
            payload.pop('CLAIM_TYPE_ID')
        payload = json.dumps(payload)
        print("Sampling Payload: ", payload)
        return payload


