import logging

from robot.api.deco import keyword
from setup.hht.HHTMenuNav import HHTMenuNav
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
from setup.sqllite.SQLLite import SQLLite


class DeliveryRepSubmit(POMLibrary):
    _locators = {
        "release_picklist_button": "//android.widget.Button[@resource-id='DLG_CommDeliveryROOT.BTN_ReleasePicklist']",
        "popup": "//*[@resource-id='popupBody']",
        "close_button": "//android.widget.Button[@resource-id='DLG_CommROOT.BBTN_Close']",
        "back_button": "//android.widget.Button[@resource-id='DLG_CommROOT.BBTN_Back']",
    }

    @keyword("user releases picklist")
    def release_picklist(self):
        HHTMenuNav().user_navigates_to_menu('Sync Device')
        self.applib().wait_until_page_contains_element(self.locator.release_picklist_button)
        self.applib().click_element(self.locator.release_picklist_button)
        self.applib().wait_until_page_contains_element(self.locator.popup)
        self.applib().click_element(self.locator.popup+'/android.widget.Button[@text="Yes"]')
        try_count = 1
        asd = 1
        while asd < 300:
            try:
                logging.warning(f'Attempt#{try_count}')
                logging.warning(f'Attempt#{self.locator.back_button}')
                try_count += 1
                self.applib().wait_until_page_contains_element(self.locator.back_button)
                break
            except Exception as e:
                print(e.__class__, "occured")

    def get_data_from_db(self, column, table):
        query = "select {0} from {1} where COMMS_STATUS = ''".format(column, table)
        print("query = ", query)
        record = SQLLite().fetch_all_record(query)
        print("record = ", record)
        return record

    @keyword('validate data is submitted')
    def validate_data(self):
        picklist_txn_id = self.get_data_from_db('ID', 'TXN_PRDVANINV_PICKLIST')
        prd_id = self.get_data_from_db('PRD_ID', 'TXN_PRDVANINV_PICKLIST')
        vancount_txn_id = self.get_data_from_db('ID', 'TXN_DELIVERY_VANCOUNT')
        self.release_picklist()
        if picklist_txn_id:
            count = len(picklist_txn_id)
            for x in range(count):
                query = "select COMMS_STATUS from TXN_PRDVANINV_PICKLIST where ID = {0}, PRD_ID = {1}".format(picklist_txn_id[x], prd_id[x])
                record = SQLLite().fetch_one_record(query)
                if record != 'S':
                    raise ValueError("Pick List data is not submitted")
        else:
            print("No pick list data to submit")

        if vancount_txn_id:
            count = len(vancount_txn_id)
            for x in range(count):
                query = "select COMMS_STATUS from TXN_DELIVERY_VANCOUNT where ID = {0}".format(vancount_txn_id[x])
                record = SQLLite().fetch_one_record(query)
                if record != 'S':
                    raise ValueError("Van Count is not submitted")
        else:
            print("No van count data to submit")
