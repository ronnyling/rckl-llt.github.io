from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, COMMON_KEY, TAB, DRPSINGLE, CHECKBOX


class SamplingAssignmentPage(PageObject):

    PAGE_TITLE = "Master Data Management / Sampling"
    PAGE_URL = "/promotion/sample"
    SAMPLE_DETAILS = "${sample_details}"
    _locators = {
        "add_dist_btn": "//*[contains(text(),'or Assignment')]/following::span[contains(text(),'Add')][1]/ancestor::core-button[1]"
    }

    @keyword('user creates ${level} assignment for sampling')
    def user_creates_assignment_for_sampling(self, level):
        TAB.user_navigate_to_tab("Sampling Assignment")
        level = level.split(":")
        self.add_assignment("Distributor", level[1])
        self.add_assignment("Customer", "")
        BUTTON.click_button("Save")

    def add_assignment(self, assignment_type, level):
        if assignment_type == "Distributor":
            self.click_add_dist_btn()
            DRPSINGLE.select_from_single_selection_dropdown("Level", level)
            CHECKBOX.select_checkbox(level + " Code", "vertical", "all", True)
            BUTTON.click_button("Assign")
        else:
            BUTTON.click_button("All")

    def click_add_dist_btn(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.add_dist_btn)
