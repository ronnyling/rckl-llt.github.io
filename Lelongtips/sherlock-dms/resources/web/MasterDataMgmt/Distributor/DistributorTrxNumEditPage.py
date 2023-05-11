from PageObjectLibrary import PageObject
from resources.web.Common import POMLibrary
from robot.libraries.BuiltIn import BuiltIn
from resources.web import CALENDAR, BUTTON, RADIOBTN
from robot.api.deco import keyword
from resources.web.MasterDataMgmt.Distributor import DistributorTrxNumAddPage


class DistributorTrxNumEditPage(PageObject):
    """ Functions in distributor transaction number add page """
    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"

    _locators = {
    }

    @keyword('user updates distributor transaction number with ${data_type} data')
    def user_updates_distributor_transaction_number_with_data(self, data_type):
        """ Function to update distributor transaction number with random/given data """
        dist_trans_details = self.builtin.get_variable_value("&{DistTrxNumDetails}")
        POMLibrary.POMLibrary().check_page_title("DistributorTrxNumAddPage")
        add_func = DistributorTrxNumAddPage.DistributorTrxNumAddPage()
        multi_status = self.builtin.get_variable_value("&{multi_status}")
        if multi_status is True:
            status = RADIOBTN.return_visibility_of_radio_buttons("Principal")
            self.builtin.should_be_equal(status, "true")
        add_func.user_inserts_prefix(dist_trans_details)
        start_num = add_func.user_inserts_start_number(dist_trans_details)
        end_num = add_func.user_inserts_end_number(dist_trans_details)
        BuiltIn().set_test_variable("${start_num}", start_num)
        BuiltIn().set_test_variable("${end_num}", end_num)
        BUTTON.click_button("Save")
