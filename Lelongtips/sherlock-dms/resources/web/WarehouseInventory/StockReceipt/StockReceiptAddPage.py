from PageObjectLibrary import PageObject
from resources.web.WarehouseInventory.StockReceipt import StockReceiptListPage
from resources.web.Common import MenuNav
from resources.web import DRPSINGLE, TEXTFIELD, BUTTON
from robot.api.deco import keyword
import datetime
import secrets


class StockReceiptAddPage(PageObject):
    PAGE_TITLE = "Warehouse Inventory / Stock Receipt"
    PAGE_URL = "/inventory/stockreceipt/NEW"

    _locators = {
        "ProdField": "//input[@placeholder='Enter Product Code / Name']",
        "ProdDate": "//td//nz-date-picker",
        "ProdPrice": "//*[contains(@ng-reflect-name,'costprice')]//input"
    }

    @keyword('user creates stock receipt with ${data_type}')
    def user_creates_stock_receipt_with(self, data_type):
        prod_code = self.builtin.get_variable_value("${prod_code}")
        MenuNav.MenuNav().user_navigates_to_menu("Warehouse Inventory | Stock Receipt")
        StockReceiptListPage.StockReceiptListPage().click_add_stock_receipt_button()
        DRPSINGLE.selects_from_single_selection_dropdown("Warehouse", "WHAdS")
        DRPSINGLE.selects_from_single_selection_dropdown("Supplier Name", "random")
        TEXTFIELD.insert_into_field_with_length("Delivery Order No.", "random", 10)
        self.selib.input_text(self.locator.ProdField, prod_code)
        self.selib.click_element("//*[text()='%s']" % prod_code)
        random_date =secrets.choice(range(1, 360))
        choose_date = datetime.datetime.now() + datetime.timedelta(days=random_date)
        choose_date = choose_date.strftime('%b %#d, %Y')
        self.builtin.wait_until_keyword_succeeds("0.5 min", "3 sec",
                  "click_element", self.locator.ProdDate)
        self.selib.input_text("//calendar-input//input", choose_date)
        number_of_uom = self.selib.get_element_count\
            ("//tr//*[text()='{0}']//following::input[contains(@ng-reflect-name,'uom')]".format(prod_code))
        uom_choice = secrets.choice(range(1, int(number_of_uom)))
        uom_random = secrets.choice(range(1, 10))
        self.selib.input_text("//tr//*[text()='{0}']//following::input[contains(@ng-reflect-name,'uom')][{1}]"
                              .format(prod_code, uom_choice), uom_random)
        price_random = secrets.choice(range(10, 99))
        self.selib.input_text(self.locator.ProdPrice, price_random)
        self.selib.click_element("//tr//*[text()='{0}']".format(prod_code))
        BUTTON.click_button("Save & Confirm")
