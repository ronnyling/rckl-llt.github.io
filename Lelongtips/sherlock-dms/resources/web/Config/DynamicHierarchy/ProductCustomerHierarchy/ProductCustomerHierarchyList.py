from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import secrets
import string


class ProductCustomerHierarchyList(PageObject):
    PAGE_TITLE = "Configuration / Dynamic Hierarchy / Product/Customer Hierarchy"
    PAGE_URL = "/dynamic-hierarchy/productcustomerhierarchy"

    _locators = \
        {
            "Add": "//span[contains(text(),'Add')]/parent::button[1]",
            "Save": "//span[contains(text(),'Save')]/parent::button[1]",
            "Delete": "//button[@class='ant-btn ng-star-inserted ant-btn-default ant-btn-icon-only']",
            "HierarchyTypeDropdown": "(//label[contains(text(),'Hierarchy Type')]/following::*//div[@class='ant-select-selection__rendered'])[1]",
            "HierarchyTypeBox": "(//label[contains(text(),'Hierarchy Type')]/following::*//input)[1]",
            "HierarchyListDropdown": "(//label[contains(text(),'Hierarchy List')]/following::*//div[@class='ant-select-selection__rendered'])[1]",
            "HierarchyListBox": "(//label[contains(text(),'Hierarchy List')]/following::*//input)[1]",
            "ItemCodeBox": "(//label[contains(text(),'Item Code')]/following::*//input)[1]",
            "ItemDescriptionBox": "(//label[contains(text(),'Item Description')]/following::*//input)[1]",
        }

    timeout = "0.5 min"
    wait = "3 sec"

    @keyword("user creates new hierarchy list value with ${data}")
    def new_list_value(self, data):
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")

        if data != 'random':

            # set hierarchy type
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.HierarchyTypeDropdown)
            self.selib.input_text(self.locator.HierarchyTypeBox,
                                  data.get('HierarchyType'))
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", "//li[contains(text(),'%s')]"
                                                     % data.get('HierarchyType'))

            # set hierarchy list
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.HierarchyListDropdown)
            self.selib.input_text(self.locator.HierarchyListBox,
                                  data.get('HierarchyType'))
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", "//li[contains(text(),'%s')]"
                                                     % data.get('HierarchyList'))

            # select level
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     "//span[contains(text(),'%s')]" % data.get('Levels'))

            # click Add
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.Add)

            # enter item code and description
            if data.get('ItemCode') != "":
                self.selib.input_text(self.locator.ItemCodeBox,
                                      data.get('ItemCode'))
                self.selib.input_text(self.locator.ItemDescriptionBox,
                                      data.get('ItemDescription'))
            else:
                self.selib.input_text(self.locator.ItemCodeBox,
                                      ''.join(secrets.choice(string.ascii_lowercase) for _ in range(7)))
                self.selib.input_text(self.locator.ItemDescriptionBox,
                                      ''.join(secrets.choice(string.ascii_lowercase) for _ in range(7)))

        else:
            total = self.selib.get_element_count(self.locator.dropdown)
            count = secrets.randint(1, total)

            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.HierarchyTypeDropdown)
            self.selib.click_element("(//*[@class='cdk-overlay-pane']//following-sibling::li)[{0}]".format(count))
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.HierarchyListDropdown)
            self.selib.click_element("(//*[@class='cdk-overlay-pane']//following-sibling::li)[{0}]".format(count))
            self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                     self.locator.Add)
            self.selib.input_text(self.locator.ItemCodeBox,
                                  ''.join(secrets.choice(string.ascii_lowercase) for _ in range(7)))
            self.selib.input_text(self.locator.ItemDescriptionBox,
                                  ''.join(secrets.choice(string.ascii_lowercase) for _ in range(7)))

        # click Save
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 self.locator.Save)

    def create_list_from_collection_of_data(self):
        data = BuiltIn().get_variable_value("&{file_data}")
        for key_invoices in data:
            self.new_list_value(key_invoices)

    def delete_list_value(self):    # there is no way to perform search via UI so this is put on hold
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 self.locator.Delete)
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
