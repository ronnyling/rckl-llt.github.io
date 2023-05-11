from robot.api.deco import keyword
from setup.hht.HHTPOMLibrary import HHTPOMLibrary as POMLibrary
import datetime
from setup.sqllite.SQLLite import SQLLite


class DeliveryRepHousekeeping(POMLibrary):

    submit_status = 'S'
    purge_date = None
    db_table_list = {
        "TXN_DELIVERY_COL", "TXN_DELIVERY_COLHDR", "TXN_DELIVERY_COLRETURN,",
        "TXN_DELIVERY_INV", "TXN_DELIVERY_VANCOUNT"
    }
    return_list = {
        "TXN_DELIVERY_NOTEHDR", "TXN_NOTEPRD_HIS", "TXN_DELIVERY_NOTEPRD", "TXN_DELIVERY_NOTEPRD_TAX",
        "TXN_DELIVERY_NOTEPROMO", "TXN_DELIVERY_NOTEPROMO_FOC", "TXN_DELIVERY_NOTEPROMO_QPS_PRD",
    }
    delivery_list = {
        "TXN_DELIVERY_INVPROMO_ALLOCFOC", "TXN_DELIVERY_INVPROMO", "TXN_DELIVERY_INVDTL_TAX",
        "TXN_DELIVERY_INVDTL_BIN", "TXN_DELIVERY_INVDTL", "TXN_INVDTL_HIS",
    }
    err_msg = "Data not purged"

    @keyword('get purge info')
    def get_purge_info(self):
        purge_day = SQLLite().fetch_one_record("select PVALUE from M_SETUP_PARAM where PARAMETER = 'h_purgeperiod'")
        purge_day = int(purge_day)
        current_date = datetime.datetime.now()
        self.purge_date = (current_date - datetime.timedelta(days=purge_day)).strftime('%Y-%m-%d')

    @keyword('validate data has been purged')
    def check_data(self):
        self.check_db_list()
        self.check_delivery_list()
        self.check_return_list()
        self.check_invoice()
        self.check_collection()
        self.check_picklist()

    def check_picklist(self):
        query = "select * from TXN_PICKLISTHDR join TXN_PICKLIST_INV on TXN_PICKLISTHDR.ID = TXN_PICKLIST_INV.TXN_ID " \
                "where ACTUAL_DELIVERY_DT <= '{0}' and COMMS_STATUS = '{1}'".format(self.purge_date, self.submit_status)
        record = SQLLite().fetch_one_record(query)
        if record != 0:
            raise ValueError(self.err_msg)

    def check_invoice(self):
        query = "select * from TXN_DELIVERY_INVOICE where DELIVERY_DT <= '{0}' and COMMS_STATUS = '{1}'"\
            .format(self.purge_date, self.submit_status)
        record = SQLLite().fetch_one_record(query)
        if record != 0:
            raise ValueError(self.err_msg)

    def check_collection(self):
        query = "select * from TXN_DELIVERY_COLHDR join TXN_DELIVERY_COLPAYDTL on TXN_DELIVERY_COLHDR.ID = " \
                "TXN_DELIVERY_COLPAYDTL.TXN_ID where TXN_DT <= '{0}' and COMMS_STATUS = '{1}'"\
            .format(self.purge_date, self.submit_status)
        record = SQLLite().fetch_one_record(query)
        if record != 0:
            raise ValueError(self.err_msg)

    def check_db_list(self):
        for x in self.db_table_list:
            query = "select * from {0} where TXN_DT <= '{1}' and COMMS_STATUS = '{2}'".format(x, self.purge_date,
                                                                                              self.submit_status)
            record = SQLLite().fetch_one_record(query)
            if record != 0:
                raise ValueError(self.err_msg)

    def check_return_list(self):
        for x in self.return_list:
            query = "select * from TXN_DELIVERY_COLRETURN join {0} on TXN_DELIVERY_COLRETURN.ID = {0}.TXN_ID where " \
                    "TXN_DT <= '{1}' and COMMS_STATUS = '{2}'".format(x, self.purge_date, self.submit_status)
            record = SQLLite().fetch_one_record(query)
            if record != 0:
                raise ValueError(self.err_msg)

    def check_delivery_list(self):
        for x in self.delivery_list:
            query = "select * from TXN_DELIVERY_INV join {0} on TXN_DELIVERY_INV.ID = {0}.TXN_ID where " \
                    "TXN_DT <= '{1}' and COMMS_STATUS = '{2}'".format(x, self.purge_date, self.submit_status)
            record = SQLLite().fetch_one_record(query)
            if record != 0:
                raise ValueError(self.err_msg)
