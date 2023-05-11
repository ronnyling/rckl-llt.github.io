from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn


class MyContactsListPage(PageObject):
    PAGE_TITLE = ""
    PAGE_URL = "/setting-ui/whatsapp"

    _locators = \
        {
            "EntityDistDefault": "//label[contains(text(),'Entity')]/following::*//div[@title='Sales Person']",
            "EntityHQDefault": "//label[contains(text(),'Entity')]/following::*//div[@title='Distributors']",
            "EntityBlank": "//div[@class='cdk-overlay-backdrop nz-overlay-transparent-backdrop cdk-overlay-backdrop-showing']",
            "Search": "//button[@class='ant-btn ng-star-inserted ant-btn-icon-only']",
            "SearchInput": "(//*[text()='My Contacts']/following::*//tr[@class='inline-filter ant-table-row ng-star-inserted']//input[@type='text'])[1]",
            "WhatsAppNoCol": "//td[7]//core-cell-render[1]//div[1]//div[1]",
            "WhatsAppButton": "//td[8]//div[1]//span[1]//core-button[1]",
            "Distributor": "//label[contains(text(),'Distributor')]",
            "DistributorInput": "//input[@placeholder='Enter Code / Name']",
        }

    data = BuiltIn().get_variable_value("&{whatsapp_data}")
    timeout = "0.2 min"
    wait = "3 sec"
    divcontains = "//div[contains(text(),'%s')]"

    def wait_till_loading_icon_done(self):
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")

    # Distributor user
    def user_verifies_Entity_default_for_distributor(self):
        self.wait_till_loading_icon_done()
        self.selib.wait_until_element_is_visible(self.locator.EntityDistDefault)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "input_text",
                                                 self.locator.SearchInput, MyContactsListPage.data.get('SalesPerson_Code'))
        self.selib.wait_until_element_is_visible(self.divcontains % MyContactsListPage.data.get('SalesPerson_Code'))
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)  # closes the search bar

    def user_searches_customer_entity(self):
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.EntityDistDefault)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", "//li[contains(text(),'Customers')]")
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "input_text",
                                                 self.locator.SearchInput, MyContactsListPage.data.get('Customers_Code'))
        self.selib.wait_until_element_is_visible(self.divcontains % MyContactsListPage.data.get('Customers_Code'))
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)  # closes the search bar

    def user_verifies_contact_able_to_use_whatsapp_feature(self):
        value = self.driver.find_element_by_xpath(self.locator.WhatsAppNoCol).text
        self.builtin.should_contain(value, str(MyContactsListPage.data.get('WhatsApp_No_SalesPerson')))    # whatsapp number is read as integer
        attribute = self.selib.get_element_attribute(self.locator.WhatsAppButton, "ng-reflect-disabled")
        self.builtin.should_contain(attribute, "false")

    def user_verifies_contact_without_whatsapp_number_unable_to_use_whatsapp_feature(self):
        attribute = self.selib.get_element_attribute(self.locator.WhatsAppButton, "ng-reflect-disabled")
        self.builtin.should_contain(attribute, "true")

    # HQ user
    def user_verifies_Entity_default_for_HQ_user(self):
        self.wait_till_loading_icon_done()
        self.selib.wait_until_element_is_visible(self.locator.EntityHQDefault)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "input_text",
                                                 self.locator.SearchInput, MyContactsListPage.data.get('Distributor_Code'))
        attribute = self.selib.get_element_attribute(self.locator.WhatsAppButton, "ng-reflect-disabled")
        self.builtin.should_contain(attribute, "true")
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)

    def user_verifies_Sales_Person_field_able_to_filtered_by_Distributor_column(self):
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.EntityHQDefault)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 "(//li[contains(text(),'Sales Person')])[2]")
        self.wait_till_loading_icon_done()
        self.selib.wait_until_page_does_not_contain_element(self.locator.WhatsAppNoCol)     # make sure list turn blank when switching Entity
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "input_text",
                                                 self.locator.DistributorInput, MyContactsListPage.data.get('Distributor_Code'))
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 self.divcontains % MyContactsListPage.data.get('Distributor_Code'))
        self.wait_till_loading_icon_done()
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "input_text",
                                                 self.locator.SearchInput, MyContactsListPage.data.get('SalesPerson_Code'))
        self.selib.wait_until_element_is_visible(self.divcontains % MyContactsListPage.data.get('SalesPerson_Code'))
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Search)
        attribute = self.selib.get_element_attribute(self.locator.WhatsAppButton, "ng-reflect-disabled")
        self.builtin.should_contain(attribute, "false")

    def user_clicks_on_header_contact_icon_after_landing_at_main_page(self):
        self.wait_till_loading_icon_done()
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element",
                                                 "//body/div[@class='basic-container']/app-root/core-top-frame/div[@class='main-container']"
                                                 "/nz-layout[@class='ant-layout ant-layout-has-sider']/nz-content[@class='ant-layout-content']"
                                                 "/core-app-header/div[@class='header-bar first-header-bar']/core-button[@class='mr-3 icon pointer']"
                                                 "/span/i[@class='anticon anticon-contacts ng-star-inserted']/*[1]")
        self.wait_till_loading_icon_done()
