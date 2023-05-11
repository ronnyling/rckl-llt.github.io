from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class APIAssertion(object):

    @keyword('expected return status code ${expected_status}')
    def expected_return_status_code(self, expected_status):
        status_code = BuiltIn().get_variable_value("${status_code}")
        print("str(expected_status)", str(expected_status))
        print("str(status_code)", str(status_code))
        assert str(expected_status) == str(status_code), "Status Code is not match"

    @keyword('expected return either status code ${expected_status} or status code ${expected_status1}')
    def expected_return_either_status_code_or_status_code(self, expected_status, expected_status1):
        """ Functions to accept either one of the status code """
        status_code = BuiltIn().get_variable_value("${status_code}")
        assert (expected_status == str(status_code) or expected_status1 == str(status_code)), "Status Code is not match"
