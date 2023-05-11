from robot.api.deco import keyword
from PageObjectLibrary import PageObject
from resources.Common import Common
from robot.libraries.BuiltIn import BuiltIn
from resources.web import TEXTFIELD, DRPSINGLE, BUTTON, RADIOBTN, CALENDAR, DRPMULTIPLE, FILEUPLOAD
from resources.web.Merchandising.MerchandisingSetup.AuditActivity import AuditActivityListPage
import secrets

class AuditActivityAddPage(PageObject):
    PAGE_TITLE = "Merchandising / Activity Setup / Audit"
    PAGE_URL = "/merchandising/activity-audit"
    SETUP_DETAILS="${setup_details}"
    BRAND_CODE = "Brand Code"
    BRAND_DESC = "Brand Description"
    ACT_SETUP = "Activity Setup"
    _locators = {
        "load_image": "//div[@class='loading-text']//img",
        "FirstCheckBox": "(//*[@nz-checkbox=''])[2]",
        "PriceAuditFirstCheckBox": "(//*[@nz-checkbox=''])[3]",
        "DistCheckFirstCheckBox": "(//*[@nz-checkbox=''])[5]",
        "LevelDropDown": "//*[contains(text(),'Price Audit')]/following::nz-select[1]",
        "ProductType" : "//tr[1]//td[4]//nz-select",
        "ProductPrice": "//tr[1]//td[5]//input",
        "ProductMinPrice": "//tr[1]//td[6]//input",
        "ProductMaxPrice": "//tr[1]//td[7]//input",
        "FirstPrdTypeSelection" : "(//*[@class='cdk-overlay-pane']//following-sibling::li[@nz-option-li=''])[1]"
    }

    @keyword('user creates audit activity using ${data_type} data')
    def user_creates_audit_activity_with_data(self, data_type):
        AuditActivityListPage.AuditActivityListPage().click_add_audit_activity_button()
        audit_desc = self.user_inserts_audit_desc()
        BuiltIn().set_test_variable("${audit_desc}", audit_desc)
        self.select_start_date_for_audit()
        self.select_end_date_for_audit()
        self.select_store_space_for_audit()
        self.select_category_for_audit()
        BUTTON.click_button("Save")

    def click_assign_facing_audit_activity_button(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Assign")
        self._wait_for_page_refresh()

    def click_apply_activity_button(self):
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Apply")
        self._wait_for_page_refresh()

    def user_add_facing_audit_activity(self):
        self.user_click_on_activity_setup_tab(self.ACT_SETUP)
        AuditActivityListPage.AuditActivityListPage().click_add_audit_activity_button()
        Common().wait_keyword_success("click_element", self.locator.FirstCheckBox)
        self.click_assign_facing_audit_activity_button()

    def user_add_price_audit_activity(self):
        self.user_click_on_activity_setup_tab(self.ACT_SETUP)
        self.user_click_on_activity_setup_tab("Price Audit")
        AuditActivityListPage.AuditActivityListPage().click_add_audit_activity_button()
        self.select_price_audit_product_level_drop_down()
        Common().wait_keyword_success("click_element", self.locator.PriceAuditFirstCheckBox)
        Common().wait_keyword_success("click_element", self.locator.ProductType)
        Common().wait_keyword_success("click_element", self.locator.FirstPrdTypeSelection)
        number = secrets.randint(10, 20)
        Common().wait_keyword_success("input_text", self.locator.ProductPrice, number)
        Common().wait_keyword_success("input_text", self.locator.ProductMinPrice, number)
        Common().wait_keyword_success("input_text", self.locator.ProductMaxPrice, number)
        self.click_apply_activity_button()

    def user_add_promo_compliance_activity(self):
        self.user_click_on_activity_setup_tab(self.ACT_SETUP)
        self.user_click_on_activity_setup_tab("Promotion Compliance")
        number = secrets.choice(range(100, 1000))
        Common().wait_keyword_success("input_text", "//tr//td[2]//input", number)
        date = CALENDAR.validate_and_return_date("today")
        Common().wait_keyword_success("click_element", "//tr//td[4]//input")
        Common().wait_keyword_success("input_text", "//calendar-input//input", date)
        Common().wait_keyword_success("press_keys", None, "RETURN")
        date = CALENDAR.validate_and_return_date("next day")
        Common().wait_keyword_success("click_element", "//tr//td[5]//input")
        Common().wait_keyword_success("input_text", "//calendar-input//input", date)
        Common().wait_keyword_success("press_keys", None, "RETURN")
        Common().wait_keyword_success("input_text", "//tr//td[3]//input", number)
        Common().wait_keyword_success("click_element", "//tr//td[6]//nz-select")
        DRPSINGLE.select_first_selection()
        BUTTON.click_button("Save")

    def user_add_distribution_check_activity(self):
        self.user_click_on_activity_setup_tab(self.ACT_SETUP)
        self.user_click_on_activity_setup_tab("Distribution Check")
        AuditActivityListPage.AuditActivityListPage().click_add_audit_activity_button()
        Common().wait_keyword_success("click_element", self.locator.DistCheckFirstCheckBox)
        Common().wait_keyword_success("click_element", self.locator.ProductType)
        Common().wait_keyword_success("click_element", self.locator.FirstPrdTypeSelection)
        self.click_apply_activity_button()

    def user_add_planogram_activity(self):
        self.user_click_on_activity_setup_tab(self.ACT_SETUP)
        self.user_click_on_activity_setup_tab("Planogram")
        AuditActivityListPage.AuditActivityListPage().click_add_audit_activity_button()
        TEXTFIELD.inserts_into_field_with_length("Planogram description", "letter", 10)
        self.upload_random_jpg_to_planogram()
        self.click_apply_activity_button()

    def upload_random_jpg_to_planogram(self):
        FILEUPLOAD.search_random_file("jpg")
        FILEUPLOAD.choose_the_file_to_upload()
        TEXTFIELD.insert_into_field_with_length("File Description", "random", 6)
        BUTTON.click_button("Ok")

    def select_price_audit_product_level_drop_down(self):
        Common().wait_keyword_success("click_element", self.locator.LevelDropDown)
        DRPSINGLE.select_first_selection()

    def user_updates_audit_activity_desc(self):
        self.user_inserts_audit_desc()
        BUTTON.click_button("Save")

    def user_click_on_activity_setup_tab(self, label):
        Common().wait_keyword_success("click_element",
                                      "//*[@role='tab']/*[contains(text(),'{0}')]".format(label))
        self._wait_for_page_refresh()

    @keyword('user back to listing page')
    def click_cancel_audit_activity_button(self):
        """ Function to click cancel and back to Audit activity listing page"""
        self.selib.wait_until_element_is_not_visible(self.locator.load_image)
        BUTTON.click_button("Cancel")
        self._wait_for_page_refresh()

    def select_store_space_for_audit(self):
        audit_given = BuiltIn().get_variable_value("${AuditDetails['StoreSpace']}")
        if audit_given is not None:
            DRPMULTIPLE.select_from_multi_selection_dropdown("Store Space", audit_given)
        else:
            DRPMULTIPLE.select_from_multi_selection_dropdown("Store Space", "random")

    def select_category_for_audit(self):
        audit_given = BuiltIn().get_variable_value("${AuditDetails['Category']}")
        if audit_given is not None:
            DRPMULTIPLE.select_from_multi_selection_dropdown("Category", audit_given)
        else:
            DRPMULTIPLE.select_from_multi_selection_dropdown("Category", "random")

    def select_start_date_for_audit(self):
        audit_given = BuiltIn().get_variable_value("${AuditDetails['StartDate']}")
        if audit_given is not None:
            start_date = CALENDAR.selects_date_from_calendar("Start date", audit_given)
        else:
            start_date = CALENDAR.selects_date_from_calendar("Start date", "next day")
        return start_date

    def select_end_date_for_audit(self):
        audit_given = BuiltIn().get_variable_value("${AuditDetails['EndDate']}")
        if audit_given is not None:
            end_date = CALENDAR.selects_date_from_calendar("End date", audit_given)
        else:
            end_date = CALENDAR.selects_date_from_calendar("End date", "greater day")
        return end_date

    def create_fixed_data_setup(self):
        setup = BuiltIn().get_variable_value(self.SETUP_DETAILS)
        DRPSINGLE.selects_from_single_selection_dropdown("Category", setup['category'])
        TEXTFIELD.insert_into_field(self.BRAND_CODE, setup['brand_code'])
        TEXTFIELD.insert_into_field(self.BRAND_DESC, setup['brand_desc'])
        RADIOBTN.select_from_radio_button("Type", setup['type'])

    def user_inserts_audit_desc(self):
        """ Function to insert warehouse code with random/fixed data """
        audit_details_given = BuiltIn().get_variable_value("&{AuditDetails['AUDIT_DESC']}")
        if audit_details_given is not None:
            audit_desc = TEXTFIELD.insert_into_field("Audit Description", audit_details_given['AUDIT_DESC'])
        else:
            audit_desc = TEXTFIELD.insert_into_field_with_length("Audit Description", "random", 15)
        return audit_desc


