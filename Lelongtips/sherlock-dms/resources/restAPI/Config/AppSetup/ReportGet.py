""" Python file related to application setup API """
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL, COMMON_KEY
from resources.restAPI.Common import APIMethod

END_POINT_URL_GEO_LEVEL_RPT = PROTOCOL + "dynamic-hierarchy" + APP_URL + "structure/hier"
END_POINT_URL_GEO_HIER = PROTOCOL + "dynamic-hierarchy" + APP_URL + "structure/active/geo tree"
END_POINT_URL_SEGMENT = PROTOCOL + "dynamic-attribute" + APP_URL + "dynamic-attribute"
END_POINT_URL_HIER_LIST = PROTOCOL + "dynamic-hierarchy" + APP_URL + "structure/list"


class ReportGet:
    """ Functions related to application setup - report GET request """

    def user_retrieves_geo_hier_id(self):
        """ Functions to retrieve option values for geo hierarchy id """
        url = END_POINT_URL_GEO_HIER
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            BuiltIn().set_test_variable("${geo_hier_id}", body_result[0]["hierId"])
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_segment(self, given_data):
        """ Functions to retrieve option values for segment """
        url = END_POINT_URL_SEGMENT
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            print("body result", body_result)
            for dic in body_result:
                print("Dic1", dic)
                if dic["ATTRIBUTE"] == given_data:
                    print('dic["ID"]', dic["ID"])
                    segment_id = (dic["ID"])
                    BuiltIn().set_test_variable("${segment_id}", segment_id)
                    break
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)


    def user_retrieves_option_values_geo_level_region(self, given_data):
        """ Functions to retrieve option values for geo level region """
        self.user_retrieves_geo_hier_id()
        geo_hier_id = BuiltIn().get_variable_value("${geo_hier_id}")
        url = "{0}/{1}".format(END_POINT_URL_GEO_LEVEL_RPT, geo_hier_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            print('Start ->', body_result)
            geo_level_region_id = []
            for dic in body_result["levels"]:
                print("dic", dic)
                print(str(dic["name"]), "->", str(given_data))
                if str(dic["name"]) == str(given_data):
                    geo_level_region_id.append(dic["treeId"])
                    break
            BuiltIn().set_test_variable("${geo_level_region_id}", geo_level_region_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_prod_hier_list_id(self):
        """ Functions to retrieve option values for prod hier list id """
        url = END_POINT_URL_HIER_LIST
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                print("Dic1", dic)
                if dic["treeDes"] == "General Product Hierarchy":
                    print('dic["id"]', dic["id"])
                    prod_level_id = (dic["id"])
                    BuiltIn().set_test_variable("${prod_level_id}", prod_level_id)
                    break
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_prod_level(self, given_data):
        """ Functions to retrieve option values for product level """
        self.user_retrieves_prod_hier_list_id()
        prod_level_id = BuiltIn().get_variable_value("${prod_level_id}")
        url = "{0}/{1}".format(END_POINT_URL_GEO_LEVEL_RPT, prod_level_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            prod_level_id = []
            for dic in body_result["levels"]:
                print("dic", dic)
                print(str(dic["name"]), "->", str(given_data))
                if str(dic["name"]) == str(given_data):
                    prod_level_id.append(dic["treeId"])
                    break
            BuiltIn().set_test_variable("${selected_prod_level_id}", prod_level_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_channel_hier_list_id(self):
        """ Functions to retrieve option values for channel hier list id """
        url = END_POINT_URL_HIER_LIST
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            for dic in body_result:
                print("Dic1", dic)
                if dic["treeDes"] == "General Customer Hierarchy":
                    print('dic["id"]', dic["id"])
                    channel_level_id = (dic["id"])
                    BuiltIn().set_test_variable("${channel_level_id}", channel_level_id)
                    break
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)

    def user_retrieves_option_values_channel_level(self, given_data):
        """ Functions to retrieve option values for channel level """
        self.user_retrieves_channel_hier_list_id()
        channel_level_id = BuiltIn().get_variable_value("${channel_level_id}")
        url = "{0}/{1}".format(END_POINT_URL_GEO_LEVEL_RPT, channel_level_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            body_result = response.json()
            channel_level_id = []
            for dic in body_result["levels"]:
                print("dic", dic)
                print(str(dic["name"]), "->", str(given_data))
                if str(dic["name"]) == str(given_data):
                    channel_level_id.append(dic["treeId"])
                    break
            BuiltIn().set_test_variable("${selected_channel_level_id}", channel_level_id)
        BuiltIn().set_test_variable(COMMON_KEY.STATUS_CODE, response.status_code)