from PageObjectLibrary import PageObject
from resources.web.Common import POMLibrary
from robot.libraries.BuiltIn import BuiltIn
from resources.web import BUTTON, RADIOBTN, DRPSINGLE, TEXTFIELD, CALENDAR
from robot.api.deco import keyword
from resources.web.MasterDataMgmt.Distributor import DistributorTrxNumListPage

import secrets


class DistributorTrxNumAddPage(PageObject):
    """ Functions in distributor transaction number add page """
    PAGE_TITLE = "Master Data Management / Distributor"
    PAGE_URL = "/distributors?template=p"

    _locators = {
    }

    @keyword('user creates distributor transaction number with ${data_type} data')
    def user_creates_distributor_transaction_number_with_data(self, data_type):
        """ Function to create distributor transaction number with random/given data """
        POMLibrary.POMLibrary().check_page_title("DistributorTrxNumListPage")
        dist_trans_details = self.builtin.get_variable_value("&{DistTrxNumDetails}")
        DistributorTrxNumListPage.DistributorTrxNumListPage().click_add_distributor_transaction_number_button()
        POMLibrary.POMLibrary().check_page_title("DistributorTrxNumAddPage")
        tran_type = self.user_selects_transaction_type_from_dropdown(dist_trans_details)
        multi_status = self.builtin.get_variable_value("&{multi_status}")
        if multi_status is True:
            self.user_selects_principal_field(dist_trans_details)
            principal = RADIOBTN.return_selected_item_of_radio_button("Principal")
            BuiltIn().set_test_variable("${principal}", principal)
        else:
            RADIOBTN.validates_radio_button("Principal", "displaying")
        self.user_inserts_prefix(dist_trans_details)
        start_num = self.user_inserts_start_number(dist_trans_details)
        end_num = self.user_inserts_end_number(dist_trans_details)
        self.user_chooses_start_date()
        self.user_chooses_end_date()
        BuiltIn().set_test_variable("${tran_type}", tran_type)
        BuiltIn().set_test_variable("${start_num}", start_num)
        BuiltIn().set_test_variable("${end_num}", end_num)
        BUTTON.click_button("Save")

    def user_selects_transaction_type_from_dropdown(self, dist_trans_details):
        """ Function to select transaction type with random/given """
        trans_type_given = self.builtin.get_variable_value("&{DistTrxNumDetails['TXN_TYPE']}")
        if trans_type_given is not None:
            tran_type = DRPSINGLE.selects_from_single_selection_dropdown("Transaction Type", dist_trans_details['TXN_TYPE'])
        else:
            tran_type = DRPSINGLE.selects_from_single_selection_dropdown("Transaction Type", "random")
        return tran_type

    def user_selects_principal_field(self, dist_trans_details):
        """ Function to select prime/non prime warehouse """
        if dist_trans_details is None:
            RADIOBTN.select_from_radio_button("Principal", "random")
        else:
            if dist_trans_details.get('PRIME_FLAG') is not None:
                RADIOBTN.select_from_radio_button("Principal", dist_trans_details['PRIME_FLAG'])
            else:
                RADIOBTN.select_from_radio_button("Principal", "random")

    def user_inserts_prefix(self, dist_trans_details):
        """ Function to insert prefix with random/given data """
        if dist_trans_details is None:
            prefix = TEXTFIELD.insert_into_field_with_length("Prefix", "letter", 5)
        else:
            if dist_trans_details.get('PREFIX') is not None:
                prefix = TEXTFIELD.insert_into_field("Prefix", dist_trans_details['PREFIX'])
            else:
                prefix = TEXTFIELD.insert_into_field_with_length("Prefix", "letter", 5)
        return prefix

    def user_inserts_start_number(self, dist_trans_details):
        """ Function to insert start number with random/given data """
        start_num_given = self.builtin.get_variable_value("&{DistTrxNumDetails['START_NUM']}")
        if start_num_given is not None:
            start_num = TEXTFIELD.insert_into_field("Start Number", dist_trans_details['START_NUM'])
        else:
            start_num = TEXTFIELD.insert_into_field_with_length("Start Number", "number", 2)
            rand_startnum = secrets.randbelow(100)
            BuiltIn().set_test_variable("${rand_startnum}", rand_startnum)
            start_num = TEXTFIELD.insert_into_field("Start Number", rand_startnum)
        return start_num

    def user_inserts_end_number(self, dist_trans_details):
        """ Function to insert end number with random/given data """
        end_num_given = self.builtin.get_variable_value("&{DistTrxNumDetails['END_NUM']}")
        if end_num_given is not None:
            end_num = TEXTFIELD.insert_into_field("End Number", dist_trans_details['END_NUM'])
        else:
            rand_startnum = BuiltIn().get_variable_value("${rand_startnum}")
            rand_endnum = int(rand_startnum) + 100
            end_num = TEXTFIELD.insert_into_field("End Number", rand_endnum)
        return end_num

    def user_inserts_suffix(self, dist_trans_details):
        """ Function to insert suffix with random/given data """
        if dist_trans_details is None:
            suffix = TEXTFIELD.insert_into_field_with_length("Suffix", "letter", 5)
        else:
            if dist_trans_details.get('SUFFIX') is not None:
                suffix = TEXTFIELD.insert_into_field("Suffix", dist_trans_details['SUFFIX'])
            else:
                suffix = TEXTFIELD.insert_into_field_with_length("Suffix", "letter", 5)
        return suffix

    def user_chooses_start_date(self):
        """ Function to select start date with random/given data """
        start_dt = CALENDAR.selects_date_from_calendar("Start Date", "next day")
        return start_dt

    def user_chooses_end_date(self):
        """ Function to select end date with random/given data """
        end_dt = CALENDAR.selects_date_from_calendar("End Date", "random")
        return end_dt
