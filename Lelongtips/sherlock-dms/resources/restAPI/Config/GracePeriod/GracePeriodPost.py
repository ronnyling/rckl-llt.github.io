
import datetime
import json
import secrets
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet

END_POINT_URL = PROTOCOL + "setting" + APP_URL
NOW = datetime.datetime.now()
DT_FORMAT = "%Y-%m-%d"


class GracePeriodPost:

    @keyword("user creates grace period using random data")
    def user_creates_grace_period(self):
        url = "{0}grace-period".format(END_POINT_URL)
        payload = self.grace_period_payload()
        response = APIMethod.APIMethod().trigger_api_request("POST", url, payload)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${grace_period_id}",  response.json()['ID'])

        BuiltIn().set_test_variable("${status_code}", response.status_code)


    def grace_period_payload(self):
        module = ["SALES_ORDER", "DEBIT_NOTE", "CREDIT_NOTE", "RETURN"]
        DistributorGet().user_retrieves_all_distributors_list()
        body_result = DistributorGet().user_gets_distributor_by_using_id()
        body_result['ADDRESS_CD'] = body_result['ADDRESS_CD']['ID']
        body_result['PRICE_GRP'] = body_result['PRICE_GRP']['ID']
        st_date = str((NOW + datetime.timedelta(days=2000)).strftime(DT_FORMAT))
        end_date = str((NOW + datetime.timedelta(days=2500)).strftime(DT_FORMAT))
        payload = {
            "TXN_TYPE": secrets.choice(module),
            "DIST_ID": body_result,
            "GRACE_PERIOD": 10,
            "START_DT": st_date,
            "END_DT": end_date
        }
        payload = json.dumps(payload)
        return payload