import secrets

from robot.api.deco import keyword
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from appium.webdriver.common.touch_action import TouchAction
from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime

from setup.sqllite.SQLLite import SQLLite

current_date = datetime.today().strftime('%d/%m/%Y')


class DigitalPlaybookList(POMLibrary):
    _locators = {
        "playbook_list": "//android.view.View[@resource-id='DLG_DigitalPlayBk.GRID_PlayBk_List']/android.view.View/android.view.View",
        "content_list": "//android.view.View[@resource-id='DLG_DigitalPlayBk.GRID_PlayBk_Content']/android.view.View/android.view.View",
        'playbook_image': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_Img"]',
        'playbook_desc': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_Desc"]',
        'playbook_priority': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_Priority"]',
        'playbook_type': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_Type"]',
        'playbook_hier': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_Hier"]',
        'playbook_last_update': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_UpdateDt"]',
        'playbook_last_played': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_PlayedDT"]',
        'playbook_completed_status_label': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_List.0.LBL_PlayBk_Completed_Status"]',

        'content_image': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_Content.{0}.LBL_PlayBk_CT_Img"]',
        'content_desc': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_Content.{0}.LBL_PlayBK_CT_Desc"]',
        'content_type': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_Content.{0}.LBL_Content_Type_Img"]',
        'content_file_length': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_Content.{0}.LBL_File_Length"]',
        'content_download_button': '//android.widget.Button[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_Content.{0}.BTN_PlayBK_CT_Download"]',
        'content_completed_status': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_Content.{0}.LBL_PlayBk_CT_Completed_Status"]',
        "playbk_ct_button": "//android.widget.Button[@resource-id='DLG_DigitalPlayBk.GRID_PlayBk_Content.{0}.BTN_PlayBK_CT_Play']",

        'playbook': "//android.view.View[@resource-id='DLG_DigitalPlayBk.GRID_PlayBk_List']",
        'select_playbook': "//android.view.View[@resource-id='DLG_DigitalPlayBk.GRID_PlayBk_List.{0}']",
        'playbook_content': '//android.view.View[@resource-id="DLG_DigitalPlayBk.GRID_PlayBk_Content"]',
        'content_display': '//android.view.View[@resource-id="DLG_DigitalPlayBk_CT_Html.HTML_CT_Play"]',
        "OKButton": "//android.widget.Button[@text='OK']",
        "operation_fail_msg": "//android.view.View[contains(@text,'Operation failed')]",
        "image": "//android.view.View[@resource-id='DLG_DigitalPlayBk_CT_Html.LBL_CT_ImageDisplay']",
        "magnifier_button": "//android.widget.Button[@resource-id='DLG_DigitalPlayBk_CT_Html.BTN_Magnifier']",
        "image_display": "//android.view.View[@resource-id='DLG_DigitalPlayBk_ViewImage.HTML_CT_ImageDisplay']",
        "back_to_ct_button": "//android.widget.Button[@resource-id='DLG_DigitalPlayBk_CT_Html.BTN_Back']",
        "back_to_playbk_button": "//android.widget.Button[@resource-id='DLG_DigitalPlayBk.BBTN_Back_Content']",
        "completed_status": "//android.view.View[@resource-id='DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_Completed_Status']",
        "last_played_dt_value": "//android.view.View[@resource-id='DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_PlayedDT_Value']",
        "last_updated_dt_value": "//android.view.View[@resource-id='DLG_DigitalPlayBk.GRID_PlayBk_List.{0}.LBL_PlayBk_UpdateDT_Value']",
    }
    file_type_list = ['V', 'I', 'A', 'P']
    wait_visibility = "Wait Until Page Contains Element"
    slt_pb = "${selected_playbook}"

    def validate_playbook_details(self, no):
        self.applib().wait_until_page_contains_element(self.locator.playbook_image.format(no))
        self.applib().wait_until_page_contains_element(self.locator.playbook_desc.format(no))
        self.applib().wait_until_page_contains_element(self.locator.playbook_priority.format(no))
        self.applib().wait_until_page_contains_element(self.locator.playbook_type.format(no))
        self.applib().wait_until_page_contains_element(self.locator.playbook_hier.format(no))
        self.applib().wait_until_page_contains_element(self.locator.playbook_last_update.format(no))
        self.applib().wait_until_page_contains_element(self.locator.playbook_last_played.format(no))

    def validate_content_details(self, no):
        self.applib().wait_until_page_contains_element(self.locator.content_image.format(no))
        self.applib().wait_until_page_contains_element(self.locator.content_desc.format(no))
        self.applib().wait_until_page_contains_element(self.locator.content_type.format(no))
        self.applib().wait_until_page_contains_element(self.locator.content_download_button.format(no))
        self.applib().wait_until_page_contains_element(self.locator.playbk_ct_button.format(no))
        ct_desc = self.applib().get_text(self.locator.content_desc.format(no))
        BuiltIn().set_test_variable("${ct_desc}", ct_desc)


    def validate_content_file_length(self, no):
        self.applib().wait_until_page_contains_element(self.locator.content_file_length.format(no))

    @keyword("user validates content file type")
    def validate_content_file_type(self):
        ct_desc = BuiltIn().get_variable_value("${ct_desc}")
        query = "select FILE_TYPE from M_PLAYBK_CT where CONTENT_DESC = '{0}'".format(ct_desc)
        record = SQLLite().fetch_one_record(query)
        if record not in self.file_type_list:
            raise ValueError("Invalid file type")

    def validate_playbook_listing(self):
        playbk = self.builtin.run_keyword_and_return_status(self.wait_visibility, self.locator.playbook)
        if playbk:
            print("Playbook listed")
            count = self.get_list_count(self.locator.playbook_list)
            for x in range(count):
                self.validate_playbook_details(x)
        else:
            print("No playbook listed")

    def validate_playbook_content_file_length(self):
        count = self.get_list_count(self.locator.content_list)
        for x in range(count):
            self.validate_content_file_length(x)

    def validate_playbook_content_listing(self):
        playbk_ct = self.builtin.run_keyword_and_return_status(self.wait_visibility, self.locator.playbook_content)
        if playbk_ct:
            print("Playbook content listed")
            count = self.get_list_count(self.locator.content_list)
            for x in range(count):
                self.validate_content_details(x)
        else:
            print("No playbook content listed")

    def validate_playbook_content_displayed(self):
        ct_display = self.builtin.run_keyword_and_return_status(self.wait_visibility, self.locator.content_display)
        if ct_display:
            print("Content displayed")
        else:
            self.close_operation_fail_popup()
            ct_display = self.builtin.run_keyword_and_return_status(self.wait_visibility, self.locator.content_display)
            if ct_display:
                print("Content displayed")
            else:
                print("No content displayed")

    def validate_last_played_date(self):
        last_played_dt = self.locator.last_played_dt_value.format(BuiltIn().get_variable_value(self.slt_pb))
        played_dt_value = self.builtin.run_keyword_and_return_status(self.wait_visibility, last_played_dt)
        el = self.applib().get_text(last_played_dt)
        print("Last Played date is ", el)
        if played_dt_value:
            print("Last played date shown")
            if el == current_date:
                print("Last played date updated")
            else:
                print("Last played date not updated")
        else:
            print("Last played date not shown")

    def validate_last_updated_date(self):
        last_updated_dt = self.locator.last_played_dt_value.format(BuiltIn().get_variable_value(self.slt_pb))
        updated_dt_value = self.builtin.run_keyword_and_return_status(self.wait_visibility, last_updated_dt)
        if updated_dt_value:
            print("Last updated date shown")
        else:
            print("Last updated date not shown")

    def get_list_count(self, el_locator):
        self.applib().wait_until_page_contains_element(el_locator)
        list_count = (self.applib().get_matching_xpath_count(el_locator))
        BuiltIn().set_test_variable("${total_playbook}", list_count)
        print("Total Playbook = ", BuiltIn().get_variable_value("${total_playbook}"))
        return int(list_count)

    @keyword('user choose ${option} from playbook listing')
    def select_playbook_from_listing(self, option):
        playbook_list_num = self.get_list_count(self.locator.playbook_list)
        if option == 'randomly':
            if playbook_list_num > 1:
                get_selection = secrets.randbelow(playbook_list_num-1)
            else:
                get_selection = playbook_list_num-1
        else:
            get_selection = option
        BuiltIn().set_test_variable(self.slt_pb, get_selection)
        selected_playbk = self.locator.select_playbook.format(get_selection)
        self.applib().wait_until_page_contains_element(selected_playbk)
        self.applib().click_element(selected_playbk)

    @keyword('user choose ${option} from content listing')
    def select_playbook_content_from_listing(self, option):
        ct_list_num = self.get_list_count(self.locator.content_list)
        if option == 'randomly':
            if ct_list_num > 1:
                get_selection = secrets.randbelow(ct_list_num-1)
            else:
                get_selection = ct_list_num-1
        else:
            get_selection = option
        BuiltIn().set_test_variable("${selected_content}", get_selection)
        selected_ct = self.locator.playbk_ct_button.format(get_selection)
        self.applib().wait_until_page_contains_element(selected_ct)
        self.applib().click_element(selected_ct)

    def close_operation_fail_popup(self):
        refresh_popup = self.builtin.run_keyword_and_return_status(self.wait_visibility,
                                                                   self.locator.operation_fail_msg)
        if refresh_popup:
            self.applib().click_element(self.locator.OKButton)

    @keyword('user zoom and move the image')
    def zoom_image(self):
        self.applib().wait_until_page_contains_element(self.locator.image)
        self.applib().click_element(self.locator.magnifier_button)
        image = self.locator.image_display
        self.applib().wait_until_page_contains_element(image)
        i = 0
        while i < 10:
            self.applib().click_element(image)
            i += 1
        actions = TouchAction(self.applib()._current_application())
        actions.long_press(x=200, y=200)
        actions.move_to(x=150, y=150)
        actions.release()
        actions.perform()

    def validate_completed_status(self):
        completed_status = self.builtin.run_keyword_and_return_status(self.wait_visibility,
                                                                      self.locator.completed_status.format(
                BuiltIn().get_variable_value(self.slt_pb)))
        if completed_status:
            print("Completion status shown")
        else:
            print("Completion status is not shown")

    @keyword('user back to ${option} page')
    def back_to_previous_page(self, option):
        if option == 'playbook':
            button_selection = self.locator.back_to_playbk_button
        elif option == 'content':
            button_selection = self.locator.back_to_ct_button
        self.applib().wait_until_page_contains_element(button_selection)
        self.applib().click_element(button_selection)

