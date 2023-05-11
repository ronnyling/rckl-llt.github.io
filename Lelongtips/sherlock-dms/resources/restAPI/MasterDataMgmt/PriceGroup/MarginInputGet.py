from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

END_POINT_URL = PROTOCOL + "price" + APP_URL


class MarginInputGet(object):

    def get_margin_input(self, pg_id):
        url = "{0}price/{1}/margin-input-pricing".format(END_POINT_URL, pg_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve Margin Input"
        body = response.json()
        return body
