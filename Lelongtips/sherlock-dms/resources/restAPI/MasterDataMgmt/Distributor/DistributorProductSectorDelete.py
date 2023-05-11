""" Python file related to distributor product sector API """
from faker import Faker
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import TokenAccess, APIMethod, APIAssertion
from resources.restAPI.MasterDataMgmt.Distributor import DistributorProductSectorGet

FAKE = Faker()

END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class DistributorProductSectorDelete:
    """ Functions related to distributor product sector DELETE request """

    @keyword('user unassigned product sector')
    def user_unassigned_product_sector_using_data(self):
        """ Functions to unassigned product sector using fixed data """
        # TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        # if data_type == "fixed":
        #     dic = BuiltIn().get_variable_value("${ProductSectorDetails}")
        #     product_sector_id = DistributorProductSectorGet.DistributorProductSectorGet().user_retrieves_product_sector_id_for("assigned", dic["productSector"])
        #
        # if product_sector_id is not None:

        ps_assignment_id = BuiltIn().get_variable_value("${ps_assignment_id}")
        url = "{0}product-sector-assign/route/{1}".format(END_POINT_URL, ps_assignment_id)
        print("TESTURL: ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    @keyword('user unassigned product sector using ${data_type} data')
    def user_unassigned_product_sector(self, data_type):
        """ Functions to unassigned product sector using fixed data """
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        if data_type == "fixed":
            dic = BuiltIn().get_variable_value("${ProductSectorDetails}")
            dist_id = BuiltIn().set_test_variable("${dist_id}")

            product_sector_id = DistributorProductSectorGet.DistributorProductSectorGet().user_retrieves_product_sector_id_for(
                "assigned", dic["productSector"])
            print("product sector id here: ", product_sector_id)

        if product_sector_id is not None:
            ps_assignment_id = BuiltIn().get_variable_value("${ps_assignment_id}")
            url = "{0}product-sector-assign/route/{1}".format(END_POINT_URL, product_sector_id)
            print("TESTURL: ", url)
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("DELETE", url, "")
            BuiltIn().set_test_variable("${status_code}", response.status_code)

    def user_unassigned_single_product_sector(self):
        ps_details = BuiltIn().get_variable_value("${ProductSectorDetails}")
        ps_code = ps_details['productSector']

        dist_id = BuiltIn().get_variable_value("${dist_id}")
        print("dist id is " + dist_id)
        url = "{0}product-sector-assign/distributor/{1}".format(END_POINT_URL, dist_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")

        all_assigned_dist_ps = response.json()
        assigned_id = None
        for assigned_ps in all_assigned_dist_ps:
            if assigned_ps['PROD_SECTOR_DESC'] == ps_code:
                assigned_id = assigned_ps['ID']
        if assigned_id is None:
            print("Product sector already not not assigned")
        url = "{0}product-sector-assign/route/{1}".format(END_POINT_URL, assigned_id)
        print("TESTURL: ", url)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        response = common.trigger_api_request("GET", url, "")

        if response.status_code == 200:
            url = "{0}product-sector-assign/distributor/{1}".format(END_POINT_URL, dist_id)
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("GET", url, "")
            all_assigned_dist_ps = response.json()
            print("after unassign, assigned ps = " + str(all_assigned_dist_ps))
            for assigned_ps in all_assigned_dist_ps:
                assert assigned_ps['PROD_SECTOR_DESC'] is ps_code, "Http success but unassign fail"

