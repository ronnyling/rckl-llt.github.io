from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web.Common import POMLibrary
from resources.web import BUTTON, TEXTFIELD, RADIOBTN


class PlaybookTypeAddPage (PageObject):
    """ Functions related to add page of playbook type """
    PAGE_TITLE = "Configuration / Reference Data / Playbook Type"
    PAGE_URL = "/objects/playbook-type"
    PLAYBOOK_CD = "Playbook Type Code"
    PLAYBOOK_DESC = "Playbook Type Description"


    @keyword('user creates playbook type with ${data_type} data')
    def user_creates_playbook_type_with_data(self, data_type):
        """ Function to create playbook type with random/fixed data """
        playbook_details = self.builtin.get_variable_value("${playbook_details}")
        self.user_creates_playbook_type()
        playbook_type_cd = self.user_inserts_playbook_type_cd(data_type)
        playbook_type_desc = self.user_inserts_playbook_type_desc(data_type, playbook_details)
        prd_hier_req = self.user_selects_prd_hier_req(data_type, playbook_details)
        if data_type != 'existing':
            self.builtin.set_test_variable("${playbook_type_cd}", playbook_type_cd)
            self.builtin.set_test_variable("${playbook_type_desc}", playbook_type_desc)
            self.builtin.set_test_variable("${prd_hier_req}", prd_hier_req)
        BUTTON.click_button("Save")

    def user_inserts_playbook_type_cd(self, data_type):
        if data_type == 'existing':
            playbook_type_cd = self.builtin.get_variable_value("${playbook_type_cd}")
            playbook_type_cd = TEXTFIELD.insert_into_field(self.PLAYBOOK_CD, playbook_type_cd)
        else:
            playbook_type_cd = TEXTFIELD.insert_into_field_with_length(self.PLAYBOOK_CD, "random", 15)
        return playbook_type_cd

    def user_inserts_playbook_type_desc(self, data_type, playbook_details):
        if data_type == "fixed":
            playbook_type_desc = TEXTFIELD.insert_into_field\
                                (self.PLAYBOOK_DESC, playbook_details['PLAYBOOK_TYPE_DESC'])
        else:
            playbook_type_desc = TEXTFIELD.insert_into_field_with_length(self.PLAYBOOK_DESC, "random", 25)
        return playbook_type_desc

    def user_selects_prd_hier_req(self, data_type, playbook_details):
        if data_type == "fixed":
            prd_hier_req = RADIOBTN.select_from_radio_button\
                        ("Product Hierarchy Required", playbook_details['PLAYBOOK_PRD_HIER_REQ'])
        else:
            prd_hier_req = RADIOBTN.select_from_radio_button("Product Hierarchy Required", "random")
        return prd_hier_req

    def user_creates_playbook_type(self):
        POMLibrary.POMLibrary().check_page_title("PlaybookTypeAddPage")
        BUTTON.click_button("Add")

    def user_cancel_creating_playbook_type(self):
        try:
            self.user_creates_playbook_type()
        except Exception as e:
            print(e.__class__, "occured")
        BUTTON.click_button("Cancel")

    def unable_to_create_successfully_with_validation_message_on_fields(self):
        TEXTFIELD.validate_validation_msg(self.PLAYBOOK_CD, "Please enter a value")
        TEXTFIELD.validate_validation_msg(self.PLAYBOOK_DESC, "Please enter a value")
