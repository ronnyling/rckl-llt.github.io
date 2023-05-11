from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import POPUPMSG, BUTTON, TEXTFIELD

import secrets
class StoreSpaceAddPage(PageObject):
    PAGE_TITLE = "Merchandising / Merchandising  space / Store Space"
    PAGE_URL = "/merchandising/merc-store-space?template=p"
    STORE_SPACE_DETAILS = "${store_space_details}"
    LABEL_PATH = "//*[contains(text(),'{0}')]"
    CHECKBOX_PATH = "//table/tbody/tr[1]/td[1]/label/span[1]/input"
    _locators = {
        "add_icon": "//core-button[@ng-reflect-icon='plus-circle']",
        "overlay": "//ngx-spinner/div",
        "desc_label": "//*[contains(text(),'{0}')]"
    }


    @keyword('user creates store space using ${data_type} data')
    def user_creates_store_space_with_data(self, data_type):
        details = self.builtin.get_variable_value(self.STORE_SPACE_DETAILS)
        self.selib.click_element(self.locator.add_icon)
        if data_type == "fixed" :
            space_code = details['space_code']
            space_desc = details['space_desc']
        else:
            if data_type == "random":
                space_code = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
                space_desc = ''.join(secrets.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(15))
        POPUPMSG.insert_into_store_space_field_in_pop_up(space_code, space_desc)
        self.builtin.set_test_variable("${space_code}",  space_code)
        self.builtin.set_test_variable("${space_category}",  space_desc)
        BUTTON.click_button("Add To List")

    @keyword('data will be limited to set length')
    def validate_data_limited_to_set_length(self):
        setup = self.builtin.get_variable_value(self.STORE_SPACE_DETAILS)
        cd_limit = TEXTFIELD.retrieves_text_field_length("Space Code")
        desc_limit = TEXTFIELD.retrieves_text_field_length("Space Description")
        assert int(cd_limit) < len(setup['space_code']), "Store Space Code is not limited to set length"
        assert int(desc_limit) < len(setup['space_desc']), "Store Space Description is not limited to set length"

    @keyword('user assign customer assignment which is present')
    def assign_customer_assignment(self):
        details = self.builtin.get_variable_value(self.STORE_SPACE_DETAILS)
        Common().wait_keyword_success("click_element", self.LABEL_PATH.format(details['space_desc']))
        BUTTON.click_button("Add")
        self.selib.click_element(self.CHECKBOX_PATH)
        BUTTON.click_button("Assign")

    @keyword('user tries to create store space using maximum data')
    def create_setup_with_maximum_length_data(self):
        BUTTON.click_button("Add")
        details = self.builtin.get_variable_value(self.STORE_SPACE_DETAILS)
        POPUPMSG.insert_into_store_space_field_in_pop_up(details['space_code'], details['space_desc'])

    @keyword('data will be limited to set length')
    def validate_data_limited_to_set_length(self):
        details = self.builtin.get_variable_value(self.STORE_SPACE_DETAILS)
        cd_limit = POPUPMSG.retrieves_text_field_length("Space Code")
        desc_limit = POPUPMSG.retrieves_text_field_length("Space Desc")
        assert int(cd_limit) < len(details['space_code']), "Space Code is not limited to set length"
        assert int(desc_limit) < len(details['space_desc']), "Space Description is not limited to set length"

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()
        BUTTON.click_button("Cancel")


