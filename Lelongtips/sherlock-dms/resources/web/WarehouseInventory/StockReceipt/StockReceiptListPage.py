from PageObjectLibrary import PageObject
from resources.web import BUTTON


class StockReceiptListPage(PageObject):
    PAGE_TITLE = "Warehouse Inventory / Stock Receipt"
    PAGE_URL = "/inventory/stockreceipt"

    _locators = {
    }

    def click_add_stock_receipt_button(self):
        BUTTON.click_button("Add")
        self._wait_for_page_refresh()
