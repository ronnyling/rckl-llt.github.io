from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, LABEL
from resources.web.Config.ReferenceData.PlaybookType import PlaybookTypeAddPage


class PlaybookTypeEditPage (PageObject):

    @keyword('user updates playbook type with ${data_type} data')
    def user_updates_playbook_type_data(self, data_type):
        LABEL.validate_label_is_visible("EDIT | Playbook Type")
        details = self.builtin.get_variable_value("${playbook_details}")
        playbook_type_desc = PlaybookTypeAddPage.PlaybookTypeAddPage().user_inserts_playbook_type_desc(data_type, details)
        prd_hier_req = PlaybookTypeAddPage.PlaybookTypeAddPage().user_selects_prd_hier_req(data_type, details)
        self.builtin.set_test_variable("${playbook_type_desc}", playbook_type_desc)
        self.builtin.set_test_variable("${prd_hier_req}", prd_hier_req)
        BUTTON.click_button("Save")
