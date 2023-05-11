from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.web import BUTTON, CALENDAR, DRPSINGLE


class RouteCoverageAddPage(PageObject):

    @keyword('user creates route coverage using ${data_type} data')
    def user_creates_route_coverage_using_data(self, data_type):
        """ Function to create route coverage with random/given data """
        BUTTON.click_button("Add")
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
        route_coverage = BuiltIn().get_variable_value("${RouteCoverage}")
        if route_coverage is not None:
            route_from = route_coverage["RouteFrom"]
            route_to = route_coverage["RouteTo"]
            start_date = route_coverage["Start_date"]
            end_date = route_coverage["End_date"]
        else:
            route_from = "random"
            route_to = "random"
            start_date = "next week"
            end_date = "next month"
        DRPSINGLE.select_from_single_selection_dropdown("From Route Name", route_from)
        DRPSINGLE.select_from_single_selection_dropdown("To Route Name", route_to)
        st_date = CALENDAR.validate_and_return_date(start_date)
        start_date = CALENDAR.selects_date_from_calendar("From Date", st_date)
        end_date = CALENDAR.select_date_from_calendar("To Date", end_date)
        BuiltIn().set_test_variable("${start_date}", st_date)
        BuiltIn().set_test_variable("${end_date}", end_date)
        BUTTON.click_button("Save")
