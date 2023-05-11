import sqlite3


class SQLLite(object):
    ROOT = ''

    def __init__(self):
        self.working_path = '.\\setup\\sqllite'
        self.connect_to_database()

    def catch_query_error(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(e)

        return wrapper

    def connect_to_database(self):
        global conn
        global cursor
        try:
            conn = sqlite3.connect(self.working_path + '\\SFADBN.db')
            print('Connected to SQLLite')
            status = "Connected"
            cursor = conn.cursor()
        except Exception as e:
            print(e)
            status = "Not Connected"
        return status

    def disconnect_from_database(self):
        conn.close()
        print("Disconnected from DB")

    @catch_query_error
    def execute_sql_string(self, sql_query):
        record = cursor.execute(sql_query)
        print(record)
        return record

    def fetch_one_record(self, sql_query):
        self.execute_sql_string(sql_query)
        record = cursor.fetchone()
        try:
            return record[0]
        except Exception as e:
            print(e)
            return 0

    def fetch_all_record(self, sql_query):
        recrod_list = []
        self.execute_sql_string(sql_query)
        record_details = cursor.fetchall()
        for i in record_details:
            print(i)
            recrod_list.append(i[0])
        return recrod_list

    def execute_query(self, sql_query):
        recrod_list = []
        self.execute_sql_string(sql_query)
        record_details = cursor.fetchall()
        for i in record_details:
            print(i)
            recrod_list.append(i)
        return recrod_list

    @catch_query_error
    def execute_sql_select_all(self, table_name):
        conn.execute('select * from %s' % table_name)
        record = conn.cursor().fetchall()
        return record

    # @catch_query_error
    def execute_sql_select_certain_column(self, table_name, required_key):
        """return specified column required
           required_key(list)
        """
        querystring = ', '.join(i for i in required_key)
        query = 'select %s from %s' % (querystring, table_name)

        recrod_list = []
        for i in conn.execute(query):
            recrod_list.append(i)
        return recrod_list

    def update_table(self, sql_query):
        cursor.execute(sql_query)
        conn.commit()
