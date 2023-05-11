import re

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from resources.Common import Common
from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Config.AppSetup import AppSetupPut
from resources.restAPI.CustTrx.RouteSettlement.RouteSettlementGet import RouteSettlementGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.restAPI.Config.DynamicHierarchy.GeoHierarchy import AssignRoutePost
from resources.restAPI.Common import TokenAccess, APIMethod
from setup.hanaDB import HanaDB
from setup.yaml import YamlDataManipulator
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.Common import Common
import secrets
import json
import datetime
from resources.Common import Common
import json

from faker import Faker

fake = Faker()

END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL
route_id = "02C42079:B8134E0D-7086-4931-9A0D-C4667507218E"


class RouteSettlementPostDeliveryPerson(object):

    def create_route_settlement(self, data, van_id, whs_id, prd_id1, routedate_to, routedate_from):
        url = "{0}route-settlement/{1}".format(END_POINT_URL, route_id)
        print(url)
        payload = self.payload_route_settlement(data, van_id, whs_id, prd_id1, routedate_to, routedate_from)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        print(response.text)
        payload = json.dumps(payload)
        print(payload)

    def payload_route_settlement(self, van_id, whs_id, prd_id1, routedate_to, routedate_from, null=None):
        payload = {
            "ROUTE_TXNDT_FROM": routedate_from,
            "ROUTE_TXNDT_TO": routedate_to,
            "VAN": {"ID": van_id, "VAN_CD": "whs12", "VAN_DESC": "whs12 desc"},
            "ROUTE": {"ID": route_id, "ROUTE_CD": "POTATOR01", "ROUTE_NAME": "POTATOR01"},
            "CREDIT_SLS": "0.000000",
            "CREDIT_RTN": "0.000000",
            "CREDIT_SLS_NET": "0.000000",
            "CREDIT_TTL_CASH": "0.000000",
            "CREDIT_TTL_CHEQUE": "0.000000",
            "CREDIT_TTL_EWALLET": "0.000000",
            "CREDIT_TTL_TRF": "0.000000",
            "CASH_TTL_CASH": "0.000000",
            "CASH_TTL_CHEQUE": "0.000000",
            "CASH_TTL_EWALLET": "0.000000",
            "CASH_TTL_TRF": "0.000000",
            "CASH_SLS": "0.000000",
            "CASH_RTN": "0.000000",
            "CASH_SLS_NET": "0.000000",
            "TTL_SLS": "0.000000",
            "TTL_RTN": "0.000000",
            "TTL_SLS_NET": "0.000000",
            "COL_CASH": "0.000000",
            "COL_EWALLET": "0.000000",
            "COL_CHEQUE": "0.000000",
            "COL_TRF": "0.000000",
            "COL_TTL_NET": "0.000000",
            "CASHIER_CASH_AMT": "0",
            "CASHIER_CHEQUE_AMT": "0",
            "CASHIER_EWALLET": "0",
            "CASHIER_TRF_AMT": "0",
            "CASHIER_TTL_AMT": "0",
            "COL_VARIANCE": "0",
            "PRD_GOOD": {
                "STKCOUNT": [],
                "PRODUCTS": [
                    {
                        "PRD_ID": prd_id1,
                        "WHS_ID": whs_id,
                        "WHS_TYPE": "G",
                        "PRD_CD": "SUSHPRD3",
                        "PRD_DESC": "SUSHPRODUCT3",
                        "TRANSFER_IN": "0.0000",
                        "RETURN": "0.0000",
                        "TRANSFER_OUT": "381.0000",
                        "CONV_GDTOBD": "0.0000",
                        "SALES": "0.0000",
                        "SALES_DISP": "0 Case / 0 Box / 0 Piece",
                        "FOC": "0.0000",
                        "FOC_DISP": "0.00 Case / 0.00 Box / 0.00 Piece",
                        "ADJUST": "0.0000",
                        "OPENBAL": "318",
                        "CLOSEBAL": "-63.0000",
                        "SYS_QTY": "0",
                        "STKCOUNT_QTY": "0",
                        "STKCOUNT_QTY_DISP": "0.00 Case / 0.00 Box / 0.00 Piece",
                        "VARIANCE": 0,
                        "STKCOUNT": {"ID": null, "TXN_NO": null, "TXN_DT": null
                                     },
                        "UOMS": [
                            {"UOM_LEVEL": 3, "CONV_FACTOR_SML": "54", "UOM_DESCRIPTION": "Case"},
                            {"UOM_LEVEL": 2, "CONV_FACTOR_SML": "6", "UOM_DESCRIPTION": "Box"},
                            {"UOM_LEVEL": 1, "CONV_FACTOR_SML": "1", "UOM_DESCRIPTION": "Piece"}],
                        "VARIANCE_QTY": "0",
                        "PHYSICAL_QTY": "0"
                    }
                ]
            }

        }

        return payload

    def user_creates_route_settlement_with_random_data(self):
        RouteSettlementGet().user_retrieves_transactions_for_route_settlement()
        route_id = BuiltIn().get_variable_value("${route_id}")
        last_rec_details = RouteSettlementGet().last_record_route(route_id)
        rs_payload = self.rs_payload(last_rec_details)
        rs_payload = json.dumps(rs_payload)
        url = "{0}route-settlement/{1}".format(END_POINT_URL, route_id)

        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, rs_payload)
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return str(response.status_code), response.json()

    def rs_payload(self, last_rec_details):

        last_rec_date = re.split("\s", last_rec_details['ROUTE_TXNDT_TO'], 1)[0] + "T00:00:00.000Z"
        route_details = {}
        route_details['ID'] = last_rec_details['ROUTE_ID']
        route_details['ROUTE_CD'] = BuiltIn().get_variable_value("${route_cd}")
        route_details['ROUTE_NAME'] = BuiltIn().get_variable_value("${route_name}")

        last_rec_details['ROUTE_TXNDT_FROM'] = last_rec_date
        last_rec_details['ROUTE_TXNDT_TO'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
        last_rec_details['CASHIER_CASH_AMT'] = 1

        last_rec_details['VAN'] = None

        last_rec_details['PRIME_FLAG'] = "PRIME"
        last_rec_details['ROUTE'] = route_details

        print("payload = " + json.dumps(last_rec_details))
        return last_rec_details
