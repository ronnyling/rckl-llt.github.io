from robot.api.deco import keyword
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
import secrets
from resources.hht import BUTTON, POPUPMSG


class TodayVisitRead(POMLibrary):
    PAGE_TITLE = "MY STORES"
    OUTLET_VISIT = '${getSelection}'

    _locators = {
        "MyStoreTab": "//android.widget.Button[@resource-id='DLG_MainMenu.BBTN_MyStores']",
        "CustList": "//android.view.View[@resource-id='DLG_CustROOT.GRID_CustList']/android.view.View/android.view.View"
    }

    def check_customer_visited_status(self, row_number):
        visited = self.builtin.run_keyword_and_return_status(
            "Element Should Be Visible",
            '//android.view.View[contains(@resource-id,"CustList.{0}.LBL_Visit_Status_Img")]'.format(row_number))
        return visited

    @keyword('choose ${option} from MyStore listing')
    def select_customer_from_listing(self, option):
        self.applib().wait_until_page_contains_element(self.locator.CustList)
        custlist_num = (self.applib().get_matching_xpath_count(self.locator.CustList))
        custlist_num = int(custlist_num)
        for x in range(1, custlist_num+1):
            if option == 'randomly':
                count = secrets.choice(range(1, custlist_num))
            else:
                count = x
            get_selection = count-1
            self.builtin.set_test_variable(self.OUTLET_VISIT, get_selection)
            if option == 'randomly':
                option = self.applib().get_text("//android.view.View[contains(@resource-id,'CustList.{0}.LBL_CustName')]/android.view.View".format(get_selection))
                break
            status = self.builtin.run_keyword_and_return_status(
                "Element Should Contain Text", "//android.view.View[contains(@resource-id,'CustList.{0}.LBL_CustName')]/android.view.View".format(get_selection), option)
            if status == 'True':
                break
        self.builtin.set_test_variable('${custName}', option)

    @keyword('user navigates to customer details')
    def view_customer_details(self):
        BUTTON.click_inline_cust_detail_button(self.builtin.get_variable_value(self.OUTLET_VISIT))

    def handle_visit_message_prompt(self, visited):
        if visited:
            POPUPMSG.selection_popup('Yes')

    @keyword('user visits customer: ${option}')
    def user_visit_customer(self, option):
        self.select_customer_from_listing(option)
        BUTTON.click_inline_cust_visit_button(self.builtin.get_variable_value(self.OUTLET_VISIT))
        visited = self.check_customer_visited_status(self.builtin.get_variable_value(self.OUTLET_VISIT))
        self.handle_visit_message_prompt(visited)
