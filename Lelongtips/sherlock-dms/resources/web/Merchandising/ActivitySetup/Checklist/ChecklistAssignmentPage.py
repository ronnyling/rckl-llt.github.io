from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, COMMON_KEY, TAB, DRPSINGLE, CHECKBOX


class ChecklistAssignmentPage(PageObject):

    PAGE_TITLE = "Merchandising / Activity Setup / Checklist"
    PAGE_URL = "/merchandising/checklist"
    CL_DETAILS = "${checklist_details}"
    _locators = {
        "dist_add_btn": "//*[contains(text(),'or Assignment')]/following::span[contains(text(),'Add')][1]/ancestor::core-button[1]"
    }

    @keyword('user adds ${level} assignment to merchandising checklist')
    def user_adds_assignment_to_merchandising_checklist(self, level):
        TAB.user_navigate_to_tab("Customer Assignment")
        level = level.split(":")
        self.add_assignment("Distributor", level[1])
        self.add_assignment("Customer", "")
        BUTTON.click_button("Save")

    def add_assignment(self, assignment_type, level):
        if assignment_type == "Distributor":
            self.click_add_dist_button()
            DRPSINGLE.select_from_single_selection_dropdown("Level", level)
            CHECKBOX.select_checkbox(level + " Code", "vertical", "all", True)
            BUTTON.click_button("Assign")
        else:
            BUTTON.click_button("All")

    def click_add_dist_button(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.dist_add_btn)
