from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import COMMON_KEY, PAGINATION, LABEL, TAB, BUTTON, POPUPMSG, CHECKBOX, DRPSINGLE
from resources.Common import Common


class DigitalPlaybookAssignmentPage(PageObject):
    """ Functions related to listing page of Digital Playbook Assignment """

    PAGE_TITLE = "Master Data Management / Digital Playbook"
    PAGE_URL = "/setting-ui/playbk-setup/${playbook_id}"
    PLAYBOOK_CD = "${playbk_cd}"
    PLAYBOOK_ASS_TO = "${playbk_ass_to}"

    dist_ass = "Distributor Assignment"
    route_ass = "Route Assignment"
    cust_ass = "Customer Assignment"
    dist_error = "Distributor assignment list is not refreshed"
    excl = " Exclusion"
    level = [
        "Country",
        "Region",
        "State",
        "Sales Office"
    ]
    _locators = {
        "tab_add_btn": "//*[contains(text(),'{0}')]/following::span[contains(text(),'Add')][1]/ancestor::core-button[1]",
        "playbk_cd": "//*[@role='row' and @row-index='0']//*[@col-id='PLAYBK_CD']",
        "add_exclusion_link": "//*[@role='tab']//*[contains(text(),'{0}')]",
        "exclusion_field": "//input[@placeholder='Enter Code / Name']",
        "select_in_exclusion_field": "//*[contains(text(),'{0}')]",
        "remove_exclusion_link": "//*[contains(text(),'{0}')]//following::*[contains(text(), 'Excluded')][1]",
        "check_all": "//*[contains(text(),'{0}')]//following::*[contains(text(),'{1}')][1]//preceding::label[1]",
        "delete_all": "//*[contains(text(),'{0}')]/following::*[contains(text(),'Selected')][1]/following::*[@ng-reflect-icon='delete'][1]",
        "first_row_selection": "//*[@role='row' and @row-index='0']//*[@col-id='{0}']",
        "load_image": "//div[@class='loading-text']//img",
        "assignment_hyperlink": "//*[contains(text(),'{0}')]/following::a[1]"
    }

    @keyword('user selects playbook to ${data_type}')
    def user_selects_playbook_to(self, action):
        """ Function to select playbook in listing to edit """
        playbook_cd = self.builtin.get_variable_value(self.PLAYBOOK_CD)
        if playbook_cd is None:
            Common().wait_keyword_success("wait_until_element_is_visible", self.locator.playbk_cd)
            playbook_cd = COMMON_KEY.wait_keyword_success("get_text", self.locator.playbk_cd)
        col_list = ["PLAYBK_CD"]
        data_list = [playbook_cd]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "Playbook", action, col_list, data_list)

    @keyword('user validates ${type} playbook assignment')
    def validate_distributor_assignment(self, type):
        LABEL.validate_label_is_visible("EDIT")
        TAB.user_navigate_to_tab("Assignment")
        LABEL.validate_label_is_visible(self.dist_ass)
        dist_before = self.selib.get_text(self.locator.assignment_hyperlink.format(self.dist_ass))
        self.add_assignment("Distributor", "Sales Office")
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        dist_after = self.selib.get_text(self.locator.assignment_hyperlink.format(self.dist_ass))
        if dist_before == dist_after:
            raise ValueError(self.dist_error)
        if type == "route":
            self.validate_route_assignment()
        elif type == "customer":
            self.validate_customer_assignment()

    def validate_route_assignment(self):
        LABEL.validate_label_is_visible("EDIT")
        TAB.user_navigate_to_tab("Assignment")
        LABEL.validate_label_is_visible(self.route_ass)
        route_before = self.selib.get_text(self.locator.assignment_hyperlink.format(self.route_ass))
        self.add_assignment("Route", "")
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        route_after = self.selib.get_text(self.locator.assignment_hyperlink.format(self.route_ass))
        if route_before == route_after:
            raise ValueError(self.dist_error)

    def validate_customer_assignment(self):
        LABEL.validate_label_is_visible("EDIT")
        TAB.user_navigate_to_tab("Assignment")
        LABEL.validate_label_is_visible(self.cust_ass)
        cust_before = self.selib.get_text(self.locator.assignment_hyperlink.format(self.cust_ass))
        self.add_assignment("Customer", "")
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        cust_after = self.selib.get_text(self.locator.assignment_hyperlink.format(self.cust_ass))
        if cust_before == cust_after:
            raise ValueError("Customer assignment list is not refreshed")

    @keyword('user add ${level} assignment to ${type} playbook')
    def user_add_assignment_to_playbook(self, level, type):
        LABEL.validate_label_is_visible("EDIT")
        TAB.user_navigate_to_tab("Assignment")
        level = level.split(":")
        self.add_assignment("Distributor", level[1])
        if type == "C":
            self.add_assignment("Customer", "")
        else:
            self.add_assignment("Route", "")
        BUTTON.click_button("Save")

    @keyword('user exclude ${excl} from ${type} playbook')
    def user_exclude_from_playbook(self, excl, type):
        LABEL.validate_label_is_visible("EDIT")
        TAB.user_navigate_to_tab("Assignment")
        excl = excl.split(":")
        if excl[0] == "Distributor":
            dist_before = self.selib.get_text(self.locator.assignment_hyperlink.format(self.dist_ass))
            self.add_exclusion("Distributor", excl[1], "")
            self.selib.wait_until_element_is_not_visible(self.locator.load_image)
            dist_after = self.selib.get_text(self.locator.assignment_hyperlink.format(self.dist_ass))
            if dist_before == dist_after:
                raise ValueError(self.dist_error)
        elif excl[0] == "Customer":
            cust_before = self.selib.get_text(self.locator.assignment_hyperlink.format(self.cust_ass))
            excl = excl[1].split(",")
            self.add_exclusion("Customer", excl[0], excl[1])
            self.selib.wait_until_element_is_not_visible(self.locator.load_image)
            cust_after = self.selib.get_text(self.locator.assignment_hyperlink.format(self.cust_ass))
            if cust_before == cust_after:
                raise ValueError("Customer assignment list is not refreshed")
        else:
            route_before = self.selib.get_text(self.locator.assignment_hyperlink.format(self.route_ass))
            excl = excl[1].split(",")
            self.add_exclusion("Route", excl[0], excl[1])
            self.selib.wait_until_element_is_not_visible(self.locator.load_image)
            route_after = self.selib.get_text(self.locator.assignment_hyperlink.format(self.route_ass))
            if route_before == route_after:
                raise ValueError("Route assignment list is not refreshed")
        BUTTON.click_button("Save")

    @keyword('user deletes assignment from playbook')
    def user_deletes_assignment_from_playbook(self):
        LABEL.validate_label_is_visible("EDIT")
        TAB.user_navigate_to_tab("Assignment")
        LABEL.validate_label_is_visible(self.dist_ass)
        dist_before = self.selib.get_text(self.locator.assignment_hyperlink.format(self.dist_ass))
        self.check_all_selection(self.dist_ass, "Level Code")
        self.click_to_delete_all(self.dist_ass)
        POPUPMSG.validate_pop_up_msg("Are you sure you want to delete?")
        BUTTON.click_pop_up_screen_button("Yes")
        LABEL.validate_label_is_visible("EDIT")
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        dist_after = self.selib.get_text(self.locator.assignment_hyperlink.format(self.dist_ass))
        if dist_before == dist_after:
            raise ValueError(self.dist_error)
        BUTTON.click_button("Save")

    @keyword('user remove ${type} exclusion from playbook')
    def user_remove_exclusion_from_playbook(self, type):
        LABEL.validate_label_is_visible("EDIT")
        TAB.user_navigate_to_tab("Assignment")
        self.remove_exclusion(type)
        BUTTON.click_button("Save")

    def add_assignment(self, type, level):
        LABEL.validate_label_is_visible(type + " Assignment")
        if type == "Distributor":
            self.click_add_button_on_tab(self.dist_ass)
            DRPSINGLE.select_from_single_selection_dropdown("Level", level)
            CHECKBOX.select_checkbox(level + " Code", "vertical", "all", True)
            BUTTON.click_button("Assign")
        else:
            BUTTON.click_button("All")

    def add_exclusion(self, type, dist_excl, next_excl):
        excl_type = type + self.excl
        self.click_to_add_exclusion(excl_type)
        LABEL.validate_label_is_visible(excl_type)
        self.insert_into_exclusion_field(dist_excl)
        self.select_data_in_exclusion(dist_excl)
        if type != "Distributor":
            self.insert_into_exclusion_field(next_excl)
            self.select_data_in_exclusion(next_excl)
        BUTTON.click_button("Exclude")

    def remove_exclusion(self, type):
        excl_type = type + self.excl
        self.click_to_remove_exclusion(type + " Assignment")
        LABEL.validate_label_is_visible(excl_type)
        self.check_all_selection(excl_type, "Distributor Code")
        self.click_to_delete_all(excl_type)
        LABEL.validate_label_is_visible("Delete")
        BUTTON.click_pop_up_screen_button("Yes")
        LABEL.validate_label_is_visible(excl_type)
        BUTTON.click_button("Cancel")
        LABEL.validate_label_is_visible("EDIT")

    def insert_into_exclusion_field(self, item):
        COMMON_KEY.wait_keyword_success("input_text", self.locator.exclusion_field, item)

    def click_exclusion_field(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.exclusion_field)

    def click_first_row(self, label):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.first_row_selection.format(label))

    def select_data_in_exclusion(self, label):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.select_in_exclusion_field.format(label))

    def check_all_selection(self, label, checkbox_label):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.check_all.format(label, checkbox_label))

    def click_to_add_exclusion(self, label):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.add_exclusion_link.format(label))

    def click_to_remove_exclusion(self, label):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.remove_exclusion_link.format(label))

    def click_add_button_on_tab(self, label):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.tab_add_btn.format(label))

    def click_to_delete_all(self, label):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.delete_all.format(label))