from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, COMMON_KEY, TAB, DRPSINGLE, CHECKBOX, LABEL


class RouteActivityAssignmentPage(PageObject):

    PAGE_TITLE = "Merchandising / Merchandising Setup / Route Activity"
    RA_DETAILS = "${activity_details}"
    _locators = {
        "popup_code": "//*[contains(text(),'Add Customer')]/following::input[3]",
        "popup_search": "//*[contains(text(),'Add Customer')]//following::core-button[@ng-reflect-icon='search']",
        "popup_visit": "(//*[text()='Visit Frequency Code']//following::*//nz-select)[4]",
        "popup_target": "(//*[contains(text(),'Target Duration')]/following::input)[14]",
        "popup_checkbox": "//*[text()='Add Customer']//following::*[contains(@class,'checkbox')][1]",
        "dist_add_btn": "//*[contains(text(),'or Assignment')]/following::span[contains(text(),'Add')][1]/ancestor::core-button[1]"
    }

    @keyword('user assigns customer to ${activity} using ${data_type} data')
    def user_assigns_customer_to_route_activity(self, activity, data_type):
        details = self.builtin.get_variable_value(self.RA_DETAILS)
        TAB.user_navigate_to_tab("Customer Assignment")
        TAB.user_navigate_to_tab(activity)
        BUTTON.click_button("Add")
        LABEL.validate_label_is_visible("Add Customer")
        self.filter_customer_by_code(details['CODE'])
        DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.popup_visit, details['VISIT_FREQUENCY'])
        self.selib.input_text(self.locator.popup_target, details['TARGET_DURATION'])
        COMMON_KEY.wait_keyword_success("click_element", self.locator.popup_checkbox)
        BUTTON.click_button("Assign")

    def filter_customer_by_code(self, code):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.popup_search)
        self.selib.input_text(self.locator.popup_code, code)

    @keyword('user adds ${level} assignment to route activity')
    def user_adds_assignment_to_route_activity(self, level):
        TAB.user_navigate_to_tab("Route Assignment")
        level = level.split(":")
        self.add_activity_assignment("Distributor", level[1])
        self.add_activity_assignment("Route", "")
        BUTTON.click_button("Save")

    def add_activity_assignment(self, assignment_type, level):
        if assignment_type == "Distributor":
            self.click_add_dist_button()
            DRPSINGLE.select_from_single_selection_dropdown("Level", level)
            CHECKBOX.select_checkbox(level + " Code", "vertical", "all", True)
            BUTTON.click_button("Assign")
        else:
            BUTTON.click_button("All")

    def click_add_dist_button(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.dist_add_btn)
