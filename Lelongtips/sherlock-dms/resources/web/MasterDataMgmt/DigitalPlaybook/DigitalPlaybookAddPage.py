from PageObjectLibrary import PageObject
from resources.restAPI.Common import TokenAccess
from robot.api.deco import keyword
from resources.web.MasterDataMgmt.DigitalPlaybook import DigitalPlaybookListPage
from robot.libraries.BuiltIn import BuiltIn
from resources.restAPI.Config.DynamicHierarchy.HierarchyStructure.StructureGet import StructureGet
from resources.restAPI.Config.AppSetup.AppSetupGet import AppSetupGet
from resources.web import BUTTON, COMMON_KEY, TEXTFIELD, DRPSINGLE, RADIOBTN, CALENDAR, FILEUPLOAD
from setup.hanaDB import HanaDB


class DigitalPlaybookAddPage(PageObject):
    """ Functions in Digital PlayBook general information add mode """
    PAGE_TITLE = "Master Data Management / Digital Playbook"
    PAGE_URL = "/setting-ui/playbk-setup/NEW"
    assign_to = "Assign To"
    pb_type = "Playbook Type"
    add_content_title = "ADD | Content"

    _locators = {
        "content_file_upload": "//*[contains(text(),'Upload File')]/following::nz-upload[1]//input",
        "content_thumbnail_upload": "//*[contains(text(),'ADD | Content')]/following::*[contains(text(),'Thumbnail')]/following::nz-upload//input",
        "error_pop_up_ok_btn": "//*[contains(text(),'Invalid file size')]//following::*[contains(text(), 'Ok')]//ancestor::button",
        "content_pop_up_cancel_btn": "//div[@class='ant-modal-body ng-star-inserted']/child::*//*[contains(text(), 'Cancel')]"
    }

    @keyword("user adds digital playbook general information with ${cond} data")
    def user_add_digital_playbook(self, cond):
        DigitalPlaybookListPage.DigitalPlaybookListPage().click_add_digital_playbook_info_button()
        digital_playbook_details = self.builtin.get_variable_value("&{DigiPlyBkDetails}")
        playbook_desc = self.user_inserts_plybk_desc(digital_playbook_details)
        self.user_selects_priority(digital_playbook_details)
        self.user_selects_playbook_type(digital_playbook_details)
        self.user_selects_assign_to(digital_playbook_details)
        self.user_selects_prd_hierarchy(digital_playbook_details)
        self.user_selects_digital_playbook_start_date(digital_playbook_details)
        self.user_selects_digital_playbook_end_date(digital_playbook_details)
        self.user_selects_objective_status(digital_playbook_details)
        self.upload_random_playbook_general_thumbnail()
        BuiltIn().set_test_variable("${playbook_desc}", playbook_desc)

    @keyword("user adds digital playbook content with ${cond} data")
    def user_add_content(self, cond):
        digital_playbook_details = self.builtin.get_variable_value("&{DigiPlyBkDetails}")
        self.click_add_digital_playbook_content_button()
        self.user_inserts_plybk_title(digital_playbook_details)
        self.user_select_file_upload_method(digital_playbook_details)
        if cond == 'fixed':
            ct_details = self.builtin.get_variable_value("&{ContentDetails}")
            if ct_details is None:
                self.user_upload_digital_playbook_content('valid')
            else:
                if 'ContentType' in ct_details:
                    ct_type = ct_details['ContentType']
                    self.user_upload_playbook_content_by_file_type(ct_type)
        else:
            self.user_select_random_file_upload_on_pop_screen()
        self.user_select_random_file_upload_on_pop_screen_thumbnail()
        self.click_add_digital_playbook_content_save_button()
        self.click_add_digital_playbook_save_button()

    def click_add_digital_playbook_content_save_button(self):
        BUTTON.click_pop_up_screen_button("Save")

    def click_add_digital_playbook_save_button(self):
        COMMON_KEY.wait_keyword_success("click_element", "//core-button//child::*[contains(text(),'Save')]//ancestor::core-button[1]")

    def user_inserts_plybk_desc(self, plybk_details):
        """ Function to insert playbook description name with random/given data """
        if plybk_details is not None and 'plybk_desc' in plybk_details:
            ply_desc = TEXTFIELD.insert_into_field("Playbook Description", plybk_details['plybk_desc'])
        else:
            ply_desc = TEXTFIELD.insert_into_field_with_length("Playbook Description", "random", 6)
        return ply_desc

    def user_selects_priority(self, plybk_details):
        """ Function to select Priority by passing random/given data """
        if plybk_details is not None and 'Priority' in plybk_details:
            priority = DRPSINGLE.select_from_single_selection_dropdown("Priority", plybk_details['Priority'])
        else:
            priority = DRPSINGLE.select_from_single_selection_dropdown("Priority", "random")
        return priority

    def user_selects_playbook_type(self, plybk_details):
        """ Function to select playbook type with random/given data """
        if plybk_details is not None and 'Playbook_Type' in plybk_details:
            playbook_type = DRPSINGLE.select_from_single_selection_dropdown(self.pb_type, plybk_details['Playbook_Type'])
        else:
            playbook_type = DRPSINGLE.select_from_single_selection_dropdown(self.pb_type, "random")
        return playbook_type

    def user_selects_assign_to(self, plybk_details):
        """ Function to select assign to with random/given data """
        if plybk_details is not None and 'Assign_To' in plybk_details:
            assign_to = DRPSINGLE.selects_from_single_selection_dropdown(self.assign_to, plybk_details['Assign_To'])
        else:
            assign_to = DRPSINGLE.selects_from_single_selection_dropdown(self.assign_to, "random")
        return assign_to

    def user_selects_prd_hierarchy(self, plybk_details):
        """ Function to select Priority with random/given data """
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        StructureGet().user_get_hierid_from_hierarchy_structure_name("General Product Hierarchy")
        StructureGet().user_get_hierarchy_structure_info_by_hierarchy_id()
        AppSetupGet().user_retrieves_details_of_application_setup()
        body_res = BuiltIn().get_variable_value("${body_result}")
        tree_id = body_res['PLAYBK_PROD_HIERARCHY_LEVEL']
        BuiltIn().set_test_variable("${tree_id}", tree_id)
        StructureGet().get_levels_from_structure(tree_id, "id")
        tree_name = BuiltIn().get_variable_value("${tree_name}")
        if plybk_details is not None and 'prd_hierarchy' in plybk_details:
            prd_hierarchy = DRPSINGLE.selects_from_single_selection_dropdown(tree_name, plybk_details['prd_hierarchy'])
        else:
            prd_hierarchy = DRPSINGLE.selects_from_single_selection_dropdown(tree_name, "random")
        return prd_hierarchy

    def user_selects_digital_playbook_start_date(self, plybk_details):
        if plybk_details is not None and 'StartDate' in plybk_details:
            option = CALENDAR.selects_date_from_calendar("Start Date", plybk_details['StartDate'])
        else:
            option = CALENDAR.selects_date_from_calendar("Start Date", "random")
            BuiltIn().set_test_variable("${date}", option)
        return option

    def user_selects_digital_playbook_end_date(self, plybk_details):
        if plybk_details is not None and 'EndDate' in plybk_details:
            option = CALENDAR.selects_date_from_calendar("End Date", plybk_details['EndDate'])
        else:
            option = CALENDAR.selects_date_from_calendar("End Date", "greater day")
        return option

    def user_selects_objective_status(self, plybk_details):
        if plybk_details is not None and 'Status' in plybk_details:
            option = RADIOBTN.select_from_radio_button("Status", plybk_details['Status'])
        else:
            option = RADIOBTN.select_from_radio_button("Status", "random")
        return option

    def user_inserts_file_desc(self):
        """ Function to insert file description name with random """
        file_desc = TEXTFIELD.insert_into_field_with_length("File Description", "random", 6)
        return file_desc

    def upload_random_playbook_general_thumbnail(self):
        FILEUPLOAD.search_random_file("jpg")
        FILEUPLOAD.choose_the_file_to_upload()
        self.user_inserts_file_desc()
        BUTTON.click_button("Ok")

    def click_add_digital_playbook_content_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    def user_inserts_plybk_title(self, plybk_details):
        """ Function to insert playbook description name with random/given data """
        if plybk_details is not None and 'Title' in plybk_details:
            content_title = TEXTFIELD.insert_into_field("Title", plybk_details['Title'])
        else:
            content_title = TEXTFIELD.insert_into_field_with_length("Title", "random", 6)
        return content_title

    def user_select_file_upload_method(self, plybk_details):
        if plybk_details is not None and 'File' in plybk_details:
            option = RADIOBTN.select_from_pop_out_screen_radio_button(self.add_content_title,"File", plybk_details['File'])
        else:
            option = RADIOBTN.select_from_pop_out_screen_radio_button(self.add_content_title,"File", "New Upload")
        return option

    def user_select_thumbnail_upload_method(self,plybk_details):
        if plybk_details is not None and 'Thumbnail' in plybk_details:
            option = RADIOBTN.select_from_pop_out_screen_radio_button(self.add_content_title, "Thumbnail", plybk_details['Thumbnail'])
        else:
            option = RADIOBTN.select_from_pop_out_screen_radio_button(self.add_content_title, "Thumbnail", "Upload")
        return option

    def user_select_random_file_upload_on_pop_screen(self):
        FILEUPLOAD.search_random_file("jpg")
        self.choose_the_file_to_upload(self.locator.content_file_upload)
        self.user_inserts_file_desc()
        BUTTON.click_button("Ok")

    @keyword('user upload digital playbook content with ${option} file size')
    def user_upload_digital_playbook_content(self, option):
        max_size = self.get_max_playbook_content_file_size()
        max_size = int(max_size)
        if option == 'valid':
            if max_size == 5000:
                file = 'dusk_till_dawn.mp4'
            elif max_size == 1000:
                file = 'file_example_JPG_500kB.jpg'
            elif max_size == 500:
                file = '400KB.PNG'
            elif max_size == 100:
                file = 'PDF_B002.pdf'
        elif option == 'invalid':
            if max_size == 5000:
                file = 'motivational_video.mp4'
            elif max_size == 1000:
                file = 'videoplayback.mp4'
            elif max_size == 500:
                file = 'file_example_JPG_500kB.jpg'
            elif max_size == 100:
                file = 'test.jpg'
            DigitalPlaybookListPage.DigitalPlaybookListPage().click_add_digital_playbook_info_button()
            self.click_add_digital_playbook_content_button()
            self.user_select_file_upload_method("")
        FILEUPLOAD.search_specific_file(file)
        self.choose_the_file_to_upload(self.locator.content_file_upload)
        if option == 'valid':
            self.user_inserts_file_desc()
            BUTTON.click_button("Ok")

    def user_upload_playbook_content_by_file_type(self, type):
        if type == 'video':
            file = 'videoplayback.mp4'
            code = 'V'
        elif type == 'image':
            file = '400KB.PNG'
            code = 'I'
        elif type == 'pdf':
            file = 'PDF_B002.pdf'
            code = 'A'
        elif type == 'ppt':
            file = 'PPT_B003.ppt'
            code = 'P'
        BuiltIn().set_test_variable("${file_type_code}", code)
        FILEUPLOAD.search_specific_file(file)
        self.choose_the_file_to_upload(self.locator.content_file_upload)
        self._wait_for_page_refresh()
        self.user_inserts_file_desc()
        BUTTON.click_button("Ok")

    def validate_file_type_code(self):
        playbk_desc = self.builtin.get_variable_value("${playbook_desc}")
        expected_code = self.builtin.get_variable_value("${file_type_code}")
        HanaDB.HanaDB().connect_database_to_environment()
        query = "select FILE_TYPE from PLAYBK, PLAYBK_CT_ASS, PLAYBK_CT where PLAYBK.ID = PLAYBK_CT_ASS.PLAYBK_ID AND " \
                "PLAYBK_CT_ASS.CONTENT_ID = PLAYBK_CT.ID AND PLAYBK.PLAYBK_DESC = '{0}'".format(playbk_desc)
        code = HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        assert code == expected_code, "File Type Code is not correct"

    def get_max_playbook_content_file_size(self):
        TokenAccess.TokenAccess().user_retrieves_token_access_as("hqadm")
        AppSetupGet().user_retrieves_details_of_application_setup()
        body_res = BuiltIn().get_variable_value("${body_result}")
        if body_res['PLAYBK_MAX_CONTENT_SIZE'] is not None:
            max_size = body_res['PLAYBK_MAX_CONTENT_SIZE']['SIZE']
        else:
            max_size = '5000'
        return max_size

    def close_pop_up_error(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.error_pop_up_ok_btn)
        BUTTON.click_pop_up_screen_button('Cancel')

    def user_select_random_file_upload_on_pop_screen_thumbnail(self):
        FILEUPLOAD.search_random_file("jpg")
        self.choose_the_file_to_upload(self.locator.content_thumbnail_upload)

    def choose_the_file_to_upload(self, xpath):
        """ Functions to select file to upload based on file path """
        file_path = BuiltIn().get_variable_value("${file_path}")
        self.selib.choose_file(xpath, str(file_path))
        self._wait_for_page_refresh()

    def user_back_to_digital_playbook_listing_page(self):
        BUTTON.click_button("Cancel")

    @keyword("user validate ${field} drop down have following value:${value}")
    def user_validate_drop_down_value(self, field, value):
        value = value.split(",")
        list_count = len(value)
        summary = DRPSINGLE.return_item_in_singledropdown(field)
        count = 0
        for web_item in summary:
            item_in_drop_down = self.selib.get_text(web_item)
            for user_input_items in value:
                if item_in_drop_down == user_input_items:
                    count = count + 1
                    break;
        assert count == list_count, "{0} not found in drop down list"

    @keyword("validated playbook code, playbook type, assign to is in disabled")
    def validate_field_is_in_disabled_after_created_digital_playbook(self):
        status = DRPSINGLE.return_disable_state_of_dropdown(self.assign_to)
        assert status == "false", "Assign To field is not in disabled"
        status = DRPSINGLE.return_disable_state_of_dropdown(self.pb_type)
        assert status == "false", "Playbook Type field is not in disabled"
        status = self.selib.get_element_attribute("//*[text()='Playbook Code']/following::input[1]", "ng-reflect-disabled")
        assert status == "false", "Playbook Code field is not in disabled"

    def validate_file_length(self, type, desc):
        HanaDB.HanaDB().connect_database_to_environment()
        query = "select * from PLAYBK, PLAYBK_CT_ASS, PLAYBK_CT where PLAYBK.ID = PLAYBK_CT_ASS.PLAYBK_ID AND " \
                "PLAYBK_CT_ASS.CONTENT_ID = PLAYBK_CT.ID AND PLAYBK_DESC = '{0}'".format(desc)
        result = HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        if type == "video" and result == "NULL" or type == "pdf" and result == "NULL":
            print("Video or PDF content saved without file length")
        elif type == "image" and result != "NULL" or type == "ppt" and result != "NULL":
            print("Image or PPT content saved with file length")


