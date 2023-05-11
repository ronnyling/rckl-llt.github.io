import secrets
from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.components import COMMON_KEY


class DrpSingleSelection(PageObject):
    SELECTED_ITEM = "${selectedItem}"

    _locators = {
        "dropdown": "//*[@class='cdk-overlay-pane']//following-sibling::li",
        "dn_cust_dropdown": "//*[@class='cdk-overlay-pane']//following-sibling::tr",
        "CustSel": "//*[@class='cdk-overlay-pane']//following-sibling::*",
        "CustDrp": "//label[text()='Customer']//following::nz-select[1]",
        "CustField": "//label[text()='Customer']//following::input[1]",
        "itemlist": "//*[@nz-option-li='']",
        "dynamic_dropdown": "{0}[contains(text(),'{1}')]",
        "dropdown_path": "//label[text()='{0}']//following::*//nz-select",
        "dropdown_first_path": "(//*[text()='{0}']//following::*//nz-select)[1]",
        "input_path": "{0}//input"
    }

    # used for module setup
    def selects_from_single_selection_dropdown(self, label, item):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.dropdown_path.format(label))
        if item == "random":
            self.randomize_dropdown_selection_in_dropdown()
        else:
            self.selib.input_text("//label[text()='{0}']//following::*//nz-select//input".format(label), item)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.dynamic_dropdown.format(self.locator.dropdown, item))
        item = self.selib.get_text(self.locator.dropdown_path.format(label))
        return item

    def select_from_single_selection_dropdown(self, label, item):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.dropdown_first_path.format(label))
        if item == "random":
            self.randomize_dropdown_selection_in_dropdown()
        else:
            self.selib.input_text("(//*[text()='{0}']//following::*//nz-select)[1]//input".format(label), item)
            self.selib.wait_until_element_is_visible(self.locator.dynamic_dropdown.format(self.locator.dropdown, item))
            self.selib.click_element(self.locator.dynamic_dropdown.format(self.locator.dropdown, item))
            item = self.selib.get_text(self.locator.dropdown_first_path.format(label))
        return item

    def select_from_single_selection_dropdown_with_count(self, label, item, count):
        COMMON_KEY.wait_keyword_success("click_element",
                                "(//*[text()='{0}']//following::*//nz-select)[{1}]".format(label, count))
        if item == "random":
            self.randomize_dropdown_selection_in_dropdown()
        else:
            self.selib.input_text(self.locator.dropdown_first_path + "//input", item)
            self.selib.wait_until_element_is_visible(self.locator.dynamic_dropdown.format(self.locator.dropdown, item))
            self.selib.click_element(self.locator.dynamic_dropdown.format(self.locator.dropdown, item))
        item = self.selib.get_text(self.locator.dropdown_first_path.format(label))
        return item

    def select_from_single_selection_dropdown_using_path(self, xpath, item):
        COMMON_KEY.wait_keyword_success("click_element", xpath)
        if item == "random":
            self.randomize_dropdown_selection_in_dropdown()
        else:
            self.selib.input_text(self.locator.input_path.format(xpath), item)
            self.selib.wait_until_element_is_visible(self.locator.dynamic_dropdown.format(self.locator.dropdown, item))
            self.selib.click_element(self.locator.dynamic_dropdown.format(self.locator.dropdown, item))
        item = self.selib.get_text(xpath)
        return item

    def selects_from_search_dropdown_selection(self, label, item):
        COMMON_KEY.wait_keyword_success(
            "click_element", "//core-dropdown[@ng-reflect-name='{0}']//following-sibling::*//nz-select".format(label))
        if item == "random":
            self.randomize_dropdown_selection_in_dropdown()
        else:
            self.selib.input_text\
                ("//core-dropdown[@ng-reflect-name='{0}']//following-sibling::*//input".format(label), item)
            self.selib.click_element(self.locator.dynamic_dropdown.format(self.locator.dropdown, item))
        item = self.selib.get_text\
                ("//core-dropdown[@ng-reflect-name='{0}']//following-sibling::*//nz-select".format(label))
        return item

    def selects_from_trx_customer_selection(self, item):
        try:
            COMMON_KEY.wait_keyword_success("click_element", self.locator.CustDrp)
            cust_path = self.locator.CustDrp
            cust_sel = self.locator.dropdown
        except Exception as e:
            print(e.__class__, "occured")
            COMMON_KEY.wait_keyword_success("click_element", self.locator.CustField)
            cust_path = self.locator.CustField
            cust_sel = self.locator.CustSel
        if item == "random":
            self.selib.wait_until_element_is_visible("{0}[@role='row']".format(self.locator.CustSel))
            total = self.selib.get_element_count("{0}[@role='row']".format(self.locator.CustSel))
            if total < 6:
                count = secrets.choice(range(1, total))
            else:
                count = secrets.choice(range(1, 5))
            attribute = self.selib.get_text(
                "({0}[@role='row'])[{1}]//*[@col-id='CUST_NAME']//div[@class]".format(self.locator.CustSel, count))
            self.builtin.set_test_variable(self.SELECTED_ITEM, attribute)
            self.selib.click_element("({0}[@role='row'])[{1}]//*[@col-id='CUST_NAME']//div[@class]".format(self.locator.CustSel, count))
        else:
            if cust_path == self.locator.CustDrp:
                self.selib.input_text(self.locator.input_path.format(cust_path), item)
            else:
                self.selib.input_text(cust_path, item)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.dynamic_dropdown.format(cust_sel, item))
        item = self.selib.get_value(cust_path)
        return item

    def randomize_dropdown_selection_in_dropdown(self):
        try:
            print()
            self.selib.wait_until_element_is_visible("{0}[1]".format(self.locator.dropdown))
            total = self.selib.get_element_count(self.locator.dropdown)
            self.builtin.set_test_variable("${dropdown_items}", total)
            print("in=",total)
        except Exception as e:
            print(e.__class__, "occured")
            self.selib.wait_until_element_is_visible("{0}[1]".format(self.locator.dn_cust_dropdown))
            total = self.selib.get_element_count(self.locator.dn_cust_dropdown)
            print("e=",total)
        if total == 1:
            count = 1
        elif total > 1:
            count = secrets.choice(range(1, total))
        else:
            return "Select"
        try:
            attribute = self.selib.get_text(
                "(//*[@class='cdk-overlay-pane']//following-sibling::li)[{0}]".format(count))
            self.builtin.set_test_variable(self.SELECTED_ITEM, attribute)
            print("selectedItem::", attribute)
            COMMON_KEY.wait_keyword_success("click_element",
                                        "(//*[@class='cdk-overlay-pane']//following-sibling::li)[{0}]".format(count))
            self.selib.wait_until_page_does_not_contain_element("//*[@class='cdk-overlay-pane']//ul[contains(@class,'dropdown')]")
            self._wait_for_page_refresh()
            print("clickedItem::", attribute)
        except Exception as e:
            print(e.__class__, "occured")
            #used for Debit Note Customer
            attribute = self.selib.get_text(
                "(//*[@class='cdk-overlay-pane']//following-sibling::tr)[{0}]".format(count))
            self.builtin.set_test_variable(self.SELECTED_ITEM, attribute)
            print("selectedItem::", attribute)
            COMMON_KEY.wait_keyword_success("click_element",
                                "(//*[@class='cdk-overlay-pane']//following-sibling::tr)[{0}]//a".format(count))
            return attribute

    def return_item_in_singledropdown(self, label):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.dropdown_path.format(label))
        summary = self.selib.get_webelements(self.locator.itemlist)
        return summary

    def select_first_selection(self):
        COMMON_KEY.wait_keyword_success("click_element", "({0})[1]".format(self.locator.dropdown))

    def return_disable_state_of_dropdown(self, label):
        get_status = self.selib.get_element_attribute \
            (self.locator.dropdown_first_path.format(label), "ng-reflect-nz-disabled")
        return get_status

    def validate_validation_msg_for_dropdown(self, label):
        """ Functions to validate validation message returned """
        validation_msg = self.selib.get_text(
            "(//*[contains(text(), '{0}')]/following:: *//validation)[1]".format(label))
        self.builtin.should_be_equal_as_strings(validation_msg, "Please select a value")

    @keyword("user selects customer route for ${description}")
    def user_selects_customer_route_for(self, description, item):
        """ Function to select customer for debit note """
        COMMON_KEY.wait_keyword_success("click_element", self.locator.CustField)
        total = self.selib.get_element_count(self.locator.CustSel)
        print("total customers:", total)
        if total <= 1:
            COMMON_KEY.wait_keyword_success("click_element", self.locator.CustDrp)
            self.select_from_single_selection_dropdown("Route", "random")
            COMMON_KEY.wait_keyword_success("click_element", self.locator.CustDrp)
        if item == "random":
            cust = self.randomize_dropdown_selection_in_dropdown()
            self.select_from_single_selection_dropdown("Route", "random")
        else:
            try:
                COMMON_KEY.wait_keyword_success("click_element", "(//*[@class='cdk-overlay-pane']//core-cell-render[@ng-reflect-cell-value='{0}']//div)[1]"
                        .format(item))
            except Exception as e:
                print(e.__class__, "occured")
                COMMON_KEY.wait_keyword_success("click_element",
                                                "//*[@class='cdk-overlay-pane']//core-cell-render[@ng-reflect-cell-value='{0}']//preceding::a[1]"
                                                .format(item))
            cust = item
        return cust

    def select_principal_from_filter(self, details):
        """ Function to select principal value from filter pop up """
        multi_status = self.builtin.get_variable_value("${multi_status}")
        if multi_status is True:
            if details.get('principal') is not None:
                principal = self.selects_from_single_selection_dropdown("Principal", details['principal'])
            else:
                principal = self.selects_from_single_selection_dropdown("Principal", "random")
            self.builtin.set_test_variable("${principal}", principal)

    def clear_selection_from_single_selection_dropdown(self, label):
        self.selib.click_element("{0}//*[@data-icon='close-circle']".format(self.locator.dropdown_first_path.format(label)))
