from PageObjectLibrary import PageObject
from resources.web import BUTTON


class AttributeModuleListPage(PageObject):
    PAGE_TITLE = "System Configuration / Attribute / Attribute Module"
    PAGE_URL = "/module"

    _locators = {
    }

    def click_add_attribute_module_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()
