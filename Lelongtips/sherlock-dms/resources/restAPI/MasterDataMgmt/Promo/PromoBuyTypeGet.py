from robot.libraries.BuiltIn import BuiltIn
import secrets
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
import json

METADATA_END_POINT_URL = PROTOCOL + "metadata" + APP_URL
SETTING_END_POINT_URL = PROTOCOL + "setting" + APP_URL
DYNAMIC_HIER_END_POINT_URL = PROTOCOL + "dynamic-hierarchy" + APP_URL


class PromoBuyTypeGet(object):

    def user_retrieves_promo_buy_type(self, buy_type, get_by):
        if get_by == "id":
            url = "{0}module-data/promotion-buy-type-ref/{1}".format(METADATA_END_POINT_URL, buy_type)
        else:
            filter_cust = {"REF_PARAM": {"$eq": buy_type}}
            filter_cust = json.dumps(filter_cust)
            str(filter_cust).encode(encoding='UTF-8', errors='strict')
            url = "{0}module-data/promotion-buy-type-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Promo Buy Type"
        return response.json()


    def user_retrieves_cust_assign_type(self, assign_type):
        filter_cust_assign_type = {"REF_PARAM": {"$eq": assign_type}}
        filter_cust_assign_type = json.dumps(filter_cust_assign_type)
        str(filter_cust_assign_type).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/ass-type-customer-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust_assign_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Promo Cust Assign Type"
        body_result = response.json()
        return body_result[0]['ID']

    def user_retrieves_promo_mechanic_type(self, m_type, get_by):

        if get_by == 'id':
            url = "{0}module-data/promotion-mechanic-type-ref/{1}".format(METADATA_END_POINT_URL, m_type)
        else:
            filter_cust = {"REF_PARAM": {"$eq": m_type}}
            filter_cust = json.dumps(filter_cust)
            str(filter_cust).encode(encoding='UTF-8', errors='strict')
            url = "{0}module-data/promotion-mechanic-type-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Promo Disc Method"
        return response.json()

    def user_retrieves_foc_cond(self, foc_cond):
        filter_cust = {"REF_PARAM": {"$eq": foc_cond}}
        filter_cust = json.dumps(filter_cust)
        str(filter_cust).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/promotion-foc-cond-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Foc Condition"
        body_result = response.json()
        return body_result[0]

    def user_retrieves_apply_on(self, apply_on):
        filter_cust = {"REF_PARAM": {"$eq": apply_on}}
        filter_cust = json.dumps(filter_cust)
        str(filter_cust).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/promotion-apply-on-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Promo Apply On"
        body_result = response.json()
        return body_result[0]

    def user_retrieves_apply_on_by_id(self, apply_on, cond):
        if cond == "id":
            url = "{0}module-data/promotion-apply-on-ref/{1}".format(METADATA_END_POINT_URL, apply_on)
        else:
            filter_cust = {"ID": {"$eq": apply_on}}
            filter_cust = json.dumps(filter_cust)
            str(filter_cust).encode(encoding='UTF-8', errors='strict')
            url = "{0}module-data/promotion-apply-on-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Promo Apply On"
        body_result = response.json()
        if cond == "id":
           return body_result
        else:
            return body_result[0]

    def user_retrieves_auto_promo(self, auto_manual):
        filter_cust = {"REF_PARAM": {"$eq": auto_manual}}
        filter_cust = json.dumps(filter_cust)
        str(filter_cust).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/promotion-auto-promo-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Auto Promo"
        body_result = response.json()
        BuiltIn().set_test_variable("${auto_promo_ref_res_body}", response.json())
        return body_result[0]

    def user_retrieves_promo_type(self, p_type, get_by):
        filter_cust = {"REF_PARAM": {"$eq": p_type}}
        filter_cust = json.dumps(filter_cust)
        if get_by == 'id':
            url = "{0}module-data/promotion-type-ref/{1}".format(METADATA_END_POINT_URL, p_type)
        else:
            url = "{0}module-data/promotion-type-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Promo Type"
        return response.json()

    def user_retrieves_promo_status(self, status):
        filter_cust = {"REF_PARAM": {"$eq": status}}
        filter_cust = json.dumps(filter_cust)
        str(filter_cust).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/promotion-promo-status-ref?filter={1}".format(METADATA_END_POINT_URL, filter_cust)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Promo Status"
        body_result = response.json()
        return body_result[0]

    def user_retrieves_prod_assign_type(self, assign_type):
        filter_assign_type = {"REF_PARAM": {"$eq": assign_type}}
        filter_assign_type = json.dumps(filter_assign_type)
        str(filter_assign_type).encode(encoding='UTF-8', errors='strict')
        url = "{0}module-data/ass-type-product-ref?filter={1}".format(METADATA_END_POINT_URL, filter_assign_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Product Assign Type"
        body_result = response.json()
        return body_result[0]

    def user_retrieves_promo_seq_by_code(self, seq):
        print("seqqq",seq)
        filter_assign_type = {"PROMO_SEQ_CD": {"$eq": seq}}
        filter_assign_type = json.dumps(filter_assign_type)
        str(filter_assign_type).encode(encoding='UTF-8', errors='strict')
        if seq == 'random':
            url = "{0}promotion-sequence".format(SETTING_END_POINT_URL)
        else:
            url = "{0}promotion-sequence?filter={1}".format(SETTING_END_POINT_URL, filter_assign_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Promo Sequence"
        body_result = response.json()
        if seq == 'random':
            body_result = secrets.choice(body_result)
        else:
            body_result =  body_result[0]

        return body_result

    def user_retrieves_hierarchy(self, assign_type):
        filter_assign_type = {"REF_PARAM": {"$eq": assign_type}}
        filter_assign_type = json.dumps(filter_assign_type)
        str(filter_assign_type).encode(encoding='UTF-8', errors='strict')
        url = "{0}structure/list?filter={1}".format(DYNAMIC_HIER_END_POINT_URL, filter_assign_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        assert response.status_code == 200, "Unable to Retrieve Product Assign Type"
        body_result = response.json()
        return body_result[0]
