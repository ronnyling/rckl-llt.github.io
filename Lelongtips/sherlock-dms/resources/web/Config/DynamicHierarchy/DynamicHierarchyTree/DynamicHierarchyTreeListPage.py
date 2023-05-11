from PageObjectLibrary import PageObject
from robot.api.deco import keyword
import time


class DynamicHierarchyTreeListPage(PageObject):
    PAGE_TITLE = "Dynamic Hierarchy Tree"
    PAGE_URL = "/hierarchy-tree"

    _locators = \
        {
            "Add": "//span[contains(text(),'Add')]/parent::button[1]",
            "Search": "(//button[@class='ant-btn ng-star-inserted ant-btn-icon-only'])[1]",
            "SearchBox": "(//div[contains(text(),'Description')]/following::input)[1]",
        }

    timeout = "0.2 min"
    wait = "3 sec"

    def wait_till_loading_icon_done(self):
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")

    def click_add(self):
        self.wait_till_loading_icon_done()
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Add)
        self.wait_till_loading_icon_done()

    @keyword("user deletes the newly created hierarchy structure with ${data}")
    def delete_structure(self, data):
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 "(//a[contains(text(),'%s')]//preceding::span[@class='ant-checkbox'])[last()]"
                                                 % data.get('DynamicHierarchyTree-Description'))
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 "//core-dynamic-actions[@class='selection-actions']//"
                                                 "button[@class='ant-btn ng-star-inserted ant-btn-icon-only']")
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 "//button[@class='ant-btn ng-star-inserted ant-btn-dafault']")
        self.wait_till_loading_icon_done()

    @keyword("user searches the newly created hierarchy structure with ${data}")
    def search_structure(self, data):
        self.wait_till_loading_icon_done()
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)
        time.sleep(2)
        self.selib.input_text(self.locator.SearchBox, data.get('DynamicHierarchyTree-Description'))
