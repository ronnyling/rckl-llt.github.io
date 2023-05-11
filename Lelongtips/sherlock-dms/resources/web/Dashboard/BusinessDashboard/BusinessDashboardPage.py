from PageObjectLibrary import PageObject


class BusinessDashboardPage(PageObject):
    """ Functions to check Dashboard title and endpoint after login """
    PAGE_TITLE = "Dashboard / Business Dashboard"
    PAGE_URL = "/rpt/Home/business_dashboard"

    _locators = {
    }
