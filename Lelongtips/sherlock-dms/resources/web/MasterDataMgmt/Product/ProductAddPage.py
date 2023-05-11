from PageObjectLibrary import PageObject
from resources.web.MasterDataMgmt.Product.ProductListPage import ProductListPage
from resources.web.CustTrx.SalesReturn.SalesReturnListPage import SalesReturnListPage
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from resources.web import BUTTON, TEXTFIELD, DRPSINGLE, RADIOBTN, PAGINATION, COMMON_KEY, CHECKBOX, LABEL
import secrets


class ProductAddPage(PageObject):
    """ function to add product """
    PAGE_TITLE = "Master Data Management / Product"
    PAGE_URL = "/products/product?template=p"
    LICENSE_CHECK = "License Checking"
    ALLOW_PROMO = "Allowable in Promotion"
    TAX_EXEMPT = "Tax Exemption"
    MOST_RECENT_ACTIVE = "Most Recent Active"
    P_TYPE = "Type"
    P_DESC = "Product Description"
    P_STATUS = "Status"
    SIZE = "Size"
    RETURN_TYPE = "(Market) Return Type"
    _locators = {
        "prd_hier_button": "//*[contains(text(), 'Size')]/following::core-button[1]",
        "checkbox": "(//*[@nz-checkbox=''])[{0}]",
        "search_button": "//core-button[@ng-reflect-icon='search']",
        "text_field": "(//*[contains(text(),'Size Desc')]/following::input)[{0}]",
        "dropdown_field": "(//*[contains(text(),'Size Desc')]/following::input)[3]/following::nz-select[{0}]//input",
        "dropdown_selection": "//li[contains(text(), '{0}')]"
    }

    @keyword('user creates product with ${data} data')
    def user_creates_product_with(self, data):
        ProductListPage().click_add_product_button()
        code = self.user_inserts_product_code()
        desc = self.user_inserts_product_desc()
        BuiltIn().set_test_variable("${PRD_CODE}", code )
        BuiltIn().set_test_variable("${PRD_DESC}", desc)
        self.user_selects_return_type()
        self.user_selects_size()
        self.user_click_save_button()

    @keyword('user edits product with ${data} data')
    def user_edits_product_with(self, data):
        desc = self.user_inserts_product_desc()
        BuiltIn().set_test_variable("${PRD_DESC}", desc)
        self.user_selects_return_type()
        self.user_selects_size()
        self.user_click_save_button()

    def user_click_save_button(self):
        BUTTON.click_button("Save")

    def user_back_to_listing_page(self):
        BUTTON.click_button("Cancel")

    def user_inserts_product_code(self):
        """ Function to insert product code with random/fixed data """
        product_cd = BuiltIn().get_variable_value("&{ProductDetails['PRD_CD']}")
        if product_cd is not None:
            product_cd = TEXTFIELD.insert_into_field("Product Code", product_cd)
        else:
            product_cd = TEXTFIELD.insert_into_field_with_length("Product Code", "letter", 8)
        return product_cd

    def user_inserts_product_desc(self):
        """ Function to insert product desc with random/fixed data """
        product_desc = BuiltIn().get_variable_value("&{ProductDetails['PRD_DESC']}")
        if product_desc is not None:
            product_desc = TEXTFIELD.insert_into_field(self.P_DESC, product_desc)
        else:
            product_desc = TEXTFIELD.insert_into_field_with_length(self.P_DESC, "letter", 8)
        return product_desc

    def user_selects_return_type(self):
        r_type = BuiltIn().get_variable_value("&{ProductDetails['RETURN_TYPE']}")
        if r_type is not None:
            option = DRPSINGLE.selects_from_single_selection_dropdown(self.RETURN_TYPE, r_type)
        else:
            option = DRPSINGLE.selects_from_single_selection_dropdown(self.RETURN_TYPE, "random")
        return option

    def user_selects_size(self):
        size = BuiltIn().get_variable_value("&{ProductDetails['size']}")
        if size is not None:
            option = DRPSINGLE.selects_from_single_selection_dropdown(self.SIZE, size)
        else:
            option = DRPSINGLE.selects_from_single_selection_dropdown(self.SIZE, "random")
        return option

    def user_selects_product_status(self):
        status = BuiltIn().get_variable_value("&{ProductDetails['Status']}")
        if status is not None:
            option = RADIOBTN.select_from_radio_button(self.P_STATUS, status)
        else:
            option = RADIOBTN.select_from_radio_button(self.P_STATUS, "random")
        return option

    def user_selects_product_type(self):
        status = BuiltIn().get_variable_value("&{ProductDetails['Type']}")
        if status is not None:
            option = RADIOBTN.select_from_radio_button(self.P_TYPE, status)
        else:
            option = RADIOBTN.select_from_radio_button(self.P_TYPE, "random")
        return option

    def user_selects_most_recent_Active(self):
        most_recent_active = BuiltIn().get_variable_value("&{ProductDetails['MostRecentActive']}")
        if most_recent_active is not None:
            option = RADIOBTN.select_from_radio_button(self.MOST_RECENT_ACTIVE, most_recent_active)
        else:
            option = RADIOBTN.select_from_radio_button(self.MOST_RECENT_ACTIVE, "random")
        return option

    def user_selects_tax_exemption(self):
        tax_exemption = BuiltIn().get_variable_value("&{ProductDetails['TaxExemption']}")
        if tax_exemption is not None:
            option = RADIOBTN.select_from_radio_button(self.TAX_EXEMPT, tax_exemption)
        else:
            option = RADIOBTN.select_from_radio_button(self.TAX_EXEMPT, "random")
        return option

    def user_selects_allowable_in_promo(self):
        allow_in_promo = BuiltIn().get_variable_value("&{ProductDetails['Allow_In_Promo']}")
        if allow_in_promo is not None:
            option = RADIOBTN.select_from_radio_button(self.ALLOW_PROMO, allow_in_promo)
        else:
            option = RADIOBTN.select_from_radio_button(self.ALLOW_PROMO, "random")
        return option

    def user_selects_license_checking(self):
        lc_check = BuiltIn().get_variable_value("&{ProductDetails['Status']}")
        if lc_check is not None:
            option = RADIOBTN.select_from_radio_button(self.LICENSE_CHECK, lc_check)
        else:
            option = RADIOBTN.select_from_radio_button(self.LICENSE_CHECK, "random")
        return option

    @keyword("validated components is not exists in type drop down")
    def validate_value_not_in_drop_down(self):
        items = DRPSINGLE.return_item_in_singledropdown("Product Type")
        for item in items:
            text = self.selib.get_text(item)
            assert text != "Components", "Components is in type drop down"

    @keyword("validate product description 1 is renamed to product description")
    def validate_value_not_in_drop_down(self):
        self.selib.wait_until_element_is_not_visible("//*[text()='Product Description 1']")
        self.selib.wait_until_element_is_visible("//*[text()='Product Description']")

    @keyword("validated POSM Material tab will appear when product type = posm")
    def validate_posm_tab_will_appear_when_product_type_is_posm(self):
        self.selib.wait_until_element_is_visible("//*[text()='POSM Material']")

    @keyword('user validates product hierarchy popup')
    def validate_product_hierarchy_popup(self):
        ProductListPage().click_add_product_button()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.prd_hier_button)
        BUTTON.validate_button_is_shown("Assign")
        BUTTON.validate_button_is_shown("Cancel")
        self.selib.wait_until_element_is_visible(self.locator.search_button)
        PAGINATION.validates_table_column_visibility("Size Desc", "displaying")
        PAGINATION.validates_table_column_visibility("Size Code", "displaying")

    def close_product_hierarchy_popup(self):
        BUTTON.click_pop_up_screen_button("Cancel")

    @keyword("user ${action} ${option} product hierarchy in product master")
    def add_product_hierarchy(self, action, option):
        if action == "adds":
            if option == "single":
                COMMON_KEY.wait_keyword_success("click_element", self.locator.checkbox.format("2"))
                BUTTON.click_pop_up_screen_button("Assign")
            elif option == "multiple":
                CHECKBOX.select_checkbox("Outlet Group Desc", "vertical", "all", True)
                self.validate_assign_button_is_disabled()
            else:
                self.validate_assign_button_is_disabled()
        elif action == "updates":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.prd_hier_button)
            COMMON_KEY.wait_keyword_success("click_element", self.locator.checkbox.format("3"))
            BUTTON.click_pop_up_screen_button("Assign")

    def validate_assign_button_is_disabled(self):
        status = BUTTON.check_button_is_disabled("Assign")
        assert status is True or status == 'true', "Assign button should be disabled"

    @keyword('user validates product hierarchy inline search')
    def validate_product_hierarchy_inline_search(self):
        hier_rs_bd = BuiltIn().get_variable_value("${hier_rs_bd}")
        rand_so = secrets.randbelow(len(hier_rs_bd))
        while hier_rs_bd[rand_so]['LEVEL4_ID'] is None:
            rand_so = secrets.randbelow(len(hier_rs_bd))
        size_desc = hier_rs_bd[rand_so]['NODE_DESC4']
        size_code = hier_rs_bd[rand_so]['NODE_NAME4']
        variant_desc = hier_rs_bd[rand_so]['NODE_DESC3']
        variant_code = hier_rs_bd[rand_so]['NODE_NAME3']
        brand_desc = hier_rs_bd[rand_so]['NODE_DESC2']
        brand_code = hier_rs_bd[rand_so]['NODE_NAME2']
        category_desc = hier_rs_bd[rand_so]['NODE_DESC1']
        category_code = hier_rs_bd[rand_so]['NODE_NAME1']
        column_list = [
            size_desc, size_code, variant_desc, variant_code, brand_desc, brand_code, category_desc, category_code
        ]
        SalesReturnListPage().user_searches_by_status("Size Desc:{0},Size Code:{1},Variant Desc:{2},Variant Code:{3},Brand Desc:{4},"
                                     "Brand Code:{5},Category Desc:{6},Category Code:{7}"
                                     .format(size_desc, size_code, variant_desc, variant_code, brand_desc, brand_code,
                                             category_desc, category_code))
        for x in column_list:
            LABEL.validate_label_is_visible(x)
        BUTTON.click_pop_up_screen_button("Cancel")

