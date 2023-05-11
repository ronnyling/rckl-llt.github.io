from PageObjectLibrary import PageObject
from robot.api.deco import keyword


class MenuNav(PageObject):

    _locators ={
        "MenuTitle": "//div[@class='app-title']",
        "MenuLogo": "//img[@class='small-logo acn-small-logo']"
    }

    @keyword("user navigates to menu ${menu}")
    def user_navigates_to_menu(self, menu):
        get_menu_title = self.selib.get_element_count(self.locator.MenuTitle)
        if get_menu_title == 0:
            self.selib.click_element(self.locator.MenuLogo)
        menu_input = menu.split(" | ")
        count = 1
        for item in menu_input:
            if count == 1 and item == 'Merchandising':
                menu_element = f'//li//i[@ng-reflect-nz-type="menu-arch-test"]//following::*[text()=" {item}"]'
            elif count == len(menu_input) and len(menu_input) == 1:
                menu_element = f'//li//*[text()=" {item} "]'
            elif count == len(menu_input) and len(menu_input) > 1:
                menu_element = menu_element + f'//following::li//*[text()=" {item} "]'
                print("menu_element inside", menu_element)
                menu_element = '({0})[1]'.format(menu_element)
                print("menu_element outside", menu_element)
            elif count >= 2:
                menu_element = menu_element + f'//following::li//*[text()=" {item}"]'
            else:
                menu_element = f'//li//*[text()=" {item}"]'
            print("menu_element", menu_element)
            self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec", "click_element", menu_element)
            count = count + 1
        self._wait_for_page_refresh()
