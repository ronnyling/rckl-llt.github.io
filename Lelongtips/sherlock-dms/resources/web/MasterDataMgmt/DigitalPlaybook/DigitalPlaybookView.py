from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, LABEL, TEXTFIELD, DRPSINGLE, COMMON_KEY, BUTTON


class DigitalPlaybookView(PageObject):

    _locators = {
        "file_upload": "//*[contains(text(),'{0}')]//following::nz-upload",
        "radio_btn_grp": "//*[text()='{0}']/following::nz-radio-group",
        "content_desc": "//*[contains(text(),'Title')]//following::a[1]",
        "popup_textfield": "//*[contains(text(),'{0}')]/following::*[contains(text(),'{1}')]/following::input[1]",
        "popup_radiogroup": "//*[contains(text(),'{0}')]//following::*[text()='{1}']/following::nz-radio-group",
        "popup_file_upload": "//*[contains(text(),'{0}')]//following::nz-upload[1]"
    }

    @keyword("user selects digital playbook:${playbook_cd} to view")
    def view_digital_playbook(self, playbook_cd):
        """ Function to select playbook in listing to edit """
        col_list = ["PLAYBK_CD"]
        data_list = [playbook_cd]
        action = "edit"
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
            ("present", "Playbook", action, col_list, data_list)

    def validates_view_mode(self):
        LABEL.validate_label_is_visible("VIEW")
        TEXTFIELD.verifies_text_field_is_disabled("Playbook Code")
        TEXTFIELD.verifies_text_field_is_disabled("Playbook Description")
        TEXTFIELD.verifies_text_field_is_disabled("Playbook Code")
        dropdown_list = {
            "Priority", "Playbook Type", "Assign To", "Brand", "Start Date", "End Date"
        }
        for x in dropdown_list:
            drp_status = DRPSINGLE.return_disable_state_of_dropdown(x)
            if drp_status is False:
                raise ValueError("{0} field is not disabled".format(x))
        self.verifies_upload_field_is_disabled("Thumbnail")
        self.verifies_radio_group_is_disabled("Status")
        COMMON_KEY.wait_keyword_success("wait_until_element_is_visible", self.locator.content_desc)
        ct_desc = self.selib.get_text(self.locator.content_desc)
        col_list = ["CONTENT_DESC"]
        data_list = [ct_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Content", "edit", col_list, data_list)
        self.verifies_popup_textfield_is_disabled(ct_desc, "Title")
        self.verifies_popup_radio_group_is_disabled(ct_desc, "File")
        self.verifies_popup_file_upload_is_disabled(ct_desc)
        BUTTON.click_pop_up_screen_button("Cancel")

    def verifies_upload_field_is_disabled(self, label):
        """ Functions to verify file upload field is disabled """
        status = self.selib.get_element_attribute(self.locator.file_upload.format(label), "ng-reflect-nz-disabled")
        self.builtin.should_be_true(bool(status))

    def verifies_radio_group_is_disabled(self, label):
        """ Functions to verify radio button group is disabled """
        status = self.selib.get_element_attribute(self.locator.radio_btn_grp.format(label), "ng-reflect-nz-disabled")
        self.builtin.should_be_true(bool(status))

    def verifies_popup_textfield_is_disabled(self, ct_desc, label):
        """ Functions to verify popup textfield is disabled """
        status = self.selib.get_element_attribute(self.locator.popup_textfield.format(ct_desc, label), "ng-reflect-disabled")
        self.builtin.should_be_true(bool(status))

    def verifies_popup_radio_group_is_disabled(self, ct_desc, label):
        """ Functions to verify popup textfield is disabled """
        status = self.selib.get_element_attribute(self.locator.popup_radiogroup.format(ct_desc, label), "ng-reflect-nz-disabled")
        self.builtin.should_be_true(bool(status))

    def verifies_popup_file_upload_is_disabled(self, ct_desc):
        """ Functions to verify popup file upload is disabled """
        status = self.selib.get_element_attribute(self.locator.popup_file_upload.format(ct_desc), "ng-reflect-nz-disabled")
        self.builtin.should_be_true(bool(status))
