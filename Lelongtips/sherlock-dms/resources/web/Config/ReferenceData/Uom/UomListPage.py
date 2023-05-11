from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import BUTTON, PAGINATION, TEXTFIELD, DRPSINGLE


class UomListPage(PageObject):
    PAGE_TITLE = "Configuration / Reference Data / UOM"
    PAGE_URL = "setting-ui/uom-setting"
    UOM_CD = "${uom_cd}"
    _locators = {
        "load_image": "//div[@class='loading-text']//img",
    }

    @keyword('user selects uom to ${action}')
    def user_selects_uom_to(self, action):
        uom_code = self.builtin.get_variable_value(self.UOM_CD)
        uom_desc = self.builtin.get_variable_value("${uom_desc}")
        col_list = ["UOM_CD", "UOM_DESCRIPTION"]
        data_list = [uom_code, uom_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "UOM", action, col_list, data_list)

    def click_add_uom_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    def verify_add_uom_button_not_visible(self):
        BUTTON.validate_button_is_hidden("Add")

    @keyword('user filters uom using ${action} data')
    def user_filters_uom(self, action):
        """ Function to filter uom using filter fields """
        uom_cd = self.builtin.get_variable_value(self.UOM_CD)
        uom_desc = self.builtin.get_variable_value("${uom_desc}")
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("UOM Code", uom_cd)
        TEXTFIELD.insert_into_filter_field("UOM Description", uom_desc)
        if action == 'Non-Prime' or action == 'Prime':
            principal = self.builtin.get_variable_value("${principal}")
            DRPSINGLE.selects_from_single_selection_dropdown("Principal", principal)
        BUTTON.click_button("Apply")

    def principal_listed_successfully_in_uom(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        principal = self.builtin.get_variable_value("${principal}")
        if principal:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='PRIME_FLAG']".format(i))
                self.builtin.should_be_equal(get_principal, principal)

    @keyword('record ${action} in uom list')
    def record_in_uom_list(self, action):
        if action == 'not displaying':
            num_row = PAGINATION.return_number_of_rows_in_a_page()
            self.builtin.should_be_equal(num_row, 0)
        else:
            get_code = self.selib.get_text("//*[@row-index='0']//*[@col-id='UOM_CD']")
            self.builtin.should_be_equal(get_code, self.builtin.get_variable_value(self.UOM_CD))
