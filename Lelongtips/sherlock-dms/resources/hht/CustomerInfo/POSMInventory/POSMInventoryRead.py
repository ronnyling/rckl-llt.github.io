from robot.api.deco import keyword
from resources.hht import DRPSINGLE
from setup.hht.HHTMenuNav import HHTMenuNav as MenuNav
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from setup.sqllite.SQLLite import SQLLite
import json
from resources.hht_api.POSMInstallation import POSMInstallationPost
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn

class POSMInventoryRead(POMLibrary):
    CUST_NAME = '${custName}'

    _locators = {
        'dropdown_label': 'POSM',
        'posm_code_label': '//android.view.View[@resource-id="DLG_Cust_Posm.LBL_PRD_CODE_T"]',
        'posm_desc_label': '//android.view.View[@resource-id="DLG_Cust_Posm.LBL_PRD_DESC_T"]',
        'posm_qty_label': '//android.view.View[@resource-id="DLG_Cust_Posm.LBL_QTY_T"]',
        'posm_qty_value': "//android.view.View[@resource-id='DLG_Cust_Posm.LBL_QTY_V']",
        'posm_code_value': "//android.view.View[@resource-id='DLG_Cust_Posm.LBL_PRD_CODE_V']",
        'posm_desc_value': "//android.view.View[@resource-id='DLG_Cust_Posm.LBL_PRD_DESC_V']",
        'posm_uom_label': "//android.view.View[@resource-id='DLG_Cust_Posm.LBL_UOM_DESC_T']",
        'posm_uom_value': "//android.view.View[@resource-id='DLG_Cust_Posm.LBL_UOM_DESC_V']",
        'posm_attribute_displayed': '//android.view.View[@resource-id="DLG_Cust_Posm.GRID_CUST_POSM_PRD_ATTR"]/android.view.View/android.view.View'
    }

    def get_driver_instance(self):
        return self.builtin.get_library_instance('AppiumLibrary')

    def click_on_customer_posm_dropdown(self):
        DRPSINGLE.click_dropdown(self.locator.dropdown_label)

    @keyword('user selects customer ${tabName} tab')
    def navigate_to_customer_posm_tab(self, tab_name):
        MenuNav().navigate_to_customer_tab(tab_name)

    @keyword('user selects a customer posm: ${item}')
    def select_customer_posm(self, item):
        self.click_on_customer_posm_dropdown()
        DRPSINGLE.select_from_single_dropdown(self.locator.dropdown_label, item)

    def user_check_labels(self):
        self.applib().element_should_contain_text(self.locator.posm_code_label, 'POSM Code')
        self.applib().element_should_contain_text(self.locator.posm_desc_label, 'POSM Description')
        self.applib().element_should_contain_text(self.locator.posm_qty_label, 'Available Quantity')
        self.applib().element_should_contain_text(self.locator.posm_uom_label, 'UOM Description')

    def user_check_avail_qty(self, dropdown_item):
        item_quantity = SQLLite().fetch_one_record("select printf('%.0f',a.qty) from m_cust_posm a left join m_prd b on a.prd_id = b.id left join m_cust c on a.cust_id = c.id where b.prd_desc = '{0}' and cust_name = '{1}'".format(dropdown_item, self.builtin.get_variable_value(self.CUST_NAME)))
        self.applib().element_should_contain_text(self.locator.posm_qty_value, str(item_quantity))

    def user_check_posm_code(self, dropdown_item):
        posm_code = SQLLite().fetch_one_record("select b.prd_cd from m_cust_posm a left join m_prd b on a.prd_id = b.id left join m_cust c on a.cust_id = c.id where b.prd_desc = '{0}' and cust_name = '{1}'".format(dropdown_item, self.builtin.get_variable_value(self.CUST_NAME)))
        self.applib().element_should_contain_text(self.locator.posm_code_value, posm_code)

    def user_check_posm_desc(self, dropdown_item):
        posm_desc = SQLLite().fetch_one_record("select b.prd_desc from m_cust_posm a left join m_prd b on a.prd_id = b.id left join m_cust c on a.cust_id = c.id where b.prd_desc = '{0}' and cust_name = '{1}'".format(dropdown_item, self.builtin.get_variable_value(self.CUST_NAME)))
        self.applib().element_should_contain_text(self.locator.posm_desc_value, posm_desc)

    def user_check_uom_desc(self, dropdown_item):
        uom_desc = SQLLite().fetch_one_record("select a.uom_description from m_prduom a left join m_prd b on a.prod_id = b.id where b.prd_desc='{0}' order by uom_level asc".format(dropdown_item))
        self.applib().element_should_contain_text(self.locator.posm_uom_value, uom_desc)

    def user_check_attribute(self, dropdown_item):
        attributes_raw = SQLLite().fetch_one_record("select b.attributes from m_cust_posm a left join m_prd b on a.prd_id = b.id left join m_cust c on a.cust_id = c.id where b.prd_desc = '{0}' and cust_name = '{1}'".format(dropdown_item, self.builtin.get_variable_value('${custName}')))
        attribute_displayed_count = int(self.applib().get_matching_xpath_count(self.locator.posm_attribute_displayed))
        if (attributes_raw is None) and attribute_displayed_count > 0:
            raise ValueError("No attribute found in M_PRD, please check the value in attribute field")
        elif (attributes_raw is not None) and attribute_displayed_count > 0:
            attributes_list = json.loads(attributes_raw)
        counter = 0
        for x in range(0, attribute_displayed_count):
            try:
                att_value = SQLLite().execute_query("select count(*), coalesce(attribute_value, 'null') from m_attr_value where attribute_code = '{0}' limit 1".format(attributes_list[x]['result']))
            except ValueError:
                att_value = SQLLite().execute_query("select 0, 'null'")
            attribute_count = len(att_value)
            if attribute_count > 0 and att_value[0][1] != 'null':
                self.applib().element_should_contain_text("//android.view.View[@resource-id='DLG_Cust_Posm.GRID_CUST_POSM_PRD_ATTR.{0}.LBL_ATTR_TITLE']".format(counter),
                                                                  attributes_list[x]['AttributeTitle'])
                self.applib().element_should_contain_text("//android.view.View[@resource-id='DLG_Cust_Posm.GRID_CUST_POSM_PRD_ATTR.{0}.LBL_ATTR_DESC']".format(counter),
                                                                  att_value[0][1])
                counter += 1

    @keyword('user verify posm details')
    def user_verify_posm_details(self):
        dropdown_item = DRPSINGLE.get_drop_down_values(self.locator.dropdown_label)
        self.user_check_labels()
        self.user_check_avail_qty(dropdown_item)
        self.user_check_posm_code(dropdown_item)
        self.user_check_posm_desc(dropdown_item)
        self.user_check_uom_desc(dropdown_item)
        self.user_check_attribute(dropdown_item)

    @keyword('user creates prerequisite for Customer Inventory')
    def user_creates_prerequisite_for_customer_inventory(self):
        Common().execute_prerequisite('1-POSMRequestPre.yaml')
        Common().execute_prerequisite('1-POSMInstallationPre.yaml')
        install_details = {
            'txn_status': 'C'
        }
        BuiltIn().set_test_variable('${InstallDetails}', install_details)
        POSMInstallationPost.POSMInstallationPost().user_creates_posm_installation_with()
