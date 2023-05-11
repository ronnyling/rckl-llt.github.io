from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, TEXTFIELD, COMMON_KEY
import secrets


class DistributorProductSectorAddPage(PageObject):

    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"
    SHIPTO_DETAILS = "${shipto_details}"

    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "first_ps": "//*[contains(text(),'Choose Product Sector(s)')]//following::*[@role='row' and @row-index='0']//*[contains(@class,'ant-table-selection-column')]//*[contains(@class,'ant-checkbox-wrapper')]",
        "popup_ok_btn": "//button//child::*[contains(text(),'Ok')]//ancestor::button[1]",
        "first_ps_desc": "//*[contains(text(),'Choose Product Sector(s)')]//following:*[@row-index='0']//*[@col-id='PROD_SECTOR_DESC']",
        "popup_ok_btn_test": "//*[contains(text(),'Choose Product Sector(s)')]//following::*[contains(text(),'Ok')]"
    }

    @keyword('user assigns product sector using ${data_type} data')
    def user_assigns_product_sector(self, data_type):

        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Add")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.first_ps)
        ps_desc = self.selib.get_text(self.locator.first_ps_desc)
        BuiltIn().set_test_variable("${ps_desc}", ps_desc)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.popup_ok_btn)
