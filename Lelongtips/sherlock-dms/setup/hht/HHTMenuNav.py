from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from robot.api.deco import keyword

class HHTMenuNav(POMLibrary):

    _locators = {
        "CustomerDetailTab": '//android.view.View[@resource-id="DLG_CustDetails.TAB_CustDetails_header"]',
        "HamburgerMenu": '//android.view.View[@resource-id="DLG_MenuDetails.SWITCH_MainMenu"]',
        "HamburgerMenuBtn": '//android.widget.Button[@resource-id="DLG_CustROOT.BBTN_MainMenu"]'
    }
    el_should_contain = "Element Should Contain Text"
    error_msg = "No menu named {0} found"

    def navigate_to_customer_tab(self, tab):
        self.applib().wait_until_page_contains_element(self.locator.CustomerDetailTab)
        tab_count = int(self.applib().get_matching_xpath_count(self.locator.CustomerDetailTab+'/android.widget.Button'))
        index = 0
        status = 'False'
        for x in range(1, tab_count + 1):
            status = self.builtin.run_keyword_and_return_status(
                self.el_should_contain,
                self.locator.CustomerDetailTab + '/android.widget.Button[{0}]'.format(x), tab.upper())
            if status:
                index = x
                break
        if status:
            if index > 3:
                self.applib().swipe_by_percent(90, 12, 7, 12)
            self.applib().click_element(self.locator.CustomerDetailTab + '/android.widget.Button[{0}]'.format(index))
        else:
            raise ValueError("No Tab named {0} found".format(tab))

    @keyword('user navigates to Hamburger Menu')
    def open_hamburger_menu_button(self):
        self.applib().wait_until_page_contains_element(self.locator.HamburgerMenuBtn)
        self.applib().click_element(self.locator.HamburgerMenuBtn)

    @keyword('user navigates to Hamburger Menu | ${menu}')
    def user_navigates_to_menu(self, menu):
        self.open_hamburger_menu_button()
        self.applib().wait_until_page_contains_element(self.locator.HamburgerMenu)
        menu_count = int(self.applib().get_matching_xpath_count(self.locator.HamburgerMenu + '/android.view.View'))
        index = 0
        status = 'False'
        for x in range(1, menu_count + 1):
            status = self.builtin.run_keyword_and_return_status(
                self.el_should_contain, self.locator.HamburgerMenu+'/android.view.View[{0}]/android.view.View[2]'
                                               .format(x), menu)
            if status:
                index = x
                break
        if status:
            self.applib().click_element(self.locator.HamburgerMenu + '/android.view.View[{0}]'.format(index))
        else:
            raise ValueError(self.error_msg.format(menu))

    @keyword('user validates ${menu} is ${menu_status}')
    def user_validates_menu(self, menu, menu_status):
        self.open_hamburger_menu_button()
        self.applib().wait_until_page_contains_element(self.locator.HamburgerMenu)
        menu_count = int(self.applib().get_matching_xpath_count(self.locator.HamburgerMenu + '/android.view.View'))
        status = 'False'
        for x in range(1, menu_count + 1):
            status = self.builtin.run_keyword_and_return_status(
                self.el_should_contain,
                self.locator.HamburgerMenu + '/android.view.View[{0}]/android.view.View[2]'
                .format(x), menu)
            if status:
                break
        if status:
            if menu_status == 'off':
                raise ValueError("Menu named {0} found".format(menu))
            else:
                print("Menu named {0} found".format(menu))
        else:
            if menu_status == 'on':
                raise ValueError(self.error_msg.format(menu))
            else:
                print(self.error_msg.format(menu))
