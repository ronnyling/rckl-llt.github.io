from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web.PerformanceMgmt.MSL import MSLAddPage
from resources import Common
from resources.web import TEXTFIELD, DRPSINGLE, BUTTON, CALENDAR, TOGGLE

class MSLUpdatePage(PageObject):
    PAGE_TITLE = "Performance Management / Must Sell List"
    PAGE_URL = "/performance/msl/NEW"
    MSL_DETAILS="${msl_details}"
    MSL_DESC = "Description"
    _locators = {
        "product_del" : "(//core-button[@ng-reflect-icon='delete'])[1]",
        "dist_del" : "(//core-button[@ng-reflect-icon='delete'])[2]",
        "route_del": "(//core-button[@ng-reflect-icon='delete'])[3]",
        "customer_del": "(//core-button[@ng-reflect-icon='delete'])[4]",
        "attr_del": "(//core-button[@ng-reflect-icon='delete'])[5]"
    }

    @keyword('user updates MSL using ${data_type} data')
    def user_updates_msl_with_data(self, data_type):
        MSLAddPage.MSLAddPage().user_creates_msl_with_data("update")


    @keyword('user deletes MSL ${type} assignment')
    def user_deletes_msl_assignment(self, type):
        if type=="product":
            Common().wait_keyword_success("click_element", self.locator.product_del)
        elif type=="distributor":
            Common().wait_keyword_success("click_element", self.locator.dist_del)
        elif type == "route":
            Common().wait_keyword_success("click_element", self.locator.route_del)
        elif type == "customer":
            Common().wait_keyword_success("click_element", self.locator.customer_del)
        else :
            Common().wait_keyword_success("click_element", self.locator.attr_del)
        BUTTON.click_pop_up_screen_button("Yes")
        BUTTON.click_button("Cancel")


