from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class WhatappGet(object):
    """ Function to retrieve Whatapp """

    @keyword("user retrieves whatapp list of ${identity}")
    def user_gets_whatapp_list_of(self, identity):
        """ Function to retrieve whatapp using identity """
        url = "{0}contact/{1}".format(END_POINT_URL, identity)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("GET", url, "")
        body_result = response.json()
        BuiltIn().set_test_variable("${status_code}", response.status_code)
        return body_result, response.status_code

