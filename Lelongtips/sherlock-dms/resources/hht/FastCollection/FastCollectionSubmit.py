from robot.api.deco import keyword

from setup.hht.HHTMenuNav import HHTMenuNav
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from setup.hanaDB import HanaDB
from resources.Common import Common

class FastCollectionSubmit(POMLibrary):
    _locators = {
        "release_picklist_button": "//android.widget.Button[@resource-id='DLG_CommDeliveryROOT.BTN_ReleasePicklist']",
        "popup": "//*[@resource-id='popupBody']",
        "close_button": "//android.widget.Button[@resource-id='DLG_CommROOT.BBTN_Close']",
        "back_button": "//android.widget.Button[@resource-id='DLG_CommDeliveryROOT.BBTN_Back']"
    }

    @keyword("user releases picklist")
    def release_picklist(self):
        HHTMenuNav().user_navigates_to_menu('Sync Device')
        self.applib().wait_until_page_contains_element(self.locator.release_picklist_button)
        self.applib().click_element(self.locator.release_picklist_button)
        self.applib().wait_until_page_contains_element(self.locator.popup)
        self.applib().click_element(self.locator.popup+'/android.widget.Button[@text="Yes"]')
        release_done = False
        print("before = ", release_done)
        while not release_done:
            release_done = self.builtin.run_keyword_and_return_status("click element", self.locator.back_button)
        print("after = ", release_done)

    def validates_fast_collect_submitted(self):
        col_id = self.builtin.get_variable_value("${col_id}")
        print("col_id = ", col_id)
        col_id = Common().convert_id_to_string(col_id)
        print("col_id 2 = ", col_id)
        HanaDB.HanaDB().connect_database_to_environment()
        query = "select FAST_COLLECT from TXN_COLHDR where ID = '{0}'".format(col_id)
        result = HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        print("result is = ", result)
        assert result == 0, "FAST COLLECT not submitted correctly"

