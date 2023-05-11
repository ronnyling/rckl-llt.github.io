import os, logging
from configparser import ConfigParser
from hdbcli import dbapi
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime
import time


class HanaDB(object):
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
    PARENT_ROOT = os.path.abspath(os.path.join(SITE_ROOT, os.pardir))
    GPARENT_ROOT = os.path.abspath(os.path.join(PARENT_ROOT, os.pardir))
    DB_CONFIG = GPARENT_ROOT + r"/setup/hanaDB/db.cfg"

    def __init__(self):
        self.conn = None

    def connect_database_to_environment(self):
        global conn
        global cursor
        env = BuiltIn().get_variable_value("${ENV}")
        trial = 0
        times = 1
        status = False
        start_time = time.time()
        timeout_cnt = 0
        while trial == 0 and timeout_cnt < 10:
            try:
                logging.warning(f'-----------------------------------')
                logging.warning(f'Attempt Time#{datetime.now()}')
                logging.warning(f'Attempt#{times}')
                logging.warning(f'Before DB connection:{status}')
                time.sleep(1)
                timeout_cnt = timeout_cnt + 1
                self.setup_db(env)
                if self.conn.isconnected():
                    print('Connected to hanaDB')
                    status = True
                    conn = self.conn
                    cursor = self.conn.cursor()
                    logging.warning(f'After Connect:{status}')
                    break
            except Exception as e:
                print(e.__class__, "occured")
                status = False
                times = times + 1
                logging.warning(f'After Connect:{status}')
                logging.warning(f'Error code: {e.args[0]}')
                logging.warning(f'Error description: {e.args[1]}')
        end_time = time.time()
        consumed_time = end_time - start_time
        logging.warning(f'Total attempt:{times}')
        logging.warning(f'Total time spent in seconds:{consumed_time}')
        logging.warning(f'-----------------------------------')
        assert status is True, "Retried to connect hanaDB but Failed"
        return self.conn, status

    def disconnect_from_database(self):
        cursor.close()
        conn.close()
        print("Disconnected from DB")

    def execute_sql_string(self, sql_query):
        record_details = cursor.execute(sql_query)
        print(record_details)
        return record_details

    def fetch_one_record(self, sql_query):
        self.execute_sql_string(sql_query)
        record_details = cursor.fetchone()
        print(record_details[0])
        return record_details[0]

    @keyword("fetch all record from ${sql_query}")
    def fetch_all_record(self, sql_query):
        recrod_list = []
        self.execute_sql_string(sql_query)
        record_details = cursor.fetchall()
        for i in record_details:
            recrod_list.append(i)
        return recrod_list

    def user_validates_database_data(self, module, body_content):
        get_id = body_content['ID']
        get_id = get_id.replace(":", "")
        get_id = get_id.replace("-", "")
        query = self.metadata_db_query(module, get_id)
        flag = self.database_data_comparing(query, body_content)
        return flag

    def metadata_db_query(self, module, id):
        query = \
            "SELECT CAST(FIELD_VALUE AS varchar), FIELD FROM MODULE_DATA_FIELDS R " \
            "INNER JOIN METADATA_FIELD F " \
            "ON R.FIELD_ID = F.ID " \
            "WHERE R.ROW_ID IN ( " \
            "SELECT ROW_ID FROM MODULE_DATA_FIELDS R " \
            "INNER JOIN METADATA_FIELD F " \
            "ON R.FIELD_ID = F.ID " \
            "INNER JOIN MODULE_DATA_ROWS D " \
            "ON D.MODULE_ID = F.MODULE_ID " \
            "WHERE F.MODULE_ID= (SELECT ID FROM METADATA_MODULE WHERE LOGICAL_ID='{0}' AND IS_DELETED=false) " \
            "AND R.ROW_ID LIKE '{1}' " \
            "AND D.IS_DELETED=false " \
            "GROUP BY ROW_ID)".format(module, id)
        return query

    def database_data_comparing(self, query, body_content):
        record_list = []
        list_field = []
        self.execute_sql_string(query)
        record_details = cursor.fetchall()
        for i in record_details:
            record_list.append(i[0])
            list_field.append(i[1])
        query_result = dict(zip(list_field, record_list))
        print("Query Result: ", query_result)
        flag = True
        for i in query_result.keys():
            if "ID" in i and query_result[i] is not None:
                if isinstance(body_content[i], dict):
                    body_content[i] = body_content[i]['ID']
                body_content[i] = body_content[i].replace(":", "")
                body_content[i] = body_content[i].replace("-", "")
            print("body content = " + str(body_content[i]))
            print("query result = " + str(query_result[i]))
            if str(body_content[i]).lower() != str(query_result[i]).lower():
                if i == "START_DT" or i == "END_DT":
                    continue
                else:
                    flag = False
                    break
        assert flag is True, "Data Mismatch"
        return flag

    def row_count(self, sql_query):
        self.execute_sql_string(sql_query)
        record_count = cursor.fetchall()
        print("Total no of records/rows is ", len(record_count))
        return len(record_count)

    def row_count_is_0(self, sql_query):
        self.execute_sql_string(sql_query)
        record_count = cursor.fetchall()
        print(len(record_count))
        if len(record_count) == 0:
            result = "Pass"
        else:
            result = "Fail"
        return result

    def row_count_is_equal_to_x(self, sql_query, row_count):
        self.execute_sql_string(sql_query)
        record_count = cursor.fetchall()
        print(len(record_count))
        if len(record_count) == int(row_count):
            result = "Pass"
        else:
            result = "Fail"
        return result

    def row_count_is_greater_than_x(self, sql_query, rowcount):
        self.execute_sql_string(sql_query)
        record_count = cursor.fetchall()
        print(len(record_count))
        if len(record_count) >= int(rowcount):
            result = "Pass"
        else:
            result = "Fail"
        return result

    def row_count_is_less_than_x(self, sql_query, row_count):
        self.execute_sql_string(sql_query)
        record_count = cursor.fetchall()
        print(len(record_count))
        if len(record_count) <= int(row_count):
            result = "Pass"
        else:
            result = "Fail"
        return result

    def query(self, sql_query):
        query_result = self.fetch_all_record(sql_query)
        return query_result

    def setup_db(self, env):
        config = ConfigParser()
        config.read([self.DB_CONFIG])
        db_address = config.get(env, 'dbaddress')
        db_port = int(config.get(env, 'dbport'))
        db_user = config.get(env, 'dbuser')
        db_password = config.get(env, 'dbpassword')
        db_current_schema = config.get(env, 'dbcurrentSchema')
        db_encrypt = config.get(env, 'dbencrypt')
        db_ssl_validate_certificate = config.get(env, 'dbsslValidateCertificate')
        logging.warning(f'db_address#{db_address}')
        logging.warning(f'db_port#{db_port}')
        self.conn = dbapi.connect(address=db_address, port=db_port, user=db_user, password=db_password,
                                          currentSchema=db_current_schema, encrypt=db_encrypt,
                                          sslValidateCertificate=db_ssl_validate_certificate)

    # Description by passing query string
    def description_by_query(self, query_string):
        status = ""
        try:
            self.execute_sql_string(query_string)
            des = cursor.description
            if len(des) > 1:
                status = "Pass"
            else:
                status = "Fail"
            print(des)
        except Exception as e:
            print(e.args)
            status = "Fail"
        return status

    #Description by passing tablename
    def description_by_tablename(self, table_name):
        status = ""
        try:
            query_string = "Select top 1 * from {table}".format(table=table_name)
            self.execute_sql_string(query_string)
            des = cursor.description
            if len(des) > 1:
                status = "Pass"
            else:
                status = "Fail"
            print(des)
        except Exception as e:
            print(e.args)
            status = "Fail"
        return status

    #Check if present in DB by passing query
    def check_if_exists_in_database_by_query(self, query_string):
        status = ""
        try:
            self.execute_sql_string(query_string)
            result = cursor.fetchall()
            status = ""
            if len(result) > 0:
                status = "Pass"
            else:
                status = "Fail"
        except Exception as e:
            print(e.args)
            status = "Fail"
        return status

    def check_if_not_exists_in_database_by_query(self, query_string):
        status = ""
        try:
            self.execute_sql_string(query_string)
            result = cursor.fetchall()
            status = ""
            if len(result) == 0:
                status = "Pass"
            else:
                status = "Fail"
        except Exception as e:
            print(e.args)
            status = "Fail"
        return status

    # Execute Commands in the file. NOTE: the commands must be seperated by ;
    def execute_sql_script(self, file_path):
        status = ""
        try:
            fd = open(file_path, 'r')
            sql_file = fd.read()
            fd.close()
            sql_commands = sql_file.split(';')
            for command in sql_commands:
                print(command)
                self.execute_sql_string(command)
                result = cursor.description
                print(result)
                status = "Pass"
        except Exception as e:
            print(e.args)
            status = "Fail"
        return status

    #Insert with data in list format
    def insert_listdata_into_table(self, conn, table_name, data):
        cursor = conn.cursor()
        datalist = data
        datastring = ', '.join('?' * len(datalist))
        query = 'INSERT INTO %s VALUES (%s)' % (table_name, datastring)
        result = cursor.execute(query, datalist)
        if result:
            print("Record Inserted")
        else:
            print("Record Not inserted")

    # Insert with data in dict format
    def insert_dictdata_into_table(self, conn, table_name, data_dict):
        cursor = conn.cursor()
        key_list, value_list = [], []
        for key, value in data_dict.items():
            key_list.append(key)
            value_list.append(value)
        key_string = ', '.join(str(e) for e in key_list)
        value_string = ', '.join('?' * len(value_list))
        query = 'INSERT INTO %s(%s) VALUES (%s);' % (table_name, key_string, value_string)
        result = cursor.execute(query, value_list)
        print(result)
        if result:
            print("Record Inserted")
        else:
            print("Record Not inserted")

    # Insert update data by passing set and condition parameters
    def update_data_in_table(self, conn, table_name, set_data_dict, condition_data_dict):
        cursor = conn.cursor()
        set_data_str = ", ".join(("{}='{}'".format(*i) for i in set_data_dict.items()))
        condition_data_str = "AND ".join(("{}='{}'".format(*i) for i in condition_data_dict.items()))
        query = 'UPDATE %s SET %s where (%s);' % (table_name, set_data_str, condition_data_str)
        print(query)
        result = cursor.execute(query)
        if result:
            print("Record updated")
        else:
            print("Record not updated")
