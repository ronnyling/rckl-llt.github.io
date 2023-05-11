import datetime
import json
import secrets
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.restAPI.Config.GracePeriod import GracePeriodPost, GracePeriodGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet

END_POINT_URL = PROTOCOL + "setting" + APP_URL
NOW = datetime.datetime.now()
DT_FORMAT = "%Y-%m-%d"


class GracePeriodPut:

    @keyword("user updates grace period using ${data_type} data")
    def user_updates_grace_period(self, data_type):
        period_id = BuiltIn().get_variable_value("${grace_period_id}")
        url = "{0}grace-period/{1}".format(END_POINT_URL, period_id)
        payload = self.grace_period_payload(period_id)
        response = APIMethod.APIMethod().trigger_api_request("PUT", url, payload)
        if response.status_code == 200:
            BuiltIn().set_test_variable("${grace_period_id}",  response.json()['ID'])
            print("Response : ", response.json())
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def grace_period_payload(self, id):
        GracePeriodGet.GracePeriodGet().user_retrieves_grace_period("created")
        body_result = BuiltIn().get_variable_value("${res_bd_grace_period}")
        days = secrets.choice(range(1, 365))
        st_date = str((NOW + datetime.timedelta(days=days)).strftime(DT_FORMAT))
        end_date = str((NOW + datetime.timedelta(days=days)).strftime(DT_FORMAT))
        print ("test", body_result["TXN_TYPE"])
        payload = {
            "TXN_TYPE": body_result['TXN_TYPE'],
            "DIST_ID": body_result['DIST_ID'],
            "GRACE_PERIOD": secrets.choice(range(1, 30)),
            "START_DT": st_date,
            "END_DT": end_date
        }
        details = BuiltIn().get_variable_value("${period_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        payload = json.dumps(payload)
        print ("PAYLOAD ",payload)
        return payload


