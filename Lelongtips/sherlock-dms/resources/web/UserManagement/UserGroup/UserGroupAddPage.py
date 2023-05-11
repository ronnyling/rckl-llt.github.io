from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import TEXTFIELD,DRPSINGLE, BUTTON


class UserGroupAddPage(PageObject):
    PAGE_TITLE = "User Management / User Group"
    PAGE_URL = "/setting-ui/user-group?template=p"
    GROUP_DETAILS="${group_details}"

    _locators = {

    }

    @keyword('user creates user group using ${data_type} data')
    def user_creates_user_group_with_data(self, data_type):
        BUTTON.click_button("Add")
        if data_type=="random":
            TEXTFIELD.insert_into_field_with_length("User Group Code", "letter", 10)
            TEXTFIELD.insert_into_field_with_length("User Group Name", "letter", 15)
            TEXTFIELD.insert_into_area_field_with_length("User Group Description", "letter", 20)
            DRPSINGLE.selects_from_single_selection_dropdown("User Role", "random")
        else:
            self.create_fixed_data_user_group()
        BUTTON.click_button("Save")
        BUTTON.click_button("Cancel")

    def create_fixed_data_user_group(self):
        setup_group = self.builtin.get_variable_value(self.GROUP_DETAILS)
        TEXTFIELD.insert_into_field("User Group Code", setup_group['code'])
        TEXTFIELD.insert_into_field("User Group Name", setup_group['name'])
        TEXTFIELD.insert_into_area_field("User Group Description", setup_group['desc'])
        DRPSINGLE.selects_from_single_selection_dropdown("User Role", setup_group['role'])

    def validate_add_button_is_not_visible(self):
        BUTTON.validate_button_is_hidden("Add")


