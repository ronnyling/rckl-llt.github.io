from PageObjectLibrary import PageObject
from robot.api.deco import keyword
from resources.web.MasterDataMgmt.PromotionMgmt.Promotion import PromotionListPage #PromotionAsgnPage
from resources.web.CustTrx.SalesInvoice import SalesInvoiceAddPage
from resources.web import DRPSINGLE, TEXTFIELD, CALENDAR, RADIOBTN, TOGGLE, COMMON_KEY, LABEL
from setup.csvreader import CsvLibrary
from robot.libraries.BuiltIn import BuiltIn
from setup.hanaDB import HanaDB
import datetime
import secrets
import string
import time
import json

NOW = datetime.datetime.now()


class PromotionAddPage(PageObject):
    PAGE_TITLE = "Master Data Management / Promotion Management / Promotion"
    Page_URL = "/promotion/NEW"

    # locator with xpath for elements that are reusable only in Promotion module.
    _locators = \
        {
            "Add": "//span[contains(text(),'Add')]/parent::button[1]",
            "Category": "//label[text()='Category']//following::*[2]//nz-select//input",
            "Save": "//span[contains(text(),'Save')]/parent::button[1]",
            "Cancel": "//span[contains(text(),'Cancel')]/parent::button[1]",

            # Scheme Options
            "CombiBox": "//span[contains(text(),'Combi')]//preceding-sibling::span[@class='ant-checkbox']",
            "FOCrecurringBox": "//span[contains(text(),'FOC Recurring')]//preceding-sibling::span[@class='ant-checkbox']",
            "SpaceBuyPayoutBox": "//span[contains(text(),'Space Buy Payout- Customer Specific')]//preceding-sibling::span[@class='ant-checkbox']",
            "QPSBox": "//span[contains(text(),'QPS')]//preceding-sibling::span[@class='ant-checkbox']",
            "MRPbox": "//span[contains(text(),'Promotion by MRP')]//preceding-sibling::span[@class='ant-checkbox']",
            "POSMAsgnBox": "//span[contains(text(),'POSM Assignment')]//preceding-sibling::span[@class='ant-checkbox']",

            # Product Assignment
            "ProductAssignmentPanel": "//nz-collapse-panel[@ng-reflect-nz-header='Product Assignment']",
            # Assign Product
            "AssignPrdSearch": "//button[@class='ant-btn ng-star-inserted ant-btn-default ant-btn-icon-only']",
            "AssignPrdSearchField": "(//*[text()='Select Product']/following::*//tr[@class='inline-filter ant-table-row ng-star-inserted']//input[@type='text'])[1]",
            "AssignPrdAdd": "//*[text()='Select Product']/following::*//span[contains(text(),'Add')]/parent::button[1]",

            # Promotion Details
            "Range": "//span[contains(text(),'Range')]//parent::*[1]//parent::label[@class='ant-checkbox-wrapper ng-star-inserted']",
            "ForEvery": "//span[contains(text(),'For Every')]//parent::*[1]//parent::label[@class='ant-checkbox-wrapper ng-star-inserted']",
            "ProRata": "//span[contains(text(),'Pro Rata')]//parent::*[1]//parent::label[@class='ant-checkbox-wrapper ng-star-inserted']",
            "Manual": "//span[contains(text(),'Manual')]//ancestor::*[1]//span//input[@class='ant-radio-input']",
            "ByQuantity": "//span[contains(text(),'By Quantity')]//ancestor::*[1]//span//input[@class='ant-radio-input']",
            "ByAmountText": "//span[contains(text(),'By Amount')]",
            "TotalBuyTextBox": "//label[contains(text(),'Total Buy :')]//following::*[1]//child::*[1]",
            "DiscountPercent": "(//label[contains(text(),', Discount (%) :')]//following::*[1]//child::*[1])",
            "DiscountRate": "(//label[contains(text(),', Discount ($) :')]//following::*[1]//child::*[1])",
            "MinBuyTextBox": "(//label[contains(text(),'Min Buy :')]//following::*[1]//child::*[1])",
            "FreeProduct": "//span[contains(text(),'Free Product')]",
            "DiscountByValue": "//span[contains(text(),'Discount by Value')]",
            "DiscountByPercent": "//span[contains(text(),'Discount by %')]",
            "Free": "(//label[contains(text(),'Free')]//following::*[1]//child::*[1])",

            # FOC product link
            "FOCproduct": "//div[contains(text(),'Please select product')]",
            "SelectFOCproduct": "//div[contains(text(),'Select FOC product')]",
            "LevelDropdown": '//*[contains(text(), "Level:")]/following::nz-select',
            "FocUpdateButtons": "//*[text()='Add FOC Product']/following::*//core-button[@ng-reflect-label='Update']",
            "FocAsgnButtons": "//*[text()='Add FOC Product']/following::*//core-button[@ng-reflect-label='Assign']",
            "FOCSearchResultCheckBox": "//*[text()='Add FOC Product']/following::*//tr[@row-index='0']//*[@class='ant-checkbox']",
            "FOCsearchText": "(//*[text()='Add FOC Product']/following::*//tr[@class='inline-filter ant-table-row ng-star-inserted']//input[@type='text'])[1]",
            # Group product link    # some shared with FOC product link
            "GroupProduct": "(//span[contains(text(),'Select Group Product')])",
            "GroupProductLevel": "//label[contains(text(),'Level')]//following::*//nz-select",
            "SearchIcon": "//button[@class='ant-btn ng-star-inserted ant-btn-icon-only']",
            "AssignedProduct": "//div[contains(text(),'Assigned Product')]",
            "SearchTextField": "(//*[text()='Add Product']/following::*//tr[@class='inline-filter ant-table-row ng-star-inserted']//input[@type='text'])[1]",
            "CoreButtons": "//*[text()='Add Product']/following::*//core-button[@ng-reflect-label='",   # requires enclosing ]" when implementing
            "SearchResultCheckBox": "//*[text()='Add Product']/following::*//tr[@row-index='0']//*[@class='ant-checkbox']",

            # MRP assignment link
            "MRPassignmentlink": "//div[contains(text(),'MRP Assignment')]",
            "MRPassignbutton": "//span[contains(text(),'Assign')]/parent::button[1]",

            # Slab controls
            "AddMainSlab": "(//label[contains(text(),'Total Buy :')]//preceding::*[1]//preceding::*[1]//parent::*[1])",
            "DeleteMainSlab": "(//label[contains(text(),'Total Buy :')]//preceding::*[2])[2]",
            "AddSubSlab": "(//label[contains(text(),'Group Id :')]//preceding::*[1]//preceding::*[1]//parent::*[1])",
            "DeleteSubSlab": "(//label[contains(text(),'Group id :')]//preceding::*[2])[2]",

            "all_custom_slider": '//*[contains(text(),"Distributor(s)")]/preceding::button//*[contains(text(), "Custom")]',
            "Assignment": "//span[contains(text(),'Assignment')]",
        }     # contains elements that are not locatable with common reference

    _attributeNames = \
        {
            "isDisabled": "ng-reflect-nz-disabled",
            "disability": "ng-reflect-is-disabled"
        }

    timeout = "0.2 min"
    wait = "3 sec"
    contain = '//li[contains(text()'
    span_contain = '//span[contains(text(),'

    def wait_till_loading_icon_done(self):
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")

    def get_scheme_options(self, data):
        return data.get('Scheme Options')

    def __init__(self):
        super().__init__()
        self.PromotionDict = {}

    ### Testcase definitions ###

    def user_setup_new_promotion_with(self, data, randomize=None):   # variable randomize defaults to Null if nothing passed in when calling the method.
        self.click_Add_button_at_list_page()
        data_details = self.provide_general_info(data, randomize)
        print("Scenario: ", data.get('Scenario'))
        print("Scheme Options: ", self.get_scheme_options(data))

        if self.get_scheme_options(data) == "Combi":
            self.select_combi_scheme_options()
        elif self.get_scheme_options(data) == "POSM Assignment":
            self.select_posm_scheme_options()
            self.product_assignment(data)
        else:
            self.product_assignment(data)   # non Combi promotion needs to assign product before going to promotion details.
            if (data.get("MRP")).lower() == "yes":
                self.select_MRP_scheme_options()
                self.assign_product_mrp(data)
        self.promotion_details(data)
        self.save_promotion()

        promo_code = BuiltIn().get_variable_value("${Promotion_Code}")

        HanaDB.HanaDB().connect_database_to_environment()
        HanaDB.HanaDB().database_data_comparing("SELECT * FROM PROMO WHERE PROMO_CD = '{0}'".format(promo_code), data_details)
        HanaDB.HanaDB().disconnect_from_database()
        newdict = {data.get('Scenario'): promo_code}
        self.PromotionDict.update(newdict)
        newdict = json.dumps(self.PromotionDict)
        BuiltIn().set_test_variable("${Promotion_Dict}", newdict)
        print("Scenario name and promo code ", newdict)

    # sending full list of data read from file to test case
    @keyword("user performs new promotion setup with list of data ${condition}")
    def user_setup_new_promotion_with_collection(self, condition=None, dictionary_list=None, randomize=None):  # handles for list/dictionary of dictionaries that keep different scenarios data.
        promolistpageobject = PromotionListPage.PromotionListPage()
        promoasgnpageobject = PromotionAsgnPage.PromotionAsgnPage()
        invoiceaddpageobject = SalesInvoiceAddPage.SalesInvoiceAddPage()
        invoicedata = {}
        if dictionary_list is None:
            dictionary_list = self.builtin.get_variable_value("&{file_data}")
        if condition == "and validate through invoice":
            csvobject = CsvLibrary.CsvLibrary()
            invoicedata = csvobject.retrieve_test_data("InvoiceData.csv", "CustTrx")

        for key in dictionary_list:
            print("Datasets in the list: ", key)
            self.user_setup_new_promotion_with(dictionary_list.get(key), randomize)
            self.user_back_to_list_page_from_view()
            promolistpageobject.user_searches_newly_created_promotion()
            promoasgnpageobject.assignment_tab_settings_distributor_customer_attribute(dictionary_list.get(key))
            promolistpageobject.user_approve_current_promotion()

            if condition == "and validate through invoice":     # find only specific key to run
                invoiceaddpageobject.user_creates_new_invoice_with(invoicedata.get('Combi AMT FOC OR'), "with new promotion")

    @keyword("user clicks Add button on Listing page")
    def click_Add_button_at_list_page(self):
        PromotionListPage.PromotionListPage().click_add_product_button()  # this method is from Promotion List Page

    ### Reusable function components in Add Promotion page ###

    def get_promo_code(self, data):
        return data.get('Promotion Code')

    def get_promo_desc(self, data):
        return data.get('Promotion Description')

    def get_claimable_percent(self, data):
        return data.get('Claimable Percentage')

    def get_promo_start_date(self, data):
        return data.get('Promotion Start Date')

    def provide_general_info(self, data, randomize=None):
        print(randomize)
        promotion_code = None
        promotion_desc = None
        promo_code = 'Promotion Code'
        promo_desc = 'Promotion Description'
        promo_date = 'Promotion Start Date'
        promo_budget = 'Promotion Budget'
        promo_end = 'Promotion End Date'
        promo_status = 'Promotion Status'
        claimable = 'Claimable'
        claimable_percent = 'Claimable Percentage'
        claimable_type = 'Claimable Type'
        claimable_deadline = 'Claim Submission Deadline'
        data_details = {
            "PROMO_CD": promo_code,
            "PROMO_DESC": promotion_desc
        }

        if randomize is None:
            promotion_code = self.get_promo_code(data) + ''.join(secrets.choice(string.ascii_lowercase) for _ in range(10))
            promotion_desc = self.get_promo_desc(data)
            TEXTFIELD.insert_into_field(promo_code, promotion_code)
            TEXTFIELD.insert_into_field(promo_desc, promotion_desc)
            DRPSINGLE.selects_from_single_selection_dropdown('Type', data.get('Type'))  # use get() to return a default value in case of missing key, that default value is None.
            DRPSINGLE.selects_from_single_selection_dropdown('Category', data.get('Category'))
            if self.get_promo_start_date(data) != "" or self.get_promo_start_date(data) == "today":
                CALENDAR.select_date_from_calendar(promo_date, "today")  # the format for calendar element is (abbreviated_month day, year).
            else:
                CALENDAR.select_date_from_calendar(promo_date, self.get_promo_start_date(data))
            TEXTFIELD.insert_into_field(promo_budget, data.get(promo_budget))
            CALENDAR.select_date_from_calendar(promo_end, data.get(promo_end))  # try not to cluster calendar element one after another, to avoid invalid element state.
            RADIOBTN.select_from_radio_button(promo_status, data.get(promo_status))     # take note when Selenium session is running, the radio buttons may not have default selection enabled.
            claim_data = True
            if data.get(claimable) == "FALSE":
                claim_data = False
            claim_toggle = TOGGLE.switch_toggle(claimable, claim_data)
            if claim_toggle:
                claim_perc = TEXTFIELD.insert_into_field(claimable_percent, data.get(claimable_percent))
                DRPSINGLE.selects_from_single_selection_dropdown(claimable_type, data.get(claimable_type))
                CALENDAR.select_date_from_calendar(claimable_deadline, data.get(claimable_deadline))

                details = {
                    "CLAIMABLE_IND": claim_toggle,
                    "CLAIMABLE_PERC": round(claim_perc, 6)
                }
                data_details.update(details)
        elif randomize is not None:
            promotion_code = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(7))
            promotion_desc = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(10))
            TEXTFIELD.insert_into_field(promo_code, promotion_code)
            TEXTFIELD.insert_into_field(promo_desc, promotion_desc)
            DRPSINGLE.selects_from_single_selection_dropdown('Type', 'random')
            DRPSINGLE.selects_from_single_selection_dropdown('Category', 'random')
            CALENDAR.select_date_from_calendar(promo_date, "today")
            TEXTFIELD.insert_into_field(promo_budget, str(secrets.randbelow(9999)))
            CALENDAR.select_date_from_calendar(promo_end, 'random')
            RADIOBTN.select_from_radio_button(promo_status, 'random')

        BuiltIn().set_test_variable("${Promotion_Code}", promotion_code)
        BuiltIn().set_test_variable("${Promotion_Description}", promotion_desc)

        return data_details

    def save_promotion(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Save)
        self.wait_till_loading_icon_done()

    @keyword("user back to list page from view/edit mode")
    def user_back_to_list_page_from_view(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Cancel)
        self._wait_for_page_refresh()   # appears will not wait for metadata loads
        self.wait_till_loading_icon_done()

    def select_combi_scheme_options(self):
        self.selib.wait_until_element_is_visible(self.locator.CombiBox)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.CombiBox)
        self.wait_till_loading_icon_done()

    def select_posm_scheme_options(self):
        self.selib.wait_until_element_is_visible(self.locator.POSMAsgnBox)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.POSMAsgnBox)
        self.wait_till_loading_icon_done()

    def select_qps_scheme_options(self):
        self.selib.wait_until_element_is_visible(self.locator.QPSBox)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.QPSBox)
        self.wait_till_loading_icon_done()

    def select_MRP_scheme_options(self):
        self.selib.wait_until_element_is_visible(self.locator.MRPbox)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.MRPbox)

    def product_assignment(self, data):     # for non Combi promotions
        checkbox = "//*[text()='Select Product']/following::*//tr[@row-index='0']//*[@class='ant-checkbox']"
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Add)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.LevelDropdown)
        COMMON_KEY.wait_keyword_success("click_element",
                                                 self.contain + ",'" + data.get('Product Level') + "')]")
        self.wait_till_loading_icon_done()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.AssignPrdSearch)
        COMMON_KEY.wait_keyword_success("input_text",
                                                 self.locator.AssignPrdSearchField, data.get('Product Assignment 1'))
        COMMON_KEY.wait_keyword_success("click_element", checkbox)
        if data.get('Product Assignment 2') != "":
            COMMON_KEY.wait_keyword_success("input_text",
                                                     self.locator.AssignPrdSearchField, data.get('Product Assignment 2'))
            COMMON_KEY.wait_keyword_success("click_element", checkbox)
        if data.get('Product Assignment 3') != "":
            COMMON_KEY.wait_keyword_success("input_text",
                                                     self.locator.AssignPrdSearchField, data.get('Product Assignment 3'))
            COMMON_KEY.wait_keyword_success("click_element", checkbox)

        COMMON_KEY.wait_keyword_success("click_element",
                                                 self.locator.AssignPrdAdd)

    def get_buy_type(self, data):
        return data.get('Buy Type')

    def get_promo_rule(self, data):
        return data.get('Promotion Rule')

    def get_disc_meth(self, data):
        return data.get('Discount Method')

    def get_foc_cond(self, data):
        return data.get('FOC Condition')

    def promotion_details(self, data):
        self.selib.wait_until_element_is_visible(self.locator.ByAmountText)     # selects whether Buy Type is by Amount or Quantity.
        COMMON_KEY.wait_keyword_success("click_element",
                                                 self.span_contain + "'" + self.get_buy_type(data) + "')]//ancestor::*[1]//span//input[@class='ant-radio-input']")
        if (self.get_buy_type(data) == 'By Quantity') and (self.get_scheme_options(data) != "Combi"):
            self.set_buy_uom(data)      # If Buy Type is Quantity AND not Combi, Buy UOM have to be defined here.
        if self.get_promo_rule(data) != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.span_contain + "'" + self.get_promo_rule(data) + "')]//parent::*[1]//parent::label[@class='ant-checkbox-wrapper ng-star-inserted']")

        # self.switch_discount_methods(data.get('Discount Method'), data)     # determines the discount methods to be applied (FOC, discount by value / %).
        self.switch_discount_methods_byif(data)

        if ((data.get("MRP")).lower() == "yes") and (self.get_scheme_options(data) == "Combi"):   # MRP set to yes with Combi promo have to assign MRP at the bottom
            self.select_MRP_scheme_options()
            self.assign_product_mrp(data)

    def switch_discount_methods(self, switchcase, data):
        switcher = \
            {
                "Free Product": self.discount_method_free_product(data),
                "Discount by Value": self.discount_method_by_value(data),
                "Discount by %": self.discount_method_by_percent(data)
            }
        func = switcher.get(switchcase, lambda: "Invalid")
        return func()

    def switch_discount_methods_byif(self, data):
        if self.get_disc_meth(data) == "Free Product":
            self.discount_method_free_product(data)
        elif self.get_disc_meth(data) == "Discount by Value":
            self.discount_method_by_value(data)
        elif self.get_disc_meth(data) == "Discount by %":
            self.discount_method_by_percent(data)

    def discount_method_free_product(self, data):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.FreeProduct)
        COMMON_KEY.wait_keyword_success("click_element", self.span_contain + "'" + self.get_foc_cond(data) + "')]")
        if self.get_foc_cond(data) == 'OR':
            self.set_foc_uom(data)
            self.selib.input_text(self.locator.Free, data.get('FOC Free 01'))   # set first FOC entitlement amount (main slab in UI)

        self.assign_foc_product(data)  # assign 1st foc product
        subslabcount = None
        count = 1

        if self.get_foc_cond(data) == 'AND':
            # AND condition will bypass the following blocks.
            pass
        elif data.get('FOC Free 02') != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab)  # click on add main slab
            self.selib.input_text(self.locator.Free + "[2]", data.get('FOC Free 02'))  # set second FOC entitlement amount (main slab in UI)
            count = 2
            # FOC product will remain same across different slabs for entitlement, hence no need to assign again
        elif data.get('FOC Free 03') != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab + "[2]")
            self.selib.input_text(self.locator.Free + "[3]", data.get('FOC Free 03'))
            count = 3

        if self.get_scheme_options(data) == 'Combi':
            # combi group
            subslabcount = self.combi_scheme_groups(data)
            # if combi: group product will remain in sync among hence no need to assign again # except the Min Buy value.
            if count > 1:       # run when main slab is more than one
                for _ in range(count-1):    # set Min Buy value for second slab, if there's 2 counts, run only 1 time
                    self.combi_scheme_groups(data, subslabcount, "slab"+str(count))
        else:
            # non combi group
            self.set_total_buy(data, count)

    def assign_foc_product(self, data):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.SelectFOCproduct)
        self.wait_till_loading_icon_done()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.LevelDropdown)
        COMMON_KEY.wait_keyword_success("click_element",
                                                 self.contain + ",'" + data.get('FOC Level') + "')]")
        self.wait_till_loading_icon_done()
        COMMON_KEY.wait_keyword_success("click_element", self.locator.SearchIcon)
        COMMON_KEY.wait_keyword_success("input_text",
                                                 self.locator.FOCsearchText, data.get('FOC Product'))
        COMMON_KEY.wait_keyword_success("click_element",
                                                 "//*[text()='Add FOC Product']/following::*//tr[@row-index='0']//*[@class='ant-checkbox']")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.FocAsgnButtons)
        if self.get_foc_cond(data) == 'AND':
            time.sleep(2)
            COMMON_KEY.wait_keyword_success("click_element",
                                                     "//*[text()='Add FOC Product']/following::*//div[contains(text(),'Select')]")
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.contain + ",'%s')]" % data.get('FOC UOM'))
            COMMON_KEY.wait_keyword_success("input_text",
                                                     "(//*[text()='Add FOC Product']/following::*//div[contains(text(),'Select')]//following::*//input)[2]", data.get('FOC Free 01'))
        COMMON_KEY.wait_keyword_success("click_element", self.locator.FocUpdateButtons)

    def combi_scheme_groups(self, data, totalsubslab=None, slab=None):    # method that reads data (before assigning group product) then add sub slabs for combi scheme
        if totalsubslab is None:
            self.selib.input_text(self.locator.MinBuyTextBox,
                                  data.get('Group Min Buy 01'))  # set entitlement requirements for group (sub slab in UI)
            self.assign_group_product(data, '01')  # assign 1st group product
            totalsubslab = 1
            if data.get('Group Min Buy 02') != "":
                COMMON_KEY.wait_keyword_success("click_element",
                                                         self.locator.AddSubSlab)  # click on add sub slab
                self.selib.input_text(self.locator.MinBuyTextBox + "[2]", data.get('Group Min Buy 02'))
                self.assign_group_product(data, '02')  # assign 2nd group product
                totalsubslab = 2
            if data.get('Group Min Buy 03') != "":
                COMMON_KEY.wait_keyword_success("click_element",
                                                         self.locator.AddSubSlab)  # click on add sub slab
                self.selib.input_text(self.locator.MinBuyTextBox + "[3]", data.get('Group Min Buy 03'))
                self.assign_group_product(data, '03')  # assign 3rd group product
                totalsubslab = 3
        else:
            # when subslab has 2 SKU products, then need find minbuy[3]&[4] for 2nd subslab
            if slab == "slab2":         # format: data.get('Group Min Buy 1 slab 2')
                for counts in range(totalsubslab):
                    self.selib.input_text(self.locator.MinBuyTextBox + "[" + str(totalsubslab + counts + 1) + "]",  # minbuy index plus counts to get the first sub slab in second group
                                          data.get("Group Min Buy "+str(counts+1)+" slab 2"))   # counts begin from 0 so need to plus 1 to corresponds to data column's name
            elif slab == "slab3":
                for counts in range(totalsubslab):
                    self.selib.input_text(self.locator.MinBuyTextBox + "[" + str(totalsubslab * 2 + counts + 1) + "]",  # minbuy indices will be doubled before counts in 3rd slab
                                          data.get("Group Min Buy "+str(counts+1)+" slab 3"))
        return totalsubslab

    group_prd_2 = 'Group Product 02'
    group_prd_3 = 'Group Product 03'

    def assign_group_product(self, data, count=None):   # method that opens Group Product link and assign product (for Combi)
        COMMON_KEY.wait_keyword_success("click_element", self.locator.GroupProduct)    # after assigning first group product, the link will change to assigned product name, hence newly added slab's group product link will be new again.
        if count == "01":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.GroupProductLevel)    # only first time assigning Group Product needs to specify Level
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.contain + ",'" + data.get('Group Level') + "')]")
            self.wait_till_loading_icon_done()
            COMMON_KEY.wait_keyword_success("click_element", self.locator.SearchIcon)
            COMMON_KEY.wait_keyword_success("input_text",
                                                     self.locator.SearchTextField, data.get('Group Product 01'))
        elif count == "02":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.SearchIcon)
            COMMON_KEY.wait_keyword_success("input_text",
                                                     self.locator.SearchTextField, data.get(self.group_prd_2))
        elif count == "03":
            COMMON_KEY.wait_keyword_success("click_element", self.locator.SearchIcon)
            COMMON_KEY.wait_keyword_success("input_text",
                                                     self.locator.SearchTextField, data.get(self.group_prd_3))

        COMMON_KEY.wait_keyword_success("click_element",
                                                 "//*[text()='Add Product']/following::*//tr[@row-index='0']//*[@class='ant-checkbox']")
        self.selib.wait_until_element_is_visible(self.locator.CoreButtons + "Assign']")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.CoreButtons + "Assign']")
        self.selib.wait_until_element_is_visible(self.locator.CoreButtons + "Update']")
        COMMON_KEY.wait_keyword_success("click_element", self.locator.CoreButtons + "Update']")

        if self.get_buy_type(data) == "By Quantity":
            self.set_buy_uom(data, count)  # for Combi, if Buy Type is Quantity, have to set Buy UOM at each groups

    def assign_product_mrp(self, data):
        render = "//div[@class='data-render ng-star-inserted'][contains(text(),'"
        holder = "//input[@placeholder='Enter Code / Name']"
        div = "//div[contains(text(),'"
        COMMON_KEY.wait_keyword_success("click_element", self.locator.MRPassignmentlink)
        COMMON_KEY.wait_keyword_success("click_element",
                                                 render + data.get('Group Product 01') + "')]")
        COMMON_KEY.wait_keyword_success("click_element", holder)
        COMMON_KEY.wait_keyword_success("click_element",
                                                 div + data.get('MRP Assignment 1') + "')]")
        if data.get(self.group_prd_2) != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     render + data.get(
                                                         self.group_prd_2) + "')]")
            COMMON_KEY.wait_keyword_success("click_element", holder)
            COMMON_KEY.wait_keyword_success("click_element",
                                                     div + data.get('MRP Assignment 2') + "')]")
        if data.get(self.group_prd_3) != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     render + data.get(
                                                         self.group_prd_3) + "')]")
            COMMON_KEY.wait_keyword_success("click_element", holder)
            COMMON_KEY.wait_keyword_success("click_element",
                                                     div + data.get('MRP Assignment 3') + "')]")

        COMMON_KEY.wait_keyword_success("click_element", self.locator.MRPassignbutton)

    per_uom = 'Per UOM'

    def discount_method_by_value(self, data):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.DiscountByValue)
        disc_val = "Discount Value Per "

        self.switch_apply_on_byif(data.get('Apply On'))
        if data.get('Apply On') == self.per_uom:
            self.apply_UOM_dropdownbox(data)    # only Apply on UOM needs assign UOM
            pertype = "UOM"
        else:
            pertype = "Product/Tier"

        self.selib.input_text(self.locator.DiscountRate, data.get(disc_val + pertype+" 1"))
        count = 1

        if data.get(disc_val + pertype + " 2") != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab)  # click on add main slab
            self.selib.input_text(self.locator.DiscountRate + "[2]", data.get(disc_val + pertype + " 2"))
            count = 2
        if data.get(disc_val + pertype + " 3") != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab + "[2]")
            self.selib.input_text(self.locator.DiscountRate + "[3]", data.get(disc_val + pertype + " 3"))
            count = 3
        if data.get(disc_val + pertype + " 4") != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab + "[3]")
            self.selib.input_text(self.locator.DiscountRate + "[4]", data.get(disc_val + pertype + " 4"))
            count = 4
        if data.get(disc_val + pertype + " 5") != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab + "[4]")
            self.selib.input_text(self.locator.DiscountRate + "[5]", data.get(disc_val + pertype + " 5"))
            count = 5

        if self.get_scheme_options(data) == 'Combi':
            subslabcount = self.combi_scheme_groups(data)
            if count > 1:
                for _ in range(count - 1):  # set Min Buy value for second slab
                    self.combi_scheme_groups(data, subslabcount, "slab" + str(count))
        else:  # non combi group
            self.set_total_buy(data, count)

    def switch_rule(self, switch):      # switch case for checking whether promotion rule is Range or otherwise.
        return \
            {
                "Range": self.locator.MinBuyTextBox,
                "others": self.locator.TotalBuyTextBox
            }[switch]

    def switch_rule_byif(self, data):
        if self.get_promo_rule(data) == 'Range':
            return self.locator.MinBuyTextBox
        else:
            return self.locator.TotalBuyTextBox

    per_prd = "Per Product"
    per_tier = "Per Tier"

    def switch_apply_on(self, switch):      # switch case for checking dicsount method by value apply on UOM, product or tier.
        return \
            {
                self.per_uom: self.apply_on_dropdownbox(self.per_uom),
                self.per_prd: self.apply_on_dropdownbox(self.per_prd),
                self.per_tier: self.apply_on_dropdownbox(self.per_tier)
            }[switch]

    def switch_apply_on_byif(self, switch):
        if switch == self.per_uom:
            self.apply_on_dropdownbox(self.per_uom)
        elif switch == self.per_prd:
            self.apply_on_dropdownbox(self.per_prd)
        elif switch == self.per_tier:
            self.apply_on_dropdownbox(self.per_tier)

    overlay = "//*[@class='cdk-overlay-pane']//following-sibling::li[contains(text(),'"

    def apply_on_dropdownbox(self, per):
        COMMON_KEY.wait_keyword_success("click_element",
                                                 "//label[contains(text(),'Apply On :')]//following::*[1]//div[contains(text(),'Select')]")
        COMMON_KEY.wait_keyword_success("input_text",
                                                 "//label[contains(text(),'Apply On :')]//following::*[1]//input",
                                                 per)
        COMMON_KEY.wait_keyword_success("click_element",
                                                 self.overlay + per + "')]")

    def apply_UOM_dropdownbox(self, data):
        COMMON_KEY.wait_keyword_success("click_element",
                                                 "//label[contains(text(),'Apply UOM :')]//following::*[1]//div[contains(text(),'DEFAULT')]")
        COMMON_KEY.wait_keyword_success("input_text",
                                                 "//label[contains(text(),'Apply UOM :')]//following::*[1]//input",
                                                 data.get('Apply UOM'))
        COMMON_KEY.wait_keyword_success("click_element",
                                                 "//li[@ng-reflect-nz-option='[object Object]']")

    def discount_method_by_percent(self, data):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.DiscountByPercent)

        self.selib.input_text(self.locator.DiscountPercent, data.get('Discount % 1'))
        count = 1
        if data.get('Buy 2') != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab)
            self.selib.input_text(self.locator.DiscountPercent + "[2]", data.get('Discount % 2'))
            count = 2
        if data.get('Buy 3') != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab + "[2]")
            self.selib.input_text(self.locator.DiscountPercent + "[3]", data.get('Discount % 3'))
            count = 3
        if data.get('Buy 4') != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab + "[3]")
            self.selib.input_text(self.locator.DiscountPercent + "[4]", data.get('Discount % 4'))
            count = 4
        if data.get('Buy 5') != "":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.locator.AddMainSlab + "[4]")
            self.selib.input_text(self.locator.DiscountPercent + "[5]", data.get('Discount % 5'))
            count = 5

        if self.get_scheme_options(data) == 'Combi':
            subslabcount = self.combi_scheme_groups(data)
            if count > 1:
                for _ in range(count - 1):  # set Min Buy value for second slab
                    self.combi_scheme_groups(data, subslabcount, "slab" + str(count))
        else:
            # non combi group
            self.set_total_buy(data, count)

    def set_total_buy(self, data, count):
        total_buy_identifier = self.switch_rule_byif(data)

        for _ in range(count):
            self.selib.input_text(total_buy_identifier + "[" + str(count) + "]", data.get('Buy ' + str(count)))

    def set_buy_uom(self, data, count=None):
        if count is None or count == "01":
            COMMON_KEY.wait_keyword_success("click_element",
                                                     "//label[contains(text(),'Buy UOM :')]//following::*[1]//div[contains(text(),'Select')]")
            COMMON_KEY.wait_keyword_success("input_text",
                                                     "//label[contains(text(),'Buy UOM :')]//following::*[1]//input",
                                                     data.get('Buy UOM'))
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.overlay + data.get(
                                                         'Buy UOM') + "')]")

        buy_uom_group_2 = 'Buy UOM group 2'
        buy_uom_group_3 = 'Buy UOM group 3'

        if (self.get_scheme_options(data) == "Combi") and (count == "01"):
            # if Combi scheme and is first round setting for Buy OUM, skip the below code
            pass
        elif ((data.get(buy_uom_group_2) != "") and (self.get_scheme_options(data) != "Combi")) or ((self.get_scheme_options(data) == "Combi") and (count == "02")):
            COMMON_KEY.wait_keyword_success("click_element",
                                                     "(//label[contains(text(),'Buy UOM :')]//following::*[1]//div[contains(text(),'Select')])[2]")
            COMMON_KEY.wait_keyword_success("input_text",
                                                     "(//label[contains(text(),'Buy UOM :')]//following::*[1]//input)[2]",
                                                     data.get(buy_uom_group_2))
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.overlay + data.get(
                                                         buy_uom_group_2) + "')]")
        elif ((data.get(buy_uom_group_3) != "") and (self.get_scheme_options(data) != "Combi")) or ((self.get_scheme_options(data) == "Combi") and (count == "03")):
            COMMON_KEY.wait_keyword_success("click_element",
                                                     "(//label[contains(text(),'Buy UOM :')]//following::*[1]//div[contains(text(),'Select')])[3]")
            COMMON_KEY.wait_keyword_success("input_text",
                                                     "(//label[contains(text(),'Buy UOM :')]//following::*[1]//input)[3]",
                                                     data.get(buy_uom_group_3))
            COMMON_KEY.wait_keyword_success("click_element",
                                                     self.overlay + data.get(
                                                         buy_uom_group_3) + "')]")

    def set_foc_uom(self, data):
        COMMON_KEY.wait_keyword_success("click_element",
                                                 "//label[contains(text(),'FOC UOM :')]//following::*[1]//div[contains(text(),'Select')]")
        COMMON_KEY.wait_keyword_success("input_text",
                                                 "//label[contains(text(),'FOC UOM :')]//following::*[1]//input", data.get('FOC UOM'))
        COMMON_KEY.wait_keyword_success("click_element",
                                                 self.overlay + data.get(
                                                     'FOC UOM') + "')]")

    # minor testcases for page UI verification purposes
    def verify_product_assignment_is_disabled_for_combi(self):
        self.select_combi_scheme_options()
        self.product_assignment_disabled()

    def verify_range_forevery_prorata_are_disabled_for_combi(self):
        self.select_combi_scheme_options()
        self.range_forevery_prorata_disabled()

    ### Page verifications section ###
    def select_disc_by_perc(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.DiscountByPercent)

    @keyword("select ${promo_type} promotion")
    def select_promotion(self, promo_type):
        DRPSINGLE.selects_from_single_selection_dropdown('Type', promo_type)

    def product_assignment_disabled(self):
        validator = "true"
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Manual)
        self.selib.wait_until_element_is_visible(self.locator.ProductAssignmentPanel)
        val = self.selib.get_element_attribute(self.locator.ProductAssignmentPanel, self._attributeNames['isDisabled'])
        self.builtin.should_contain(val, validator)
        print("Product Assignment panel disabled. ")

    def range_forevery_prorata_disabled(self):
        validator = "true"
        COMMON_KEY.wait_keyword_success("click_element", self.locator.ByQuantity)
        self.selib.wait_until_element_is_visible(self.locator.Range)
        val1 = self.selib.get_element_attribute(self.locator.Range, self._attributeNames['isDisabled'])
        self.builtin.should_contain(val1, validator)
        val2 = self.selib.get_element_attribute(self.locator.ForEvery, self._attributeNames['isDisabled'])
        self.builtin.should_contain(val2, validator)
        val3 = self.selib.get_element_attribute(self.locator.ProRata, self._attributeNames['isDisabled'])
        self.builtin.should_contain(val3, validator)
        print("Range, For Every, Prorata checkboxes disabled. ")

    def verify_group_id_is_generated_for_combi(self):
        val = self.selib.get_element_attribute("//input[@id='groupId_0_0']",'ng-reflect-model')
        self.builtin.should_contain(val, "1")
        print("Group ID is automatically generated")

    def verify_must_buy_is_aways_yes_and_disabled(self):
        val1 = self.selib.get_element_attribute("//label[contains(text(),'Must Buy')]//following::core-dropdown[1]", 'ng-reflect-model')
        self.builtin.should_contain(val1, "Yes")
        val2 = self.selib.get_element_attribute("//label[contains(text(),'Must Buy')]//following::core-dropdown[1]", 'ng-reflect-is-disabled')
        self.builtin.should_contain(val2, "true")

    def verify_foc_recurring_space_buy_qps_are_disabled(self):
        self.selib.wait_until_element_is_visible(self.span_contain + "'FOC Recurring')]"
                                                 "//preceding-sibling::span[@class='ant-checkbox ant-checkbox-disabled']")
        self.selib.wait_until_element_is_visible(self.span_contain + "'Space Buy Payout')]"
                                                 "//preceding-sibling::span[@class='ant-checkbox ant-checkbox-disabled']")
        self.selib.wait_until_element_is_visible(self.span_contain + "'QPS')]"
                                                 "//preceding-sibling::span[@class='ant-checkbox ant-checkbox-disabled']")

    def verify_combi_promo_is_disabled(self):
        self.selib.wait_until_element_is_visible(self.span_contain + "'Combi')]"
                                                 "//preceding-sibling::span[@class='ant-checkbox ant-checkbox-disabled']")

    def validate_all_custom_slider_button_is_hidden_successfully(self):
        self.selib.wait_until_page_does_not_contain_element(self.locator.all_custom_slider)

    def validate_total_number_of_distributors_hyperlink_shown_successfully(self):
        self.wait_till_loading_icon_done()
        self.builtin.wait_until_keyword_succeeds(self.timeout, self.wait, "click_element", self.locator.Assignment)
        self.selib.wait_until_page_does_not_contain_element("//div[@class='loading-text']//img")
        LABEL.validate_label_is_visible("Distributor(s)")

    def user_back_to_promotion_list_page(self):
        COMMON_KEY.wait_keyword_success("click_element", self.locator.Cancel)

    @keyword("user validates the claimable percentage field is ${status}")
    def user_validates_the_claimable_percentage_fields(self, status):
        TOGGLE.switch_toggle("Claimable", True)
        TEXTFIELD.verifies_text_field_is_visible("Claimable Percentage", status)

    @keyword("user creates '${type}' promotion with '${scheme_type}' scheme")
    def user_creates_promotion_to_validate_scheme(self, type, scheme_type):
        self.click_Add_button_at_list_page()
        self.select_promotion(type)
        user = BuiltIn().get_variable_value("${user_role}")
        if scheme_type == 'POSM Assignment' and user == 'hqadm':
            self.select_posm_scheme_options()
        if scheme_type == 'QPS':
            self.select_qps_scheme_options()

    @keyword("promotion scheme '${scheme_type}' should be ${visibility}")
    def promo_scheme_should_be(self, scheme_type, visibility):
        self.selib.wait_until_element_is_visible\
                ("//span[contains(text(),'{0}')]//preceding-sibling::span[contains(@class,'ant-checkbox')]"
                .format(scheme_type))
        val = self.selib.get_element_attribute\
                ("//span[contains(text(),'{0}')]//preceding-sibling::span[contains(@class,'ant-checkbox')]//input"
                 .format(scheme_type), self._attributeNames['disability'])
        if visibility == 'disabled':
            self.builtin.should_contain(val, 'true')
        else:
            self.builtin.should_contain(val, 'false')
