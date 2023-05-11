from PageObjectLibrary import PageObject
from resources.web.CustTrx.Collection.CollectionListPage import CollectionListPage
from robot.libraries.BuiltIn import BuiltIn
from resources.web import DRPSINGLE, FILEUPLOAD, TEXTFIELD, BUTTON, COMMON_KEY, LABEL, POPUPMSG, CALENDAR
from robot.api.deco import keyword
import datetime
import re
import secrets


class CollectionAddPage(PageObject):
    """ Functions for Collection Add Page actions """
    PAGE_TITLE = "Customer Transaction / Collection"
    PAGE_URL = "/customer-transactions-ui/customer-collection/NEW"

    YEAR_MONTH_DAY = '%Y-%m-%d'

    _locators = {
        "dropdown": "//label[text()='{0}']//following::*//nz-select",
        "outstanding_amt": "//tr//td[6]",
        "payment_mode": "(//*[text()='Setting Payment Mode']//following::*//nz-select)[1]",
        "amount": "(//*[contains(text(), 'Setting Payment Mode')]/following::input)[4]",
        "ref_no": "(//*[contains(text(), 'Setting Payment Mode')]/following::input)[5]",
        "date": "(//*[contains(text(), 'Setting Payment Mode')]/following::input)[6]",
        "bank": "(//*[text()='Setting Payment Mode']//following::*//nz-select)[2]",
        "ewallet": "(//*[text()='Setting Payment Mode']//following::*//nz-select)[3]",
        "other_payment": "//i[@ng-reflect-nz-type='plus']",
        "expand_collection": "(//td[1]//following::span)[1]",
        "open_item": "//*[contains(text(), 'Doc. Number')]/following::tr[{0}]",
        "doc_date": "//*[contains(text(), 'Doc. Number')]/following::tr[{0}]//td[2]",
        "first_collection_no": "//tr[1]//td[2]",
        "open_item_cash": "//*[contains(text(),'Doc. Number')]/following::*//tr[{0}]//td[7]//input",
        "checkbox": "//*[text()='{0}']//following::*/label[contains(@class,'checkbox')]"
    }

    def select_route_for_collection(self, details):
        """ Function to select route in collection add page """
        if details is None:
            DRPSINGLE.selects_from_single_selection_dropdown("Route", "random")
        else:
            if details.get("route") is not None:
                DRPSINGLE.selects_from_single_selection_dropdown("Route", details['route'])
            else:
                DRPSINGLE.selects_from_single_selection_dropdown("Route", "random")
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)

    def select_route_plan_for_collection(self, details):
        """ Function to select route plan in collection add page """
        route_plan = "Route Plan"
        if details is None:
            DRPSINGLE.selects_from_single_selection_dropdown(route_plan, "random")
        else:
            if details.get("routePlan") is not None:
                DRPSINGLE.selects_from_single_selection_dropdown(route_plan, details['routePlan'])
            else:
                DRPSINGLE.selects_from_single_selection_dropdown(route_plan, "random")
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)

    def select_customer_type_for_collection(self, details):
        """ Function to select customer type in collection add page """
        cust_type = "Customer Type"
        if details is None:
            DRPSINGLE.selects_from_single_selection_dropdown(cust_type, "random")
        else:
            if details.get("customerType") is not None:
                DRPSINGLE.selects_from_single_selection_dropdown(cust_type, details['customerType'])
            else:
                DRPSINGLE.selects_from_single_selection_dropdown(cust_type, "random")
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)

    def select_customer_for_collection(self, details):
        """ Function to select customer in collection add page """
        if details is None:
            self.select_from_multi_selection_dropdown("Customer", "random")
        else:
            if details.get("customer") is not None:
                self.select_from_multi_selection_dropdown("Customer", details['customer'])
            else:
                self.select_from_multi_selection_dropdown("Customer", "random")
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)

    def select_payment_mode(self, details):
        """ Function to select payment mode """
        if details is None:
            payment_mode = DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.payment_mode, "random")
        else:
            if details.get("paymentMode") is not None:
                payment_mode = DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.payment_mode, details['paymentMode'])
            else:
                payment_mode = DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.payment_mode, "random")
        print("payment_mode = ", payment_mode)
        BuiltIn().set_test_variable("${payment_mode}", payment_mode)
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)

    def select_bank(self, details):
        """ Function to select bank """
        if details is None:
            DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.bank, "random")
        else:
            if details.get("bank") is not None:
                DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.bank, details['bank'])
            else:
                DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.bank, "random")
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)

    def select_ewallet(self, details):
        """ Function to select e-wallet """
        if details is None:
            DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.ewallet, "random")
        else:
            if details.get("ewallet") is not None:
                DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.ewallet, details['ewallet'])
            else:
                DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.ewallet, "random")
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)

    def select_date(self, details):
        """ Function to select bank """
        if details is None:
            date = "random"
        else:
            if details.get("date") is not None:
                date = details['date']
            else:
                date = "random"
        self.selects_date_from_calendar_using_path(date, self.locator.date)

    def get_payment_amount(self, details):
        rand_amt = secrets.randbelow(100)
        if details is None:
            pay_amt = rand_amt
        else:
            if details.get("paymentAmount") is not None:
                pay_amt = details['paymentAmount']
            else:
                pay_amt = rand_amt
        return pay_amt

    def get_reference_no(self, details):
        rand_ref_no = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4))
        if details is None:
            ref_no = rand_ref_no
        else:
            if details.get("referenceNo") is not None:
                ref_no = details['referenceNo']
            else:
                ref_no = rand_ref_no
        return ref_no

    def upload_ewallet_receipt(self, details):
        if details is not None:
            if details.get("receipt") is not None:
                file = details['receipt']
                FILEUPLOAD.search_specific_file(file)
            else:
                FILEUPLOAD.search_random_file("jpg")
        FILEUPLOAD.choose_the_file_to_upload()
        TEXTFIELD.insert_into_field_with_length("File Description", "random", 6)
        BUTTON.click_button("Ok")

    @keyword("user validates new generated ${item} added")
    def validate_new_generated_open_item_added(self, item):
        if item == "invoice":
            item_no = BuiltIn().get_variable_value("${inv_no}")
        elif item == "debit note":
            item_no = BuiltIn().get_variable_value("${dn_no}")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.expand_collection)
        status = LABEL.return_visibility_status_for(item_no)
        if status:
            print("{0} is added in the collection".format(item_no))
        else:
            raise ValueError("{0} is not added in the collection".format(item_no))

    @keyword("user validates update amount reallocate")
    def validate_update_amount_reallocate(self):
        amt = COMMON_KEY.wait_keyword_success("get_text", self.locator.outstanding_amt)
        print("out amt = ", amt)
        TEXTFIELD.insert_into_field("Cash", amt)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.expand_collection)
        total_num_row = int(self.selib.get_element_count("//*[contains(text(),'Doc. Number')]/following::*//tr"))
        print("ttl num row = ", total_num_row)
        i = 1
        total_amt = 0
        while i <= total_num_row:
            cash_locator = self.locator.open_item_cash.format(i)
            cash = self.selib.get_text(cash_locator)
            cash = float(cash)
            total_amt += cash
            i += 1

        if amt == total_amt:
            print("Amount is reallocated")
        else:
            raise ValueError("Amount is not reallocated")

    @keyword("user validates adjustment in edit mode")
    def validate_adjustment_button(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.checkbox.format("Customer Wise"))

    @keyword("user validates open item list")
    def validate_open_item_list(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.expand_collection)
        total_num_row = int(self.selib.get_element_count("//*[contains(text(),'Doc. Number')]/following::*//tr"))
        print("ttl num row = ", total_num_row)
        i = 1
        date_list = []
        while i <= total_num_row:
            date_locator = self.locator.doc_date.format(i)
            date_string = self.selib.get_text(date_locator)
            date = datetime.datetime.strptime(date_string, "%b %d, %Y").strftime("%d/%m/%Y")
            date_list.append(date)
            i += 1
        flag = 0
        count = 1
        while count < len(date_list):
            if date_list[count] < date_list[count - 1]:
                flag = 1
            count += 1
        if not flag:
            print("Open item listed in ascending order by date")
        else:
            raise ValueError("Open item is not listed in ascending order by date")

    @keyword("user applies collection header")
    def apply_collection_header(self):
        CollectionListPage().click_add_collection_button()
        details = BuiltIn().get_variable_value("${ColDetails}")
        self.select_route_for_collection(details)
        self.select_customer_for_collection(details)
        BUTTON.click_button("Apply")

    @keyword("user ${action} collection with ${type} data")
    def create_collection(self, action, type):
        details = BuiltIn().get_variable_value("${ColDetails}")
        if details is not None:
            if details.get("cashAmount") is not None:
                cash_amt = details['cashAmount']
            else:
                cash_amt = 1
        else:
            cash_amt = 1
        outstanding_amt = COMMON_KEY.wait_keyword_success("get_text", self.locator.outstanding_amt)
        print("out amt = ", outstanding_amt)
        print("cash amt = ", cash_amt)
        TEXTFIELD.insert_into_field("Cash", cash_amt)
        self.add_payment(details)
        BUTTON.click_button("Save")
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)
        col_no = self.selib.get_text(self.locator.first_collection_no)
        print("Col no = ", col_no)
        BuiltIn().set_test_variable("${col_no}", col_no)

    def add_payment(self, details):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.other_payment)
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)
        self.select_payment_mode(details)
        payment_mode = self.builtin.get_variable_value("${payment_mode}")
        print("pay amt = ", self.get_payment_amount(details))
        COMMON_KEY.wait_keyword_success("input_text", self.locator.amount, self.get_payment_amount(details))
        COMMON_KEY.wait_keyword_success("input_text", self.locator.ref_no, self.get_reference_no(details))
        self.select_date(details)
        if payment_mode == "E-wallet":
            self.select_ewallet(details)
            self.upload_ewallet_receipt(details)
        else:
            self.select_bank(details)
        BUTTON.click_button("Save")
        status = LABEL.return_visibility_status_for("Setting Payment Mode")
        print("status 1=", status)
        while status:
            status = LABEL.return_visibility_status_for("Setting Payment Mode")
            print("status in=", status)

    @keyword("user uploads ${type} file with ${size} size for e-wallet receipt")
    def uploads_receipt(self, type, size):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.other_payment)
        self.selib.wait_until_element_is_not_visible(CollectionListPage().locator.load_image)
        DRPSINGLE.select_from_single_selection_dropdown_using_path(self.locator.payment_mode, "E-wallet")
        if size == "invalid":
            file = "motivational_video.mp4"
        else:
            if type == "valid":
                file = "test.jpg"
            else:
                file = "images.jfif"
        FILEUPLOAD.search_specific_file(file)
        FILEUPLOAD.choose_the_file_to_upload()
        if type == "valid":
            BUTTON.click_button("Ok")
            BUTTON.click_button("Cancel")

    def close_payment_pop_up(self):
        POPUPMSG.click_button_on_pop_up_msg()
        BUTTON.click_button("Cancel")

    def select_from_multi_selection_dropdown(self, label, choice):
        COMMON_KEY.wait_keyword_success("click_element",
                                      "//*[contains(text(),'{0}')]/following::nz-select[4]".format(label))
        if choice == 'all' or choice == "random":
            selection_list = self.selib.get_webelements("//*[@class='cdk-overlay-pane']//following-sibling::li")
        else:
            selection_list = choice.split(",")
        for element in selection_list:
            if choice == 'random':
                select = secrets.choice(range(1, 3))
            else:
                select = 1
            if choice == 'random' or choice == 'all':
                text = self.selib.get_text(element)
            else:
                text = self.builtin.set_variable(element)
            if select == 1:
                COMMON_KEY.wait_keyword_success("click_element",
                            "//*[@class='cdk-overlay-pane']//following-sibling::*[contains(text(),'{0}')]".format(text))
        COMMON_KEY.wait_keyword_success("press_keys", None, "ESC")

    def selects_date_from_calendar_using_path(self, date, path):
        choose_date = CALENDAR.validate_and_return_date(date)
        COMMON_KEY.wait_keyword_success("click_element", path)
        self.selib.input_text("//calendar-input//input", choose_date)
        try:
            COMMON_KEY.wait_keyword_success("click_element",
                                          "//date-table//td[contains(@class, 'ant-calendar-selected-day')]")
        except Exception as e:
            print(e.__class__, "occured")
            COMMON_KEY.wait_keyword_success("press_keys", None, "RETURN")
        return choose_date
