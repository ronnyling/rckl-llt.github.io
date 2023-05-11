from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web.Common.MenuNav import MenuNav
from resources.web import RADIOBTN, TAB, BUTTON, PAGINATION
MENU_NAVIGATE = MenuNav()

class CreditLimit(PageObject):

    PAGE_TITLE = "Master Data Management / Customer"
    PAGE_URL = "refdata/distributors/3CAF4BF6:8C7572E0-F133-4341-9B42-8C5D32CC6352/customer?template=p"

    _locators = {
        "OutBalance": "//*[contains(text(),'Outstanding Balance')]/following::input[1]",
        "CreditLimit": "(//label[contains(text(),'Credit Limit')])[2]/following::input[1]"
    }

    def splt_to_int(self, data):
        data = data.split(".")
        data = data[0]
        data = data.replace(",", "")
        data = int(data)
        print("data=",data)
        return data

    @keyword('turned ${onoff} customer limit to ${block_or_warning} condition and ${limit} credit limit')
    def check_limit_checking(self, onoff, cond, limit):
        self.credit_limit_onoff(onoff)
        RADIOBTN.select_from_radio_button("Credit Limit Checking", cond)
        self.check_limit_check(limit)

    def credit_limit_onoff(self, cond):
        TAB.user_navigates_to_tab("Customer Option")
        if cond == 'on':
            cond = 'Yes'
        else:
            cond = 'No'
        RADIOBTN.select_from_radio_button("Credit Limit Checking", cond)
        BUTTON.click_button("Save")


    def check_limit_check(self, cond):
        total = 0
        self.selib.wait_until_element_is_visible(self.locator.CreditLimit)
        CR = self.selib.get_element_attribute(self.locator.CreditLimit, 'ng-reflect-model')
        CR = self.splt_to_int(CR)
        self.selib.wait_until_element_is_visible(self.locator.OutBalance)
        OB = self.selib.get_element_attribute(self.locator.OutBalance, 'ng-reflect-model')
        OB = self.splt_to_int(OB)
        total = OB + CR
        if total < 0:
            if cond == 'increase':
                total = CR - OB + 100
                self.input_and_save_credit_limit(total)
        else:
            if cond == 'decrease':
                total = CR + OB - 100
                self.input_and_save_credit_limit(total)

    def input_and_save_credit_limit(self, num):
        self.selib.input_text("self.locator.CreditLimit", num)
        BUTTON.click_button("Save")
        self._wait_for_page_refresh()

    @keyword('user validates created CX is in the table and select to ${cond}')
    def user_validate_data_in_cx_listing(self, cond):
        col_list = ["CUST_CD", "CUST_NAME"]
        cx_code = "CT0000001545"
        cx_name = "CreditLimitTest"
        data_list = [cx_code, cx_name]
        PAGINATION.validate_the_data_is_in_the_table_and_select_to("present", "CX", cond, col_list,
                                                                   data_list)


