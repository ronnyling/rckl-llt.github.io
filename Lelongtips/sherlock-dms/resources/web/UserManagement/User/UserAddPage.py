from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TEXTFIELD,DRPSINGLE,BUTTON,POPUPMSG
from faker import Faker

FAKE = Faker()
class UserAddPage(PageObject):
    PAGE_TITLE = "User Management / User"
    PAGE_URL = "/setting-ui/user?template=p"
    USER_DETAILS="${user_details}"
    email = f'{FAKE.word()}{FAKE.email()}'

    _locators = {
        "geo_apply" : "(//core-button//child::*[contains(text(),'Apply')]//ancestor::core-button[1])[1]",
        "emp_apply": "(//core-button//child::*[contains(text(),'Apply')]//ancestor::core-button[1])[2]",
    }

    @keyword('user creates user using ${data_type} data')
    def user_creates_user_with_data(self, data_type):
        BUTTON.click_button("Add")
        if data_type=="random":
            TEXTFIELD.insert_into_field_with_length("Login ID", "letter", 8)
            TEXTFIELD.insert_into_field_with_length("Name", "letter", 15)
            TEXTFIELD.insert_into_field("Email", self.email)
            DRPSINGLE.selects_from_single_selection_dropdown("User Role", "random")
            self.select_geo_assignment_and_employee_org()
        else:
            self.create_fixed_data_user()
        BUTTON.click_button("Save")

    def create_fixed_data_user(self):
        setup_user = self.builtin.get_variable_value(self.USER_DETAILS)
        TEXTFIELD.insert_into_field("Login ID", setup_user['login'])
        TEXTFIELD.insert_into_field("Name", setup_user['name'])
        TEXTFIELD.insert_into_field("Email", setup_user['email'])
        DRPSINGLE.selects_from_single_selection_dropdown("User Role", "random")
        self.select_geo_assignment_and_employee_org()

    def select_geo_assignment_and_employee_org(self):
        DRPSINGLE.selects_from_single_selection_dropdown("Geo Level", "random")
        DRPSINGLE.selects_from_single_selection_dropdown("Geo Value", "random")
        self.selib.click_element(self.locator.geo_apply)

        DRPSINGLE.selects_from_single_selection_dropdown("Employee Org", "random")
        DRPSINGLE.selects_from_single_selection_dropdown("Level", "random")
        self.selib.click_element(self.locator.emp_apply)

    @keyword("expect pop up message: ${msg}")
    def expect_error(self, msg):
        POPUPMSG.validate_pop_up_msg(msg)
        POPUPMSG.click_button_on_pop_up_msg()


