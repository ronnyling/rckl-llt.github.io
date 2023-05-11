from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
import secrets

class HHTDrpSingleSelection(POMLibrary):
    DIV_LOCATOR = "//android.view.View[contains(@text, '{0}')]"
    _locators = {
        "dropdown": "//android.widget.ListView",
        "swipeCount": 3,
        "confirmBtn": "//android.view.View[contains(@text,'Confirm')]"
    }

    def get_drop_down_values(self, label):
        self.applib().wait_until_page_contains_element(self.DIV_LOCATOR.format(label))
        dropdown_value = self.applib().get_text("//android.view.View[contains(@text, '{0}')]/../.."
                                                        "/android.view.View[2]/android.view.View[1]/android.view.View[1]"
                                                        .format(label))
        return dropdown_value

    def click_dropdown(self, label):
        self.applib().wait_until_page_contains_element(self.DIV_LOCATOR.format(label))
        self.applib().click_element("//android.view.View[contains(@text, '{0}')]/.."
                                            "/../android.view.View[2]/android.view.View[1]"
                                            .format(label))

    def check_dropdown_value(self, label, item):
        self.applib().wait_until_page_contains_element(self.DIV_LOCATOR.format(label))
        dropdown_value = self.applib().get_text("//android.view.View[contains(@text, '{0}')]/../.."
                                                        "/android.view.View[2]/android.view.View[1]/android.view.View[1]"
                                                        .format(label))
        if dropdown_value != item:
            raise ValueError("Drop Down selection Failed. Please check on hht_components\DrpSingleSelection.py")

    def select_from_single_dropdown(self, label, item):
        index = 0
        status = False
        self.applib().wait_until_page_contains_element(self.locator.dropdown+'//android.view.View')
        item_count = int(self.applib().get_matching_xpath_count(self.locator.dropdown+'//android.view.View'))
        if item == 'random':
            index = secrets.choice(range(1, item_count))
            item = self.applib().get_text(self.locator.dropdown+'//android.view.View[{0}]'.format(index))
            status = True
            print("Index: ", index, " item: ", item)
        else:
            for x in range(1, item_count+1):
                temp_item = self.applib().get_text(self.locator.dropdown+'//android.view.View[{0}]'.format(x))
                print("Index: ", x, " temp_item: ", temp_item)
                if temp_item == item:
                    index = x
                    status = True
                    break
        if not status:
            raise ValueError("{0} not found in {1} dropdown.".format(item, label))
        num_of_swipes = round(index/self.locator.swipeCount)
        for x in range(0, num_of_swipes):
            self.applib().swipe_by_percent(50, 95, 50, 67)
        self.applib().click_element("//android.view.View[contains(@text,'{0}')]".format(item))
        self.builtin.run_keyword_and_ignore_error("click_element", self.locator.confirmBtn)
        self.check_dropdown_value(label, item)
