import json
import secrets
from resources.restAPI.Common import APIMethod
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword


END_POINT_URL = PROTOCOL + "setting" + APP_URL


class PromoPriorityPost(object):

    @keyword('user creates promotion sequence using ${type} data')
    def create_promo_sequence(self, type):
        url = "{0}promotion-sequence".format(END_POINT_URL)
        payload = self.payload_details(type)
        payload = json.dumps(payload)
        print(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.status_code)
        if response.status_code == 201:
            body_result = response.json()
            print(body_result)
            sequence_id = body_result['ID']
            promo_seq_cd = response.json()['PROMO_SEQ_CD']
            promo_priority = response.json()['PROMO_PRIORITY']
            BuiltIn().set_test_variable('${promo_seq_cd}', promo_seq_cd)
            if not BuiltIn().get_variable_value("${promo_priority}"):
                BuiltIn().set_test_variable('${promo_priority}', promo_priority)
            BuiltIn().set_test_variable('${sequence_id}', sequence_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def payload_details(self, type):
        if type in ('existing', 'update', 'updatePriority', 'deleted'):
            promotion_seq_cd = BuiltIn().get_variable_value("${promo_seq_cd}")
        else:
            promotion_seq_cd = 'PROSEQCD' + str(secrets.randbelow(999999999999))
        if type in ('existingPriority', 'updatePriority', 'deletedPriority'):
            promotion_priority = int(BuiltIn().get_variable_value("${promo_priority}"))
        else:
            promotion_priority = secrets.randbelow(9999999)
        payload = {
            'PROMO_SEQ_CD': promotion_seq_cd,
            'PROMO_SEQ_DESC': ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(50)),
            'PROMO_PRIORITY': promotion_priority,
            'VERSION': 1
        }
        fix_data = BuiltIn().get_variable_value("${PromoSeq}")
        if fix_data:
            payload.update((k, v) for k, v in fix_data.items())
        return payload
