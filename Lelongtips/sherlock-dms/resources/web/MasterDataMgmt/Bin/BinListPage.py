from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON, TEXTFIELD

class BinListPage(PageObject):
    PAGE_TITLE = "Master Data Management / Bin"
    PAGE_URL = "/objects/module-data/warehouse-bin?template=p"
    BIN_DETAILS="${bin_details}"

    _locators = {

    }
    @keyword('user perform ${action} on bin')
    def user_perform_on_bin(self, action):
        setup = BuiltIn().get_variable_value(self.BIN_DETAILS)
        setup_code = setup['code']
        setup_desc = setup['desc']
        col_list = ["BIN_CODE","BIN_DESC"]
        data_list = [setup_code,setup_desc]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
        ("present", "Bin", action, col_list, data_list)

    @keyword('user searches created bin in listing page by ${type}')
    def user_search_created_bin(self,type):
        setup = BuiltIn().get_variable_value(self.BIN_DETAILS)
        BUTTON.click_icon("search")
        if type == "code":
            TEXTFIELD.insert_into_search_field("Bin Code",setup['code'])
        elif type=="description":
            TEXTFIELD.insert_into_search_field("Bin Description", setup['desc'])

    @keyword('user filters created bin in listing page by ${type}')
    def user_filters_created_bin(self,type):
        setup = BuiltIn().get_variable_value(self.BIN_DETAILS)
        BUTTON.click_icon("filter")
        if type=="code":
            TEXTFIELD.insert_into_filter_field("Bin Code", setup['code'])
        elif type=="description":
            TEXTFIELD.insert_into_filter_field("Bin Description", setup['desc'])
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No Bin in listing"

