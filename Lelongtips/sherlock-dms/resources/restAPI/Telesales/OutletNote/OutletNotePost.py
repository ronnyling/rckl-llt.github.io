import json
import secrets
import datetime
import logging

from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.restAPI.MasterDataMgmt.RouteMgmt.Route import RouteGet
from resources.restAPI.MasterDataMgmt.Distributor import DistributorGet
from resources.Common import Common
from setup.hanaDB import HanaDB

END_POINT_URL = PROTOCOL + "customer-transactions" + APP_URL


class OutletNotePost(object):
    """ Functions to create collection """

    @keyword('user creates outlet note with ${data_type} data')
    def user_creates_outlet_note_with(self, data_type):
        url = "{0}outletnote".format(END_POINT_URL)
        payload = self.note_payload()
        payload = json.dumps(payload)
        print(payload)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("POST", url, payload)
        assert response.status_code == 201
        BuiltIn().set_test_variable("${status_code}", response.status_code)

    def note_payload(self):
        dist_id = BuiltIn().get_variable_value("${distributor_id}")
        cust_id = BuiltIn().get_variable_value("${cust_id}")
        contact_id = BuiltIn().get_variable_value("${contact_id}")
        route_id = BuiltIn().get_variable_value("${route_id}")
        payload = {
              "DIST_ID": dist_id,
              "ROUTE_ID": route_id,
              "CUST_ID": cust_id,
              "CONTACT_ID": contact_id,
              "NOTES": ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10)),
        }

        details = BuiltIn().get_variable_value("${note_details}")
        if details:
            payload.update((k, v) for k, v in details.items())
        return payload

