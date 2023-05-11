from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, LABEL


class CustomerGroupDiscountListPage(PageObject):

    _locators = {

    }

    @keyword('user selects customer group discount to ${action}')
    def user_selects_customer_group_discount_to(self, action):
        disc_cd = BuiltIn().get_variable_value("${disc_code}")
        col_list = ["GRPDISC_CD"]
        data_list = [disc_cd]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "grp disc", action, col_list, data_list)

    @keyword('validate user is redirected back to listing')
    def user_redirected_to_listing(self):
        LABEL.validate_label_is_visible("Customer Group Discount")
        PAGINATION.validates_table_column_visibility("Group Discount Code")
        PAGINATION.validates_table_column_visibility("Group Discount Description")