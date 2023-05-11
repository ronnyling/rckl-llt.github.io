from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod

import json

END_POINT_URL = PROTOCOL + "price" + APP_URL
METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL


class ProductPriceGet(object):

    def get_product_price_by_id(self, price_id, product_price_id):
        url = "{0}price/{1}/prod-price/{2}".format(END_POINT_URL, price_id, product_price_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve product price"
        body_result = response.json()
        return body_result

    def get_all_product_price(self,price_id):
        url = "{0}price/{1}/prod-price/".format(END_POINT_URL, price_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve product price"
        body_result = response.json()
        return body_result

    def get_prd_price(self, pg_id, prdname):
        filter_prd_price = {"PRD_CD": {"$eq": prdname}}
        filter_prd_price = json.dumps(filter_prd_price)
        str(filter_prd_price).encode(encoding='UTF-8', errors='strict')
        url = "{0}price/{1}/prod-price?filter={2}".format(END_POINT_URL, pg_id, filter_prd_price)
        print(url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to retrieve prd price"
        body_result = response.json()
        return body_result[0]
