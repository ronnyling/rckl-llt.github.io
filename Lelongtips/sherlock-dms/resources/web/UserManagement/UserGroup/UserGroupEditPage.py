from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.web import  BUTTON, TEXTFIELD, LABEL

class UserGroupEditPage(PageObject):
    PAGE_TITLE = "User Management / User Group"
    PAGE_URL = "/setting-ui/user-group?template=p"
    GROUP_DETAILS = "${group_details}"

    _locators = {

    }
    @keyword('user is able to navigate to EDIT | User Group')
    def user_able_to_navigate_to_edit_page(self):
        LABEL.validate_label_is_visible("EDIT | User Group")

    @keyword('user updates user group using ${data_type} data')
    def user_updates_user_group_with_data(self, data_type):
        TEXTFIELD.insert_into_field_with_length("User Group Name", "letter", 15)
        TEXTFIELD.insert_into_area_field_with_length("User Group Description", "letter", 20)
        BUTTON.click_button("Save")

