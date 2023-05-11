from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web import PAGINATION, BUTTON, TEXTFIELD, DRPSINGLE


class PlaybookTypeListPage(PageObject):
    """ Functions related to listing page of Playbook Type """
    PAGE_TITLE = "Configuration / Reference Data / Playbook Type"
    PAGE_URL = "/objects/playbook-type"
    PLYBOOK_CD = "${playbook_type_cd}"
    PLYBOOK_DESC = "${playbook_type_desc}"
    PRD_HIER_REQ = "${prd_hier_req}"

    _locators = {
        "first_playbook": "//tr[1]//td[2]//core-cell-render//div//a",
        "load_image": "//div[@class='loading-text']//img"
    }

    @keyword('user selects playbook type to ${action}')
    def user_selects_playbook_type_to(self, action):
        """ Function to select playbook type in listing to edit/delete """
        playbook_type_cd = self.builtin.get_variable_value(self.PLYBOOK_CD)
        playbook_type_desc = self.builtin.get_variable_value(self.PLYBOOK_DESC)
        prd_hier_req = self.builtin.get_variable_value(self.PRD_HIER_REQ)
        if playbook_type_cd is None:
            playbook_type_cd = self.selib.get_text("//*[@role='row' and @row-index='0']//*[@col-id='PLAYBOOK_TYPE_CD']")
            playbook_type_desc = self.selib.get_text(
                                            "//*[@role='row' and @row-index='0']//*[@col-id='PLAYBOOK_TYPE_DESC']")
            prd_hier_req = self.selib.get_text(
                                            "//*[@role='row' and @row-index='0']//*[@col-id='PLAYBOOK_PRD_HIER_REQ']")
        col_list = ["PLAYBOOK_TYPE_CD", "PLAYBOOK_TYPE_DESC", "PLAYBOOK_PRD_HIER_REQ"]
        data_list = [playbook_type_cd, playbook_type_desc, prd_hier_req]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to\
            ("present", "Playbook Type", action, col_list, data_list)

    def user_filters_playbook_type_using_created_data(self):
        """ Function to filter playbook type using filter fields """
        playbook_type_cd = self.builtin.get_variable_value(self.PLYBOOK_CD)
        playbook_type_desc = self.builtin.get_variable_value(self.PLYBOOK_DESC)
        prd_hier_req = self.builtin.get_variable_value(self.PRD_HIER_REQ)
        BUTTON.click_icon("filter")
        TEXTFIELD.insert_into_filter_field("Playbook Type Code", playbook_type_cd)
        TEXTFIELD.insert_into_filter_field("Playbook Type Description", playbook_type_desc)
        DRPSINGLE.selects_from_single_selection_dropdown("Product Hierarchy Required", prd_hier_req)
        BUTTON.click_button("Apply")

    def user_searches_playbook_type_using_created_data(self):
        """ Function to search playbook type using search fields """
        playbook_type_cd = self.builtin.get_variable_value(self.PLYBOOK_CD)
        playbook_type_desc = self.builtin.get_variable_value(self.PLYBOOK_DESC)
        prd_hier_req = self.builtin.get_variable_value(self.PRD_HIER_REQ)
        BUTTON.click_icon("search")
        TEXTFIELD.insert_into_search_field("PLAYBOOK_TYPE_CD", playbook_type_cd)
        TEXTFIELD.insert_into_search_field("PLAYBOOK_TYPE_DESC", playbook_type_desc)
        DRPSINGLE.selects_from_search_dropdown_selection("PLAYBOOK_PRD_HIER_REQ", prd_hier_req)

    def playbook_type_listed_successfully_in_listing(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        playbook_type_cd = self.builtin.get_variable_value(self.PLYBOOK_CD)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        for i in range(0, int(num_row)):
            get_code = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='PLAYBOOK_TYPE_CD']".format(i))
            self.builtin.should_be_equal(get_code, playbook_type_cd)
