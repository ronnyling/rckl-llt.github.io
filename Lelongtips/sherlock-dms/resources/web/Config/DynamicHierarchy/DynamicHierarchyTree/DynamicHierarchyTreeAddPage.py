from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web.Config.DynamicHierarchy.DynamicHierarchyTree import DynamicHierarchyTreeListPage


class DynamicHierarchyTreeAddPage(PageObject):
    PAGE_TITLE = "ADD / Dynamic Hierarchy Tree"
    PAGE_URL = "/hierarchy-tree"

    _locators = \
        {
            "DescriptionBox": "(//label[contains(text(),'Description')]/following::*//input)[1]",
            "HierarchyStructureDropdown": "(//label[contains(text(),'Hierarchy Structure')]/following::*//div[@class='ant-select-selection__rendered'])[1]",
            "HierarchyStructureBox": "(//label[contains(text(),'Hierarchy Structure')]/following::*//input)[1]",
            "SaveButton": "//span[contains(text(),'Save')]/parent::button[1]",
            "HierarchyLevelAdd": "//div[@class='ant-card-extra ng-star-inserted']//button[@class='ant-btn ng-star-inserted ant-btn-default ant-btn-icon-only']",
            "LineOfBusinessDropdown": "(//label[contains(text(),'Line of Business')]/following::*//div[@class='ant-select-selection__rendered'])[1]",
            "LineOfBusinessBox": "(//label[contains(text(),'Line of Business')]/following::*//input)[1]",
            "HierarchyLevelsBox": "(//*[text()='Hierarchy Level']/following::*//core-textfield[@class='ng-untouched ng-pristine ng-valid ng-star-inserted']//input)",
        }

    timeout = "0.5 min"
    wait = "3 sec"

    @keyword("user creates new hierarchy structure with ${data}")
    def create_new_structure(self, data):
        DynamicHierarchyTreeListPage.DynamicHierarchyTreeListPage().click_add()
        self.selib.input_text(self.locator.DescriptionBox, data.get('DynamicHierarchyTree-Description'))

        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 self.locator.HierarchyStructureDropdown)
        self.selib.input_text(self.locator.HierarchyStructureBox, data.get('DynamicHierarchyTree-HierarchyStructure'))
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", "//li[contains(text(),'%s')]"
                                                 % data.get('DynamicHierarchyTree-HierarchyStructure'))

        if data.get('DynamicHierarchyTree-LOB') is not None:    # LOB selection only shows up when hierarchy structure is Sales Org type
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.LineOfBusinessDropdown)
            self.selib.input_text(self.locator.LineOfBusinessBox,
                                  data.get('DynamicHierarchyTree-LOB'))
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", "//li[contains(text(),'%s')]"
                                                     % data.get('DynamicHierarchyTree-LOB'))

        if data.get('DynamicHierarchyTree-HierarchyLevels 1') != "":    # optional hierarchy levels assignment to structure
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.HierarchyLevelAdd)
            self.selib.input_text(self.locator.HierarchyLevelsBox,
                                  data.get('DynamicHierarchyTree-HierarchyLevels 1'))

        if data.get('DynamicHierarchyTree-HierarchyLevels 2') != "":      # optional hierarchy levels assignment to structure
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.HierarchyLevelAdd)
            self.selib.input_text(self.locator.HierarchyLevelsBox,
                                  data.get('DynamicHierarchyTree-HierarchyLevels 2'))

        if data.get('DynamicHierarchyTree-HierarchyLevels 3') != "":      # optional hierarchy levels assignment to structure
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.HierarchyLevelAdd)
            self.selib.input_text(self.locator.HierarchyLevelsBox,
                                  data.get('DynamicHierarchyTree-HierarchyLevels 3'))

        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 self.locator.SaveButton)

    def create_new_structure_with_collection_of_data(self):
        data = BuiltIn().get_variable_value("&{file_data}")
        for key_invoices in data:
            self.create_new_structure(key_invoices)
