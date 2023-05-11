from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import CALENDAR

class RouteCoverageEditPage(PageObject):


    @keyword('user updates the route coverage date')
    def update_route_coverage_date(self):
        st_date = 'Jan 1, 2025'
        end_date = 'Jan 1, 2026'
        CALENDAR.selects_date_from_calendar("From Date", st_date)
        CALENDAR.selects_date_from_calendar("To Date", end_date)