import time
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, LABEL, COMMON_KEY
from resources.web.Common import MenuNav
from robot.api.deco import keyword


class ParameterAddPage(PageObject):
    """ Functions related to delivery sheet - parent page list page """
    PAGE_TITLE = "Customer Transaction | Pick List "
    PAGE_URL = "/customer-transactions-ui/picklist/delivery-optimisation/NEW"
    AVG_TIME = "Average Service Time Per Customer (Mins)"
    DELIVERY_OPT = "Delivery Optimization"

    _locators = {
        "average_service_time_per_customer": "(//label[contains(text(),'Average Service Time Per Customer (Mins)')]/following::input)[1]",
        "average_van_speed": "(//label[contains(text(),'Average Van Speed (KM/H)')]/following::input)[2]",
        "delivery_start_time": "(//label[contains(text(),'Delivery Start Time')]/following::input)[1]",
        "delivery_end_time": "(//label[contains(text(),'Delivery End Time')]/following::input)[1]",
        "overlay": "//*[@class='cdk-overlay-container']"
    }

    @keyword('user creates parameter with ${data_type} data')
    def user_inserts_parameter_info(self, data_type):
        print("Average Time = ", self.locator.AVG_TIME)
        BUTTON.click_button(self.locator.DELIVERY_OPT)
        time.sleep(30)
        if data_type == 'fixed':
            details = BuiltIn().get_variable_value("${ParameterDetails}")
            print("DETAILS ==== ", details)
            if details['avg_time']:
                TEXTFIELD.insert_into_field(self.locator.AVG_TIME, details['avg_time'])
            if details['start_hours']:
                COMMON_KEY.wait_keyword_success("click_element",
                                                "(//*[contains(text(),'Delivery Start Time')]/following::input)[1]")
                COMMON_KEY.wait_keyword_success("click_element",
                                                "//div[@class='ant-time-picker-panel-select ng-star-inserted'][1]//li[contains(text(),'{0}')]".format(
                                                    details['start_hours']))
                COMMON_KEY.wait_keyword_success("click_element",
                                                "//div[@class='ant-time-picker-panel-select ng-star-inserted'][2]//li[contains(text(),'{0}')]".format(
                                                    details['minutes']))
                COMMON_KEY.wait_keyword_success("click_element",
                                                self.locator.overlay)
            if details['end_hours']:
                COMMON_KEY.wait_keyword_success("click_element",
                                                "(//*[contains(text(),'Delivery End Time')]/following::input)[1]")
                COMMON_KEY.wait_keyword_success("click_element",
                                                "//div[@class='ant-time-picker-panel-select ng-star-inserted'][1]//li[contains(text(),'{0}')]".format(
                                                    details['end_hours']))
                COMMON_KEY.wait_keyword_success("click_element",
                                                "//div[@class='ant-time-picker-panel-select ng-star-inserted'][2]//li[contains(text(),'{0}')]".format(
                                                    details['minutes']))
                COMMON_KEY.wait_keyword_success("click_element",
                                                self.locator.overlay)
        else:
            TEXTFIELD.insert_into_field_with_length(self.locator.AVG_TIME, "number", 2)
            COMMON_KEY.wait_keyword_success("click_element",
                                            "(//*[contains(text(),'Delivery Start Time')]/following::input)[1]")
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//div[@class='ant-time-picker-panel-select ng-star-inserted'][1]//li[contains(text(),'09')]")
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//div[@class='ant-time-picker-panel-select ng-star-inserted'][2]//li[contains(text(),'30')]")
            COMMON_KEY.wait_keyword_success("click_element",
                                            self.locator.overlay)

            COMMON_KEY.wait_keyword_success("click_element",
                                            "(//*[contains(text(),'Delivery End Time')]/following::input)[1]")
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//div[@class='ant-time-picker-panel-select ng-star-inserted'][1]//li[contains(text(),'16')]")
            COMMON_KEY.wait_keyword_success("click_element",
                                            "//div[@class='ant-time-picker-panel-select ng-star-inserted'][2]//li[contains(text(),'30')]")
            COMMON_KEY.wait_keyword_success("click_element",
                                            self.locator.overlay)

        BUTTON.click_button("Next")

    @keyword('user validates ${field_type} button is ${status}')
    def user_validates_next_button(self, field_type, status):
        """ Function to validate next button visibility """
        BUTTON.click_button("Delivery Optimization")
        time.sleep(30)
        if status == 'disable':
            BUTTON.click_button("Next")
            status = LABEL.return_visibility_status_for(field_type)
            assert status is False, "Next button is disabled!"
        else:
            status = BUTTON.check_button_is_disabled("Next")
            assert status is True, "Next button not being disabled!"

    @keyword('validate UI display in parameter page')
    def validate_UI_display_on_parameter_tab(self, title):
        """ Functions to validate UI display in parameter page """
        if title == "average_service_time_per_customer":
            MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | Pick List")
            BUTTON.click_button(self.locator.DELIVERY_OPT)
            time.sleep(30)

            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.average_service_time_per_customer)
        elif title == "average_van_speed":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.average_van_speed)
        elif title == "delivery_start_time":
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.delivery_start_time)
        else:
            COMMON_KEY.wait_keyword_success("page_should_contain_element",
                                            self.locator.delivery_end_time)

    @keyword('validate the mandatory field on parameter tab')
    def validate_mandatory_field_on_parameter_tab(self, label_list):
        """ Functions to validate the mandatory field on parameter tab """
        print(label_list)
        if label_list == self.locator.AVG_TIME:
            MenuNav.MenuNav().user_navigates_to_menu("Customer Transaction | Pick List")
            BUTTON.click_button(self.locator.DELIVERY_OPT)
            time.sleep(40)
            status = LABEL.return_visibility_status_for("Next")

        if label_list == "Average Van Speed (KM/H)":
            status = LABEL.return_visibility_status_for("Next")

        if label_list == "Delivery Start Time":
            status = LABEL.return_visibility_status_for("Next")

        if label_list == "Delivery End Time":
            TEXTFIELD.insert_into_field_with_length(self.locator.AVG_TIME, "10", 2)
            status = LABEL.return_visibility_status_for("Next")
        print(status, "Next button is disabled")
