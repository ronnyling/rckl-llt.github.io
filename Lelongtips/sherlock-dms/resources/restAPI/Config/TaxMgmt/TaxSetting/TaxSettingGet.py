
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "taxation" + APP_URL


class TaxSettingGet(object):

    def get_tax_sett(self,ts_id):

        url = "{0}tax-structure/{1}/tax-setting".format(END_POINT_URL, ts_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve customer option"
        body_result = response.json()
        return body_result