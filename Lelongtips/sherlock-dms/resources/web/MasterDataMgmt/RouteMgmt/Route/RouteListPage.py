from PageObjectLibrary import PageObject
from resources.web import PAGINATION, BUTTON, DRPSINGLE
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB
import re


class RouteListPage(PageObject):
    """ Functions in route listing page """
    PAGE_TITLE = "Master Data Management / Route Management / Route"
    PAGE_URL = "/route?template=p"

    _locators = {
        "load_image": "//div[@class='loading-text']//img"
    }

    def click_add_route_button(self):
        """ Function to click add button for new route """
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()

    @keyword('user selects route to ${action}')
    def user_selects_route_to(self, action):
        """ Function to select route to edit/delete """
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        route_cd = BuiltIn().get_variable_value("${route_cd}")
        route_name = BuiltIn().get_variable_value("${route_name}")
        route_op = BuiltIn().get_variable_value("${route_op}")
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        col_list = ["ROUTE_CD"]
        data_list = [route_cd]
        print("col :", col_list)
        print("data :", data_list)
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "Route", action, col_list, data_list)

    def user_retrieves_route_id_from_database(self):
        route_cd = BuiltIn().get_variable_value("${route_cd}")
        query = "SELECT CAST(ROW_ID as VARCHAR) FROM MODULE_DATA_FIELDS R INNER JOIN METADATA_FIELD F ON R.FIELD_ID = F.ID " \
                "WHERE R.ROW_ID IN (SELECT ROW_ID FROM MODULE_DATA_FIELDS R INNER JOIN METADATA_FIELD F " \
                "ON R.FIELD_ID = F.ID INNER JOIN MODULE_DATA_ROWS D ON D.MODULE_ID = F.MODULE_ID " \
                "WHERE F.MODULE_ID= (SELECT ID FROM METADATA_MODULE WHERE LOGICAL_ID='route' AND IS_DELETED=false) " \
                "AND FIELD_VALUE = '{0}' AND D.IS_DELETED=false GROUP BY ROW_ID)".format(route_cd)
        HanaDB.HanaDB().connect_database_to_environment()
        record = HanaDB.HanaDB().fetch_one_record(query)
        HanaDB.HanaDB().disconnect_from_database()
        res_bd_route_id = re.sub(r'(.{8})(.{8})(.{4})(.{4})(.{4})(.{4})', r'\1:\2-\3-\4-\5-\6', record)
        self.builtin.set_test_variable("${res_bd_route_id}", res_bd_route_id)

    def user_refresh_the_route_listing_to_get_updated_list(self):
        self.selib.reload_page()

    @keyword('user searches route using ${data}')
    def user_searches_route(self, data):
        BUTTON.click_icon("search")
        multi_status = self.builtin.get_variable_value("${multi_status}")
        np_warehouse = self.builtin.get_variable_value("${np_warehouse}")
        op_type = self.builtin.get_variable_value("${route_op}")
        if multi_status is True:
            DRPSINGLE.selects_from_search_dropdown_selection("NON_PRIME_WHS", np_warehouse)
        else:
            DRPSINGLE.selects_from_search_dropdown_selection("OP_TYPE", op_type)
        BUTTON.click_icon("search")

    def record_listed_successfully_with_searched_data(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        num_row = PAGINATION.return_number_of_rows_in_a_page()
        np_warehouse = self.builtin.get_variable_value("${np_warehouse}")
        if np_warehouse:
            for i in range(0, int(num_row)):
                get_principal = self.selib.get_text("//*[@row-index='{0}']//*[@col-id='NON_PRIME_WHS']".format(i))
                self.builtin.should_be_equal(get_principal, np_warehouse)
