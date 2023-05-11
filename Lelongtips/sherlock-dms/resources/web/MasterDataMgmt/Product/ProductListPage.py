from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, PAGINATION, TEXTFIELD
from robot.libraries.BuiltIn import BuiltIn


class ProductListPage(PageObject):
    """ PRE-REQUISITE SAMPLE ONLY - Functions for product listing page """
    PAGE_TITLE = "Master Data Management / Product"
    PAGE_URL = "/products/product?template=p"
    PRD_CODE = "${PRD_CODE}"
    PRD_DESC = "${PRD_DESC}"

    _locators = {
        "ProductPriority" : "/div[contains(text(),'Product Priority')]"
    }

    @keyword("user lands on product add mode")
    def click_add_product_button(self):
        """ Function to click add for new product """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects product to ${action}')
    def user_selects_product_to(self, action):
        """ Function to selects product to edit/delete """
        prd_cd = BuiltIn().get_variable_value(self.PRD_CODE)
        prd_desc = BuiltIn().get_variable_value(self.PRD_DESC)
        col_list = ["PRD_CD", "PRD_DESC"]
        data_list = [prd_cd, prd_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "product", action, col_list, data_list)
        if action == "delete":
            BUTTON.click_button("Yes")

    @keyword('user filters product using ${action} data')
    def user_filters_product(self, action):
        """ Function to filter product using filter fields """
        prd_cd = BuiltIn().get_variable_value(self.PRD_CODE)
        prd_desc = BuiltIn().get_variable_value(self.PRD_DESC)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Product Code", prd_cd)
        TEXTFIELD.insert_into_filter_field("Product Description", prd_desc)
        BUTTON.click_button("Apply")

    @keyword('user searches product using ${action} data')
    def user_searches_product(self, action):
        """ Function to search product with inline search """
        prd_cd = BuiltIn().get_variable_value(self.PRD_CODE)
        prd_desc = BuiltIn().get_variable_value(self.PRD_DESC)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("Product Code", prd_cd)
        TEXTFIELD.insert_into_search_field("Product Description", prd_desc)
        BUTTON.click_icon("search")

    def product_record_display_in_listing_successfully(self):
        """ Function to validate product showing in listing """
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "Filtering not working correctly"


    def validated_product_priority_is_removed_from_listing_page(self):
        self.selib.wait_until_element_is_not_visible(self.locator.ProductPriority)