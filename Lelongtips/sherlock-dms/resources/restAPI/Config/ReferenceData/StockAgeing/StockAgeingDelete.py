from resources.restAPI import PROTOCOL, APP_URL
from resources.restAPI.Common import APIMethod
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword

END_POINT_URL = PROTOCOL + "setting" + APP_URL


class StockAgeingDelete(object):

    @keyword('user deletes the ${aging_type} aging period')
    def user_deletes_the_aging_period(self, aging_type):
        """ Function to delete the aging period """
        if aging_type == 'created':
            aging_period_id = BuiltIn().get_variable_value("${AgingPeriodID}")
        else:
            aging_period_id = None
        url = "{0}aging-period/{1}".format(END_POINT_URL, aging_period_id)
        common = APIMethod.APIMethod()
        response = common.trigger_api_request("DELETE", url, "")
        BuiltIn().set_test_variable("${status_code}", response.status_code)
