from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.Config.DynamicHierarchy.GeoHierarchy import AssignRoutePost
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route.RouteGet import RouteGet
from resources.restAPI.MasterDataMgmt.Van.VanGet import VanGet
from resources.restAPI.Common import TokenAccess, APIMethod
from setup.hanaDB import HanaDB
from setup.yaml import YamlDataManipulator
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.Common import Common
import secrets
import json
import datetime

END_POINT_URL = PROTOCOL + "profile-route" + APP_URL
END_POINT_URL_DYNAMIC_HIER = PROTOCOL + "dynamic-hierarchy" + APP_URL

class RoutePost(object):
    """ Functions to create route record """
    ROUTE_ID = "${res_bd_route_id}"

    @keyword('When user creates route with ${data_type} data')
    def user_creates_route_with(self, data_type):
        """ Function to create route using fixed/random data"""
        distributor_id = BuiltIn().get_variable_value("${distributor_id}")
        #user_role = BuiltIn().get_variable_value("${user_role}")
        #print("User_role: ", user_role)
        url = "{0}distributors/{1}/route".format(END_POINT_URL, distributor_id)
        BuiltIn().set_test_variable("${lob_id}", "725CF01F:47872CD4-29A5-4F6A-88AD-41D76C825538") #LOB module not done, so using hardcoded for now
        payload = self.payload_route(data_type)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        if response.status_code == 201:
            print("created route = " + str(response.json()))
            print("created route id = " + str(response.json()['ID']))
            body_result = response.json()
            res_bd_route_id = body_result['ID']
            BuiltIn().set_test_variable(self.ROUTE_ID, res_bd_route_id)
            BuiltIn().set_test_variable("${res_bd_route}", body_result)
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_route(self, data_type):
        """ Function for route payload content """
        van_id = BuiltIn().get_variable_value(self.ROUTE_ID)
        res_bd_lob_id = BuiltIn().get_variable_value("${lob_id}")
        dist_cd = BuiltIn().get_variable_value("${dist_cd}")
        yaml_output = YamlDataManipulator.YamlDataManipulator().user_retrieves_data_from_yaml("1-RoutePre.yaml", "Output")

        if van_id is not None:
            van_id = {"ID": van_id}
        if res_bd_lob_id is not None:
            res_bd_lob_id = {"ID": res_bd_lob_id}

        payload = {
            "ROUTE_CD": 'RCD' + str(secrets.choice(range(1, 9999999))),
            "ROUTE_NAME": 'route' + str(secrets.choice(range(1, 9999999))),
            "DIST_CD": dist_cd,
            "OP_TYPE": 'O',
            "VAN": van_id,
            "MAIN_WHSE": None,
            "DIST_BRACH": secrets.choice(['DIST1', 'DIST2', 'DIST3']),
            "COMPANY": secrets.choice(['1', '0']),
            "HHT_USRFLG": 'No',
            "GPS_IND": False,
            "IMAGE": False,
            "LANGUAGE": secrets.choice(['[en-US]']),
            "LOB": res_bd_lob_id,
            "EFFECT_DATE": None,
            "EFFECT_END_DATE": None,
            "NON_PRIME_WHS": None
        }

        if yaml_output['1_WarehousePost'].get('ID') is not None:
            wh = BuiltIn().get_variable_value("${res_bd_prime_warehouse}")
            payload['MAIN_WHSE'] = wh
        if yaml_output['2_WarehousePost'].get('ID') is not None:
            wh = BuiltIn().get_variable_value("${res_bd_non_prime_warehouse}")
            payload['NON_PRIME_WHS'] = wh

        print("Main warehouse: ", payload['MAIN_WHSE'])

        details = BuiltIn().get_variable_value("${route_details}")
        if details:
            if 'OP_TYPE' in details.keys():
                if details['OP_TYPE'] == 'T':
                    payload['VAN'] = None
                if details['OP_TYPE'] == 'A':
                    payload['COMPANY'] = '0'
                    payload['MAIN_WHSE'] = None
                    payload['VAN'] = None
            if 'VAN_CD' in details.keys():
                van_id = VanGet().user_gets_van_id_by_using_code("3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352", details['VAN_CD'])
                payload['VAN'] = {"ID": van_id}
            payload.update((k, v) for k, v in details.items())


        payload = json.dumps(payload)
        print("Route Payload: ", payload)
        return payload

    def user_creates_prerequisite_for_route(self):
        """ Function to create pre-requisite for route """
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        DistributorGet.DistributorGet().user_gets_distributor_by_using_code("DistEgg")
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        Common().execute_prerequisite('1-RoutePre.yaml')

    def user_assign_route_to_geotree_with_started_date(self):
        """ Function to assign route to geo tree and patch start date """
        TokenAccess.TokenAccess().user_retrieves_token_access_as("distadm")
        AssignRoutePost.AssignRoutePost().user_assign_route_to_geotree()
        route_id = BuiltIn().get_variable_value(self.ROUTE_ID)
        route_id = route_id.replace(":", "")
        route_id = route_id.replace("-", "")
        today_date = datetime.datetime.today().strftime("%Y-%m-%d")
        query = "UPDATE HIER_GEO_SLSMAN_ASSIGN SET START_DATE='{0}' WHERE SLSMAN_ID='{1}'".format(today_date, route_id)
        HanaDB.HanaDB().connect_database_to_environment()
        HanaDB.HanaDB().execute_sql_string(query)
        HanaDB.HanaDB().disconnect_from_database()

    def user_creates_route_as_prerequisite(self):
        self.user_creates_route_with("random")

    def user_assign_nodes(self):
        route_id = BuiltIn().get_variable_value("${res_bd_route_id}")
        url = "{0}route/{1}/nodes".format(END_POINT_URL_DYNAMIC_HIER, route_id)
        payload = self.gen_node_payload()
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("PUT", url, payload)
        print("payload = " + str(payload))
        if response.status_code == 200:
            body_result = response.json()
            print("response body = " + str(body_result))
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def gen_node_payload(self):
        payload = []
        node_details = {}
        RouteGet().user_retrieve_nodes_to_assign()
        nodes_to_assign = BuiltIn().get_variable_value("${nodes_to_assign}")
        rand = secrets.choice(nodes_to_assign)
        node_details['NODE_ID'] = rand['NODEID']
        node_details['START_DATE'] = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        node_details['END_DATE'] = "2999-01-01"
        payload.append(node_details)
        payload = json.dumps(payload)
        return payload