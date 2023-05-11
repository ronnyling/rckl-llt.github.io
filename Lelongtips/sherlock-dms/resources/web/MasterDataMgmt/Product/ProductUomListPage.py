from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, PAGINATION, TAB


class ProductUomListPage(PageObject):

    PAGE_TITLE = "Master Data Management / Product"
    PAGE_URL = "/products/product?template=p"
    UOM_DETAILS = "${uom_details}"

    @keyword('user validates buttons for product uom listing page')
    def user_validates_buttons(self):
        TAB.user_navigates_to_tab("Product UOM")
        BUTTON.validate_button_is_shown("Add")
        BUTTON.validate_icon_is_shown("delete")
        BUTTON.validate_icon_is_shown("search")
        BUTTON.validate_icon_is_shown("filter")

    @keyword('user selects product uom to ${action}')
    def user_selects_product_uom_to(self, action):
        uom_cd = BuiltIn().get_variable_value("${uom_cd}")
        col_list = ["UOM_ID"]
        data_list = [uom_cd]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Product UOM", action, col_list, data_list)
        if action == "delete":
            BUTTON.click_button("Yes")
