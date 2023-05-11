""" Python file related to vs score card API """
import datetime
import json
import secrets
import string

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from setup.hanaDB import HanaDB

END_POINT_URL_VSSCORECARD = PROTOCOL + "vs-scorecard" + APP_URL + "vs-scorecard"
END_POINT_URL_KPI_ASSIGNMENT = PROTOCOL + "vs-scorecard" + APP_URL + "kpi-assignment"
NOW = datetime.datetime.now()


class ScoreCardSetupPost:
    """ Functions related to vs score card POST request """

    @keyword("user creates vs score card using ${data_type} data")
    def user_creates_vs_score_card_using_data(self, data_type):
        """ Functions to create vs score card using random/fixed data """
        if data_type == "random":
            payload = self.create_vsscorecard_payload()
        print(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", END_POINT_URL_VSSCORECARD, payload)
        data = response.json()
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        BuiltIn().set_test_variable("${vs_score_card_id}", data['ID'])

    def create_vsscorecard_payload(self):
        """ Functions to create payload for vs score card """
        today = datetime.date.today()
        year = today.year

        start_month = secrets.choice(range(1, 12))
        start_year = secrets.choice(range(year, year + year))

        payload = {
            "SCORECARD_DESC": "DESC".join(secrets.choice('0123456789ASZ') for _ in range(5)),
            "START_PERIOD": "{:02}-{:02}".format(start_month, start_year),
            "END_PERIOD": "{:02}-{:02}".format(secrets.choice(range(start_month, 12)),
                                                 secrets.choice(range(start_year, year + year))),
            "FREQUENCY": "A",
            "STATUS": "A"
        }

        return json.dumps(payload)

    @keyword("user creates kpi assignment using ${data_type} data")
    def user_creates_kpi_assignment_using_data(self, data_type):
        """ Functions to create kpi assignment using random/fixed data """
        vs_score_card_id = BuiltIn().get_variable_value("${vs_score_card_id}")
        if vs_score_card_id:
            url = "{0}/scorecard/{1}".format(END_POINT_URL_KPI_ASSIGNMENT, vs_score_card_id)

            payload = self.create_vsscorecard_kpi_assignment_payload(data_type)
            print("POST url", url)
            print("POST payload", payload)
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("POST", url, payload)
            BuiltIn().set_test_variable("${status_code}", response.status_code)
            # HanaDB.HanaDB().connect_database_to_environment()
            # HanaDB.HanaDB().check_if_exists_in_database_by_query(
            #     "SELECT KPI_DESC, ACHIEVEMENT_BY FROM VS_DTL WHERE SCORECARD_ID = '{0}'".format(vs_score_card_id))
            # HanaDB.HanaDB().disconnect_from_database()

    def create_vsscorecard_kpi_assignment_payload(self, data_type):
        """ Functions to create payload for vs score card kpi assignment """
        alphabet = string.digits + string.ascii_letters

        payload = {
            "ENABLE_SCORE": secrets.choice([True, False]),
            "KPI_TYPE_ID": "C90923E7:EBEF4E22-3C70-490F-A0BD-83B6D694017B",  # hardcoded for now
            "NATURE": secrets.choice(["T", "P"]),
            "KPI_DESC": ''.join(secrets.choice(alphabet) for _ in range(5)),
            "MEASUREMENT": "MSL",
            "ACHIEVEMENT_BY": "P",
            "VS_MSL_PRDCAT_SCORE": None,
            "VS_MSL_SCORE": None,
            "VS_DCC_SCORE": None
        }

        if data_type == "fixed":
            details = BuiltIn().get_variable_value("${VSScoreCardDetails}")
            payload.update((k, v) for k, v in details.items())

        if payload["MEASUREMENT"] == "MA":
            StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
            StructureGet().user_retrieves_hierarchy_structure("valid")
            hier_rs_bd = BuiltIn().get_variable_value("${hier_rs_bd}")
            tree_id = None
            for hier in hier_rs_bd['levels']:
                if hier.get('name') == "Brand":
                    tree_id = hier.get('treeId')
                    break
            BuiltIn().set_test_variable("${tree_id}", tree_id)
            StructureGet().user_get_prd_or_or_cust_hierearchy_info()
            tree_view_bd = BuiltIn().get_variable_value("${tree_view_bd}")
            valid_categories = []
            for tree in tree_view_bd:
                if len(tree.get('children')) > 0:
                    for child in tree.get('children'):
                        valid_categories.append(child.get('nodeId'))
            rand_cat = secrets.choice(valid_categories)
            rand_cat_id = rand_cat
            dic = {
                "CATEGORY_ID": rand_cat_id,
                "HIT_TO": 1,
                "KPI_ID": "51e65051:c7fc22af-c4da-4376-a5b9-a22fa44bf798",
                "SCORE": 50,
                "SPACE_ID": "EB8EEE88:666117F3-E9DA-47C0-B08F-7AFB9271B296"
            }
            payload["VS_MA_SCORE"] = [dic]
        elif payload["MEASUREMENT"] == "MSL":
            dic = {
                "HIT_TO": 100,
                "KPI_ID": "51E65051:11D613DF-6336-44E0-9A57-94A9E2CE5C67",
                "SCORE": 100
            }
            payload["VS_MSL_SCORE"] = [dic]

        return json.dumps(payload)
