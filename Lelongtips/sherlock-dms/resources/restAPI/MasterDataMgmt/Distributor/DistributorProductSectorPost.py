""" Python file related to distributor product sector API """
import json
import secrets

from faker import Faker
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL, BuiltIn
from resources.restAPI.Common import APIMethod
from resources.restAPI.MasterDataMgmt.Distributor.DistributorProductSectorGet import DistributorProductSectorGet
from resources.restAPI.MasterDataMgmt.Distributor.DistributorGet import DistributorGet
from resources.restAPI.MasterDataMgmt.ProductSector.ProductSectorGet import ProductSectorGet

FAKE = Faker()

END_POINT_URL = PROTOCOL + "product-sector" + APP_URL


class DistributorProductSectorPost:
    """ Functions related to distributor product sector POST request """

    @keyword('user assigned product sector using ${data_type} data')
    def user_assigned_product_sector_using_data(self, data_type):
        """ Functions to assign product sector using fixed data """
        """ Distributor_id is set using user_gets_distributor_by_using_code, please run in prerequisites"""

        if data_type == "fixed":
            dist_id = BuiltIn().get_variable_value("${dist_id}")
            assert dist_id is not None, "Distributor not setup, please include prerequisite"

            url = "{0}product-sector-assign/distributor/{1}".format(END_POINT_URL, dist_id)
            ps_details = BuiltIn().get_variable_value("${ProductSectorDetails}")
            ps_code = ps_details['productSector']
            print("PS code = " + ps_code)

            ProductSectorGet().user_retrieve_product_sector(ps_code)
            prdsector_list = BuiltIn().get_variable_value("${ps_br}")
            print("ps list here " + str(prdsector_list))

            ps_id = None
            for available_product_sector in prdsector_list:
                if available_product_sector['PROD_SECTOR_DESC'] == ps_code:
                    ps_id = available_product_sector['ID']
                    print("ps id is = " + ps_id)
                    BuiltIn().set_test_variable("${ps_id}", ps_id)
                    break
            assert ps_id is not None, "Unable to retrieve product sector id using code"

            payload = self.payload_product_sector(ps_id)
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("POST", url, payload)
            if response.status_code == 201:
                body_result = response.json()
                print("Body Result: ", body_result)
                BuiltIn().set_test_variable("${ps_assignment_id}", body_result['assignedSector'][0])
            BuiltIn().set_test_variable("${status_code}", response.status_code)
        else:
            DistributorGet().user_retrieves_random_distributor()
            dist_id = BuiltIn().get_variable_value("${dist_id}")

            url = "{0}product-sector-assign/distributor/{1}".format(END_POINT_URL, dist_id)

            DistributorProductSectorGet().user_retrieves_assigned_product_sector()
            assigned_dist_sector = BuiltIn().get_variable_value("${assigned_dist_sector}")
            assigned_ps_id = []
            for ps_id in assigned_ps_id:
                assigned_ps_id.append(ps_id['PROD_SECTOR_ID'])

            ProductSectorGet().user_retrieve_product_sector("all")
            prdsector_list = BuiltIn().get_variable_value("${ps_br}")
            unassigned_ps_ids = []
            for ps in prdsector_list:
                if ps['ID'] not in assigned_ps_id:
                    unassigned_ps_ids.append(ps['ID'])
            payload = self.payload_product_sector(unassigned_ps_ids[0])
            common = APIMethod.APIMethod()
            response = common.trigger_api_request("POST", url, payload)
            print("payload " + payload)
            if response.status_code == 201:
                body_result = response.json()
                print("Body Result: ", body_result)
                BuiltIn().set_test_variable("${ps_assignment_id}", body_result['assignedSector'][0])
            BuiltIn().set_test_variable("${status_code}", response.status_code)

    def payload_product_sector(self, product_sector_id):
        """ Functions to create payload for product sector """
        payload = {"PRODUCT_SECTOR_CODES": [product_sector_id]}
        payload = json.dumps(payload)
        return payload