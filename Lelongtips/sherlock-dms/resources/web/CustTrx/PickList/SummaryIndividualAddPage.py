import time
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, COMMON_KEY
from resources.web.Common import MenuNav


class SummaryIndividualAddPage(PageObject):
    """ Functions related to delivery sheet - parent page list page """
    PAGE_TITLE = "Customer Transaction | Pick List "
    PAGE_URL = "/customer-transactions-ui/picklist/delivery-optimisation/NEW"
    DELIVERY_OPT = "Delivery Optimization"

    _locators = {
        "total_customers": "(//div[@class='ant-col ant-col-4'][contains(text(),'Total Customers:')]/following::input)[1]",
        "estimate_service_time": "(//div[contains(text(),'Estimated Service Time (MINS):')]/following::input)[2]",
        "available_capacity": "(//div[contains(text(),'Available Capacity (KG):')]/following::input)[1]",
        "sequence": "(//div[@class='cell-render integer ng-star-inserted'][contains(text(),'Sequence')]/following::input)[1]",
        "customer": "(//div[@class='cell-render text ng-star-inserted'][contains(text(),'Customer')]/following::input)[1]",
        "address": "(//div[@class='cell-render text ng-star-inserted'][contains(text(),'Address')]/following::input)[1]",
        "net_weight": "(//div[@class='cell-render text ng-star-inserted'][contains(text(),'Net Weight (KG)')]/following::input)[1]"
    }

    @keyword("user able to view the delivery route for ${cust_num} customer")
    def user_view_delivery_route(self, cust_num):
        if cust_num == 'one':
            BUTTON.click_tab("1")
            COMMON_KEY.wait_keyword_success("click_element",
                                            "(//*[text()='Sequence']/following::*//*[@class='ant-checkbox'])[1]")
            self.user_navigates_to_tab("View Delivery Route Map")
            BUTTON.click_zoom_in_button("+")
            BUTTON.click_zoom_out_button("-")
            BUTTON.click_fullscreen_button("Full Screen")
            time.sleep(3)
            BUTTON.click_fullscreen_button("Full Screen")
            BUTTON.click_close_button('svg')
        else:
            BUTTON.click_tab("1")
            COMMON_KEY.wait_keyword_successs("click_element",
                                             "(//*[text()='Sequence']/following::*//*[@class='ant-checkbox'])[0]")

    @keyword("Validate UI shown in Summary individual van page")
    def validate_UI_display_on_summary_individual_van_tab(self, title):
        """ Functions to validate UI display in Summary individual van  page """
        if title == "total_customers":
            MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | Pick List")
            BUTTON.click_button(self.locator.DELIVERY_OPT)
            time.sleep(30)
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.total_customers)
        elif title == "estimate_service_time":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.estimate_service_time)
        elif title == "available_capacity":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.available_capacity)
        elif title == "sequence":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.sequence)
        elif title == "customer":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.customer)
        elif title == "address":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.address)
        else:
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.net_weight)

    @keyword("user click the ${save} button")
    def validate_save_button(self, save):
        BUTTON.click_button(self.locator.DELIVERY_OPT)
        time.sleep(30)
        BUTTON.click_button(save)

    def user_navigates_to_tab(self, tab_label):
        """ Functions to navigate to specific tab """
        COMMON_KEY.wait_keyword_success("click_element",
                                        "//a[contains(text(),'{0}')]".format(tab_label))
