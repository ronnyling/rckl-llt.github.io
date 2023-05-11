from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from resources.web import PAGINATION, BUTTON, TEXTFIELD, DRPSINGLE
from resources.web.Common import MenuNav

class SupplierListPage(PageObject):
    PAGE_TITLE = "Master Data Management / Supplier"
    PAGE_URL = "/setting-ui/supplier?template=p"
    SUPPLIER_DETAILS = "${supplier_details}"

    _locators = {
    }


    @keyword('user validate created supplier is listed in the table and select to ${delete}')
    def user_perform_on_supplier(self, action):
        setup_code = BuiltIn().get_variable_value("${supp_code}")
        setup_name = BuiltIn().get_variable_value("${supp_name}")
        col_list = ["SUPP_CD", "SUPP_NAME"]
        data_list = [setup_code, setup_name]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to \
        ("present", "Supplier", action, col_list, data_list)

    @keyword('user searches created supplier in listing page by ${type}')
    def user_search_created_supplier(self,type):
        setup = BuiltIn().get_variable_value(self.SUPPLIER_DETAILS)
        BUTTON.click_icon("search")
        if type == "code":
            TEXTFIELD.insert_into_search_field("Supplier Code","${supp_code}")
        elif type=="name":
            TEXTFIELD.insert_into_search_field("Supplier Name", "${supp_name}")
        elif type=="businessregistration":
            TEXTFIELD.insert_into_search_field("Business Registration No.", "${br_no}")
        elif type=="telephone":
            TEXTFIELD.insert_into_search_field("Telephone Number", "${telephone}")
        elif type=="contact":
            TEXTFIELD.insert_into_search_field("Contact Person", "${contact}")
        elif type=="principal":
            DRPSINGLE.select_from_single_selection_dropdown("Principal", setup['principal'])

    @keyword('user filters created supplier in listing page by ${type}')
    def user_filters_created_supplier(self, type):
        setup = BuiltIn().get_variable_value(self.SUPPLIER_DETAILS)
        BUTTON.click_icon("filter")
        if type=="supplier_code":
            TEXTFIELD.insert_into_filter_field("Supplier Code", setup['code'])
        elif type=="supplier_name":
            TEXTFIELD.insert_into_filter_field("Supplier Name", setup['name'])
        elif type=="principal":
            DRPSINGLE.selects_from_single_selection_dropdown("Principal", setup['principal'])
        BUTTON.click_button("Apply")

    def record_display_in_listing_successfully(self):
        record_count = PAGINATION.return_number_of_rows_in_a_page()
        assert record_count == 1, "No Supplier in listing"





