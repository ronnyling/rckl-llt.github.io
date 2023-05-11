from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import BUTTON, DRPSINGLE
from resources.web.Common import POMLibrary
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure import StructureGet
from resources.restAPI.Common import TokenAccess


class DigitalPlaybookEditPage(PageObject):
    """ Functions related to digital playbook page """

    PAGE_TITLE = "Configuration / Application Setup"
    PAGE_URL = "/setting-ui/application-setup?template=p"
    PROD_HIER_LEVEL = 'Product Hierarchy Level'
    MAX_PLYBOOK_SIZE = 'Max Playbook Content Size'
    RAND = "random"

    @keyword("user updates digital playbook using ${data_type} data")
    def user_updates_digital_playbook_using_data(self, data_type):
        """ Functions to create digital playbook using random/given data """
        POMLibrary.POMLibrary().check_page_title("DigitalPlaybookEditPage")
        if data_type == "fixed":
            given_data = self.builtin.get_variable_value("${PlaybookDetails}")
            print("given_data", given_data)

            list_of_key = given_data.keys()
            for label in list_of_key:
                print("label", label)
                key = label.replace("_", " ")
                print("key", key)
                DRPSINGLE.select_from_single_selection_dropdown(key, given_data[label])
        elif data_type == 'empty':
            DRPSINGLE.select_from_single_selection_dropdown(self.PROD_HIER_LEVEL, self.RAND)
            DRPSINGLE.select_from_single_selection_dropdown(self.MAX_PLYBOOK_SIZE, self.RAND)
            DRPSINGLE.clear_selection_from_single_selection_dropdown(self.PROD_HIER_LEVEL)
            DRPSINGLE.clear_selection_from_single_selection_dropdown(self.MAX_PLYBOOK_SIZE)
        else:
            DRPSINGLE.select_from_single_selection_dropdown(self.PROD_HIER_LEVEL, self.RAND)
            DRPSINGLE.select_from_single_selection_dropdown(self.MAX_PLYBOOK_SIZE, self.RAND)
        BUTTON.click_button("Save")

    def user_validates_dropdown_selection_for_product_hierarchy(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        prod_hier = StructureGet.StructureGet().get_prd_hierarchy()
        prod_level_name = []
        prod_hier_list = []
        for dic in prod_hier[0]["levels"]:
            prod_level_name.append(dic["name"])
        get_prod_hier_list = DRPSINGLE.return_item_in_singledropdown(self.PROD_HIER_LEVEL)
        for item in get_prod_hier_list:
            value = self.selib.get_text(item)
            prod_hier_list.append(value)
        self.builtin.set_test_variable("${prod_level_name}", prod_level_name)
        self.builtin.set_test_variable("${prod_hier_list}", prod_hier_list)

    def dropdown_of_product_hierarchy_displaying_correctly(self):
        prod_level_name = self.builtin.get_variable_value("${prod_level_name}")
        prod_hier_list = self.builtin.get_variable_value("${prod_hier_list}")
        assert prod_level_name == prod_hier_list
        DRPSINGLE.randomize_dropdown_selection_in_dropdown()

    def digital_playbook_fields_are_disabled(self):
        prd_hier_status = DRPSINGLE.return_disable_state_of_dropdown(self.PROD_HIER_LEVEL)
        max_size_status = DRPSINGLE.return_disable_state_of_dropdown(self.MAX_PLYBOOK_SIZE)
        self.builtin.should_be_equal(prd_hier_status, 'true')
        self.builtin.should_be_equal(max_size_status, 'true')
