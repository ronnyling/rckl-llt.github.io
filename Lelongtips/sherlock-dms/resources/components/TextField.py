import secrets
import string
from robot.api.deco import keyword
from resources.Common import Common
from PageObjectLibrary import PageObject


class TextField(PageObject):
    INPUT_ITEM = "${inputItem}"

    _locators = {
        "product": "//input[@placeholder='Enter Code / Description']",
        "productList": "//input[@placeholder='Enter Code / Description']//following::tr[@role='row']",
        "service_field": '//core-custom-field[@ng-reflect-component-id="RefNoComponent"]//input',
        "remarks_field": '//core-custom-field[@ng-reflect-component-id="RemarksComponent"]//input',
        "amount_field": '//core-custom-field[@ng-reflect-component-id="AmountTestComponent"]//input',
        "service_np": '(//core-custom-field[@ng-reflect-component-id="RefNoCNComponent"]//input)[1]',
        "remarks_np": '//core-custom-field[@ng-reflect-component-id="CnNpRemarksComponent"]//input',
        "amount_np": '//core-custom-field[@ng-reflect-component-id="CnNpAmountComponent"]//input',
        "input_field": '(//*[contains(text(),"{0}")]/following::input)[1]',
        "input_area": '(//*[contains(text(),"{0}")]/following::textarea)[1]'
    }

    def insert_into_field_with_length(self, label, item, length):
        item = self.randomize_data(item, length)
        Common().wait_keyword_success("input_text", self.locator.input_field.format(label), item)
        for _ in range(3):
            self.selib.input_text(self.locator.input_field.format(label), item)
            get_msg = self.selib.get_value(self.locator.input_field.format(label))
            if get_msg == item:
                break
        self.builtin.set_test_variable(self.INPUT_ITEM, item)
        return item


    def inserts_into_field_with_length(self, label, item, length):
        item = self.randomize_data(item, length)
        Common().wait_keyword_success("input_text", "(//*[text()='{0}']/following::input)[1]".format(label), item)
        self.builtin.set_test_variable(self.INPUT_ITEM, item)
        return item

    def randomize_data(self, item, length):
        if item == 'random':
            item = ''.join([secrets.choice(string.ascii_letters + string.digits) for _ in range(length)])
        elif item == 'number':
            item = ''.join(secrets.choice(string.digits) for _ in range(length))
        elif item == 'letter':
            item = ''.join(secrets.choice(string.ascii_letters) for _ in range(length))
        else:
            item = self.builtin.set_variable(item)
        return item

    def insert_into_field(self, label, item):
        for _ in range(3):
            self.selib.input_text(self.locator.input_field.format(label), item)
            get_msg = self.selib.get_value(self.locator.input_field.format(label))
            if get_msg == item:
                break
        return item

    def insert_into_filter_field(self, label, item):
        self.selib.input_text("//*[contains(text(),'{0}')]/following::input[1][@type='text']".format(label), item)

    def insert_into_search_field(self, label, item):
        self.selib.wait_until_element_is_not_visible("//div[@class='loading-text']//img")
        try:
            Common().wait_keyword_success("input_text", "//core-textfield[@ng-reflect-name='{0}']//following-sibling::"
                                                        "*//input".format(label), item)
        except Exception as e:
            print(e.__class__, "occured")
            Common().wait_keyword_success("input_text", "//core-textfield[@ng-reflect-desc='{0}']//following-sibling::"
                                                        "*//input".format(label), item)

    def validate_validation_msg(self, label, item):
        """ Functions to validate validation message returned """
        validation_msg = self.selib.get_text(
            "(//*[contains(text(), '{0}')]/following:: *//validation)[1]".format(label))
        self.builtin.should_contain(validation_msg, item)

    @keyword('verifies text field ${label} is disabled')
    def verifies_text_field_is_disabled(self, label):
        """ Functions to verify text field is disabled """
        status = self.selib.get_element_attribute(self.locator.input_field.format(label), "ng-reflect-is-disabled")
        self.builtin.should_be_true(bool(status))

    def retrieves_text_field_text(self, label):
        text = Common().wait_keyword_success("get_text", self.locator.input_field.format(label))
        return text

    def retrieves_text_field_length(self,label):
        length = self.selib.get_element_attribute(self.locator.input_field.format(label), "ng-reflect-maxlength")
        return length

    def inserts_into_trx_field(self, prod_code, prod_uom):
        """ Function for transaction product and product uom field  """
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
        Common().wait_keyword_success("click_element", self.locator.product)
        if prod_code == 'random':
            self.selib.wait_until_page_contains_element(self.locator.productList)
            number_of_prod = self.selib.get_element_count(self.locator.productList)
            if number_of_prod < 10:
                prod_count = secrets.choice(range(1, number_of_prod))
            else:
                prod_count = secrets.choice(range(1, 10))
            prod_code = self.selib.get_text("{0}[{1}]//*[@col-id='PRD_CD']"
                                            .format(self.locator.productList, prod_count))
        Common().wait_keyword_success("input_text", self.locator.product, prod_code)
        Common().wait_keyword_success("click_element", "//*[text()='%s']" % prod_code)
        self._wait_for_page_refresh()
        if prod_uom == 'random':
            uom_choice = self.selib.get_element_count("//tr//*[text()='%s']//following::input[contains(@class,'ant-input-number')\
                                                                     and (@max='Infinity')]" % prod_code)
            if uom_choice > 1:
                uom_choice = secrets.choice(range(1, int(uom_choice)))
            uom_random = secrets.choice(range(1, 10))
            Common().wait_keyword_success("input_text",
                                        "//tr//*[text()='{0}']//following::input[@ng-reflect-model='0'][{1}]"
                                        .format(prod_code, uom_choice), uom_random)
            uom = self.selib.get_text("//tr//*[text()='{0}']//following::input"
                                      "[@ng-reflect-model='0'][{1}]//following::*[1]".format(prod_code, uom_choice))
            prod_uom = "{0}:{1}".format(uom, uom_random)
        else:
            prod_uom_split = prod_uom.split(",")
            for uom in prod_uom_split:
                uom_selected = uom.split(":")
                Common().wait_keyword_success("input_text",
                                            "//tr//*[text()='{0}']/following::*[text()='{1}'][1]/preceding::input[1]"
                                                         .format(prod_code, uom_selected[0]), uom_selected[1])
        Common().wait_keyword_success("click_element", "//div[text()='%s']" % prod_code)
        return prod_code, prod_uom

    def inserts_into_transaction_service_field(self, trx_type=None):
        cn_np_details = self.builtin.get_variable_value("${CNNPDetails['ItemRefNo']}")
        ref_item = self.randomize_data("random", 5)
        remark_item = self.randomize_data("random", 5)
        amt_item = self.randomize_data("number", 3)
        if cn_np_details:
            cn_np_details = self.builtin.get_variable_value("${CNNPDetails}")
            ref_item = cn_np_details['ItemRefNo']
            remark_item = cn_np_details['ItemRemark']
            amt_item = cn_np_details['ItemAmt']
        if trx_type:
            Common().wait_keyword_success("input_text", self.locator.service_np, ref_item)
            Common().wait_keyword_success("input_text", self.locator.remarks_np, remark_item)
            Common().wait_keyword_success("input_text", self.locator.amount_np, amt_item)
        else:
            Common().wait_keyword_success("input_text", self.locator.service_field, ref_item)
            Common().wait_keyword_success("input_text", self.locator.remarks_field, remark_item)
            Common().wait_keyword_success("input_text", self.locator.amount_field, amt_item)

    def return_disable_state_of_field(self, label):
        get_status = self.selib.get_element_attribute \
            ("(//*[text()='{0}']/following::input)[1]".format(label), "ng-reflect-disabled")
        return get_status

    def insert_into_field_without_label(self, row, reflect_name, item, length):
        item = self.randomize_data(item, length)
        Common().wait_keyword_success("input_text", "//tr[@row-index='{0}']//*[@ng-reflect-name='{1}']//child::input"
                                                 .format(row, reflect_name), item)
        self.builtin.set_test_variable(self.INPUT_ITEM, item)
        return item

    def insert_into_area_field_with_length(self, label, item, length):
        item = self.randomize_data(item, length)
        Common().wait_keyword_success("input_text", "//label[contains(text(),'{0}')]//following::textarea[1]".format(label), item)
        self.builtin.set_test_variable(self.INPUT_ITEM, item)
        return item

    def inserts_into_area_field_with_length(self, label, item, length):
        item = self.randomize_data(item, length)
        Common().wait_keyword_success("input_text", "(//*[text()='{0}']/following::textarea[1]".format(label), item)
        self.builtin.set_test_variable(self.INPUT_ITEM, item)
        return item

    def insert_into_area_field(self, label, item):
        Common().wait_keyword_success("input_text", self.locator.input_area.format(label), item)
        return item

    def verifies_text_area_field_is_disabled(self, label):
        """ Functions to verify text area field is disabled """
        status = self.selib.get_element_attribute(self.locator.input_area.format(label), "ng-reflect-is-disabled")
        self.builtin.should_be_true(bool(status))

    def retrieves_text_area_field_text(self, label):
        text = Common().wait_keyword_success("get_text", self.locator.input_area.format(label))
        return text

    def return_disable_state_of_area_field(self, label):
        get_status = self.selib.get_element_attribute \
            ("(//*[text()='{0}']/following::textarea)[1]".format(label), "ng-reflect-disabled")
        return get_status

    def verifies_text_field_is_visible(self, label, status):
        if status == 'visible':
            self.selib.page_should_contain_element(self.locator.input_field.format(label))
        else:
            self.selib.page_should_not_contain_element(self.locator.input_field.format(label))

    def select_from_textfield_selection(self, label, col_id, selection=None):
        Common().wait_keyword_success("click_element", "//*[contains(text(),'{0}')]/following::*[1]//input".format(label))
        if selection is None:
            number_of_data = self.selib.get_element_count("//label[contains(text(),'{0}')]//following::tr[@role='row']".format(label))
            count = secrets.choice(range(1, int(number_of_data)))
            selection = self.selib.get_text("//label[text()='{0}']//following::tr[@role='row'][{1}]//*[@col-id='{2}']"
                                                      .format(label, count, col_id))
        self.selib.input_text("//*[contains(text(),'{0}')]/following::*[1]//input".format(label), selection)
        Common().wait_keyword_success("click_element", "//*[text()='%s']" % selection)
        return selection
