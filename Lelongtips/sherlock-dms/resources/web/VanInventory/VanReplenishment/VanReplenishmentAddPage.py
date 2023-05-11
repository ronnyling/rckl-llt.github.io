from PageObjectLibrary import PageObject
from resources.web.VanInventory.VanReplenishment import VanReplenishmentListPage
from resources.web import COMMON_KEY, BUTTON, TEXTFIELD, RADIOBTN, DRPSINGLE
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword


class VanReplenishmentAddPage(PageObject):
    """ Functions for Van Replenishment Add Page actions """
    PAGE_TITLE = "Van Inventory / Van Replenishment"
    PAGE_URL = "inventory/van-stock-replenish/NEW"
    REP_DETAILS = "${RepDetails}"

    _locators = {
        "PrdRow": "//*[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']/following::tr//td[2]",
        "product": "//input[@placeholder='Enter Code / Description']",
        "productList": "//input[@placeholder='Enter Code / Description']//following::tr[@role='row']",
        "LoadingImg": "//div[@class='loading-text']//img"
    }

    @keyword("user provides van replenishment header details")
    def user_provides_van_replenishment_header_details(self):
        BUTTON.validate_button_is_shown("Add")
        details = BuiltIn().get_variable_value(self.REP_DETAILS)
        VanReplenishmentListPage.VanReplenishmentListPage().click_add_van_replenishment_button()
        RADIOBTN.select_from_radio_button("Principal", details['principal'])
        DRPSINGLE.select_from_single_selection_dropdown("Source Warehouse", details['warehouse'])
        DRPSINGLE.select_from_single_selection_dropdown("Route", details['route'])

    def product_not_populated_in_dropdown(self):
        details = self.builtin.get_variable_value(self.REP_DETAILS)
        self.selib.wait_until_page_does_not_contain_element(self.locator.LoadingImg)
        element = self.driver.find_element_by_xpath(self.locator.product)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.product)
        COMMON_KEY.wait_keyword_success("input_text", self.locator.product, details['product'])
        self.selib.page_should_not_contain_element("//*[text()='%s']" % details['product'])
        COMMON_KEY.wait_keyword_success("press_keys", None, "TAB")

    @keyword("user creates van replenishment with ${data_type} data")
    def user_creates_van_replenishment_with(self, data_type):
        """ Function to create return with random/fixed data """
        details = self.builtin.get_variable_value(self.REP_DETAILS)
        if data_type == "fixed":
            self.user_provides_van_replenishment_header_details()
            element = self.driver.find_element_by_xpath(self.locator.product)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            if details is not None:
                if isinstance(details['product'], list):
                    for i in details['product']:
                        TEXTFIELD.inserts_into_trx_field(i['product'], i['productUom'])
                else:
                    TEXTFIELD.inserts_into_trx_field(details['product'], details['productUom'])
            else:
                TEXTFIELD.inserts_into_trx_field("random", "random")
            BUTTON.click_button("Save")

    @keyword("orange colour ${selection} successfully in product selection")
    def orange_colour_successfully_in_product_selection(self, selection):
        self._wait_for_page_refresh()
        BUTTON.validate_button_is_shown("Cancel")
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        if selection == "shown":
            self.selib.page_should_contain_element('//tr[contains(@class, "orange")]')
            self.selib.page_should_contain_element('//return-prod-table//a[@ng-reflect-nz-trigger="hover"]')
        else:
            self.selib.page_should_not_contain_element('//tr[contains(@class, "orange")]')
